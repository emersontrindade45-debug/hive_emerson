#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""UserPromptSubmit - Squad Routing.

Detecta o squad pelo assunto e anuncia a SKILL OBRIGATORIA correspondente.
Regra do CLAUDE.md raiz: squad acionado, skill acionada.

Palavras-chave em PT-BR (o Emerson escreve em portugues) + personas corretas
do HIVE. A versao anterior usava termos em ingles e personas de outro projeto
(Victor/Maya/Owen), entao "roteiro", "meta" e "vender" nao disparavam nada.
"""
import json, sys

SQUADS = {
    "commercial": ["comercial","vend","venda","lead","pipeline","proposta","crm","tatiane",
                   "negocia","prospec","cliente","precific","preco","preço","orcamento","icp","araujo","araújo"],
    "cs":         ["customer success","onboarding","churn","health score","figueiredo","retencao","retenção","nps","suporte"],
    "marketing":  ["marketing","conteudo","conteúdo","marca","campanha","rede social","pietro","copy","audiencia","audiência",
                   "seo","roteiro","video","vídeo","canal","youtube","hook","thumbnail","titulo","título","pauta",
                   "storytelling","retencao de video","instagram","tiktok","linkedin","bio","territorio","território","tese"],
    "product":    ["produto","roadmap","story","sprint","feature","paes","backlog","prioriza","user story"],
    "finance":    ["financeiro","finance","fatura","fluxo de caixa","orcamento mensal","lorenzo","receita","despesa",
                   "p&l","dre","imposto","cobranca","cobrança","custo","caixa","mei"],
    "dev":        ["dev","codigo","código","bug","pull request","brenda","branch","arquitetura","refatora","teste",
                   "typescript","python","deploy de codigo","api"],
    "infra":      ["infra","servidor","deploy","dns","ssl","monitoramento","emilly","vps","ci/cd","docker",
                   "kubernetes","nginx","backup","seguranca","segurança","credencial"],
    "operations": ["operacoes","operações","contrata","okr","cultura","cristina","sop","processo","meta","metas",
                   "trimestre","rotina","prioridade","planejamento","produtividade","neotriad","agenda","o que faco","o que faço"],
    "quality":    ["qualidade","auditoria","padrao","padrão","trindade","stranger test","checklist"],
    "intelligence":["inteligencia","inteligência","concorrente","concorrencia","concorrência","pesquisa de mercado",
                    "war game","bias","oportunidade","modelo de negocio","modelo de negócio","recorrencia","recorrência",
                    "escala","margem","vale a pena","monetiz"],
    "orchestrator":["stamper","orquestr","todos os squads","status da empresa","visao geral","visão geral","semanal"],
}

# Squad -> (skill, gatilho). Squads sem acervo destilado nao entram.
SKILLS = {
    "marketing":   [("roteiro-youtube",    "roteiro, hook, titulo, thumbnail, pauta"),
                    ("influencia-digital", "marca, territorio, tese, bio, Hero/Hub/Help"),
                    ("dados-verificados",  "qualquer numero/estatistica que va ao ar")],
    "operations":  [("metas-performance",  "meta, trimestre, rotina, prioridade, Neotriad")],
    "commercial":  [("vendas",             "venda, proposta, negociacao, lead, ICP"),
                    ("modelo-de-negocios", "ao precificar: preco sai do ROI do cliente")],
    "intelligence":[("modelo-de-negocios", "oportunidade nova, os 3 pilares")],
}

SEM_ACERVO = {"dev","infra","cs","product","finance","quality"}


def detect(prompt):
    pl = prompt.lower()
    return [s for s, kws in SQUADS.items() if any(kw in pl for kw in kws)]


def anuncia_skills(squads):
    linhas, vistos = [], set()
    for s in squads:
        for nome, gatilho in SKILLS.get(s, []):
            if nome in vistos:
                continue
            vistos.add(nome)
            linhas.append("  -> SKILL OBRIGATORIA: %s  (%s)" % (nome, gatilho))
    if linhas:
        print("[hive/skills] Squad acionado, skill acionada - invocar ANTES de responder:")
        for l in linhas:
            print(l)
    sem = [s for s in squads if s in SEM_ACERVO]
    if sem:
        print("[hive/skills] Sem acervo destilado: %s - nao improvisar como se houvesse."
              % ", ".join(sem))


def main():
    try:
        data = json.loads(sys.stdin.read())
    except Exception:
        sys.exit(0)
    prompt = data.get("prompt", "")
    if not prompt:
        sys.exit(0)
    squads = detect(prompt)
    if not squads:
        sys.exit(0)
    if len(squads) == 1:
        s = squads[0]
        print("[hive/routing] Squad detectado: %s" % s)
        print("  Contexto: squads/%s/CLAUDE.md | Estado: squads/%s/memory/STATE.md" % (s, s))
        if s != "orchestrator":
            print("  /open-squad %s para o contexto completo" % s)
    else:
        print("[hive/routing] Multiplos squads: %s" % ", ".join(squads))
        for s in squads:
            print("  squads/%s/" % s)
    anuncia_skills(squads)
    sys.exit(0)


if __name__ == "__main__":
    main()
