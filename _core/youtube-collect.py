#!/usr/bin/env python3
"""
Coletor de inteligencia de YouTube — compartilhado entre squads.

Raspa os canais listados no channels.json do squad: metadados + transcricao
no idioma original (pt-orig, en-orig, ...). Grava um .json por video em
transcripts/ e usa isso como cache — video ja baixado nunca e rebaixado.

Uso:
    python _core/youtube-collect.py --dir squads/marketing/data/youtube-intel
    python _core/youtube-collect.py --dir squads/infra/data/tech-intel --days 14
    python _core/youtube-collect.py --resolve https://youtube.com/@canal
    python _core/youtube-collect.py --dir <dir> --no-transcript   # so metadados

IMPORTANTE: rode sempre da raiz do repo. Nao use "cd" para subpasta —
os hooks de sessao do HIVE resolvem caminho relativo ao cwd e quebram.

O idioma vem do campo "lang" de cada canal em channels.json (default: pt).
"""

import argparse
import glob
import io
import json
import os
import re
import subprocess
import sys
import time
from datetime import datetime, timedelta, timezone

# Coletor compartilhado: cada squad passa seu proprio diretorio via --dir.
# Ex.: --dir squads/infra/data/tech-intel
REPO = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
DEFAULT_DIR = os.path.join(REPO, "squads", "marketing", "data", "youtube-intel")

# definido em main() a partir de --dir
TRANSCRIPTS = None

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
            # fixar o idioma do canal evita títulos auto-traduzidos pelo YouTube
            "--extractor-args", f"youtube:lang={channel.get('lang', 'pt')}",
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
            "--extractor-args", f"youtube:lang={channel.get('lang', 'pt')}",
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

    # video privado, removido ou so-para-membros faz o yt-dlp devolver "null"
    if not isinstance(meta, dict):
        return None, "indisponivel (privado/removido/membros)"

    # Passo 2 - legenda, sem "-J", para que os arquivos sejam escritos.
    transcript = ""
    transcript_status = "nao solicitada"
    if want_transcript:
        # "<lang>-orig" e a legenda no idioma original em que o video foi
        # falado (pt-orig, en-orig, ...). Pegamos o idioma preferido do canal
        # e caimos para o generico se ele nao existir. Pedir variantes demais
        # gera HTTP 429.
        lang = channel.get("lang", "pt")
        _, sub_err = run_ytdlp(
            [
                "--extractor-args", f"youtube:lang={lang}",
                "--skip-download",
                "--write-auto-subs",
                "--write-subs",
                "--sub-langs", f"{lang}-orig,{lang}",
                "--sub-format", "json3",
                "-o", tmp_prefix + ".%(ext)s",
                video["url"],
            ],
            timeout=240,
        )
        err = (err or "") + (sub_err or "")
        # o yt-dlp nomeia como <prefixo>.<lang>.json3; o "-orig" tem
        # prioridade por ser a fala original, sem tradução automática.
        candidates = sorted(
            glob.glob(tmp_prefix + ".*.json3"),
            key=lambda p: (0 if "-orig." in p else 1, p),
        )
        if candidates:
            try:
                transcript = parse_json3(candidates[0])
                transcript_status = "ok"
            except Exception as exc:
                transcript_status = f"erro no parse: {exc}"
            finally:
                for leftover in glob.glob(tmp_prefix + ".*.json3"):
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
    ap.add_argument(
        "--dir",
        default=DEFAULT_DIR,
        help="diretorio do squad (contem channels.json; grava em transcripts/)",
    )
    args = ap.parse_args()

    if args.resolve:
        resolve_channel(args.resolve)
        return

    global TRANSCRIPTS
    base = args.dir if os.path.isabs(args.dir) else os.path.join(REPO, args.dir)
    TRANSCRIPTS = os.path.join(base, "transcripts")
    channels_file = os.path.join(base, "channels.json")

    if not os.path.exists(channels_file):
        log(f"ERRO: nao encontrei {channels_file}")
        sys.exit(1)

    os.makedirs(TRANSCRIPTS, exist_ok=True)
    with io.open(channels_file, encoding="utf-8") as fh:
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
