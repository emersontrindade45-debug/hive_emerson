#!/usr/bin/env python3
"""
Coletor de inteligência de YouTube para o squad Marketing.

Raspa os canais listados em channels.json: metadados + transcrição (legenda
automática em PT). Guarda cada vídeo como um .json em transcripts/ e usa isso
como cache — vídeo já baixado nunca é rebaixado.

Uso:
    python collect.py                    # novos vídeos dos últimos 7 dias
    python collect.py --days 30          # janela maior
    python collect.py --max 5            # limita vídeos por canal
    python collect.py --resolve <url>    # descobre o channel_id de uma URL
    python collect.py --no-transcript    # só metadados (rápido)

Saída: imprime um resumo e grava transcripts/<video_id>.json
"""

import argparse
import io
import json
import os
import re
import subprocess
import sys
import time
from datetime import datetime, timedelta, timezone

BASE = os.path.dirname(os.path.abspath(__file__))
TRANSCRIPTS = os.path.join(BASE, "transcripts")
CHANNELS_FILE = os.path.join(BASE, "channels.json")

# O YouTube devolve 429 se pedirmos legendas rápido demais. Pausa entre vídeos.
THROTTLE_SECONDS = 2.5


def log(msg):
    """stdout do Windows é cp1252 e quebra com emoji; força UTF-8."""
    sys.stdout.write(msg + "\n")
    sys.stdout.flush()


def run_ytdlp(args, timeout=180):
    """Chama yt-dlp como módulo (não depende do .exe estar no PATH)."""
    env = dict(os.environ, PYTHONIOENCODING="utf-8")
    cmd = [sys.executable, "-m", "yt_dlp"] + args
    try:
        proc = subprocess.run(
            cmd, capture_output=True, timeout=timeout, env=env
        )
    except subprocess.TimeoutExpired:
        return None, "timeout"
    out = proc.stdout.decode("utf-8", errors="replace")
    err = proc.stderr.decode("utf-8", errors="replace")
    return out, err


def resolve_channel(url):
    """Descobre o channel_id a partir de qualquer URL/handle de canal."""
    out, err = run_ytdlp(
        ["--flat-playlist", "--playlist-items", "1", "-J", url.rstrip("/") + "/videos"]
    )
    if not out:
        log(f"ERRO ao resolver {url}: {err[:300]}")
        return
    data = json.loads(out)
    log(f"nome      : {data.get('channel')}")
    log(f"channel_id: {data.get('channel_id')}")


def list_videos(channel, days, max_videos):
    """Lista vídeos recentes do canal (rápido: só metadados achatados)."""
    url = f"https://www.youtube.com/channel/{channel['channel_id']}/videos"
    out, err = run_ytdlp(
        [
            "--flat-playlist",
            "--playlist-items", f"1-{max_videos}",
            # lang=pt evita que o YouTube devolva títulos auto-traduzidos p/ inglês
            "--extractor-args", "youtube:lang=pt",
            "-J", url,
        ]
    )
    if not out:
        log(f"  ERRO ao listar: {err[:300]}")
        return []

    try:
        data = json.loads(out)
    except json.JSONDecodeError:
        log(f"  ERRO: resposta invalida do yt-dlp")
        return []

    cutoff = datetime.now(timezone.utc) - timedelta(days=days)
    videos = []
    for entry in data.get("entries") or []:
        if not entry or not entry.get("id"):
            continue
        # timestamp costuma vir nulo no modo flat; filtramos por data depois,
        # ao buscar os detalhes de cada vídeo.
        videos.append(
            {
                "video_id": entry.get("id"),
                "title": entry.get("title") or "",
                "url": f"https://www.youtube.com/watch?v={entry.get('id')}",
                "duration": entry.get("duration"),
                "views": entry.get("view_count"),
            }
        )
    return videos, cutoff


def parse_json3(path):
    """Converte legenda json3 do YouTube em texto corrido."""
    with io.open(path, encoding="utf-8") as fh:
        data = json.load(fh)
    parts = []
    for event in data.get("events") or []:
        text = "".join(s.get("utf8", "") for s in (event.get("segs") or []))
        if text.strip():
            parts.append(text.strip())
    full = " ".join(parts)
    full = re.sub(r"\s+", " ", full)
    # remove marcadores de som ([música], >>) que poluem a análise
    full = re.sub(r"\[[^\]]{0,30}\]", "", full)
    full = full.replace(">>", " ")
    return re.sub(r"\s+", " ", full).strip()


def fetch_video(video, channel, want_transcript):
    """Busca metadados completos + transcrição de um vídeo."""
    vid = video["video_id"]
    tmp_prefix = os.path.join(TRANSCRIPTS, f"_tmp_{vid}")

    # Passo 1 - metadados. "-J" imprime o JSON no stdout, mas nesse modo o
    # yt-dlp NAO grava os arquivos de legenda em disco. Por isso a legenda
    # exige uma segunda chamada, sem "-J".
    out, err = run_ytdlp(
        [
            "--extractor-args", "youtube:lang=pt",
            "--skip-download",
            "-J",
            video["url"],
        ],
        timeout=240,
    )
    if not out:
        return None, err[:200] if err else "sem resposta"

    try:
        meta = json.loads(out)
    except json.JSONDecodeError:
        return None, "json invalido"

    # Passo 2 - legenda, sem "-J", para que os arquivos sejam escritos.
    transcript = ""
    transcript_status = "nao solicitada"
    if want_transcript:
        _, sub_err = run_ytdlp(
            [
                "--extractor-args", "youtube:lang=pt",
                "--skip-download",
                "--write-auto-subs",
                "--write-subs",
                # pt-orig = legenda no idioma original. Pedir variantes demais gera 429.
                "--sub-langs", "pt-orig",
                "--sub-format", "json3",
                "-o", tmp_prefix + ".%(ext)s",
                video["url"],
            ],
            timeout=240,
        )
        err = (err or "") + (sub_err or "")
        found = None
        for suffix in (".pt-orig.json3", ".pt.json3"):
            candidate = tmp_prefix + suffix
            if os.path.exists(candidate):
                found = candidate
                break
        if found:
            try:
                transcript = parse_json3(found)
                transcript_status = "ok"
            except Exception as exc:
                transcript_status = f"erro no parse: {exc}"
            finally:
                # limpa os temporários
                for suffix in (".pt-orig.json3", ".pt.json3"):
                    leftover = tmp_prefix + suffix
                    if os.path.exists(leftover):
                        os.remove(leftover)
        else:
            transcript_status = "indisponivel"
            if "429" in (err or ""):
                transcript_status = "bloqueado (429 - rate limit)"

    record = {
        "video_id": vid,
        "channel": channel["name"],
        "channel_id": channel["channel_id"],
        "title": meta.get("title") or video["title"],
        "url": video["url"],
        "upload_date": meta.get("upload_date"),
        "duration_seconds": meta.get("duration"),
        "view_count": meta.get("view_count"),
        "like_count": meta.get("like_count"),
        "comment_count": meta.get("comment_count"),
        "description": (meta.get("description") or "")[:4000],
        "transcript": transcript,
        "transcript_status": transcript_status,
        "transcript_words": len(transcript.split()) if transcript else 0,
        "collected_at": datetime.now(timezone.utc).isoformat(),
    }
    return record, None


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--days", type=int, default=7, help="janela em dias (default 7)")
    ap.add_argument("--max", type=int, default=10, help="max de videos por canal")
    ap.add_argument("--no-transcript", action="store_true")
    ap.add_argument("--resolve", metavar="URL", help="descobre o channel_id de uma URL")
    ap.add_argument("--force", action="store_true", help="rebaixa mesmo se ja existir")
    args = ap.parse_args()

    if args.resolve:
        resolve_channel(args.resolve)
        return

    os.makedirs(TRANSCRIPTS, exist_ok=True)
    with io.open(CHANNELS_FILE, encoding="utf-8") as fh:
        channels = json.load(fh)["channels"]

    cutoff_date = (datetime.now(timezone.utc) - timedelta(days=args.days)).strftime("%Y%m%d")
    log(f"Janela: ultimos {args.days} dias (>= {cutoff_date}) | max {args.max}/canal")
    log("")

    novos, pulados, falhas = [], 0, []

    for channel in channels:
        log(f"[{channel['name']}]")
        result = list_videos(channel, args.days, args.max)
        if not result:
            continue
        videos, _ = result

        for video in videos:
            vid = video["video_id"]
            dest = os.path.join(TRANSCRIPTS, f"{vid}.json")

            if os.path.exists(dest) and not args.force:
                pulados += 1
                continue

            record, error = fetch_video(video, channel, not args.no_transcript)
            if error:
                log(f"  x {vid}: {error}")
                falhas.append(vid)
                time.sleep(THROTTLE_SECONDS)
                continue

            # filtro de data acontece aqui, com o upload_date real
            if record.get("upload_date") and record["upload_date"] < cutoff_date:
                continue

            with io.open(dest, "w", encoding="utf-8") as fh:
                json.dump(record, fh, ensure_ascii=False, indent=2)

            novos.append(record)
            words = record["transcript_words"]
            flag = "" if record["transcript_status"] == "ok" else f" [{record['transcript_status']}]"
            log(f"  + {record['upload_date']} {record['title'][:52]} ({words}p){flag}")

            time.sleep(THROTTLE_SECONDS)
        log("")

    log("=" * 60)
    log(f"Novos: {len(novos)} | Ja em cache: {pulados} | Falhas: {len(falhas)}")
    if novos:
        log("")
        log("Arquivos gravados em transcripts/. Rode /update-youtube para analisar.")
    if falhas:
        log(f"Falhas: {', '.join(falhas)}")


if __name__ == "__main__":
    main()
