# Infra STATE

[L1]
Squad ativado (2026-08-14). Emilly é **tomadora de decisão técnica do negócio** — escolha de stack, arquitetura e infra para os apps/softwares/IA que Emerson vai construir (não é decisão de conteúdo/canal).

**Base de decisão ativa (desde 2026-08-23):** `/update-tech-intel` monitora NetworkChuck, Anton Putra e ByteByteGo (inglês; leitura no original, playbook em PT-BR). Acervo: `data/tech-intel/transcripts/` (42 vídeos). Playbook: `foundation/tech-decision-playbook.md`.

**Critérios fixos de toda decisão:** economia, segurança, confiabilidade. Teto orçamentário real: MEI, receita R$ 0, R$ 400/mês (ver `../finance/foundation/budget.md`) — conselho que pressupõe orçamento de startup financiada é marcado como fora de alcance, não omitido.

**Colisão vira pergunta:** canal vs doc oficial vs produção → apresentar o tradeoff a Emerson, nunca decidir em silêncio nem descartar o canal.

[L2]
- [ ] Documentar inventário de servidores em foundation/server-inventory.md — dados já existem no roadmap do Product (Vercel, Supabase, n8n, Evolution API); extrair
- [ ] Configurar checklist de deploy em foundation/deploy-checklist.md
- [ ] **Lacunas do playbook** (nenhum canal monitorado cobre): custo real de Vercel/Supabase em escala; n8n em produção (maior ponto cego — o Hub depende dele); backup e recuperação com cliente real rodando

[L3]
- Configure monitoring and alerting
- Document DNS and SSL setup
- Define backup and recovery procedures
