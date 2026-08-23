# Orchestrator STATE

[L1]
**ESTRATEGIA DO TRIMESTRE (revisada 2026-08-23):** foco em **Mercado Araujo** (converter piloto gratuito em contrato pago, R$ 4.000/mes) + **conteudo no canal** (leads inbound). **Prospeccao ativa por ligacao EXCLUIDA do trimestre** por decisao do Emerson.

**Plano:** `squads/operations/foundation/plano-trimestral-2026-Q4.md` — 23/08 a 31/10/2026, microtarefas com data, horario e criterio de verificacao.

**Disponibilidade:** 20h/semana para o negocio — 4h/dia (2h manha + 2h tarde), seg a sex. Sabado da familia.

**Grade:** Bloco A Araujo 09:00-11:00 seg-sex (inegociavel) | Bloco B Conteudo 14:00-16:00 seg-qui | Revisao sex 14:00-15:00.

**RISCO CENTRAL — o Araujo nao paga nada hoje.** E piloto gratuito e preco NUNCA foi mencionado ao cliente. Os R$ 4.000 sao estimativa do Emerson, nao sinalizacao do Araujo. Com a prospeccao excluida, nao ha plano B ativo.

**19/09 e a data de decisao do trimestre** (marco A3, reuniao de precificacao). Se o Araujo recusar: reabrir prospeccao no mesmo dia — a base de 238 leads e o script continuam intactos.

**Marcos Araujo:** A1 estavel 05/09 | A2 relatorio de valor 12/09 | A3 REUNIAO DE PRECO 19/09 | A4 proposta 26/09 | A5 contrato 10/10 | A6 pagamento 31/10.
**Marcos Conteudo:** C1 linha editorial 29/08 | C2 1o video 12/09 | C3 4 videos 10/10 | C4 8 videos + 1 lead 31/10.

**Aplicado no Notion via API (23/08):** meta 4 renomeada para "Converter Mercado Araujo em contrato pago (R$ 4.000/mes)", alvo 2000->4000, prazo 31/12->31/10. Meta 7 "Gerar leads por conteudo no canal" criada. Saude Emerson e Familia repactuadas para 31/10. Pausadas ate 01/11: Automatizar despesas e Processo de Compras. Painel "CENTRAL — Empresa IA" reescrito com a semana 1.

**EME-5 e EME-6 entraram no caminho critico** — sistema estavel e pre-requisito do marco A1 (05/09). Deixaram de ser divida tecnica e viraram parte da venda.

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
