# Análise de divisões — os 10 squads não-Marketing

> Feita em 2026-08-26 a pedido do Emerson. Pergunta: *"os outros setores não cabe criar divisões como no Marketing?"*
> Método: (1) leitura do L2 real de cada squad · (2) pesquisa de mercado sobre o limiar de subdivisão de cada função.
> **Veredito: nenhum dos 10 squads deve receber divisões hoje.** Um deles precisa de outra coisa — ver Product, § Achado crítico.

---

## Parte 1 — O que o mercado diz sobre quando subdividir

Pesquisa em fontes de design organizacional, agosto/2026. Quatro achados convergentes:

| Achado | Fonte | Implicação para o HIVE |
|---|---|---|
| **Substrutura operacional aparece quando uma função cruza ~50 pessoas.** Camadas de Dunbar: ~5 íntimos, ~15 colaboradores de confiança, ~50 relações de trabalho, ~150 conexões estáveis. Span de primeira linha fica em 5–7 | [Psych Safety](https://psychsafety.com/psychological-safety-82-dunbars-number-and-team-size/) · [Andreas Timm](https://andreastimm.com/why-team-sizes-cluster-where-they-do/) | O HIVE tem **1 pessoa**. Está 50× abaixo do primeiro limiar de substrutura |
| **Times se dividem quando perdem contexto compartilhado** — não por headcount. Sinal: dependências que exigem sincronização diária entre times | [Sense & Respond Learning](https://www.senseandrespond.co/blog/organizational-design-product-teams) | É o mesmo teste do HIVE (T2/T3). Uma pessoa nunca perde contexto de si mesma |
| **Adotar prática de empresa grande antes da hora é antipadrão declarado.** Times tentam adotar práticas de organizações maiores antes de estarem prontos, o que gera obstáculos e atrasa o progresso | [LeadDev](https://leaddev.com/culture/tackling-some-devops-antipatterns) · [YLD](https://www.yld.com/blog/overcome-team-based-silos-by-tackling-devops-antipatterns) | Criar 30 divisões copiando org chart de corporação é literalmente esse antipadrão |
| **Solopreneur: a falha típica é estrutura, não habilidade** — mas a recomendação é processo mínimo, validando antes de investir em formalização | [Bask Health](https://bask.health/blog/solopreneur-business-model) · [Ken Yarmosh](https://kenyarmosh.com/blog/one-person-business/) | Estrutura leve é a recomendação para o porte do Emerson |

**Reforço do modelo adotado:** a Apple, com 137 mil funcionários, *eliminou* as unidades de negócio e voltou ao funcional único ([HBR, Podolny & Hansen 2020](https://hbr.org/2020/11/how-apple-is-organized-for-innovation)). Estrutura funcional argumenta a favor de **menos** unidades.

---

## Parte 2 — Squad a squad

Legenda: **T1** volume (≥6 itens abertos *em execução*) · **T2** função distinta (material de referência diferente) · **T3** bloqueio independente.

### 🔴 Finance (Lorenzo) — 6 itens · o caso mais tentador

| T1 | T2 | T3 | Veredito |
|---|---|---|---|
| ⚠️ no limite | ❌ | ❌ | **Não dividir** |

Os 6 itens: CNPJ Impulso IA · busca INPI · decisão Canva · conta Capacitação (×2, duplicada) · consolidar meses de 2026.

**Por que falha:** todos respondem à mesma pergunta — *"cabe nos R$5,79/mês de folga?"* — e travam pelo mesmo motivo. Não são frentes distintas; são consequências de uma restrição só.

**O que o mercado diz:** empresas de US$0–1M tipicamente só precisam de um contador terceirizado ([Ramp](https://ramp.com/blog/how-to-structure-and-scale-your-finance-team)). A separação Controller × FP&A só se justifica quando o fechamento do mês consome o Controller a ponto de o forecast escorregar ([Numeric](https://www.numeric.io/blog/finance-team-structure)). Com R$0 de receita não há fechamento nem forecast.

**Ação real:** deduplicar o item "conta Capacitação" (aparece 2×). Isso resolve mais que qualquer divisão.

---

### 🔴 Product (Paes) — 5 itens · ⚠️ ACHADO CRÍTICO

| T1 | T2 | T3 | Veredito |
|---|---|---|---|
| ❌ | ❌ | ❌ | **Não dividir — mas há urgência real escondida** |

**O problema não é estrutura, é visibilidade.** Dois itens marcados **Urgent** no Linear estão enfileirados junto com "definir cadência de sprint":

- **EME-5** — vazamento apps-auth (n8n)
- **EME-6** — rotacionar credencial Postgres exposta

Pelo STATE do Orchestrator, ambos **entraram no caminho crítico**: sistema estável é pré-requisito do marco A1 (04/09) — deixaram de ser dívida técnica e viraram parte da venda. São credenciais expostas num sistema com cliente real rodando.

**O que o mercado diz:** no início, um único time cross-funcional com posse clara da visão, roadmap e entrega ([Aha!](https://www.aha.io/roadmapping/guide/product-management/what-makes-up-the-product-team)).

**Ação real: promover EME-5 e EME-6 ao topo do L2 com marcação de urgência.** Dividir Product em subáreas enterraria esses dois itens mais fundo.

---

### 🔴 Operations (Cristina) — 2 itens · bloqueada na entrada

| T1 | T2 | T3 | Veredito |
|---|---|---|---|
| ❌ | ❌ | ❌ | **Não dividir — destravar** |

⛔ **3 respostas que só o Emerson pode dar:** (1) área prioritária do trimestre · (2) meta SMART com número/prazo/indicador · (3) indicador semanal.

Sem elas a rotina diária não tem o que priorizar — e o problema declarado do Emerson é exatamente *"minha grande dificuldade é saber o que fazer no dia"*. **Este é o squad com maior retorno por unidade de esforço: 3 respostas destravam o squad inteiro.**

Pendência menor: diagnosticar qual das 3 composições perigosas da Tríade do Tempo (Super-Homem / Homer Simpson / Equilibrista) bate com o Emerson.

---

### 🔴 Dev (Brenda) — 3 itens

| T1 | T2 | T3 | Veredito |
|---|---|---|---|
| ❌ | ❌ | ❌ | **Não dividir** |

Item de risco real: **auditar webhooks do Hub** — idempotência (reentrega duplicada) e verificação de origem (requisição forjada), num sistema que recebe Evolution API/WhatsApp e Instagram com cliente em produção. Risco levantado, **não verificado**.

**O que o mercado diz — o argumento mais direto contra dividir:** separar DevOps/SRE cedo demais é antipadrão nomeado. Quanto maior a separação entre as pessoas envolvidas nas várias partes do processo, maiores os ciclos de feedback, menor o entendimento, e mais frequentemente outros times bloquearão o seu ([LeadDev](https://leaddev.com/culture/tackling-some-devops-antipatterns) · [Alex King](https://alexwking.medium.com/organizational-anti-patterns-that-impact-devops-cbe70e2f39c9)). A recomendação é o oposto: **dissolver times dedicados e embutir a especialidade no time de produto**.

Higiene pendente: `foundation/tech-stack.md` está 100% em template `_e.g._` enquanto a stack real está em `context/squad-context.md` — duplicação a resolver.

---

### 🔴 Infra (Emilly) — 3 itens

| T1 | T2 | T3 | Veredito |
|---|---|---|---|
| ❌ | ❌ | ❌ | **Não dividir** |

Mesmo argumento do Dev — e aqui a fronteira Dev × Infra **já é** a separação funcional. Subdividir criaria a fragmentação que o antipadrão descreve.

**Ponto cego declarado no próprio STATE:** nenhum canal monitorado cobre *n8n em produção* — e o Hub depende dele. Também faltam custo real de Vercel/Supabase em escala e backup/recuperação com cliente real rodando.

---

### 🔴 Commercial (Tatiane) — 2 itens · o dado de mercado mais relevante do trimestre

| T1 | T2 | T3 | Veredito |
|---|---|---|---|
| ❌ | ❌ | ❌ | **Não dividir** |

**O que o mercado diz:** feche seus primeiros **10–20 clientes você mesmo** antes de contratar os 2 primeiros executivos de vendas; a transição de founder-led sales acontece por volta de **US$1M ARR** ([SaaStr](https://www.saastr.com/what-are-the-best-ways-to-transition-from-the-founder-led-sales-stage/)).

O Emerson tem **0 clientes pagantes** (Araújo é piloto gratuito, preço nunca mencionado). Está no início absoluto do founder-led sales. Dividir vendas aqui não tem paralelo em nenhum modelo.

⚠️ **Risco registrado no Orchestrator:** prospecção ativa foi excluída do trimestre por decisão do Emerson — **não há plano B ativo** se o Araújo recusar em 18/09. A base de 238 leads e o script continuam intactos.

---

### 🔴 CS (Figueiredo) — 2 itens · sem cliente pagante

| T1 | T2 | T3 | Veredito |
|---|---|---|---|
| ❌ | ❌ | ❌ | **Não dividir** |

**O que o mercado diz:** a separação Sales × CS se justifica por sintomas operacionais — account managers sem dar conta de vendas *e* calls de sucesso, sem tempo para calls proativas, liderança incapaz de prever churn ([SignalFire](https://www.signalfire.com/blog/split-customer-success-sales)). **Nenhum sintoma existe com 1 cliente piloto.**

---

### 🔴 Quality (Trindade) — 2 itens

| T1 | T2 | T3 | Veredito |
|---|---|---|---|
| ❌ | ❌ | ❌ | **Não dividir** |

"Aguardando definição de processos/SOPs prioritários." Um squad sem trabalho não recebe subdivisão de trabalho.

---

### 🔴 Intelligence (Emerson) — 0 abertos, 4 concluídos

| T1 | T2 | T3 | Veredito |
|---|---|---|---|
| ❌ | ⚠️ 3 frentes | ❌ | **Não dividir** |

Único squad com **L2 zerado** — tudo entregue. Tem 3 frentes nominais (radar semanal de conteúdo · scouting de modelos de negócio · radar diário de ferramentas), o que superficialmente parece função distinta.

**Mas falha em T1 e T3:** frentes que rodam sem gerar item aberto não precisam de divisão — precisam de cadência. Divisão organiza *trabalho em disputa por atenção*; aqui não há disputa.

---

### 🔴 Orchestrator (Stamper) — 4 itens · é a própria camada

| T1 | T2 | T3 | Veredito |
|---|---|---|---|
| ❌ | ❌ | ❌ | **Não dividir — por definição** |

O Orchestrator **é** a camada de coordenação. Subdividi-lo é criar coordenação da coordenação.

⚠️ **O aviso mais importante do repositório está no STATE dele:**

> **Padrão a evitar:** 134 databases, 6 bases de tarefas, 3 planners. Quando algo não anda, a resposta tem sido criar estrutura nova. O HIVE não deve virar mais uma camada.

Esta análise existe para honrar esse aviso.

---

## Parte 3 — Quadro consolidado

| Squad | Abertos | T1 | T2 | T3 | Veredito | Limiar de mercado para dividir |
|---|---|---|---|---|---|---|
| **Marketing** | ~8 | ✅ | ✅ | ✅ | ✅ **tem divisões** | — |
| Finance | 6 | ⚠️ | ❌ | ❌ | ❌ | Controller consumido pelo fechamento |
| Product | 5 | ❌ | ❌ | ❌ | ❌ | Perda de contexto compartilhado |
| Orchestrator | 4 | ❌ | ❌ | ❌ | ❌ | É a camada |
| Dev | 3 | ❌ | ❌ | ❌ | ❌ | Antipadrão declarado |
| Infra | 3 | ❌ | ❌ | ❌ | ❌ | Antipadrão declarado |
| Operations | 2 | ❌ | ❌ | ❌ | ❌ | Bloqueado na entrada |
| Commercial | 2 | ❌ | ❌ | ❌ | ❌ | ~US$1M ARR / 10–20 clientes |
| CS | 2 | ❌ | ❌ | ❌ | ❌ | Sintomas de sobrecarga |
| Quality | 2 | ❌ | ❌ | ❌ | ❌ | Sem trabalho |
| Intelligence | 0 | ❌ | ⚠️ | ❌ | ❌ | L2 zerado |

**Total de itens abertos fora do Marketing: 29, em 10 squads — média de 2,9 por squad.** O Marketing sozinho tem ~8 em 4 especialidades.

---

## Parte 4 — Por que o Marketing foi diferente

O Marketing não ganhou divisões porque alguém decidiu organizá-lo. **Ganhou porque a divisão já existia de fato antes de ter nome:**

- **M2** já rodava `/youtube-gaps`, tinha `channels.json`, `termos.json`, relatórios datados
- **M4** já tinha `brand-voice.md` e `creator-profile.md` preenchidos
- **M1** já tinha roteiro escrito e 20 ângulos mapeados
- **M3** já tinha o kit de canal pronto para colar

Os rótulos **descreveram trabalho existente**. Nos outros 10 squads seria o inverso: rótulo primeiro, trabalho nunca. Essa inversão é a definição operacional de estrutura prematura.

---

## Parte 5 — As 5 ações que substituem "criar divisões"

Ordenadas por retorno sobre as 20h/semana do Emerson:

| # | Ação | Squad | Por quê |
|---|---|---|---|
| 1 | **Responder as 3 perguntas do Operations** | Operations | Destrava o squad inteiro e ataca o problema declarado ("não sei o que fazer no dia"). Só o Emerson pode |
| 2 | **Promover EME-5 e EME-6 ao topo do L2** | Product | Credenciais expostas, cliente real, caminho crítico do marco A1 (04/09) |
| 3 | **Auditar webhooks do Hub** | Dev | Risco levantado e não verificado num sistema em produção |
| 4 | **Setup do canal + gravar vídeo 1** | Marketing | Tudo escrito, zero placeholder. Marco C2 é 11/09 |
| 5 | **Deduplicar "conta Capacitação"** | Finance | Item repetido 2× no mesmo L2. 1 minuto |

**Nenhuma delas precisa de estrutura nova. Todas precisam de execução** — que é o gargalo declarado do negócio.

---

## Quando reabrir esta análise

- **Meados de setembro/2026** — junto com a revisão do piloto de divisões do Marketing (após o vídeo 1, marco C2 em 11/09)
- **Ou antes**, se qualquer squad passar nos 3 testes. O gatilho mais provável: **Product ou Dev**, se o Araújo virar contrato pago em 18/09 e o Hub precisar replicar multi-tenant (EME-7) — aí a frente "sustentar cliente atual" passa a se bloquear por motivo diferente de "construir para o próximo"
