#!/usr/bin/env python3
"""
Baixa videos avulsos (por URL ou ID) para o acervo de um squad.

Complementa o youtube-collect.py: aquele raspa canais inteiros por cadencia,
este pega um video especifico que o Emerson mandou.

Uso:
    python _core/youtube-fetch-video.py --dir squads/operations/data/performance-intel URL [URL...]
    python _core/youtube-fetch-video.py --dir <dir> --lang pt VIDEO_ID

IMPORTANTE: rodar da raiz do repo. Nao usar "cd" para subpasta — os hooks do
HIVE resolvem caminho relativo ao cwd e quebram.
"""

import argparse
import io
import os
import re
import sys

BASE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, BASE)

# reaproveita a logica ja testada do coletor de canais
_collect = __import__("youtube-collect")


def extrair_id(entrada):
    """Aceita URL completa, youtu.be, ou o proprio ID."""
    entrada = entrada.strip()
    padroes = [
        r"(?:v=|/videos/|youtu\.be/|/embed/|/shorts/)([A-Za-z0-9_-]{11})",
        r"^([A-Za-z0-9_-]{11})$",
    ]
    for p in padroes:
        m = re.search(p, entrada)
        if m:
            return m.group(1)
    return None


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("urls", nargs="+", help="URLs ou IDs de video")
    ap.add_argument("--dir", required=True, help="diretorio de dados do squad")
    ap.add_argument("--lang", default="pt", help="idioma da legenda (default pt)")
    ap.add_argument("--force", action="store_true", help="rebaixa se ja existir")
    args = ap.parse_args()

    repo = os.path.dirname(BASE)
    base = args.dir if os.path.isabs(args.dir) else os.path.join(repo, args.dir)
    destino = os.path.join(base, "transcripts")
    os.makedirs(destino, exist_ok=True)

    # o coletor usa a global TRANSCRIPTS para montar o caminho temporario
    _collect.TRANSCRIPTS = destino

    canal = {
        "name": "(avulso)",
        "channel_id": "",
        "lang": args.lang,
    }

    ok = falhou = pulado = 0
    for entrada in args.urls:
        vid = extrair_id(entrada)
        if not vid:
            print(f"  x nao consegui extrair o ID de: {entrada}")
            falhou += 1
            continue

        alvo = os.path.join(destino, f"{vid}.json")
        if os.path.exists(alvo) and not args.force:
            print(f"  = {vid} ja existe (use --force para rebaixar)")
            pulado += 1
            continue

        video = {
            "video_id": vid,
            "title": "",
            "url": f"https://www.youtube.com/watch?v={vid}",
        }
        registro, erro = _collect.fetch_video(video, canal, True)
        if erro:
            print(f"  x {vid}: {erro}")
            falhou += 1
            continue

        # o nome real do canal vem dos metadados, nao do placeholder
        registro["channel"] = registro.get("channel") or "(avulso)"
        registro["origem"] = "avulso — enviado pelo Emerson"

        with io.open(alvo, "w", encoding="utf-8") as fh:
            import json

            json.dump(registro, fh, ensure_ascii=False, indent=2)

        print(
            f"  + {registro['upload_date']} {registro['title'][:50]} "
            f"({registro['transcript_words']}p)"
        )
        ok += 1

    print(f"\nBaixados: {ok} | Ja existiam: {pulado} | Falhas: {falhou}")


if __name__ == "__main__":
    main()
