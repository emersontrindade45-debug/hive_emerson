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

## Painel de Inteligência — Fontes nomeadas (definido 2026-08-19)

> Curadoria pessoal de Emerson (CEO), organizada por Emerson (Intelligence) em 3 níveis por relevância ao perfil do negócio (n8n, agentes, APIs, RAG, automação). Cobre as duas trilhas: ferramentas (diária) e IA aplicada a negócios/tecnologia de fronteira (semanal).

### Nível 1 — obrigatório (checar sempre)

| Fonte | Canal principal | Por que importa |
|---|---|---|
| **Andrej Karpathy** | [YouTube](http://www.youtube.com/@AndrejKarpathy) · [X](https://x.com/karpathy) · [site](https://karpathy.ai) · [LinkedIn](https://linkedin.com/in/andrej-karpathy-9a650716) · [Eureka Labs](https://eurekalabs.ai) | Conceitos de IA direto da fonte — Nível 3 na origem, mas prioridade 1 pelo peso da opinião |
| **Andrew Ng** | [LinkedIn](https://www.linkedin.com/in/andrewyng/) · [site](https://cs.stanford.edu) · [Coursera](https://coursera.org) | IA aplicada a negócios, referência global |
| **Matt Wolfe** | [YouTube](https://www.youtube.com/@mreflow) · [FutureTools.io](https://futuretools.io) · [Newsletter](https://futuretools.beehiiv.com/subscribe) · [X](https://twitter.com/mreflow) · [Instagram](https://instagram.com/mr.eflow) | Descoberta diária de ferramentas novas — fonte primária do digest diário (Grupo Ferramentas). Nota: Future Tools migrou o foco para curadoria/reviews, não só listagem |
| **Allie K. Miller** | [YouTube (AKM)](https://www.youtube.com/@AKMofficial) · [LinkedIn](https://linkedin.com/in/alliekmiller) · [X](https://twitter.com/alliekmiller) · [Instagram](https://instagram.com/alliekmiller) · [TikTok](https://tiktok.com/@alliekmiller) · [site](https://alliekmiller.com) | IA + negócios + ferramentas — tradução direta pra aplicação prática |
| **Ethan Mollick** | [LinkedIn](https://linkedin.com/in/emollick) · [site](https://startupinnovation.org) | "Como a IA muda o trabalho" — direto pro ângulo de ROI/produtividade |
| **The AI Advantage (Igor)** | [YouTube](https://joinaiaclub.com/igor) | Formato pegar ferramenta → testar → mostrar uso — bom modelo de conteúdo prático |

### Nível 2 — inteligência de mercado

| Fonte | Canal principal | Por que importa |
|---|---|---|
| **Ben's Bites** | Newsletter (já listada acima) | Curadoria diária de notícias de IA |
| **Demis Hassabis** | [LinkedIn](https://linkedin.com/in/demishassabis) · [DeepMind](https://deepmind.google) | Direção estratégica da IA (Google DeepMind) |
| **Dario Amodei** | (CEO Anthropic — perfis a confirmar) | Direção estratégica da IA (Anthropic) — dona da LLM em uso ativo no Hub |
| **Yann LeCun** | [LinkedIn](https://linkedin.com/in/yann-lecun) · [site](https://yann.lecun.com) · [NYU](https://cs.nyu.edu) | Para onde a tecnologia está indo — visão crítica/alternativa |

### Nível 3 — pesquisa/futuro

| Fonte | Canal principal | Por que importa |
|---|---|---|
| **Fei-Fei Li** | [LinkedIn](https://linkedin.com/in/fei-fei-li-4541247) · [Stanford](https://profiles.stanford.edu) | Computer vision, spatial intelligence, IA aplicada, modelos multimodais |
| Outros pesquisadores de frontier AI | — | Adicionar conforme emergirem |

### Fontes adicionais — descoberta de ferramentas (apoio ao Nível 1)

- **MattVidPro AI** — [YouTube](https://www.youtube.com/@mattvidpro) · [X](https://twitter.com/mattvidpro) · [Instagram](https://instagram.com/mattvidpro) · [TikTok](https://tiktok.com/@mattvidpro) — descoberta de ferramentas
- **Dinastia (IA para Negócios)** — [YouTube](https://www.dinastia.uk) — IA aplicada a negócios, conteúdo BR

### Fontes específicas de stack (uso direto no Hub — prioridade Produto/Dev)

- **Cursor** — [YouTube](https://www.youtube.com/@cursor_ai) — IDE em uso
- **Claude Code** — [YouTube](https://www.youtube.com/@claude) — ferramenta de execução em uso ativo
- **Grok** — [YouTube](https://www.youtube.com/@Grok) — LLM no watchlist fixo (ver seção Ferramentas acima)
- **OpenAI** — [YouTube](https://www.youtube.com/@OpenAI) — LLM no watchlist fixo
- **Linear** — [site](https://linear.app) — ferramenta de PM já em uso (Linear MCP conectado)
- **AI Hero (Matt Pocock)** — [site](https://aihero.dev) — tutoriais de engenharia aplicada, útil para Dev

### Como usar o painel

- **Trilha diária (Ferramentas → Paes + Pietro):** Nível 1 (Matt Wolfe, The AI Advantage, AKM) + MattVidPro + fontes de stack — checar por lançamentos que passem no critério de entrada já definido acima
- **Trilha semanal (Tendências → Pietro):** Nível 1 completo + Nível 2 — sinais que viram conteúdo Hero/Hub/Help
- **Radar trimestral/sob demanda (Frontier AI → CEO/Intelligence):** Nível 3 — não vira conteúdo direto, alimenta visão estratégica de Emerson (CEO) sobre para onde a IA está indo

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

- **[x] Fechado 2026-08-19:** painel de inteligência com fontes nomeadas definido (ver seção acima) — 6 fontes Nível 1, 4 Nível 2, Nível 3 aberto para pesquisadores frontier AI
- Rodar primeiro digest semanal de tendências usando o painel novo
- Definir se cadência semanal evolui para automação (n8n) depois do primeiro ciclo manual
- Aguardar material de business/consultoria de ROI que Emerson vai enviar, para incorporar como fonte própria (não só externa)
