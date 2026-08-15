# Budget — Estrutura de Custos Real

> Dados reais fornecidos por Emerson em 2026-08-15, a partir do extrato completo de gastos empresariais Jan–Dez 2026. Nenhum valor aqui é estimativa — o que não foi confirmado fica em branco, conforme regra do Lorenzo (sem aproximação em relatório financeiro).

## Contexto

- **Entidade legal:** MEI
- **Receita atual:** R$ 0 — projeto AI Retail Automation Hub (cliente Araújo) ainda em piloto, sem cobrança
- **Reserva/capital próprio:** R$ 400,00/mês (aporte recorrente confirmado — não é saldo acumulado, é quanto Emerson reserva por mês para custear a empresa)
- **Empresa:** 100% custeada com capital próprio, sem receita ainda entrando

---

## 1. Custo Fixo Recorrente — Ferramentas Digitais (6004)

> Consolidado a partir do extrato completo Jan–Dez 2026. Cada item confirmado com Emerson item a item (2026-08-15).

**Custo fixo mensal atual, confirmado (base Set/Out/Nov/2026 — padrão estável mais recente):**

| Ferramenta | Valor mensal (R$) | Uso | Status |
|---|---:|---|---|
| Cursor Pro | 113,38 | IDE / dev com IA | Ativo |
| Claude Code (Anthropic) | 117,85 | Agente de dev com IA | Ativo |
| Google One (×2 assinaturas confirmadas) | 19,98 (9,99 × 2) | Armazenamento | Ativo o ano todo |
| VPS Hostinger | 108,00 | Hospedagem (provável n8n) — mesmo servidor o ano todo; valor subiu de R$89,99 (jan/fev) → R$70,99 (mai/jun) → R$108,00 (jul em diante, confirmado como preço atual) | Ativo |
| **Total fixo confirmado** | **359,21/mês** | | |

**Fora do fixo — não entra no cálculo acima:**

- **ChatGPT (R$106,33, abril)** — gasto pontual/avulso, nunca foi assinatura recorrente. Confirmado pelo Emerson.
- **Canva (R$35, julho)** — foi uso avulso único até agora. Emerson vai assinar em breve (necessidade confirmada para criação de conteúdo — ver squad Marketing) — **não contar como custo atual, mas prever como próximo custo fixo a entrar**.
- **Domínio mercadoaraujo.com (~R$51) e "Hostinger Renovação Domínio evo.api" (R$181,08)** — registro de domínio, recorrência anual, não mensal.
- **Hospedagem Hostinger (R$51,99)** — **descontinuada, confirmado pelo Emerson.** Não conta mais em nenhum mês daqui em diante.

**Projeção com Canva entrando:** R$ 359,21 + R$ 35,00 = **~R$ 394,21/mês** quando a assinatura for contratada.

## 2. Capacitação — Cursos (sem código COGS/OPEX ainda — sugestão: nova conta "Capacitação")

| Curso | Valor | Padrão |
|---|---:|---|
| Nocode | R$ 157,53/mês | **Encerra em agosto/2026, confirmado pelo Emerson.** A partir de setembro/2026 este custo sai do fixo mensal. |
| Arkad | R$ 156,32 | Parcelado 1/2 (jan) e 2/2 (fev) — encerrado, não é custo recorrente contínuo |
| ChatGPT | R$ 106,33 | Gasto avulso único (abril) — não é curso nem recorrente |

Este é o material-base do `metodo-influencia-digital.md` e `business-opportunities.md` do squad Marketing/Intelligence — o investimento em aprendizado já está gerando ativo de conteúdo documentado.

## 3. Marketing — Tráfego Pago (6003, variável por natureza)

Facebook Ads: valores irregulares, de R$ 6 a R$ 225 por lançamento de campanha, concentrados em jan/fev/jun/jul de 2026. **Não é custo fixo** — depende de decisão ativa de investir em campanha. Marketing/Pietro deve reportar cada campanha lançada para o Finance rastrear ROI por campanha.

## 4. Investimento Pontual — Aquisições Empreendimento (não é OPEX recorrente)

Gastos físicos ligados à validação do piloto Araújo — ringlight, luminária, prateleira, fone, impressões de material (fev–jun/2026, concentrado no início do projeto). Tratar como investimento pontual de validação de produto/mercado, não como custo estrutural do negócio. Não entra no cálculo de "custo fixo mensal".

---

## Custo fixo total mensal (visão consolidada)

**Até agosto/2026:** R$ 359,21 (Ferramentas) + R$ 157,53 (Nocode) = **R$ 516,74/mês**.

**A partir de setembro/2026 (Nocode encerrado):** custo fixo cai para **R$ 359,21/mês**, só ferramentas digitais.

## Reserva vs. custo fixo — situação de caixa

- **Reserva mensal do Emerson:** R$ 400,00/mês
- **Custo fixo até agosto:** R$ 516,74/mês → **déficit de R$ 116,74/mês** (reserva não cobre o custo fixo enquanto o Nocode estava ativo)
- **Custo fixo a partir de setembro:** R$ 359,21/mês → **sobra de R$ 40,79/mês** (reserva passa a cobrir o fixo, com folga pequena)

A folga de ~R$ 40,79/mês a partir de setembro é o que sobra para: Canva (R$35, projetado), qualquer novo custo fixo, ou tráfego pago pontual. Com Canva entrando (R$394,21/mês de fixo), a folga real cai para ~R$ 5,79/mês — margem muito apertada, quase sem espaço para imprevisto.

---

## Pendências para fechar a estrutura

- [x] VPS Hostinger vs. Hospedagem Hostinger — confirmado como mesmo servidor, preço reajustado ao longo do ano (não são serviços duplicados)
- [x] ChatGPT — confirmado como gasto avulso, não recorrente
- [x] Canva — confirmado como avulso até agora; assinatura recorrente prevista para entrar em breve
- [x] Hospedagem Hostinger — confirmado descontinuada
- [x] Nocode — confirmado encerramento em agosto/2026
- [x] Reserva/capital próprio — confirmado R$ 400,00/mês
- [ ] Criar conta própria no chart-of-accounts.md para "Capacitação/Cursos" — hoje não tem código dedicado
- [ ] Decidir se Canva entra já ou se espera a folga de caixa crescer (hoje ficaria em ~R$5,79/mês de sobra, risco alto)

## Active Priorities

<!-- O que Lorenzo deve focar agora -->
- Alertar Emerson: a partir de setembro/2026 a reserva de R$400/mês passa a cobrir o custo fixo (R$359,21), mas com folga mínima (~R$40,79). Qualquer novo custo fixo (Canva incluso) aperta a margem para quase zero. Antes de assinar Canva, avaliar se algum custo atual pode ser cortado ou se a reserva mensal deve subir.
