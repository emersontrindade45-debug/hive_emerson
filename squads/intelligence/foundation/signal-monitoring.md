# Signal Monitoring — Radar de IA & Business

> Rex usa este playbook para alimentar o Pietro (Marketing) com atualizações relevantes de IA e negócios, traduzidas e priorizadas por potencial de virar conteúdo. Objetivo: manter Emerson à frente da curva sem ele precisar garimpar sozinho.

---

## Como funciona hoje

**Mecanismo:** sob demanda via WebSearch/WebFetch dentro da conversa — ainda não há automação recorrente rodando sozinha em background.

**Cadência alvo:** resumo semanal.

**Gatilho:** Emerson pede ("Rex, traz o radar da semana") ou eu proativamente sugiro ao abrir o squad Intelligence/Marketing se fizer mais de 7 dias desde o último digest (ver `memory/STATE.md`).

**Idioma:** toda fonte em inglês é traduzida para PT-BR no resumo. Termos técnicos mantidos em inglês entre parênteses quando não há tradução natural (ex: "ajuste fino (fine-tuning)").

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

- Validar lista de fontes/canais específicos com Emerson (quais ele já segue e confia)
- Definir se cadência semanal evolui para automação (n8n) depois do primeiro ciclo manual
- Aguardar material de business/consultoria de ROI que Emerson vai enviar, para incorporar como fonte própria (não só externa)
