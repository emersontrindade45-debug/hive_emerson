# Engineering Playbook

Base de **decisão e habilidade técnica** da Brenda — como construímos software, que padrões seguimos, o que mudou no ecossistema que afeta nosso código.

**Não é** insumo de conteúdo (isso é `squads/marketing/`). **Não é** decisão de infraestrutura (isso é `squads/infra/foundation/tech-decision-playbook.md`).

**Última atualização:** 2026-08-23

---

## Como usar

Consultar antes de arquitetar feature, escolher biblioteca ou definir padrão de código. Cada item traz **origem** (canal + data) e **aplicação ao nosso stack**.

Ecossistema JS/IA envelhece rápido: item com +6 meses precisa de revalidação antes de virar decisão.

**Regra de colisão** (igual à do Infra): canal vs doc oficial vs o que já roda em produção → apresentar o tradeoff a Emerson. Nunca decidir em silêncio, nunca descartar o canal por ser "só YouTube".

## Nosso stack

Next.js 15 (mobile-first) · Node/TypeScript · Supabase/PostgreSQL (Realtime, pgvector) · n8n · Evolution API · Resend · Vercel · Multi-repo

---

## Arquitetura de agentes de IA

> Área mais relevante hoje: o Hub do Araújo é um sistema de agentes em produção, e o próximo produto também será.

### Projetar o agente a partir do processo humano, não da tecnologia
`freeCodeCamp, 2026-08-14` — "System Design for AI Agents"

O erro padrão (e o que "400 tutoriais" ensinam): pegar o input, jogar num prompt com RAG, chamar de pronto. Isso **não** é sistema de produção.

O método proposto, componente a componente:

1. **Achar o sistema humano que já resolveu o problema.** Observar como um sênior de verdade faz a tarefa.
2. **Trazer o contexto** que esse humano consultaria → vira o *retriever*.
3. **Separar preocupações.** Um revisor humano pensa em segurança, qualidade, correção, teste, documentação — mentalidades distintas → vira **arquitetura multi-agente**, não um reasoner único.
4. **Toda conclusão carrega evidência** → cada achado do agente precisa de **rationale + confidence**.

**A pergunta que define a arquitetura:** não é "como automatizar a tarefa", é **"o que o agente decide sozinho e o que merece julgamento humano"**. A seletividade é a arquitetura inteira.

### Enumerar modos de falha antes de codar
`freeCodeCamp, 2026-08-14`

Para cada componente, perguntar "o que pode dar errado?" em duas direções:

- **Engenharia:** webhook reentregue em duplicata; requisição forjada que não veio da origem oficial; a origem exige ACK em 10s mas o agente leva 90s.
- **LLM:** modelo alucina; retriever puxa o trecho errado.

Classificar as falhas numa matriz 2×2: *o que sei que não sei* × *o que reconheço quando vejo* × *o que nunca considerei*. Segundo o autor, o design do componente "se escreve sozinho" depois disso.

> **Aplicação direta ao Hub:** o Hub recebe webhook de WhatsApp (Evolution API) e Instagram. **Reentrega duplicada e requisição forjada são riscos reais nossos, hoje.** Vale auditar se tratamos idempotência e verificação de origem. Item para o `/dev-debate`.

### O que um sistema de agente de produção precisa ter
`freeCodeCamp, 2026-08-14`

- Fila de aprovação humana
- Trace viewer (rastrear o que cada agente fez)
- **Dashboard de custo** — economia de LLM é parte da arquitetura, não detalhe
- Verificador independente que confere se o trabalho foi realmente feito
- Definition of done explícita por milestone

---

## Trabalhar com IA para escrever código

### Dirigir o agente, não delegar o pensamento
`freeCodeCamp, 2026-08-14`

A postura recomendada: definir invariantes, definition of done e o que cada milestone entrega — e então rodar o loop com **gates de verificação**. O agente executa contra essa espinha dorsal; você dirige e mantém o controle, em vez de esperar que ele pense por você.

Alinha com a regra do HIVE: nunca declarar incompleto como pronto.

### Modelos verificam o próprio trabalho — e alucinam com mais confiança
`Fireship, 2026-07-29`

Sobre o Claude Opus 5: 1M de contexto, até 128k de saída, níveis de thinking (low → max). Ponto que importa para nós: a **taxa de alucinação subiu 14 pontos percentuais**, chegando a ~50% nos casos em que o modelo não sabe a resposta.

Não significa que metade do que sai é falso — significa que, **quando não sabe, ele tem mais chance de construir uma explicação bem argumentada de um fato inventado**.

> **Regra prática:** resposta bem escrita e confiante não é evidência de correção. Verificar contra doc oficial ou execução real. Vale para mim também — foi exatamente o que aconteceu quando inventei um ID de vídeo no radar de Marketing e precisei corrigir.

---

## Ecossistema — o que observar

### O fosso do "saber codar" está encolhendo
`Fireship, 2026-07-29`

Tese do vídeo: o modelo indie hacker (aprender a codar → achar nicho → shippar micro-SaaS) tinha o código como barreira de entrada. Com IA, essa barreira cai.

> **Leitura para o nosso negócio:** se escrever código deixa de ser o diferencial, o diferencial vira **o domínio do problema** — entender a operação de um açougue/mercearia a ponto de modelar o processo. É o que o Hub do Araújo já é. Reforça a estratégia atual em vez de ameaçá-la.

---

## Lacunas conhecidas

Nenhum canal monitorado cobre:

- **n8n em produção** — o Hub depende dele. Mesmo ponto cego do Infra.
- **Padrões de Next.js 15 App Router** — Fireship dá notícia, não profundidade. Consultar doc oficial.
- **Supabase Realtime em escala** — sem cobertura.

Registrado de propósito: saber o que não sabemos vale mais que preencher com achismo.
