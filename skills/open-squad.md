# /open-squad

Loads a squad's full context into the session: CLAUDE.md persona, STATE.md current status, and context/squad-context.md company data.

## Usage

```
/open-squad commercial
/open-squad dev
/open-squad infra
```

## When to activate

- "open [squad name]", "switch to [squad]", "work on [area]"
- `/open-squad <name>` explicit invocation

---

## Steps

### 1 — Validate squad exists

Check that `squads/<name>/` exists and has a `CLAUDE.md`.

If not found:
```
Squad '<name>' not found. Available squads:
commercial, cs, marketing, product, finance, dev, infra, operations, quality, intelligence, orchestrator
```

### 2 — Read squad files (in order)

1. `squads/<name>/CLAUDE.md` — persona, scope, rules
2. `squads/<name>/memory/STATE.md` — current L1/L2/L3
3. `squads/<name>/context/squad-context.md` — company-specific context
4. `squads/<name>/memory/decisions.md` — if relevant to current work
5. `squads/<name>/memory/gotchas.md` — if relevant to current work

### 3 — Announce squad is active

Print:
```
Squad open: <Name> (<Persona> — <Role>)

Status (L1): <L1 content from STATE.md>

In progress (L2):
<L2 content>

Context: <1-line summary of squad-context.md if filled, or "not yet configured — run /hive-setup">

Ready. What are we working on?
```

### 4 — Invocar as skills obrigatórias do squad (ANTES de responder)

**Squad acionado, skill acionada.** Consultar a tabela em `squads/<name>/CLAUDE.md` § "Skills obrigatórias deste squad" e invocar cada skill listada **antes de qualquer resposta**, inclusive antes de pergunta de esclarecimento.

| Squad | Skills |
|---|---|
| marketing | `roteiro-youtube` (M1) · `influencia-digital` (M4) · `dados-verificados` (M2) |
| operations | `metas-performance` |
| commercial | `vendas` (+ `modelo-de-negocios` ao precificar) |
| intelligence | `modelo-de-negocios` |
| dev, infra, cs, product, finance, quality | *nenhuma — acervo bruto, não destilado* |

Se o squad tem mais de uma skill, invocar a que corresponde à divisão/assunto em questão; se o assunto cruza duas, invocar as duas. Para squad sem skill, dizer que não há acervo destilado — nunca improvisar como se houvesse.

### 5 — Adopt persona

For the rest of the session, respond as the squad persona. Apply the scope, rules, and absolute rules from the squad's CLAUDE.md.

---

## Rules

1. **Always read STATE.md** — never open a squad blind.
2. **Announce L1 immediately** — if L1 says "BLOCKED" or "urgent", surface it.
3. **Don't mix personas** — if asked about another squad's scope, defer: "That's [other squad]'s territory — want me to switch?"
4. **Squad context empty** means `/hive-setup` hasn't been run for this squad — say so.
5. **Nunca responder antes de invocar as skills obrigatórias do squad** (passo 4). A skill carrega o acervo destilado — sem ela, a resposta ignora o conhecimento acumulado.
