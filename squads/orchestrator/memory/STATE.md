# Orchestrator STATE

[L1]
**Mapa do negócio levantado (2026-08-23):** `foundation/mapa-do-negocio.md` — estado real cruzando Notion (1.990 objetos, 134 databases) + Neotriad (121 tarefas) via API. Painel consolidado criado na página **Negócio** do Notion ("🎯 Central de Operação").

**Diagnóstico central:** não falta método nem meta — ambos já existiam no Notion desde abril. Falta execução. 30 leads prospectados e zero contactados; 2 ciclos de 12 semanas vencidos e nunca fechados; Planner Semanal parado desde 24/05. Receita R$ 0.

**Padrão a evitar:** 134 databases, 6 bases de tarefas, 3 planners. Quando algo não anda, a resposta tem sido criar estrutura nova. O HIVE não deve virar mais uma camada — a consolidação de 23/08 não criou nenhum database novo.

**Gargalo único:** ligar para os 30 leads. Indicador semanal = leads que mudaram de etapa.

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
- [x] Linear MCP conectado e confirmado (2026-08-15). Projeto "AI Retail Automation Hub" criado no Linear (team Emerson/EME) com issues NOW: EME-5 (vazamento apps-auth, Urgent), EME-6 (credencial Postgres exposta, Urgent), EME-7 (decisão multi-tenant, Medium).

[L3]
- Configurar ferramenta de PM (padrão: Linear — ver docs/how-to-customize.md)
- Configurar workers para tarefas recorrentes
- Rodar primeiro /status após popular foundation/
