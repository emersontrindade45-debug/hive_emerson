#!/usr/bin/env python3
"""
Descoberta de LACUNA de conteudo no YouTube — worker da divisao M2 (Intelligence).

Diferente de youtube-collect.py, que VIGIA canais ja conhecidos, este worker
PROSPECTA: busca por termo, mede a razao views/inscritos de cada video e
destaca os que performaram muito acima do tamanho do canal.

Tese do sinal (Emerson, 2026-08-25):
    Video com muitas views em canal pequeno = DEMANDA VALIDADA SEM AUTORIDADE.
    Se um canal de 300 inscritos faz 80k views, o algoritmo nao empurrou por
    causa do canal — empurrou por causa do TEMA. Logo: procura existe, oferta
    boa nao. Isso e lacuna explorável.

Uso:
    python _core/youtube-gaps.py --termos "automacao whatsapp ia,n8n tutorial"
    python _core/youtube-gaps.py --termos-arquivo squads/marketing/data/youtube-intel/termos.json
    python _core/youtube-gaps.py --termos "ia para pequenas empresas" --max 30 --meses 12

IMPORTANTE: rode sempre da raiz do repo. Nao use "cd" para subpasta —
os hooks de sessao do HIVE resolvem caminho relativo ao cwd e quebram.
"""

import argparse
import io
import json
import os
import subprocess
import sys
import time
from datetime import datetime, timedelta, timezone

UA = "Mozilla/5.0 (Windows NT 10.0; Win64; x64)"


def log(msg):
    sys.stderr.write(msg + "\n")
    sys.stderr.flush()


def run_ytdlp(args, timeout=180):
    cmd = [sys.executable, "-m", "yt_dlp"] + args
    try:
        p = subprocess.run(cmd, capture_output=True, text=True,
                           timeout=timeout, encoding="utf-8", errors="replace")
        return p.stdout, p.stderr, p.returncode
    except subprocess.TimeoutExpired:
        return "", "timeout", 1


def buscar(termo, max_videos):
    """Busca no YouTube e devolve metadados rasos (flat) de cada resultado."""
    out, err, rc = run_ytdlp([
        f"ytsearch{max_videos}:{termo}",
        "--flat-playlist", "--dump-json",
        "--no-warnings", "--user-agent", UA,
    ], timeout=240)
    if rc != 0 and not out.strip():
        log(f"  ! busca falhou para '{termo}': {err.strip()[:160]}")
        return []
    vids = []
    for line in out.splitlines():
        line = line.strip()
        if not line:
            continue
        try:
            vids.append(json.loads(line))
        except json.JSONDecodeError:
            continue
    return vids


def detalhar(video_id):
    """Puxa metadados completos de 1 video, incluindo inscritos do canal."""
    out, err, rc = run_ytdlp([
        f"https://www.youtube.com/watch?v={video_id}",
        "--dump-json", "--skip-download",
        "--no-warnings", "--user-agent", UA,
    ], timeout=120)
    if rc != 0 or not out.strip():
        return None
    try:
        return json.loads(out.splitlines()[0])
    except (json.JSONDecodeError, IndexError):
        return None


def classificar(ratio, subs):
    """Traduz a razao views/inscritos em rotulo acionavel."""
    if subs < 1000 and ratio >= 20:
        return "LACUNA FORTE", "canal minusculo, alcance grande: o tema carregou sozinho"
    if ratio >= 20:
        return "LACUNA FORTE", "views muito acima do tamanho do canal"
    if ratio >= 5:
        return "LACUNA MEDIA", "tema puxou alem da base do canal"
    if ratio >= 1.5:
        return "ACIMA DA BASE", "performance boa, mas dentro do esperado"
    return "NORMAL", "alcance compativel com o canal"


def analisar(termo, max_videos, meses, pausa):
    log(f"\n[busca] {termo}")
    rasos = buscar(termo, max_videos)
    if not rasos:
        return []
    log(f"  {len(rasos)} resultados; detalhando...")

    corte = datetime.now(timezone.utc) - timedelta(days=meses * 30)
    achados = []

    for i, r in enumerate(rasos, 1):
        vid = r.get("id")
        if not vid:
            continue
        d = detalhar(vid)
        time.sleep(pausa)
        if not d:
            continue

        subs = d.get("channel_follower_count") or 0
        views = d.get("view_count") or 0
        if not views:
            continue

        # janela temporal: ignora video antigo demais
        up = d.get("upload_date")
        if up:
            try:
                dt = datetime.strptime(up, "%Y%m%d").replace(tzinfo=timezone.utc)
                if dt < corte:
                    continue
            except ValueError:
                pass

        # subs=0 significa canal que oculta a contagem: nao da pra medir razao
        if subs <= 0:
            continue

        ratio = views / subs
        rotulo, motivo = classificar(ratio, subs)

        achados.append({
            "termo": termo,
            "video_id": vid,
            "titulo": d.get("title"),
            "url": f"https://www.youtube.com/watch?v={vid}",
            "canal": d.get("channel") or d.get("uploader"),
            "canal_url": d.get("channel_url"),
            "inscritos": subs,
            "views": views,
            "ratio": round(ratio, 2),
            "likes": d.get("like_count"),
            "comentarios": d.get("comment_count"),
            "duracao_seg": d.get("duration"),
            "upload_date": up,
            "sinal": rotulo,
            "motivo": motivo,
        })
        log(f"  [{i}/{len(rasos)}] {ratio:7.1f}x  {rotulo:14s}  {str(d.get('title'))[:56]}")

    return achados


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--termos", help="termos separados por virgula")
    ap.add_argument("--termos-arquivo", help="json com lista em 'termos'")
    ap.add_argument("--max", type=int, default=20, help="resultados por termo (default 20)")
    ap.add_argument("--meses", type=int, default=18, help="janela em meses (default 18)")
    ap.add_argument("--min-ratio", type=float, default=5.0, help="ratio minimo para o relatorio (default 5)")
    ap.add_argument("--pausa", type=float, default=1.2, help="segundos entre chamadas (throttle 429)")
    ap.add_argument("--out", default="squads/marketing/data/youtube-intel/gaps",
                    help="diretorio de saida")
    a = ap.parse_args()

    termos = []
    if a.termos:
        termos += [t.strip() for t in a.termos.split(",") if t.strip()]
    if a.termos_arquivo:
        with io.open(a.termos_arquivo, encoding="utf-8") as f:
            termos += json.load(f).get("termos", [])
    if not termos:
        ap.error("informe --termos ou --termos-arquivo")

    todos = []
    for t in termos:
        todos += analisar(t, a.max, a.meses, a.pausa)

    todos.sort(key=lambda x: x["ratio"], reverse=True)
    fortes = [x for x in todos if x["ratio"] >= a.min_ratio]

    os.makedirs(a.out, exist_ok=True)
    hoje = datetime.now().strftime("%Y-%m-%d")
    caminho = os.path.join(a.out, f"{hoje}.json")
    with io.open(caminho, "w", encoding="utf-8") as f:
        json.dump({
            "gerado_em": datetime.now(timezone.utc).isoformat(),
            "termos": termos,
            "parametros": {"max": a.max, "meses": a.meses, "min_ratio": a.min_ratio},
            "total_analisado": len(todos),
            "total_acima_do_corte": len(fortes),
            "achados": todos,
        }, f, ensure_ascii=False, indent=2)

    log(f"\n{'='*64}")
    log(f"analisados: {len(todos)}  |  acima de {a.min_ratio}x: {len(fortes)}")
    log(f"salvo em: {caminho}")
    log(f"{'='*64}")
    for x in fortes[:15]:
        log(f"{x['ratio']:7.1f}x  {x['inscritos']:>9,} insc  {x['views']:>10,} views  {x['titulo'][:52]}")


if __name__ == "__main__":
    main()
