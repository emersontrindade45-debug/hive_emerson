# Orchestrator STATE

[L1]
**⚠️ ESTRATEGIA REVISADA 2026-08-26 — A PRIORIDADE VIROU CONTEUDO.** Decisao do Emerson respondendo as 3 perguntas do Operations. **Quando conteudo e Araujo disputarem a mesma hora, conteudo ganha.** Meta SMART: **4 videos publicados ate 09/10/2026** (marco C3; C4/8 videos vira esticada). Indicador semanal: **videos publicados (acumulado)**, olhado na revisao de sexta 14:00. Registro completo em `../operations/memory/STATE.md`.

**⛔ MOTIVO — ARAUJO BLOQUEADO POR TERCEIRO:** a rede do Araujo esta **fechada para o Hub se comunicar com o ERP deles**. Emerson ja falou com o dono; o cliente ficou de acionar o rapaz de redes. **Sem data.** O Araujo deixou de avancar por esforco do Emerson — virou **item de espera, nao tarefa**. Cobrar retorno do dono se nao houver noticia ate o inicio de setembro.

**Consequencia nos marcos Araujo:** A1 (04/09) e toda a cadeia ate a reuniao de preco A3 (18/09) ficam **em risco por causa externa**. Nao replanejar datas ate a rede liberar — replanejar sobre dependencia sem data e ficcao.

**Consequencia em EME-5/EME-6:** seguem urgentes (credenciais expostas, cliente real em producao), mas **saem do caminho critico da venda** enquanto a rede estiver fechada — o marco A1 nao depende mais so deles. Continuam prioridade de seguranca.

**ESTRATEGIA ANTERIOR (2026-08-23 a 2026-08-26, superada):** foco em **Mercado Araujo** (converter piloto gratuito em contrato pago, R$ 4.000/mes) + **conteudo no canal** (leads inbound). **Prospeccao ativa por ligacao EXCLUIDA do trimestre** por decisao do Emerson — essa exclusao **continua valendo**.

**Plano:** `squads/operations/foundation/plano-trimestral-2026-Q4.md` — 23/08 a 31/10/2026, microtarefas com data, horario e criterio de verificacao.

**Disponibilidade:** 20h/semana para o negocio — 4h/dia (2h manha + 2h tarde), seg a sex. Sabado da familia.

**Grade:** Bloco A Araujo 09:00-11:00 seg-sex (inegociavel) | Bloco B Conteudo 14:00-16:00 seg-qui | Revisao sex 14:00-15:00.

**RISCO CENTRAL (atualizado 26/08) — agora sao DOIS riscos empilhados no Araujo:**
1. **Comercial:** o Araujo nao paga nada hoje. E piloto gratuito e preco NUNCA foi mencionado ao cliente. Os R$ 4.000 sao estimativa do Emerson, nao sinalizacao do Araujo.
2. **Tecnico/externo (NOVO):** a rede do Araujo esta fechada para o Hub falar com o ERP deles. **Sem isso, nao ha o que precificar** — o Hub nao entrega o valor que sustentaria a conversa de preco.

Com a prospeccao excluida, **nao ha plano B ativo**. A mitigacao escolhida pelo Emerson foi deslocar a prioridade para conteudo, que depende so dele.

**18/09 era a data de decisao do trimestre** (marco A3, reuniao de precificacao). **Essa data agora depende de terceiro** — o rapaz de redes do Araujo. Se a rede nao liberar a tempo, A3 escorrega por causa externa. **Gatilho a vigiar:** se nao houver liberacao ate o inicio de setembro, cobrar o dono; se ainda assim nao destravar, reabrir a decisao de prospeccao (a base de 238 leads e o script continuam intactos).

**Correcao 24/08:** o rascunho original do plano trimestral rotulava a Semana 1 como "Seg 25/08" e todos os marcos "sex" caiam em sabados no calendario real — todas as datas do plano foram deslizadas -1 dia para bater com os dias da semana corretos.

**Marcos Araujo:** A1 estavel 04/09 | A2 relatorio de valor 11/09 | A3 REUNIAO DE PRECO 18/09 | A4 proposta 25/09 | A5 contrato 09/10 | A6 pagamento 30/10.
**Marcos Conteudo:** C1 linha editorial 28/08 | C2 1o video 11/09 | C3 4 videos 09/10 | C4 8 videos + 1 lead 30/10.

**Aplicado no Notion via API (24/08):** criada a base **📅 Calendário — Trimestre Q4** (em Metas - 2026) com 13 marcos + 10 tarefas/ritual da Semana 1, propriedade Data pronta para conectar ao Notion Calendar. Criada a página **🌳 Mapa de Objetivos — Q4 2026** com árvore mermaid (Trimestre → Metas → Marcos). Página "🎯 CENTRAL — Empresa IA" corrigida (estava com a meta antiga "Faturar R$ 2.000/mês" e marcos de ligação, desatualizada desde 23/08) e datas deslizadas -1 dia. Indicadores de Meta 4, Meta 7 e Meta 2 em "Metas Principais" corrigidos com as mesmas datas.

**Aplicado no Notion via API (23/08):** meta 4 renomeada para "Converter Mercado Araujo em contrato pago (R$ 4.000/mes)", alvo 2000->4000, prazo 31/12->31/10. Meta 7 "Gerar leads por conteudo no canal" criada. Saude Emerson e Familia repactuadas para 31/10. Pausadas ate 01/11: Automatizar despesas e Processo de Compras. Painel "CENTRAL — Empresa IA" reescrito com a semana 1.

**EME-5 e EME-6 entraram no caminho critico** — sistema estavel e pre-requisito do marco A1 (05/09). Deixaram de ser divida tecnica e viraram parte da venda.

**Padrão a evitar:** 134 databases, 6 bases de tarefas, 3 planners. Quando algo não anda, a resposta tem sido criar estrutura nova. O HIVE não deve virar mais uma camada — a consolidação de 23/08 não criou nenhum database novo.

**Gargalo único:** ligar para os 30 leads. Indicador semanal = leads que mudaram de etapa.

HIVE configurado. Empresa: my-company | Indústria: Agência de IA para PMEs | Estágio: Pré-receita
Squads ativos: todos os 10 — Commercial (Tatiane), Dev (Brenda), Marketing (Pietro), Finance (Lorenzo), Intelligence (Emerson), CS (Figueiredo), Product (Paes), Infra (Emilly), Operations (Cristina), Quality (Trindade)
Visão de ciclo operacional integrado registrada em foundation/ciclo-operacional.md — conteúdo → lead → demanda → MVP → produto → infra → mais conteúdo, com Finance travando margem/escala/recorrência.
Sessão pausada em 2026-08-14 — retomar pelos itens L2 abaixo.

[L2]
- [ ] **2º canal "Concurso com IA" aprovado em princípio (27/08), sob guarda-chuva Impulso IA — CONGELADO até marco C3 (09/10).** Emerson é concurseiro desde 2017, aprovado em 5 concursos. Pesquisa completa em `squads/intelligence/foundation/business-opportunities.md`. Não consome atenção nem execução antes de 09/10 — registrado aqui só para o caminho crítico não ser reaberto por engano antes da meta do trimestre.
- [ ] **SaaS de método de estudo (Ciclo EARA) para concurseiros — registrado 27/08, mesma trava de 09/10.** Emerson tem planilha própria aplicando o Ciclo EARA (método já validado no mercado, não inventado) — serviria de MVP. Formaria esteira com o 2º canal (audiência → produto recorrente). **Pendência explícita: estudo de mercado ainda não feito** (concorrência direta, volume de busca, os 3 pilares recorrência/escala/margem) — nada a decidir antes disso, e nada disso antes de 09/10. Detalhe em `squads/intelligence/foundation/business-opportunities.md`.
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
