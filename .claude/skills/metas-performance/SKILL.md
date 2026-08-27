---
name: metas-performance
description: Use ao definir meta, planejar trimestre, priorizar o dia, montar rotina ou decidir "o que fazer agora" — e sempre que o squad Operations for acionado. Cobre o método de metas do Joel Jota, a Tríade do Tempo e a operação no Neotriad. Dispara em "meta", "objetivo", "trimestre", "prioridade", "rotina", "o que faço hoje", "planejamento", "produtividade", "Neotriad", "agenda", "revisão semanal".
---

# Metas e Alta Performance

**Squad:** Operations (Cristina)

⚠️ **Joel Jota tem DOIS materiais neste repo.** Este é o de **Alta Performance** (metas, rotina, produtividade). Assunto de rede social/marca vai para a skill `influencia-digital`. Nunca trocar um pelo outro.

## Passo 1 — Ler a fonte

**`squads/operations/foundation/alta-performance-playbook.md`** (384 linhas), níveis conforme a pergunta:

| Pergunta | Nível |
|---|---|
| "Para onde estou indo?" | Nível 1 — Direção |
| "Qual a meta?" | Nível 2 — Meta |
| "Meta de quanto tempo?" | Nível 3 — Trimestre, não ano |
| "Como virar tarefa?" | Nível 4 — Desdobrar |
| "O que faço hoje?" | Nível 5 — Operacional + Rotina diária |
| "Isso é urgente ou importante?" | Tríade do Tempo (Christian Barbosa) |

E o plano vigente: **`squads/operations/foundation/plano-trimestral-2026-Q4.md`** (23/08 a 31/10).

## Passo 2 — Respeitar as travas da agenda

- **20h/semana** para o negócio — 4h/dia (2h manhã + 2h tarde), seg a sex. **Sábado é da família.**
- **Bloco A (Araújo)** 09:00–11:00 seg–sex · **Bloco B (Conteúdo)** 14:00–16:00 seg–qui · **Revisão** sex 14:00–15:00
- **Regra de colisão atual (26/08): quando conteúdo e Araújo disputarem a mesma hora, CONTEÚDO GANHA.** Isso inverteu a regra original do plano — o Araújo está bloqueado por terceiro.
- **Meta SMART do trimestre: 4 vídeos publicados até 09/10.** Indicador semanal: vídeos publicados (acumulado).
- Regra ao falhar: falhou um dia → retoma no seguinte. Falhou a semana → revisa o **marco**, nunca a meta.

## Passo 3 — Neotriad (integração ativa)

Leitura: `python _core/neotriad.py status|hoje|papeis`

Escrita — **ler `_core/neotriad.py` antes**, o docstring traz as pegadinhas. As três que mais custam:
- Corpo de POST/PUT/DELETE é sempre **lista**, mesmo para 1 item
- **Papel só grava no POST** e no formato `Papel:[{"id_papel":"<guid>"}]` — lista de GUIDs devolve 201 e é **ignorada em silêncio**
- **Não existe endpoint de metas nem de projetos** — meta só se cria na interface web

Papel EMPREENDEDOR em uso: `ae2604df-bfa6-4673-a809-0d715a240367` (há um duplicado com zero uso — não usar a descrição para escolher, usar a contagem).

## Passo 4 — O padrão a evitar

Registrado no STATE do orchestrator: 134 databases, 6 bases de tarefas, 3 planners. **Quando algo não anda, a resposta tem sido criar estrutura nova.** O gargalo declarado do negócio é **execução, não estrutura** — propor mais estrutura é quase sempre a resposta errada.

## Ressalva sobre a Tríade

100% das tarefas do Emerson no Neotriad estão marcadas como "I" (Importante), contra alvo de 70%. Se tudo é importante, a tríade deixa de ordenar. Reclassificar as recorrências de rotina faria o painel voltar a informar.
