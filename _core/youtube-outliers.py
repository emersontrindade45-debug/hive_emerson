#!/usr/bin/env python3
"""
Descoberta de OUTLIER em canal de porte definido — worker da divisao M2 (Intelligence).

Diferente de youtube-gaps.py, que busca por TERMO e mede views/inscritos, este
worker parte do CANAL: acha canais dentro de uma faixa de inscritos e pergunta
quais videos recentes bateram muito acima da propria media do canal.

Tese do sinal (Emerson, 2026-08-26):
    Canal de 10k-20k inscritos e grande o bastante para ter base estavel e
    pequeno o bastante para nao ser empurrado por marca. Nessa faixa, video
    que estoura acima da media do proprio canal esta estourando pelo TEMA.
    Comparar o video com o canal dele mesmo remove o tamanho do canal da conta.

Como mede:
    baseline = MEDIANA de views dos videos maduros do canal (fora da janela).
    multiplo = views do video recente / baseline.
    Usa mediana, nao media: um unico viral antigo distorce media e nao mediana.

VIES CONHECIDO — o resultado e conservador:
    Video de 3 dias e comparado com videos que tiveram meses para acumular view.
    Logo o multiplo SUBESTIMA o desempenho do video novo. Quem passa do corte
    passou com folga; quem nao passou nao esta necessariamente mal.

Uso:
    python _core/youtube-outliers.py --termos-arquivo squads/marketing/data/youtube-intel/termos.json
    python _core/youtube-outliers.py --min-insc 10000 --max-insc 20000 --dias 7

IMPORTANTE: rode sempre da raiz do repo. Nao use "cd" para subpasta —
os hooks de sessao do HIVE resolvem caminho relativo ao cwd e quebram.
"""

import argparse
import json
import os
import statistics
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


def linhas_json(out):
    itens = []
    for line in out.splitlines():
        line = line.strip()
        if not line.startswith("{"):
            continue
        try:
            itens.append(json.loads(line))
        except json.JSONDecodeError:
            continue
    return itens


def descobrir_canais(termos, max_busca, pausa):
    """Fase 1: varre a busca por termo so para colher canais distintos."""
    canais = {}
    for t in termos:
        out, err, rc = run_ytdlp([
            f"ytsearch{max_busca}:{t}",
            "--flat-playlist", "--dump-json",
            "--no-warnings", "--user-agent", UA,
        ], timeout=300)
        achados = linhas_json(out)
        novos = 0
        for a in achados:
            cid = a.get("channel_id")
            if not cid or cid in canais:
                continue
            canais[cid] = {
                "canal_id": cid,
                "canal": a.get("channel"),
                "canal_url": a.get("channel_url") or f"https://www.youtube.com/channel/{cid}",
                "achado_em": t,
            }
            novos += 1
        log(f"  [busca] {t[:44]:44} {len(achados):>3} videos, +{novos} canais")
        time.sleep(pausa)
    return list(canais.values())


def inscritos_do_canal(canal_url):
    """Fase 2: 1 chamada por canal, sem listar video, so para pegar inscritos."""
    out, err, rc = run_ytdlp([
        canal_url, "--playlist-items", "0", "-J",
        "--no-warnings", "--user-agent", UA,
    ], timeout=120)
    if rc != 0 or not out.strip():
        return None
    try:
        d = json.loads(out)
    except json.JSONDecodeError:
        return None
    return d.get("channel_follower_count")


def listar_videos(canal_url, quantos):
    """Lista rasa da aba /videos — mais novo primeiro, com view_count."""
    base = canal_url.rstrip("/")
    if not base.endswith("/videos"):
        base += "/videos"
    out, err, rc = run_ytdlp([
        base, "--flat-playlist", "--playlist-end", str(quantos),
        "--dump-json", "--no-warnings", "--user-agent", UA,
    ], timeout=240)
    return linhas_json(out)


def detalhar(video_id):
    """Metadados completos de 1 video — traz upload_date e titulo original."""
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


def classificar(multiplo):
    if multiplo >= 5:
        return "OUTLIER FORTE", "muito acima da propria base do canal"
    if multiplo >= 2:
        return "OUTLIER", "dobrou ou mais a mediana do canal"
    if multiplo >= 1.2:
        return "ACIMA DA MEDIA", "performance boa para o canal"
    return "NORMAL", "dentro da base do canal"


def analisar_canal(c, dias, recentes, amostra, min_maduros, pausa):
    """Fase 3: separa video recente de video maduro e compara um com o outro."""
    vids = listar_videos(c["canal_url"], amostra)
    if len(vids) < min_maduros + 1:
        return [], f"so {len(vids)} videos listados"

    corte = datetime.now(timezone.utc) - timedelta(days=dias)
    recentes_ok, idx_ultimo_recente = [], -1

    # a aba /videos vem do mais novo pro mais velho: para no 1o fora da janela
    for i, v in enumerate(vids[:recentes]):
        vid = v.get("id")
        if not vid:
            continue
        d = detalhar(vid)
        time.sleep(pausa)
        if not d:
            continue
        up = d.get("upload_date")
        if not up:
            continue
        try:
            dt = datetime.strptime(up, "%Y%m%d").replace(tzinfo=timezone.utc)
        except ValueError:
            continue
        if dt < corte:
            break
        idx_ultimo_recente = i
        recentes_ok.append((i, d))

    if not recentes_ok:
        return [], "nenhum video na janela"

    maduros_raso = [v for v in vids[idx_ultimo_recente + 1:] if (v.get("view_count") or 0) > 0]
    if len(maduros_raso) < min_maduros:
        return [], f"so {len(maduros_raso)} videos maduros para baseline"

    baseline = statistics.median([v["view_count"] for v in maduros_raso])
    if baseline <= 0:
        return [], "baseline zerada"

    # engajamento: detalha uma amostra dos maduros mais proximos da janela para
    # pegar likes/comentarios reais (a listagem rasa nao traz isso) e calcular
    # a TAXA de comentario/curtida tipica do canal, nao so o volume de views.
    amostra_engaj = maduros_raso[:min_maduros]
    taxas_coment, taxas_like = [], []
    for v in amostra_engaj:
        vid = v.get("id")
        if not vid:
            continue
        dm = detalhar(vid)
        time.sleep(pausa)
        if not dm:
            continue
        vv = dm.get("view_count") or 0
        if vv <= 0:
            continue
        taxas_coment.append((dm.get("comment_count") or 0) / vv)
        taxas_like.append((dm.get("like_count") or 0) / vv)

    base_coment = statistics.median(taxas_coment) if taxas_coment else 0.0
    base_like = statistics.median(taxas_like) if taxas_like else 0.0

    saida = []
    for _, d in recentes_ok:
        views = d.get("view_count") or 0
        mult = views / baseline
        rotulo, motivo = classificar(mult)
        up = d.get("upload_date")
        idade = (datetime.now(timezone.utc) -
                 datetime.strptime(up, "%Y%m%d").replace(tzinfo=timezone.utc)).days

        comentarios = d.get("comment_count") or 0
        likes = d.get("like_count") or 0
        taxa_coment = (comentarios / views) if views else 0.0
        taxa_like = (likes / views) if views else 0.0
        # multiplo de engajamento: taxa do video / taxa tipica do canal.
        # protegido contra canal com base_coment=0 (canal com comentario raro
        # onde qualquer comentario novo faria a divisao explodir sem sentido)
        mult_coment = (taxa_coment / base_coment) if base_coment > 0 else (
            float("inf") if comentarios > 0 else 0.0)

        saida.append({
            "canal": c["canal"],
            "canal_url": c["canal_url"],
            "inscritos": c["inscritos"],
            "achado_em": c["achado_em"],
            "video_id": d.get("id"),
            "titulo": d.get("title"),
            "url": f"https://www.youtube.com/watch?v={d.get('id')}",
            "upload_date": up,
            "idade_dias": idade,
            "views": views,
            "baseline_mediana": int(baseline),
            "baseline_n": len(maduros_raso),
            "multiplo": round(mult, 2),
            "likes": likes,
            "comentarios": comentarios,
            "taxa_comentario_pct": round(taxa_coment * 100, 3),
            "taxa_like_pct": round(taxa_like * 100, 3),
            "baseline_taxa_comentario_pct": round(base_coment * 100, 3),
            "baseline_taxa_like_pct": round(base_like * 100, 3),
            "multiplo_engajamento": (round(mult_coment, 2)
                                      if mult_coment != float("inf") else None),
            "duracao_seg": d.get("duration"),
            "sinal": rotulo,
            "motivo": motivo,
        })
    return saida, None


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--termos", help="termos separados por virgula")
    ap.add_argument("--canais-arquivo", help="json de uma rodada anterior: reusa o "
                    "painel de canais em vez de redescobrir. Cohort fixo e o que "
                    "torna comparacao entre semanas valida")
    ap.add_argument("--termos-arquivo", help="json com lista em 'termos'")
    ap.add_argument("--min-insc", type=int, default=10000)
    ap.add_argument("--max-insc", type=int, default=20000)
    ap.add_argument("--dias", type=int, default=7, help="janela de 'recente' (default 7)")
    ap.add_argument("--max-busca", type=int, default=30, help="resultados por termo na descoberta")
    ap.add_argument("--recentes", type=int, default=6, help="quantos videos do topo checar por canal")
    ap.add_argument("--amostra", type=int, default=30, help="videos listados por canal")
    ap.add_argument("--min-maduros", type=int, default=6, help="minimo de videos para baseline confiavel")
    ap.add_argument("--max-canais", type=int, default=0, help="teto de canais a analisar (0 = sem teto)")
    ap.add_argument("--pausa", type=float, default=1.2)
    ap.add_argument("--out", default="squads/marketing/data/youtube-intel/outliers")
    a = ap.parse_args()

    # painel fixo: pula fase 1 e 2 e vai direto pros canais ja conhecidos
    if a.canais_arquivo:
        with open(a.canais_arquivo, encoding="utf-8") as f:
            prev = json.load(f)
        vistos, na_faixa = set(), []
        for x in prev["achados"]:
            if x["canal_url"] in vistos:
                continue
            vistos.add(x["canal_url"])
            na_faixa.append({"canal": x["canal"], "canal_url": x["canal_url"],
                             "inscritos": x["inscritos"], "achado_em": x.get("achado_em")})
        log(f"painel fixo: {len(na_faixa)} canais reusados de {a.canais_arquivo}")
        termos = prev.get("termos", [])
        canais = na_faixa
        return rodar_fase3(a, termos, canais, na_faixa)

    if a.termos_arquivo:
        with open(a.termos_arquivo, encoding="utf-8") as f:
            termos = json.load(f)["termos"]
    elif a.termos:
        termos = [t.strip() for t in a.termos.split(",") if t.strip()]
    else:
        log("informe --termos ou --termos-arquivo")
        return 2

    log(f"FASE 1 — descobrindo canais em {len(termos)} termos")
    canais = descobrir_canais(termos, a.max_busca, a.pausa)
    log(f"  {len(canais)} canais distintos")

    log(f"\nFASE 2 — filtrando por {a.min_insc:,}-{a.max_insc:,} inscritos")
    na_faixa = []
    for i, c in enumerate(canais, 1):
        subs = inscritos_do_canal(c["canal_url"])
        time.sleep(a.pausa)
        if subs is None:
            continue
        if a.min_insc <= subs <= a.max_insc:
            c["inscritos"] = subs
            na_faixa.append(c)
            log(f"  [{i}/{len(canais)}] ✓ {subs:>8,}  {str(c['canal'])[:46]}")
    log(f"  {len(na_faixa)} canais na faixa")

    if a.max_canais:
        na_faixa = na_faixa[:a.max_canais]

    return rodar_fase3(a, termos, canais, na_faixa)


def rodar_fase3(a, termos, canais, na_faixa):
    log(f"\nFASE 3 — outliers dos ultimos {a.dias} dias")
    achados, sem_dado = [], []
    for i, c in enumerate(na_faixa, 1):
        res, motivo = analisar_canal(c, a.dias, a.recentes, a.amostra,
                                     a.min_maduros, a.pausa)
        if motivo:
            sem_dado.append({"canal": c["canal"], "motivo": motivo})
            log(f"  [{i}/{len(na_faixa)}] — {str(c['canal'])[:40]:40} {motivo}")
            continue
        for r in res:
            achados.append(r)
            log(f"  [{i}/{len(na_faixa)}] {r['multiplo']:6.1f}x {r['sinal']:14s} "
                f"{r['views']:>8,}v vs {r['baseline_mediana']:>8,}  {str(r['titulo'])[:44]}")

    # ordena por engajamento primeiro (o pedido e comentario/curtida, nao view
    # crua) e usa o multiplo de views como desempate para quem nao tem taxa
    achados.sort(key=lambda x: (
        x["multiplo_engajamento"] if x["multiplo_engajamento"] is not None else -1,
        x["multiplo"],
    ), reverse=True)
    os.makedirs(a.out, exist_ok=True)
    dest = os.path.join(a.out, f"{datetime.now().strftime('%Y-%m-%d')}.json")
    with open(dest, "w", encoding="utf-8") as f:
        json.dump({
            "gerado_em": datetime.now(timezone.utc).isoformat(),
            "termos": termos,
            "parametros": {
                "min_insc": a.min_insc, "max_insc": a.max_insc, "dias": a.dias,
                "max_busca": a.max_busca, "amostra": a.amostra,
                "min_maduros": a.min_maduros,
            },
            "canais_descobertos": len(canais),
            "canais_na_faixa": len(na_faixa),
            "videos_na_janela": len(achados),
            "canais_sem_dado": sem_dado,
            "achados": achados,
        }, f, ensure_ascii=False, indent=2)

    log(f"\n{'='*64}")
    log(f"canais {len(canais)} → na faixa {len(na_faixa)} → videos na janela {len(achados)}")
    log(f"salvo em: {dest}")
    log(f"{'='*64}")
    log("  views_mult | engaj_mult | coment% (base%) | canal | video")
    for r in achados[:25]:
        em = r["multiplo_engajamento"]
        em_s = f"{em:5.1f}x" if em is not None else "  inf"
        log(f"  {r['multiplo']:6.1f}x | {em_s} | {r['taxa_comentario_pct']:.3f}% "
            f"({r['baseline_taxa_comentario_pct']:.3f}%) | {str(r['canal'])[:20]:20} "
            f"{str(r['titulo'])[:40]}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
