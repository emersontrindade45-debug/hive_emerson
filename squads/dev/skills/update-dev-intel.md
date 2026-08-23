# /update-dev-intel

Atualiza a base de decisão e habilidade técnica da Brenda a partir dos canais monitorados. Alimenta escolha de padrão, arquitetura de software e prática de engenharia.

**Propósito:** decidir e manter habilidade atualizada — **não** gerar conteúdo (isso é `squads/marketing/`).

## When to use

- Antes de arquitetar feature, escolher biblioteca ou definir padrão
- Atualização periódica do acervo
- `/update-dev-intel` explícito

## Cadência

**A cada 2–3 semanas, janela de 30 dias:**

```bash
python _core/youtube-collect.py --dir squads/dev/data/dev-intel --days 30
```

Mais frequente que Infra (ecossistema JS/IA muda rápido, Fireship publica quase diário), menos que Marketing. Mosh publica raramente — janela curta não o alcança, e isso é esperado.

---

## Steps

### Step 1 — Coletar

```bash
python _core/youtube-collect.py --dir squads/dev/data/dev-intel --days 30
```

**Regra crítica:** rodar da raiz do repositório. Nunca `cd` para subpasta — os hooks de sessão do HIVE resolvem caminho relativo ao cwd e travam todas as ferramentas.

Canais em inglês. Ler no original, escrever o playbook em português, preservando termo técnico onde traduzir atrapalha (`retriever`, `connection pooling`, `definition of done`).

### Step 2 — Filtrar duro

Esses canais produzem muito volume e pouca decisão. Só entra o que **muda como escrevemos ou entregamos código**:

| Entra | Não entra |
|---|---|
| Padrão de arquitetura com justificativa | "Aprenda X em 10 minutos" |
| Modo de falha concreto e como evitar | Notícia de release sem impacto no nosso stack |
| Mudança que afeta Next.js/TS/Supabase/agentes | Hype de IA sem aplicação |
| Prática de engenharia com tradeoff explícito | Ranking de linguagem, opinião de carreira |

Curso longo do freeCodeCamp (20k–240k palavras) raramente entra inteiro — extrair a **tese de arquitetura**, descartar o passo a passo. Referência de sintaxe é doc oficial, não YouTube.

Se um vídeo não muda nenhuma decisão, não vai para o playbook.

### Step 3 — Aplicar ao nosso stack

Todo item precisa responder: **o que isso muda no Hub do Araújo ou no próximo produto?**

Se não muda nada, dizer que não se aplica — isso é informação útil, não item descartável.

Stack de referência: Next.js 15 · Node/TS · Supabase (Realtime, pgvector) · n8n · Evolution API · Resend · Vercel.

### Step 4 — Colisão vira pergunta

Canal contrariando doc oficial ou o que já roda em produção: registrar os dois lados, explicitar o tradeoff, **perguntar a Emerson**. Não decidir sozinho, não descartar o canal.

### Step 5 — Gravar

- Playbook acumulado: `foundation/engineering-playbook.md` — editar item existente em vez de duplicar
- Padrão que já nos queimou vai para `memory/gotchas.md` no formato existente (sintoma → causa raiz → errado/certo → regra)
- Atualizar `[L1]` em `memory/STATE.md`

---

## Output

Chat: no máximo 3 parágrafos ou uma tabela. Abrir pelo que **muda uma decisão**. "Nada relevante nesta rodada" é resposta legítima e preferível a encher linguiça.

---

## Gotchas

- freeCodeCamp publica cursos de até 240k palavras — nunca despejar no contexto inteiro; buscar a seção que interessa
- Mosh e canais de baixa cadência voltam vazios em janela curta; normal
- Vídeo privado/removido devolve `null` e vira falha tratada, sem derrubar a coleta
- Item com +6 meses no ecossistema JS/IA precisa de revalidação
