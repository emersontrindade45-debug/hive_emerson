# Organograma HIVE — do CEO às divisões

> Criado 2026-08-25. Mapa completo das 3 camadas de administração.
> **Camada 1 — Estratégica:** Emerson (CEO) · **Camada 2 — Tática:** 11 Heads de squad · **Camada 3 — Operacional:** divisões dentro do squad.
> Cadeia de reporte: **divisão → Head → CEO**. Divisão nunca reporta direto ao CEO.

---

## Visão geral

```mermaid
flowchart TD
    CEO["👤 EMERSON — CEO<br/><i>Camada Estratégica</i><br/>direção · prioridade do trimestre"]

    CEO --> ST["🎯 Stamper — Chief of Staff<br/><i>Orquestração</i>"]

    ST --> MKT["📣 Pietro<br/>Marketing"]
    ST --> COM["💼 Tatiane<br/>Commercial"]
    ST --> CS["🤝 Figueiredo<br/>CS"]
    ST --> PRD["📦 Paes<br/>Product"]
    ST --> FIN["💰 Lorenzo<br/>Finance"]
    ST --> DEV["⚙️ Brenda<br/>Dev"]
    ST --> INF["🖥️ Emilly<br/>Infra"]
    ST --> OPS["📋 Cristina<br/>Operations"]
    ST --> QLT["✅ Trindade<br/>Quality"]
    ST --> INT["🔍 Emerson<br/>Intelligence"]

    MKT --> M1["M1 · Conteúdo e Editorial 🟢"]
    MKT --> M2["M2 · Inteligência 🟢"]
    MKT --> M3["M3 · Operações e Análise 🟢"]
    MKT --> M4["M4 · Marca e Criação 🟢"]
    MKT --> M5["M5 · Distribuição e Comunidade 🟡"]
    MKT --> M6["M6 · Crescimento e Performance 🔴"]

    classDef ceo fill:#16181D,stroke:#F2A03D,stroke-width:3px,color:#EDE7DE
    classDef head fill:#1F232B,stroke:#8A9099,color:#EDE7DE
    classDef ativa fill:#1d3b2a,stroke:#4ade80,color:#e8f5ee
    classDef dormente fill:#3d3520,stroke:#eab308,color:#faf5e6
    classDef congelada fill:#3d2020,stroke:#ef4444,color:#fae6e6
    class CEO ceo
    class ST,MKT,COM,CS,PRD,FIN,DEV,INF,OPS,QLT,INT head
    class M1,M2,M3,M4 ativa
    class M5 dormente
    class M6 congelada
```

**Legenda de status:** 🟢 ATIVA (trabalho recorrente) · 🟡 DORMENTE (definida, aguarda gatilho) · 🔴 CONGELADA (gatilho duplo)

---

## Camada 1 — Estratégica

| Papel | Quem | Decide |
|---|---|---|
| **CEO** | Emerson | Direção da empresa, prioridade do trimestre, o que entra e o que sai, aprovação de custo |
| **Chief of Staff** | Stamper | Não decide direção — **orquestra**: roteia assunto ao squad certo, agrega L1, rastreia loop aberto |

**Capacidade real:** 20h/semana. É a restrição que dimensiona todo o resto — ver `disponibilidade-emerson`.

---

## Camada 2 — Tática (11 squads)

| Squad | Head | Escopo | Divisões |
|---|---|---|---|
| `marketing/` | **Pietro** | Conteúdo, campanha, marca, social | **6** (ver abaixo) |
| `commercial/` | **Tatiane** | Lead gen, proposta, CRM, pipeline | — |
| `cs/` | **Figueiredo** | Onboarding, sucesso do cliente, suporte | — |
| `product/` | **Paes** | Roadmap, stories, priorização, **Product Marketing** | — |
| `finance/` | **Lorenzo** | DRE, faturamento, fluxo de caixa, orçamento | — |
| `dev/` | **Brenda** | Código, review, arquitetura, deploy | — |
| `infra/` | **Emilly** | VPS, monitoramento, CI/CD, segurança | — |
| `operations/` | **Cristina** | RH, cultura, metas, processos | — |
| `quality/` | **Trindade** | SOPs, auditoria, padrões | — |
| `intelligence/` | **Emerson** | Intel competitiva, pesquisa, **Comms/PR** | — |

**Só Marketing tem divisões hoje.** Condição para replicar: o squad precisa de volume real e recorrente em frentes que se bloqueiam por motivos diferentes. Nenhum outro atende hoje.

---

## Camada 3 — Operacional (divisões do Marketing)

```mermaid
flowchart LR
    P["📣 Pietro<br/>Head of Marketing"]

    subgraph ATIVAS["🟢 Ativas — trabalho recorrente hoje"]
        M4["<b>M4 · Marca e Criação</b><br/>identidade · narrativa<br/>tese · território"]
        M2["<b>M2 · Inteligência</b><br/>radar · técnica<br/>dado verificado"]
        M1["<b>M1 · Conteúdo e Editorial</b><br/>calendário · roteiro<br/>pauta · SEO"]
        M3["<b>M3 · Operações e Análise</b><br/>stack · dados<br/>atribuição · setup"]
    end

    subgraph ESPERA["🟡🔴 Aguardando gatilho"]
        M5["<b>M5 · Distribuição<br/>e Comunidade</b> 🟡<br/>gatilho: 2ª plataforma<br/>ou 8º vídeo"]
        M6["<b>M6 · Crescimento</b> 🔴<br/>gatilho: verba<br/><b>E</b> ≥8 vídeos"]
    end

    P --> M4 & M2 & M1 & M3
    P -.-> M5 & M6

    M4 -->|"rege a voz"| M1
    M2 -->|"dado verificado<br/>+ técnica"| M1
    M1 -->|"peça pronta"| M3
    M3 -->|"métrica"| M1
    M3 -.->|"padrão contraria<br/>hipótese"| M4
    M1 -.->|"peça original"| M5

    classDef head fill:#1F232B,stroke:#F2A03D,stroke-width:2px,color:#EDE7DE
    classDef ativa fill:#1d3b2a,stroke:#4ade80,color:#e8f5ee
    classDef espera fill:#33302a,stroke:#8A9099,color:#e8e6e3
    class P head
    class M1,M2,M3,M4 ativa
    class M5,M6 espera
```

### Detalhe das divisões

| # | Divisão | Equivalente de mercado | Status | Gatilho |
|---|---|---|---|---|
| **M1** | Conteúdo e Editorial | *Content / Editorial* | 🟢 | — |
| **M2** | Inteligência | *Market / Competitive Intel* | 🟢 | — |
| **M3** | Operações e Análise de Marketing | *Marketing Ops & Analytics* | 🟢 | — |
| **M4** | Marca e Criação | *Brand & Creative* | 🟢 | — |
| **M5** | Distribuição e Comunidade | *Distribution + Community* | 🟡 | 2ª plataforma publicando **ou** 8º vídeo / 100 inscritos |
| **M6** | Crescimento e Performance | *Growth / Performance* | 🔴 | Verba aprovada **E** ≥8 vídeos |

---

## Padrão de estrutura: **funcional** (modelo Apple)

O HIVE recorta por **função/especialidade**. Referência: Apple sob P&L único e organização funcional desde 1997, mantida com 137 mil funcionários ([HBR, Podolny & Hansen, 2020](https://hbr.org/2020/11/how-apple-is-organized-for-innovation)).

| Princípio Apple | No HIVE |
|---|---|
| P&L único da empresa | Divisão não tem orçamento nem meta própria — P&L é da empresa (Lorenzo) |
| Função, não produto/mercado | Divisão nasce de especialidade distinta, nunca de cliente, canal ou plataforma |
| *Experts leading experts* | Autoridade vem do material de referência obrigatório, não do cargo |
| Sem gerente geral de unidade | Divisão é escopo, não cargo. O Head segue único dono tático |

**Modelos avaliados e descartados:** geografia (McDonald's — 3 segmentos: U.S., IOM, IDL) não se aplica com 1 mercado · linha de produto com P&L próprio (Dell — ISG e CSG) não se aplica sem receita a segmentar · CEO com N reports diretos (Tesla — 7 diretos, sem COO) contradiz a cadeia divisão → Head → CEO.

⚠️ A Apple é o caso de uma empresa que **reduziu** unidades para inovar mais. Estrutura funcional argumenta a favor de **menos** divisões, não de mais.

---

## Interfaces — funções de mercado que NÃO são do Marketing

Existem no organograma, mas o dono é outro squad. Evita dois donos para a mesma coisa.

```mermaid
flowchart LR
    M4["M4 · Marca e Criação<br/><i>Marketing</i>"]
    PRD["📦 Paes — Product<br/><b>Product Marketing</b><br/>posicionamento de oferta<br/>lançamento"]
    COM["💼 Tatiane — Commercial<br/>usa material de venda"]
    INT["🔍 Emerson — Intelligence<br/><b>Comms / PR</b><br/>imprensa · relações públicas"]

    M4 -->|"narrativa e voz<br/>aprovadas"| PRD
    M4 -->|"narrativa aprovada"| INT
    PRD -->|"material de venda"| COM

    classDef mkt fill:#1d3b2a,stroke:#4ade80,color:#e8f5ee
    classDef outro fill:#1F232B,stroke:#8A9099,color:#EDE7DE
    class M4 mkt
    class PRD,COM,INT outro
```

| Função | Dono | Papel do Marketing |
|---|---|---|
| **Product Marketing** — posicionamento de oferta, lançamento, material de venda | **Product (Paes)** + Commercial (Tatiane) | M4 fornece narrativa e voz. **Não decide a oferta** |
| **Comms / PR** — imprensa, relações públicas, crise | **Intelligence (Emerson)** | M4 fornece narrativa aprovada. **Não conduz o relacionamento** |

⚠️ Demanda de posicionamento de oferta → rotear para **Paes**. Imprensa → rotear para **Intelligence**. Nunca duplicar no Marketing.

---

## Regras que governam o modelo

1. **Reporte sobe um nível por vez.** Divisão → Head → CEO. Divisão nunca fala direto com o CEO — isso esvaziaria a camada tática e multiplicaria os fluxos que chegam a quem tem 20h/semana.
2. **Divisão executa, Head prioriza, CEO decide direção.** Divisão não escolhe o que é prioridade.
3. **Dormente não custa.** Não gera tarefa, não entra em revisão de STATE, não recebe prefixo no L2.
4. **Anti-inchaço:** divisão 🟢 sem item no L2 por 30 dias é rebaixada a 🟡.
5. **Replicar divisões a outro squad** só quando houver volume real e recorrente em frentes que se bloqueiam por motivos distintos.
6. **Uma função, um dono.** Se duas caixas reivindicam a mesma coisa, uma delas está errada.

**Revisar o modelo:** meados de setembro/2026, depois do marco C2 (11/09).
