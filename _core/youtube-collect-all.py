#!/usr/bin/env python3
"""
Coleta de inteligencia de YouTube para todos os squads, cada um na sua cadencia.

Cada squad tem uma frequencia propria, derivada de quanto os canais dele
realmente publicam. Rodar tudo semanalmente geraria coletas vazias.

Uso:
    python _core/youtube-collect-all.py            # respeita a cadencia
    python _core/youtube-collect-all.py --force    # ignora a cadencia
    python _core/youtube-collect-all.py --squad dev

O controle de cadencia usa .last-run em cada diretorio de dados. Quem chama
(Task Scheduler) pode rodar diariamente: os squads fora da janela sao pulados.

Saida: grava um resumo em _core/.youtube-pending.md, que a skill /update-all
le para saber o que ainda precisa de analise.
"""

import argparse
import io
import json
import os
import subprocess
import sys
from datetime import datetime, timedelta

REPO = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
COLLECTOR = os.path.join(REPO, "_core", "youtube-collect.py")
PENDING = os.path.join(REPO, "_core", ".youtube-pending.md")

# dias_entre_coletas = cadencia; janela = quantos dias de video buscar.
# A janela e maior que a cadencia de proposito, para dar sobreposicao e nao
# perder video caso uma execucao falhe (o cache evita rebaixar).
SQUADS = [
    {
        "nome": "marketing",
        "dir": "squads/marketing/data/youtube-intel",
        "cadencia_dias": 7,
        "janela_dias": 10,
        "max": 8,
        "assunto": "crescimento no YouTube, roteiro, canal como negocio",
    },
    {
        "nome": "dev",
        "dir": "squads/dev/data/dev-intel",
        "cadencia_dias": 14,
        "janela_dias": 30,
        "max": 10,
        "assunto": "praticas de engenharia, ecossistema, arquitetura de agentes",
    },
    {
        "nome": "infra",
        "dir": "squads/infra/data/tech-intel",
        "cadencia_dias": 28,
        "janela_dias": 60,
        "max": 8,
        "assunto": "decisao de stack, banco, custo e confiabilidade",
    },
    {
        "nome": "operations",
        "dir": "squads/operations/data/performance-intel",
        "cadencia_dias": 14,
        "janela_dias": 30,
        "max": 8,
        "assunto": "metas, alta performance, decisao do que fazer no dia",
    },
]


LOGFILE = os.path.join(REPO, "_core", ".youtube-collect.log")
_log_buffer = []


def log(msg):
    """Escreve no console e acumula para o arquivo de log.

    Sob o Task Scheduler com pythonw.exe nao existe console: sys.stdout pode
    ser None ou lancar erro. O log em arquivo e a fonte de verdade para
    depurar execucao agendada.
    """
    _log_buffer.append(msg)
    try:
        if sys.stdout is not None:
            sys.stdout.write(msg + "\n")
            sys.stdout.flush()
    except (OSError, ValueError, AttributeError):
        pass  # sem console: o arquivo de log basta


def gravar_log():
    try:
        with io.open(LOGFILE, "w", encoding="utf-8") as fh:
            fh.write("\n".join(_log_buffer) + "\n")
    except OSError:
        pass


def last_run_path(squad):
    return os.path.join(REPO, squad["dir"], ".last-run")


def deve_rodar(squad, force):
    if force:
        return True, "forcado"
    path = last_run_path(squad)
    if not os.path.exists(path):
        return True, "primeira coleta"
    try:
        marca = datetime.fromisoformat(
            io.open(path, encoding="utf-8").read().strip()
        )
    except (ValueError, OSError):
        return True, "marca invalida"
    dias = (datetime.now() - marca).days
    if dias >= squad["cadencia_dias"]:
        return True, f"ultima ha {dias}d"
    return False, f"ultima ha {dias}d (cadencia {squad['cadencia_dias']}d)"


def marcar_rodado(squad):
    io.open(last_run_path(squad), "w", encoding="utf-8").write(
        datetime.now().isoformat(timespec="seconds")
    )


def contar_transcricoes(squad):
    d = os.path.join(REPO, squad["dir"], "transcripts")
    if not os.path.isdir(d):
        return set()
    return {f for f in os.listdir(d) if f.endswith(".json")}


def marca_analise_path(squad):
    return os.path.join(REPO, squad["dir"], ".last-analyzed")


def nao_analisados(squad):
    """Transcricoes coletadas depois da ultima analise.

    Derivar do disco (em vez de so olhar o que surgiu nesta execucao) faz o
    pendente sobreviver a execucoes repetidas: enquanto /update-all nao
    marcar a analise, os videos continuam aparecendo como pendentes.
    """
    path = marca_analise_path(squad)
    corte = None
    if os.path.exists(path):
        try:
            corte = datetime.fromisoformat(
                io.open(path, encoding="utf-8").read().strip()
            )
        except (ValueError, OSError):
            corte = None

    d = os.path.join(REPO, squad["dir"], "transcripts")
    if not os.path.isdir(d):
        return []
    pendentes = []
    for nome in os.listdir(d):
        if not nome.endswith(".json"):
            continue
        caminho = os.path.join(d, nome)
        try:
            reg = json.load(io.open(caminho, encoding="utf-8"))
            coletado = datetime.fromisoformat(
                reg["collected_at"].replace("Z", "+00:00")
            ).replace(tzinfo=None)
        except (OSError, json.JSONDecodeError, KeyError, ValueError):
            continue
        if corte is None or coletado > corte:
            pendentes.append(nome)
    return pendentes


def coletar(squad):
    """Roda o coletor e devolve os arquivos novos que surgiram."""
    antes = contar_transcricoes(squad)
    cmd = [
        sys.executable,
        COLLECTOR,
        "--dir", squad["dir"],
        "--days", str(squad["janela_dias"]),
        "--max", str(squad["max"]),
    ]
    env = dict(os.environ, PYTHONIOENCODING="utf-8")
    try:
        proc = subprocess.run(
            cmd, capture_output=True, timeout=3600, env=env, cwd=REPO
        )
        saida = proc.stdout.decode("utf-8", errors="replace")
    except subprocess.TimeoutExpired:
        return None, "timeout na coleta"

    depois = contar_transcricoes(squad)
    return sorted(depois - antes), saida


def descrever(squad, novos):
    """Le titulo e canal dos videos novos, para o resumo."""
    d = os.path.join(REPO, squad["dir"], "transcripts")
    itens = []
    for nome in novos:
        try:
            reg = json.load(io.open(os.path.join(d, nome), encoding="utf-8"))
        except (OSError, json.JSONDecodeError):
            continue
        itens.append(
            {
                "titulo": reg.get("title", "?"),
                "canal": reg.get("channel", "?"),
                "data": reg.get("upload_date", "?"),
                "palavras": reg.get("transcript_words", 0),
                "url": reg.get("url", ""),
            }
        )
    itens.sort(key=lambda i: i["data"], reverse=True)
    return itens


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--force", action="store_true", help="ignora a cadencia")
    ap.add_argument("--squad", help="roda so este squad")
    args = ap.parse_args()

    alvos = [s for s in SQUADS if not args.squad or s["nome"] == args.squad]
    if not alvos:
        log(f"squad desconhecido: {args.squad}")
        sys.exit(1)

    log(f"Coleta HIVE — {datetime.now().strftime('%Y-%m-%d %H:%M')}")
    log("")

    resumo = []
    for squad in alvos:
        rodar, motivo = deve_rodar(squad, args.force)
        if not rodar:
            log(f"[{squad['nome']}] pulado — {motivo}")
            continue

        log(f"[{squad['nome']}] coletando — {motivo}")
        novos, saida = coletar(squad)
        if novos is None:
            log(f"  ERRO: {saida}")
            continue

        marcar_rodado(squad)
        itens = descrever(squad, novos)
        if itens:
            for i in itens:
                log(f"  + [{i['canal']}] {i['titulo'][:52]} ({i['palavras']}p)")
        else:
            log("  nada novo nesta coleta")
        log("")

    # O pendente e derivado do disco, nao do que surgiu nesta execucao: assim
    # ele sobrevive a execucoes repetidas ate /update-all analisar de fato.
    for squad in SQUADS:
        itens = descrever(squad, nao_analisados(squad))
        if itens:
            resumo.append((squad, itens))

    # grava o pendente, que a skill /update-all consome
    linhas = [
        "# Coleta pendente de analise",
        "",
        f"> Gerado por `_core/youtube-collect-all.py` em "
        f"{datetime.now().strftime('%Y-%m-%d %H:%M')}.",
        "> Rode `/update-all` para analisar. Apagado ao ser analisado.",
        "",
    ]
    total = 0
    for squad, itens in resumo:
        if not itens:
            continue
        total += len(itens)
        linhas.append(f"## {squad['nome']} — {len(itens)} video(s) novo(s)")
        linhas.append(f"_{squad['assunto']}_")
        linhas.append("")
        for i in itens:
            linhas.append(
                f"- **{i['titulo']}** — {i['canal']}, {i['data']} "
                f"({i['palavras']} palavras) — {i['url']}"
            )
        linhas.append("")

    # O pendente reflete sempre o estado real do disco: some so quando tudo
    # foi analisado (marcado em .last-analyzed por /update-all), e sobrevive
    # a execucoes repetidas enquanto houver video sem analise.
    log("=" * 60)
    if total:
        io.open(PENDING, "w", encoding="utf-8").write("\n".join(linhas))
        log(f"{total} video(s) aguardando analise. Rode /update-all.")
    else:
        if os.path.exists(PENDING):
            os.remove(PENDING)
        log("Nada pendente — tudo coletado ja foi analisado.")


if __name__ == "__main__":
    try:
        main()
    except Exception as exc:  # noqa: BLE001 — precisa registrar qualquer falha
        import traceback

        log("")
        log("ERRO NAO TRATADO:")
        log(traceback.format_exc())
        gravar_log()
        sys.exit(1)
    gravar_log()
