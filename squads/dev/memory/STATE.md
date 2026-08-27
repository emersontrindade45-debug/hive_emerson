# Dev STATE

[L1]
Squad ativado via /hive-setup (2026-08-14). Stack: Next.js 15 + Node/TypeScript + Supabase (Realtime, pgvector) + n8n + Evolution API + Vercel. Multi-repo.

**Base de decisão ativa (desde 2026-08-23):** `/update-dev-intel` monitora Fireship, freeCodeCamp e Programming with Mosh (inglês; leitura no original, playbook em PT-BR). Acervo: `data/dev-intel/transcripts/` (25 vídeos). Playbook: `foundation/engineering-playbook.md`.
Propósito é **decisão e habilidade técnica** — não geração de conteúdo (isso é marketing). Colisão canal × doc oficial × produção vira pergunta a Emerson, nunca decisão silenciosa.

**⚠️ Risco levantado, não verificado:** o Hub recebe webhooks (Evolution API/WhatsApp, Instagram). Reentrega duplicada e requisição forjada são modos de falha conhecidos desse padrão. **Auditar se tratamos idempotência e verificação de origem** — ver `foundation/engineering-playbook.md`.

[L2]
- [ ] **Auditar webhooks do Hub:** idempotência (reentrega duplicada) + verificação de origem (requisição forjada) + tempo de ACK
  **⛔ BLOQUEADO POR ACESSO (verificado 26/08):** o código do Hub **não está neste repositório** — o HIVE é multi-repo e aqui só há documentação/orquestração. A auditoria exige abrir o repo do Hub (ou os workflows n8n). **Emerson precisa indicar onde o código vive.** Checklist pronto para rodar assim que houver acesso: (1) endpoint de webhook valida assinatura/token de origem? (2) há chave de idempotência por evento — `message_id`/`event_id` persistido antes de processar? (3) ACK volta antes do processamento pesado ou depois? (4) retry da Evolution API reprocessa ou descarta duplicado?
- [ ] `foundation/tech-stack.md` está 100% em template `_e.g._`, mas a stack real já está em `context/squad-context.md` — resolver a duplicação (preencher a partir do context ou remover o arquivo)
- [ ] Definir princípios de código em foundation/code-principles.md

[L3]
- Define branch and commit conventions
- Set up review checklist
- Document architecture decisions baseline
