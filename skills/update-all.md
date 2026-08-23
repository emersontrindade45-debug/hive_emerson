# /update-all

Analisa tudo que foi coletado dos canais monitorados e ainda não virou conhecimento. Uma leitura só, cobrindo todos os squads.

## When to use

- Abertura de sessão, para saber o que mudou desde a última vez
- `/update-all` explícito
- Sempre que `_core/.youtube-pending.md` existir

## Como o sistema funciona

**A coleta é automática** (Task Scheduler roda `_core/youtube-collect-all.py` diariamente; cada squad é coletado na sua cadência própria). **A análise não é** — depende desta skill numa sessão.

Cadências, derivadas da frequência real de publicação de cada canal:

| Squad | Cadência | Janela | Por quê |
|---|---|---|---|
| marketing | 7 dias | 10 dias | Canais publicam quase diariamente; algoritmo muda toda semana |
| dev | 14 dias | 30 dias | Fireship é frequente, mas nem toda notícia muda decisão |
| infra | 28 dias | 60 dias | Anton Putra publica a cada ~2 meses; benchmark não envelhece rápido |
| operations | 14 dias | 30 dias | Joel Jota publica com frequência; Neotriad é esporádico |

---

## Steps

### Step 1 — Ver o que está pendente

```bash
cat _core/.youtube-pending.md
```

Se o arquivo não existir: **nada a analisar**. Dizer isso em uma linha e parar. Não inventar trabalho.

Se quiser forçar uma coleta antes:

```bash
python _core/youtube-collect-all.py --force
```

**Regra crítica:** rodar da raiz do repositório. Nunca `cd` para subpasta — os hooks do HIVE resolvem caminho relativo ao cwd e travam todas as ferramentas.

### Step 2 — Ler as transcrições pendentes

Cada squad tem seu diretório: `squads/<nome>/data/*/transcripts/<video_id>.json`.

Ler o campo `transcript`. Canais em inglês: ler no original, escrever em português.

**Curso longo (20k–240k palavras) nunca entra inteiro no contexto** — buscar a tese, descartar o passo a passo.

### Step 3 — Aplicar o filtro de cada squad

Seguir a skill correspondente, que já define o filtro:

| Squad | Skill | Propósito |
|---|---|---|
| marketing | `squads/marketing/skills/update-youtube.md` | Criar conteúdo |
| dev | `squads/dev/skills/update-dev-intel.md` | Decidir e manter habilidade técnica |
| infra | `squads/infra/skills/update-tech-intel.md` | Decidir stack, custo, confiabilidade |
| operations | (sem skill própria) | Método de metas e decisão diária — grava em `squads/operations/foundation/alta-performance-playbook.md` |

**Marketing é o único voltado a conteúdo.** Dev e Infra são decisão — não gerar pauta a partir deles.

Regra comum: se um vídeo não muda nenhuma decisão nem vira técnica aplicável, **não entra no playbook**. Volume não é meta.

### Step 4 — Gravar

Cada squad no seu lugar:

- `squads/marketing/foundation/youtube-playbook.md` + relatório em `data/youtube-intel/reports/YYYY-MM-DD.md`
- `squads/dev/foundation/engineering-playbook.md`
- `squads/infra/foundation/tech-decision-playbook.md`
- `squads/operations/foundation/alta-performance-playbook.md`

Editar item existente em vez de duplicar. Atualizar `[L1]` do STATE de cada squad que mudou.

### Step 5 — Marcar como analisado

**Obrigatório**, senão os mesmos vídeos reaparecem como pendentes:

```bash
python -c "import io,os;from datetime import datetime,timezone;a=datetime.now(timezone.utc).replace(tzinfo=None).isoformat(timespec='seconds');[io.open(os.path.join(d,'.last-analyzed'),'w',encoding='utf-8').write(a) for d in ['squads/marketing/data/youtube-intel','squads/dev/data/dev-intel','squads/infra/data/tech-intel','squads/operations/data/performance-intel']]"
```

Marcar **somente** os squads efetivamente analisados. `.last-analyzed` é UTC, para bater com `collected_at`.

---

## Output

Um resumo único no chat, no máximo uma tabela ou 3 parágrafos curtos:

1. **O que exige ação sua** — primeiro, sempre. Mudança de plataforma, risco em produção, janela curta.
2. **O que entrou no playbook** — uma linha por squad.
3. **O que foi descartado e por quê** — se muita coisa foi cortada, dizer.

Se nada relevante saiu: dizer isso na primeira linha. É resposta legítima.

---

## Gotchas

- Coleta ≠ análise. O agendador coleta; só uma sessão analisa.
- `.last-analyzed` em UTC — hora local causa falso pendente.
- Squad fora da cadência é pulado; isso é esperado, não falha.
- Vídeo privado/removido vira falha tratada, sem derrubar a coleta.
- O pendente persiste entre execuções até ser analisado — nenhuma coleta se perde.
