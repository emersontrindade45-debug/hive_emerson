#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Radar semanal de YouTube — LISTA sem baixar.

Decisao do Emerson (2026-08-27): nada de transcricao baixada automaticamente.
Toda segunda-feira este script varre TODOS os canais de TODOS os squads e
monta uma lista de candidatos. O Emerson escolhe quais valem transcricao;
so entao roda-se o download daquele video especifico.

Motivo: transcricao baixada que ninguem le vira acervo morto (havia 67
transcricoes baixadas e nunca lidas em 27/08). A escolha e humana.

Uso:
    python _core/youtube-radar.py                  # varre tudo, gera o relatorio
    python _core/youtube-radar.py --dias 7         # janela custom (default 7)
    python _core/youtube-radar.py --squad marketing

Saida: data/youtube-radar/YYYY-MM-DD.md (lista numerada, pronta para escolher)
       e o mesmo conteudo no stdout.

Para BAIXAR o que foi escolhido, use o comando impresso no fim do relatorio:
    python _core/youtube-fetch-video.py --dir <dir do squad> <URL>
"""

import argparse
import io
import json
import os
import subprocess
import sys
from datetime import datetime, timedelta, timezone

REPO = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
SAIDA = os.path.join(REPO, "data", "youtube-radar")

# Mesmos squads/dirs do youtube-collect-all.py. Commercial entra aqui mesmo
# sem canal fixo — se um dia ganhar canal, o radar ja cobre.
SQUADS = [
    ("marketing",   "squads/marketing/data/youtube-intel"),
    ("operations",  "squads/operations/data/performance-intel"),
    ("dev",         "squads/dev/data/dev-intel"),
    ("infra",       "squads/infra/data/tech-intel"),
    ("commercial",  "squads/commercial/data/sales-intel"),
]


def run_ytdlp(args, timeout=180):
    try:
        p = subprocess.run(
            [sys.executable, "-m", "yt_dlp"] + args,
            capture_output=True, text=True, timeout=timeout,
            encoding="utf-8", errors="replace",
        )
        return p.stdout, p.stderr
    except subprocess.TimeoutExpired:
        return "", "timeout"
    except Exception as exc:  # yt-dlp ausente etc
        return "", str(exc)


def ja_temos(base):
    """IDs ja transcritos — nao entram no radar como novidade."""
    d = os.path.join(base, "transcripts")
    if not os.path.isdir(d):
        return set()
    return {f[:-5] for f in os.listdir(d) if f.endswith(".json")}


def lista_canal(ch, dias, maximo=15):
    """Lista videos recentes SEM baixar nada (flat-playlist)."""
    url = "https://www.youtube.com/channel/%s/videos" % ch["channel_id"]
    out, err = run_ytdlp([
        "--flat-playlist",
        "--playlist-items", "1-%d" % maximo,
        "--extractor-args", "youtube:lang=%s" % ch.get("lang", "pt"),
        "-J", url,
    ])
    if not out:
        return [], (err or "")[:160]
    try:
        data = json.loads(out)
    except json.JSONDecodeError:
        return [], "resposta invalida do yt-dlp"

    vids = []
    for e in data.get("entries") or []:
        if not e or not e.get("id"):
            continue
        vids.append({
            "id": e.get("id"),
            "titulo": (e.get("title") or "").strip(),
            "url": "https://www.youtube.com/watch?v=%s" % e.get("id"),
            "duracao": e.get("duration"),
            "views": e.get("view_count"),
            "ts": e.get("timestamp"),
        })
    return vids, None


def detalhes(ids):
    """Data/duracao/views reais, em UMA chamada para varios videos.

    O --flat-playlist nao traz upload_date (vem nulo), entao sem isto o filtro
    por janela nao funciona — foi o bug da primeira versao, que listava video
    de 3 meses atras como novidade da semana. O --print le so metadados:
    nao baixa video nem legenda.
    """
    if not ids:
        return {}
    urls = ["https://www.youtube.com/watch?v=%s" % i for i in ids]
    out, _ = run_ytdlp([
        "--skip-download", "--no-warnings",
        "--print", "%(id)s|%(upload_date)s|%(duration)s|%(view_count)s",
    ] + urls, timeout=max(120, 20 * len(ids)))
    info = {}
    for linha in (out or "").splitlines():
        partes = linha.strip().split("|")
        if len(partes) != 4:
            continue
        vid, data, dur, views = partes
        info[vid] = {
            "data": data if data and data != "NA" else None,
            "duracao": int(dur) if dur.isdigit() else None,
            "views": int(views) if views.isdigit() else None,
        }
    return info


def fmt_dur(seg):
    if not seg:
        return "?"
    seg = int(seg)
    return ("%dh%02d" % (seg // 3600, (seg % 3600) // 60)) if seg >= 3600 else "%dmin" % (seg // 60)


def fmt_views(v):
    if not v:
        return "?"
    if v >= 1_000_000:
        return "%.1fM" % (v / 1_000_000)
    if v >= 1_000:
        return "%.0fk" % (v / 1_000)
    return str(v)


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--dias", type=int, default=7, help="janela em dias (default 7)")
    ap.add_argument("--squad", help="varrer so um squad")
    ap.add_argument("--max", type=int, default=15, help="videos por canal a inspecionar")
    args = ap.parse_args()

    corte = datetime.now(timezone.utc) - timedelta(days=args.dias)
    hoje = datetime.now().strftime("%Y-%m-%d")
    L = []
    P = L.append

    P(u"# Radar YouTube — %s" % datetime.now().strftime("%d/%m/%Y"))
    P("")
    P(u"Janela: últimos **%d dias**. **Nada foi baixado** — esta é a lista para o Emerson escolher." % args.dias)
    P("")

    total = 0
    item = 0
    escolhas = []

    for nome, rel in SQUADS:
        if args.squad and args.squad != nome:
            continue
        base = os.path.join(REPO, rel)
        cf = os.path.join(base, "channels.json")
        if not os.path.exists(cf):
            continue
        chans = (json.load(io.open(cf, encoding="utf-8")) or {}).get("channels") or []
        if not chans:
            continue

        vistos = ja_temos(base)
        linhas_squad = []

        for ch in chans:
            if not ch.get("channel_id"):
                continue
            vids, erro = lista_canal(ch, args.dias, args.max)
            if erro:
                linhas_squad.append(u"- ⚠️ **%s** — erro ao listar: %s" % (ch.get("name"), erro))
                continue
            candidatos = [v for v in vids if v["id"] not in vistos]
            info = detalhes([v["id"] for v in candidatos])
            novos = []
            for v in candidatos:
                d = info.get(v["id"]) or {}
                if not d.get("data"):
                    continue  # sem data confiavel, nao entra
                dt = datetime.strptime(d["data"], "%Y%m%d").replace(tzinfo=timezone.utc)
                if dt < corte:
                    continue
                v["data"] = dt.strftime("%d/%m")
                v["duracao"] = d.get("duracao") or v.get("duracao")
                v["views"] = d.get("views") or v.get("views")
                novos.append(v)
            novos.sort(key=lambda x: x["data"], reverse=True)
            if not novos:
                continue
            linhas_squad.append(u"")
            linhas_squad.append(u"**%s**" % ch.get("name"))
            linhas_squad.append(u"")
            linhas_squad.append(u"| # | Data | Vídeo | Duração | Views |")
            linhas_squad.append(u"|---|---|---|---|---|")
            for v in novos:
                item += 1
                total += 1
                escolhas.append((item, nome, rel, v))
                linhas_squad.append(u"| **%d** | %s | [%s](%s) | %s | %s |" % (
                    item, v["data"], v["titulo"][:70], v["url"],
                    fmt_dur(v["duracao"]), fmt_views(v["views"])))

        if linhas_squad:
            P(u"## %s" % nome.upper())
            L.extend(linhas_squad)
            P("")

    if total == 0:
        P(u"**Nenhum vídeo novo na janela.** Nada a decidir esta semana.")
    else:
        P(u"---")
        P("")
        P(u"## Como escolher")
        P("")
        P(u"Responda com os números que quer transcritos — ex: `1, 4, 7`.")
        P(u"Só o que você escolher vira transcrição; o resto é descartado (fica no YouTube, pode ser pedido depois).")
        P("")
        P(u"**Total de candidatos: %d**" % total)
        P("")
        P(u"<!-- mapa para o agente baixar o escolhido -->")
        for n, squad, rel, v in escolhas:
            P(u"<!-- %d | %s | python _core/youtube-fetch-video.py --dir %s %s -->" % (n, squad, rel, v["url"]))

    txt = u"\n".join(L)
    if not os.path.isdir(SAIDA):
        os.makedirs(SAIDA)
    # varredura pontual (squad especifico ou janela != semanal) nao pode
    # sobrescrever o radar semanal do mesmo dia
    sufixo = ""
    if args.squad:
        sufixo += "-" + args.squad
    if args.dias != 7:
        sufixo += "-%dd" % args.dias
    dest = os.path.join(SAIDA, hoje + sufixo + ".md")
    io.open(dest, "w", encoding="utf-8").write(txt)
    sys.stdout.write(txt.encode("ascii", "replace").decode() + "\n")
    sys.stderr.write("\n[radar] salvo em %s\n" % dest)


if __name__ == "__main__":
    main()
