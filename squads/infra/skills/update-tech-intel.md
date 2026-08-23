# /update-tech-intel

Atualiza a base de decisão técnica da Emilly a partir dos canais monitorados. Alimenta escolha de stack, arquitetura e infraestrutura para os apps/softwares/IA do negócio.

## When to use

- Antes de escolher tecnologia, dimensionar servidor ou mudar arquitetura
- Atualização periódica do acervo (**não semanal** — ver cadência abaixo)
- `/update-tech-intel` explícito

## Cadência — diferente do Marketing

Marketing é semanal porque algoritmo muda toda semana. **Infra não.** Anton Putra publica a cada ~2 meses; benchmark de janeiro continua válido em agosto.

**Rode a cada 3–4 semanas com janela larga:**

```bash
python _core/youtube-collect.py --dir squads/infra/data/tech-intel --days 60
```

Uma janela de 7 dias volta vazia quase sempre — isso é esperado, não é falha.

---

## Steps

### Step 1 — Coletar

```bash
python _core/youtube-collect.py --dir squads/infra/data/tech-intel --days 60
```

**Regra crítica:** rodar da raiz do repositório. Nunca `cd` para subpasta — os hooks de sessão do HIVE resolvem caminho relativo ao cwd e travam todas as ferramentas.

Canais em inglês. Leio no original e **escrevo o playbook em português**, preservando o termo técnico onde traduzir atrapalha (`connection pooling`, `cold start`, `blast radius`).

### Step 2 — Filtrar pelo que decide

A maior parte do conteúdo é tutorial ou notícia — **descartar**. Só entra no playbook o que ajuda a **decidir**:

| Entra | Não entra |
|---|---|
| Benchmark com número medido | "Como instalar X" |
| "Por que escolhi X e não Y em produção" | Notícia de release |
| O que quebrou em escala e por quê | Sintaxe / referência de API |
| Tradeoff explícito de custo ou risco | Opinião sem dado |

Se um vídeo não muda nenhuma decisão, ele não vai para o playbook. Volume não é meta.

### Step 3 — Classificar cada item

Todo item registrado leva:

- **Origem:** canal + data de publicação
- **Confiança:** `medido` > `experiência` > `opinião`
- **Eixo:** economia / segurança / confiabilidade
- **Aplicação ao nosso caso:** como se relaciona com o stack real (Next.js, Supabase, n8n, Evolution API, Vercel). Se não se aplica, **dizer que não se aplica** — isso é informação útil.

### Step 4 — Testar contra o orçamento

Ler `squads/finance/foundation/budget.md`. Hoje: MEI, receita R$ 0, R$ 400/mês.

Recomendação que assume orçamento de startup financiada deve ser marcada como **fora do nosso alcance atual** — não silenciosamente omitida.

### Step 5 — Tratar colisão como pergunta

Quando um canal contrariar a documentação oficial, ou algo já rodando em produção:

1. Registrar o que o canal diz
2. Registrar o que a doc oficial diz
3. Explicitar o tradeoff
4. **Perguntar ao Emerson** — não decidir sozinho, não descartar o canal por ser "só YouTube"

### Step 6 — Gravar

- Playbook acumulado: `foundation/tech-decision-playbook.md` — editar item existente em vez de duplicar
- Atualizar `[L1]` em `memory/STATE.md`
- Se houver risco relevante ao Hub em produção, dizer na resposta, não só gravar no arquivo

---

## Output

Chat: no máximo 3 parágrafos ou uma tabela. Abrir pelo que **muda uma decisão**. Se nada muda, dizer isso na primeira linha — é resposta legítima.

---

## Gotchas

- Canal com pouco vídeo público (ex.: Hussein Nasser, conteúdo de membros) não é raspável — não insistir
- `--days 7` volta vazio em infra; é normal
- Vídeo privado/removido devolve `null` e é registrado como falha tratada, sem derrubar a coleta
- Item com +12 meses precisa de revalidação antes de virar decisão
