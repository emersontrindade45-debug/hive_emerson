# Product Roadmap

## Produto 1 — AI Retail Automation Hub

> Plataforma de automação de atendimento e operação comercial para mercearias, açougues e padarias. **Já em produção** com cliente real (Açougue/Padaria/Mercearia Araújo). Código-fonte: `C:\Users\emers\Desktop\Projeto Sites\Automação Atendimento`. PRD completo em `docs/PRD.md` do próprio projeto.

### O que já existe (não é mais MVP — é produto funcionando)

- **Canais de entrada:** Landpage, WhatsApp (via Evolution API), Instagram
- **Atendimento por IA (n8n):** identifica intenção (saudação/consulta_preço/fazer_pedido/fechar_pedido/humano), RAG com base de conhecimento da loja, busca semântica de produtos (embeddings + pgvector), handoff pra humano quando ambíguo
- **CRM próprio:** Kanban visual, funil de 9 etapas (Novo → Atendimento → Fechamento → Pedido → Separação → Rota → Pós-venda → Follow-up → Marketing)
- **Atualização de preço/estoque via WhatsApp** — texto ou áudio (transcrição Whisper), reflete em tempo real via Supabase Realtime
- **RBAC completo** — papéis: admin, atendimento, separação, expedição, follow-up
- **Importação de catálogo em lote** (CSV/XLSX) com prévia e validação
- **Conciliação de catálogo com ERP** (integração Cosmos/CCG/SEFAZ) — trabalho pesado de engenharia de dados para casar produtos do Hub com códigos do ERP por nome/EAN/preço, com base de conhecimento própria que aprende abreviações do ERP

### Stack técnica

Next.js 15 (mobile-first) + Supabase/PostgreSQL (Realtime, pgvector) + n8n (orquestração) + Evolution API (WhatsApp) + Resend (e-mail) + Vercel (deploy).

### Status milestones (M1–M10, ver `plan.md`/`docs/RETOMAR-AQUI.md` do projeto)

M1–M9 concluídos: CRM, atendimento automatizado, fluxos avançados (CEP, preço por voz, busca semântica, busca por categoria), RBAC, importação de catálogo. M10 em ajustes finos.

**Pendências reais no momento (ver `docs/PENDENCIAS.md` do projeto):**
- Fila de conciliação de catálogo com o ERP ainda tem milhares de casos abertos (a maioria já triada por automação, resta revisão pontual)
- Bug de infraestrutura conhecido: vazamento de conexões em `apps-auth` que já derrubou o n8n
- Segurança: porta do banco exposta precisa de rotação de senha

### Caminho para virar oferta replicável (não só o cliente atual)

Hoje é uma solução sob medida para um cliente (Araújo). Para virar produto/SaaS vendável a outros comércios locais (conforme ICP do Commercial — "comércio local sem conhecimento de vendas online"), falta:
- Multi-tenant (hoje parece ser single-tenant, dedicado ao Araújo)
- Onboarding replicável para novo cliente sem trabalho manual de engenharia
- Precificação como serviço/SaaS (ver os 3 pilares do Intelligence: recorrência, escala, margem)

## Horizons

### NOW — Current Quarter
> Focus: estabilizar o AI Retail Automation Hub com o cliente piloto (Araújo) e avaliar caminho de replicação.

| Epic | Status | Success Metric | Owner |
|------|--------|---------------|-------|
| Corrigir vazamento `apps-auth` (n8n) | Pendente | Zero quedas de n8n por esgotamento de conexão | Brenda/Emilly |
| Rotacionar credencial do Postgres exposto | Pendente | Porta 5432 fechada/senha trocada | Emilly |
| Avaliar multi-tenant para replicar a outros clientes | Não iniciado | Decisão: seguir single-tenant vs. investir em multi-tenant | Paes |

### NEXT — Following Quarter
> Focus: transformar o Hub em oferta replicável.

| Epic | Status | Success Metric | Owner |
|------|--------|---------------|-------|
| Modelo de precificação como serviço/SaaS | Planned | Bate os 3 pilares (Intelligence): recorrência + escala + margem ≥30% | Paes + Lorenzo |
| Onboarding replicável para novo cliente | Planned | Novo cliente ativo em < X dias sem trabalho manual pesado | Paes + Brenda |

### LATER — 6–12 Months
> Focus: apostas estratégicas.

| Epic | Hypothesis | Signal to Proceed |
|------|-----------|------------------|
| Expandir para outros nichos de comércio local além de açougue/padaria/mercearia | O motor de atendimento é genérico o bastante para outros varejos | 1 cliente piloto fora do nicho original validado |
| **Produto 2 — produtos digitais (ebooks/ferramentas) sobre dor de usar IA na rotina** (registrado 27/08/2026) | Pessoas/empresas têm dificuldade recorrente e específica em aplicar IA no dia a dia — dá pra empacotar como ebook, template ou mini-ferramenta vendável | Pipeline de oportunidades em `../intelligence/foundation/business-opportunities.md` acumular pelo menos 1 dor validada em múltiplas fontes (repetição = sinal). **Não iniciado — vigilância passiva só, sem hospedagem definida** |

---

## Active Metrics (this quarter)

| Metric | Baseline | Target | Current |
|--------|---------|--------|---------|
| _e.g. Activation rate_ | _45%_ | _60%_ | _—_ |
| _e.g. Monthly active users_ | _1,200_ | _1,800_ | _—_ |
| _e.g. Feature adoption (reporting)_ | _—_ | _35%_ | _—_ |

---

## Process
- Roadmap reviewed: **quarterly** (full) + **monthly** (NOW adjustments)
- Changes to NEXT/LATER require: PM + stakeholder alignment
- Changes to NOW require: PM + Engineering Lead sign-off
