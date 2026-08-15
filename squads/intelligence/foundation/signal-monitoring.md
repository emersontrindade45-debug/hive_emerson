# Signal Monitoring — Radar de IA & Business

> Emerson usa este playbook para alimentar o Pietro (Marketing) com atualizações relevantes de IA e negócios, e o Paes (Product) com ferramentas novas para melhoria contínua de produto e de criação de conteúdo. Traduzido e priorizado por potencial de uso real. Objetivo: manter Emerson à frente da curva sem ele precisar garimpar sozinho.

---

## Duas trilhas, duas cadências

| Trilha | Conteúdo | Cadência | Consumidor |
|---|---|---|---|
| **Tendências (IA/Business)** | Ver seções "Fontes por plataforma" abaixo | Semanal | Pietro (Marketing) |
| **Ferramentas** | Novas ferramentas de dev/produto e de criação de conteúdo | **Diária** | Paes (Product) + Pietro (Marketing) |

---

## Como funciona hoje

**Mecanismo:** sob demanda via WebSearch/WebFetch dentro da conversa — ainda não há automação recorrente rodando sozinha em background.

**Gatilho:** Emerson pede ("Emerson, traz o radar da semana" / "traz as ferramentas novas de hoje") ou eu proativamente sugiro ao abrir o squad Intelligence/Marketing/Product se fizer mais de 7 dias (tendências) ou 1 dia (ferramentas) desde o último digest (ver `memory/STATE.md`).

**Idioma:** toda fonte em inglês é traduzida para PT-BR no resumo. Termos técnicos mantidos em inglês entre parênteses quando não há tradução natural (ex: "ajuste fino (fine-tuning)").

---

## Trilha de Ferramentas (diária)

> Objetivo declarado por Emerson: quanto mais ferramentas testadas, maior a chance de melhoria contínua no trabalho e na entrega do produto final. Cobre dois usos distintos — não misturar no digest.

### A. Ferramentas para Produto/Dev (consumidor: Paes)

**Modelos/agentes de IA em alta — acompanhar sempre (lista fixa, 2026-08-15):**
- **Claude Code** (Anthropic) — já em uso ativo no Hub
- **Grok** (xAI)
- **ChatGPT / Codex** (OpenAI)
- Demais LLMs/agentes que emergirem como relevantes para produção de produto (adicionar aqui conforme aparecerem)

**Fontes de descoberta:**
- **Product Hunt** — lançamentos diários, categoria AI/Developer Tools
- **GitHub Trending** — repositórios novos em alta (diário/semanal)
- **Changelogs de plataformas já em uso:** Vercel, Supabase, n8n, Anthropic/Claude, Cursor — novidades que podem melhorar o AI Retail Automation Hub
- **Hacker News (Show HN)** — ferramentas lançadas pela comunidade dev
- **Canais de YouTube/Instagram das próprias empresas donas das LLMs** (OpenAI, Anthropic, xAI, Google) — pendente lista específica, Emerson vai informar quais outros canais (BR ou não) ele confia para tradução/análise de lançamento

### B. Ferramentas para Criação de Conteúdo (consumidor: Pietro)
- **Product Hunt** — categoria AI/Content/Video/Design
- **Ferramentas de edição de vídeo/imagem com IA** (novos lançamentos ou updates relevantes)
- **Novos recursos em ferramentas já usadas:** Canva, CapCut, edição nativa de redes sociais
- **Comunidades de criadores de conteúdo BR** — o que estão testando/recomendando

### Critério de entrada no digest (ferramentas)
Só entra se passar em pelo menos 1 destes:
1. Resolve um problema concreto já identificado (ex: gargalo técnico do Hub, dificuldade de produção de conteúdo)
2. É gratuita ou tem teste grátis — Emerson pode validar sem custo
3. Tem tração real (não é vaporware) — lançada, com usuários, não só anunciada

### Formato do digest diário de ferramentas

```
## Ferramentas Novas — [data]

### 🛠️ Para Produto/Dev
- [Nome] — [o que faz, 1 frase] — [por que pode ajudar o Hub]

### 🎨 Para Criação de Conteúdo
- [Nome] — [o que faz, 1 frase] — [que tipo de conteúdo melhora]
```

---

## Fontes por plataforma

### YouTube
- Canais de lançamento/anúncio oficial: OpenAI, Google DeepMind, Anthropic, Microsoft AI
- Canais de análise/tradução BR: canais brasileiros de tecnologia e IA que já traduzem e comentam lançamentos (a validar com Emerson quais ele já acompanha e confia)
- Buscar por: anúncios de modelo novo, cases de aplicação em pequenas empresas, keynotes de eventos (Google I/O, OpenAI DevDay)

### LinkedIn
- Posts de líderes de IA (pesquisadores, fundadores de startups de IA) com alto engajamento na última semana
- Publicações de consultorias (McKinsey, BCG, Deloitte) sobre adoção de IA em PMEs
- Hashtags/temas: #AI, #InteligenciaArtificial, #PME, #TransformacaoDigital

### Instagram
- Contas de divulgação científica/tech em PT-BR
- Reels de criadores de IA que já traduzem novidades — bom para observar formato, não só conteúdo

### TikTok
- Tendências de formato curto sobre IA (referência de como estruturar Hero/Hub/Help — ver `metodo-influencia-digital.md`)
- Criadores BR que já traduzem lançamentos internacionais

### Outras fontes de tech/IA (majoritariamente em inglês)
- Changelog/blog oficial: OpenAI, Anthropic, Google AI, Vercel AI
- Newsletters: TLDR AI, The Batch (DeepLearning.AI), Ben's Bites
- Comunidades: Hacker News (seção IA), Product Hunt (categoria AI)

---

## Critério de priorização (o que vira conteúdo)

Um sinal só entra no digest se passar em pelo menos 2 destes filtros:

1. **Aplicável a PME/negócio local** — dá pra traduzir em algo que um comerciante entende e usa
2. **Novidade real** — lançamento, mudança de comportamento de mercado, não é rehash
3. **Gera ROI tangível** — Emerson consegue conectar a uma solução de consultoria (foco declarado: sempre ROI ao cliente)
4. **Mapeia num dos 10 tipos de conteúdo** (ver `metodo-influencia-digital.md`) — se não vira post, não entra no digest

---

## Formato do digest semanal

```
## Radar da Semana — [data]

### 🔥 Destaque (1 item)
[O sinal mais forte da semana — o que definitivamente vira conteúdo]

### 📡 Sinais de IA
- [Fonte] — [resumo em PT-BR] — [por que importa pra PME]

### 💼 Sinais de Business/Consultoria
- [Fonte] — [resumo em PT-BR] — [conexão com ROI/aplicação prática]

### 💡 Sugestões de pauta
- [Ideia de conteúdo já classificada: Hero/Hub/Help + tipo dos 10]
```

---

## Active Priorities

- **Pendente:** Emerson vai informar canais específicos de YouTube/Instagram (BR e/ou oficiais das empresas donas de LLM) para completar a lista de fontes de descoberta da trilha de ferramentas
- Validar lista de fontes/canais específicos com Emerson (quais ele já segue e confia) — trilha de tendências (semanal)
- Definir se cadência semanal evolui para automação (n8n) depois do primeiro ciclo manual
- Aguardar material de business/consultoria de ROI que Emerson vai enviar, para incorporar como fonte própria (não só externa)
