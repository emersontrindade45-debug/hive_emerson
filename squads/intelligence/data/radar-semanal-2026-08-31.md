# Radar da Semana — 2026-08-31

> Segundo digest semanal. **12 dias sem radar** — o anterior é de 19/08, e a cadência declarada em `foundation/signal-monitoring.md` é semanal. Fontes: WebSearch (US-only; nenhuma fonte BR indexada).

---

### 🔥 Destaque da semana — e é um alerta, não uma curiosidade

**A Meta colocou um agente de IA nativo dentro do WhatsApp Business, globalmente, e em agosto passou a cobrar por token.** Mais de **1 milhão de negócios** já usam o Meta Business Agent no WhatsApp e Messenger. Ele responde perguntas, recomenda produtos, agenda, qualifica lead e transfere para humano — no idioma e no tom do cliente.

**Por que isso é o item mais importante deste radar:** o AI Retail Automation Hub vende exatamente essa promessa. O diferencial "atendimento por WhatsApp com IA" **deixou de ser diferencial** — passou a vir de fábrica.

⚠️ **Dois documentos ficam desatualizados por causa disto:**
1. O **dever de casa do Contrapeso** (marco A3, reunião do Araújo em 18/09) — a seção "diferenciais do Hub" precisa ser reescrita sabendo que existe um concorrente embutido e sem custo de setup. Se o Araújo descobrir isso na reunião e você não tiver resposta, a âncora de R$4.000 não se sustenta.
2. O **`mapa-teste-publico.md`** — o Pilar 1 (WhatsApp com IA) continua sendo a porta mais limpa em busca, mas o ângulo mudou: não é mais "dá pra colocar IA no WhatsApp", é "a Meta já colocou — e o que ela não faz".

⚠️ **Ressalva de data:** o lançamento global foi em **03/06/2026** (TechCrunch), não nesta semana. O que é de agosto é a **mudança de cobrança para por token**. O achado real aqui não é a novidade — é que isso nunca entrou em nenhum STATE do repo, e já tem quase 3 meses.

---

### 📡 Sinais de IA

- **[Meta Business Agent — WhatsApp Business](https://whatsappbusiness.com/blog/introducing-meta-business-agent-ai/)** — agente nativo global; +1 milhão de negócios ativos; automatiza suporte, recomendação, agendamento e qualificação de lead — **impacto direto no produto e na pauta do canal**
- **[Cobrança por token — Meta developers](https://developers.facebook.com/documentation/business-messaging/whatsapp/pricing/ai-providers)** — desde agosto/2026 cada resposta de IA é cobrada por consumo de token, não por mensagem fixa — muda a conta de quem revende automação de WhatsApp
- **[Anthropic — Claude Sonnet 5](https://llm-stats.com/llm-updates)** — preço promocional virou permanente em 10/08: US$2 por milhão de tokens de entrada, US$10 de saída. Claude Opus 5 (24/07) chegou perto do nível Fable 5 por cerca de metade do preço — o custo unitário do que o Hub faz continua caindo
- **[Salesforce + Anthropic — "Claudeforce"](https://www.informationweek.com/responsible-ai/the-week-of-aug-24-28-what-happened-what-matters-what-s-next)** — Claude embarcado no Salesforce como modelo de raciocínio padrão do Agentic AI. Sinal de que IA em CRM/atendimento virou infraestrutura, não recurso
- **[Governança de agentes](https://www.informationweek.com/responsible-ai/the-week-of-aug-24-28-what-happened-what-matters-what-s-next)** — Google publica o Agent Payments Protocol (AP2), NIST trabalha identidade/permissão de agente, e tramita o AI AGENT Act (S.5051). Microsoft abriu em 18/08 a gestão multi-tenant de agentes no admin do M365
- **[OpenAI](https://llm-stats.com/llm-updates)** — GPT-5.5 Omni (multimodal em tempo real) e atualização do GPT-5.6 no ChatGPT em 06/08
- **[Google DeepMind](https://www.cnbc.com/2026/08/12/google-deepmind-koray-kavukcuoglu.html)** — a reorganização sinalizada no radar de 19/08 se consolidou: Hassabis como chairman, Kavukcuoglu na operação, fim da divisão Brain/DeepMind entre dois continentes

### 🛠️ Ferramentas — n8n (pilar 2 do canal)

- **[n8n release notes](https://docs.n8n.io/release-notes)** — nó AI Agent reconstruído com tool calling em Claude, GPT-4o, Gemini, Mistral, Groq e endpoints compatíveis com OpenAI; quatro tipos de nó de memória (in-memory, Redis, Postgres, Motorhead)
- **Validação de schema JSON em toda chamada de tool**, com retry automático quando o modelo devolve formato errado — mata o problema de loop infinito e requisição alucinada. **Isso é matéria de vídeo Help**: é a dor nº1 de quem monta agente em n8n
- Trilha 2.35/2.36: limite de token na verificação de credencial subiu (modelos de contexto grande deixaram de falhar), módulo `instance-ai` ligado por padrão, busca no registro MCP exposta ao assistente

---

### 💡 Sugestões de pauta

1. **Hero — "A Meta acabou de colocar uma IA de graça no WhatsApp do seu concorrente"** — tipo: tendência traduzida. Pilar 1. Público P1/P2. O gancho é urgência real, não hype, e o eixo do canal ("IA aplicada a trabalho que já existe") cai perfeito
2. **Help — "O que a IA nativa do WhatsApp NÃO faz"** — tipo: educativo/diferenciação. É o mesmo raciocínio que você precisa para o Araújo: onde a solução embutida para, e o que exige alguém que conheça o negócio. **Escrever esta pauta e o dever de casa do Contrapeso é o mesmo trabalho feito duas vezes**
3. **Help — "Seu agente de IA entra em loop? O n8n resolveu isso"** — tipo: técnico aplicado. Pilar 2. Aproveita que o Brasil é o maior mercado global de buscas por "n8n" (12,7%, 193k/mês, relatório de 26/08)

---

## Fontes consultadas

- [Introducing Meta Business Agent on WhatsApp — WhatsApp for Business](https://whatsappbusiness.com/blog/introducing-meta-business-agent-ai/)
- [Meta's AI agent for WhatsApp Business is now available globally — TechCrunch](https://techcrunch.com/2026/06/03/metas-ai-agent-for-whatsapp-business-is-now-available-globally/)
- [New pricing policy for AI Providers leveraging the WhatsApp Business Platform — Meta for Developers](https://developers.facebook.com/documentation/business-messaging/whatsapp/pricing/ai-providers)
- [AI Updates Today (August 2026) — llm-stats](https://llm-stats.com/llm-updates)
- [The week of Aug. 24-28: What happened, what matters, what's next — InformationWeek](https://www.informationweek.com/responsible-ai/the-week-of-aug-24-28-what-happened-what-matters-what-s-next)
- [Release notes — n8n Docs](https://docs.n8n.io/release-notes)
- [Google's new AI boss inherits a race to catch OpenAI and Anthropic — CNBC](https://www.cnbc.com/2026/08/12/google-deepmind-koray-kavukcuoglu.html)

**Confiança:** Média. Buscas via WebSearch, que é US-only — nenhuma fonte brasileira entrou no painel, e o mercado que interessa ao canal é o BR. Datas e preços foram lidos de agregadores, não das páginas oficiais de cada empresa; conferir antes de citar número em vídeo (regra da skill `dados-verificados`).
