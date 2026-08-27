---
name: radar-youtube
description: Use toda SEGUNDA-FEIRA, ou quando o Emerson pedir o radar/lista de vídeos novos dos canais monitorados. Lista o que foi publicado SEM baixar transcrição — o Emerson escolhe quais valem, e só então elas são baixadas e viram skill. Dispara em "radar", "o que saiu de novo", "lista da semana", "vídeos novos", "segunda-feira", "o que os canais postaram".
---

# Radar YouTube — lista semanal para decisão

**Decisão do Emerson (27/08/2026): nada de transcrição baixada automaticamente.**

## A regra

O agente **lista**, o Emerson **escolhe**, só então o agente **baixa**.

Transcrição baixada que ninguém lê vira acervo morto — em 27/08 havia **67 transcrições baixadas e nunca lidas** (Dev, Infra, Commercial). A escolha do que merece virar conhecimento é humana, não automática.

## Passo 1 — Rodar o radar (segunda-feira)

```bash
python _core/youtube-radar.py --dias 7
```

Varre **todos os canais de todos os squads** e salva em `data/youtube-radar/YYYY-MM-DD.md`. Não baixa vídeo nem legenda — só lê metadados (título, data, duração, views).

Opções: `--dias N` (janela) · `--squad <nome>` (um squad só) · `--max N` (vídeos inspecionados por canal).

## Passo 2 — Apresentar a lista ao Emerson

Mostrar a tabela numerada por squad e canal. Pedir os números que ele quer transcritos.

**Não opinar antes de ele escolher, a menos que ele peça.** Se pedir recomendação, usar como critério: cruzamento com os pilares do canal, prazo do trimestre e lacunas conhecidas do acervo — nunca views isoladas.

## Passo 3 — Baixar SÓ o escolhido

O rodapé do relatório traz o comando pronto de cada item, em comentário HTML:

```bash
python _core/youtube-fetch-video.py --dir <dir do squad> <URL>
```

O que não foi escolhido é descartado — fica no YouTube e pode ser pedido depois.

## Passo 4 — Destilar em skill

Transcrição baixada **não é o fim**. Ela precisa virar entrada no playbook do squad dono e, por consequência, alimentar a skill correspondente:

| Squad | Playbook | Skill alimentada |
|---|---|---|
| marketing | `foundation/youtube-playbook.md` | `roteiro-youtube` |
| operations | `foundation/alta-performance-playbook.md` | `metas-performance` |
| commercial | `foundation/sales-playbook.md` | `vendas` |
| intelligence | `foundation/business-opportunities.md` | `modelo-de-negocios` |
| dev, infra | *sem playbook ainda* | — |

**Regra de precedência:** entrada nova que conflita com uma existente vale pela **data de publicação da fonte mais recente**, não pela ordem de registro.

## Canais monitorados (10)

| Squad | Canais |
|---|---|
| marketing | Nerds de Negócios · Guria de Negócios · Gabriel Tomaz · JP Labs · Larissa Gomes · Itamar Rocha · onsmartAI · Julio |
| operations | **Joel Jota** · Neotriad |
| dev | Fireship · freeCodeCamp · Programming with Mosh |
| infra | NetworkChuck · Anton Putra · ByteByteGo |
| commercial | *nenhum fixo — sob demanda* |

Para adicionar canal: incluir em `squads/<squad>/data/<intel>/channels.json` com `channel_id`.

## ⚠️ Coleta automática está DESLIGADA

A tarefa `HIVE-YouTube-Intel` do Windows, que baixava transcrição sozinha, foi desativada em 27/08 por esta decisão. Se ela reaparecer ativa, é regressão — desligar de novo.
