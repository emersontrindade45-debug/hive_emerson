# Tech Decision Playbook

Base de conhecimento para **decisão técnica de negócio** — escolha de stack, arquitetura, banco e infraestrutura ao construir apps, software e IA.

**Não é** insumo de conteúdo (isso é `squads/marketing/foundation/youtube-playbook.md`).

---

## Como usar este arquivo

Consultar antes de escolher tecnologia, dimensionar servidor ou mudar arquitetura. Cada item traz:

- **Origem** — canal + data (conteúdo de infra envelhece; item com +12 meses vira suspeito)
- **Confiança** — `medido` (benchmark com número) > `experiência` (relato de produção) > `opinião`
- **Eixo** — economia / segurança / confiabilidade

### Regras de uso

1. **Enriquecer, não substituir.** YouTube traz o tradeoff vivido em produção; a doc oficial traz a verdade da API. Onde divergirem, **eu pergunto ao Emerson** — não decido sozinho nem descarto o canal.
2. **Contexto de orçamento é regra dura.** Hoje: MEI, receita R$ 0, R$ 400/mês de capital próprio (ver `squads/finance/foundation/budget.md`). Conselho que assume orçamento de startup financiada **não se aplica** — e isso deve ser dito explicitamente, não silenciado.
3. **Operação destrutiva exige "sim" explícito.** Regra do HIVE, vale aqui integralmente.

---

## Stack atual (o que já está em produção)

Hub de automação do cliente Araújo — ver `squads/product/foundation/roadmap.md`:

Next.js 15 · Supabase/PostgreSQL (Realtime, pgvector) · n8n · Evolution API (WhatsApp) · Resend · Vercel

Toda decisão abaixo é avaliada contra **este** stack, não contra um projeto hipotético.

---

## Banco de dados

### PostgreSQL vs SQLite — quando cada um
`Anton Putra, 2026-01-04` · **medido** · confiabilidade + economia

SQLite é **significativamente mais rápido** que Postgres no mesmo servidor — escrever em arquivo local elimina a rede. Teste com CRUD completo de carrinho de compras (insert/select/update/delete + join).

- **SQLite:** biblioteca embarcada, arquivo local. Um servidor só. Casos: mobile, IoT, app pequeno de servidor único (ex.: WordPress).
- **Postgres:** aplicação separada, acessada por rede. Necessário quando há mais de um servidor ou acesso concorrente distribuído.

**Truque de latência:** app e Postgres no mesmo servidor → conectar por **unix socket** em vez de TCP/IP. Menor latência e mais estável. Limitação: servidor único.

> **Aplicação ao nosso caso:** o Hub usa Supabase (Postgres gerenciado, remoto) — a troca por SQLite **não** se aplica, porque precisamos de Realtime, pgvector e acesso de múltiplos clientes. Mas a lição do unix socket vale se algum dia rodarmos Postgres próprio em VPS.

**Ferramenta citada:** `PGTune` — gera config de Postgres otimizada para o hardware. Ponto de partida recomendado.

---

## Cache

### Redis — o que é e quando faz sentido
`ByteByteGo, 2026-02-18` · **experiência** · confiabilidade

Servidor de estrutura de dados **em memória, single-thread**. Três consequências de design:

1. **Execução sequencial.** Comandos rodam um por vez, em ordem. Sem lock, sem escrita concorrente na mesma chave — operações como `INCR` são atômicas de graça. **Contrapartida:** um comando lento bloqueia todos os outros atrás dele.
2. **Dados em RAM.** Latência sub-milissegundo. **Contrapartida:** se a máquina morre, os dados somem — a menos que persistência esteja configurada.
3. **Estruturas expostas direto:** string, list, hash, set, sorted set, stream.

Velocidade apesar do single-thread vem de **pipelining** — agrupar comandos numa ida de rede só.

**Três posturas de durabilidade (escolha consciente):**

| Postura | Como | Risco aceito |
|---|---|---|
| Cache puro | Persistência desligada; banco é fonte da verdade | Perde o cache no crash; app reconstrói consultando o banco |
| Cache + réplicas | Primário escreve, réplicas leem; promoção em falha | Segundos de indisponibilidade no failover |
| Persistência ligada | Configurar RDB/AOF | Custo de I/O e complexidade |

> **Aplicação ao nosso caso:** hoje **não temos Redis** e provavelmente não precisamos. Com receita R$ 0 e um cliente, adicionar Redis é custo mensal + superfície de falha sem ganho mensurável. Reavaliar só quando houver gargalo medido de leitura no Supabase — **nunca preventivamente**.

### Redis vs Valkey
`Anton Putra, 2026-02-24` · **medido** · economia

Valkey é o fork open-source do Redis (criado após a mudança de licença do Redis). Existe benchmark comparativo 8.6 vs 9.0. Relevante caso um dia precisemos de cache — Valkey evita risco de licença.

---

## Linguagem de backend

### Python/FastAPI vs JavaScript/Bun
`Anton Putra, 2025-12-30` · **medido** · confiabilidade

Comparação de latência, throughput, CPU e memória, com e sem Postgres. Ponto relevante levantado: **comportamento do connection pool no Bun** exigiu correção — pool mal configurado distorce qualquer benchmark (e derruba app em produção).

Bun (2021, escrito em Zig) compete com linguagens mais especializadas como Go.

> **Aplicação ao nosso caso:** o Hub é Next.js (Node). Não há motivo de migrar. A lição que importa é **connection pooling** — com Supabase, pool mal dimensionado é a causa clássica de erro sob carga. Verificar antes de escalar para o segundo cliente.

---

## Segurança e rede

### VPN — revisão de posição
`NetworkChuck, 2026-06-15` — "I was wrong about VPNs" · **experiência** · segurança

O autor revisa publicamente sua recomendação anterior sobre VPNs comerciais. Relevante como lembrete de que conselho de segurança envelhece — inclusive o deste playbook.

> ⚠️ Item a aprofundar quando formos tratar de acesso remoto a VPS. Ainda não extraí a conclusão específica.

---

## Lacunas conhecidas

O que este playbook **não** cobre e seria preciso para decisão bem-informada:

- **Custo real de Vercel/Supabase em escala** — os canais monitorados não tratam disso. É consulta à doc oficial + cálculo próprio.
- **n8n em produção** — nenhum canal cobre. Nosso maior ponto cego, já que o Hub depende dele.
- **Backup e recuperação** — nada coletado ainda. Crítico com cliente real em produção.

Registrado aqui de propósito: **saber o que não sabemos** vale mais que preencher com achismo.
