# Orchestrator STATE

[L1]
HIVE configurado. Empresa: my-company | Indústria: Agência de IA para PMEs | Estágio: Pré-receita
Squads ativos: todos os 10 — Commercial (Tatiane), Dev (Brenda), Marketing (Pietro), Finance (Lorenzo), Intelligence (Emerson), CS (Figueiredo), Product (Paes), Infra (Emilly), Operations (Cristina), Quality (Trindade)
Visão de ciclo operacional integrado registrada em foundation/ciclo-operacional.md — conteúdo → lead → demanda → MVP → produto → infra → mais conteúdo, com Finance travando margem/escala/recorrência.
Sessão pausada em 2026-08-14 — retomar pelos itens L2 abaixo.

[L2]
- [x] Primeiro produto identificado: AI Retail Automation Hub (já em produção, cliente Araújo) — ver squads/product/foundation/roadmap.md
- [ ] Corrigir vazamento apps-auth (n8n) e rotacionar credencial Postgres exposta — Infra
- [ ] Decidir caminho multi-tenant para replicar o Hub a outros clientes
- [x] Popular foundation/ do Finance com estrutura de custos real — custo fixo fechado em R$359,21/mês (set/2026+), ver squads/finance/foundation/budget.md
- [ ] Definir e publicar primeiro conteúdo real (usar metodo-influencia-digital.md + signal-monitoring.md)
- [ ] Popular foundation/ dos demais squads ativos (CS, Operations, Quality)
- [ ] Confirmar Linear MCP conectado — Emerson confirmou que vai usar Linear pra gerenciar todos os projetos em desenvolvimento (2026-08-15); é o padrão nativo do HIVE, falta só ativar a conexão via /mcp ou configurações claude.ai

[L3]
- Configurar ferramenta de PM (padrão: Linear — ver docs/how-to-customize.md)
- Configurar workers para tarefas recorrentes
- Rodar primeiro /status após popular foundation/
