# Budget — Estrutura de Custos Real

> Dados reais fornecidos por Emerson em 2026-08-15, a partir de extrato de gastos empresariais de 2026. Nenhum valor aqui é estimativa — o que não foi confirmado fica em branco, conforme regra do Lorenzo (sem aproximação em relatório financeiro).

## Contexto

- **Entidade legal:** MEI
- **Receita atual:** R$ 0 — projeto AI Retail Automation Hub (cliente Araújo) ainda em piloto, sem cobrança
- **Reserva/capital próprio:** existe, valor a confirmar
- **Empresa:** 100% custeada com capital próprio, sem receita ainda entrando

---

## 1. Custo Fixo Recorrente — Ferramentas Digitais (6004)

> Assinaturas mensais previsíveis. Valores variam ligeiramente mês a mês (câmbio/plano), faixa observada:

| Ferramenta | Faixa mensal (R$) | Uso |
|---|---:|---|
| Cursor Pro | 113 – 118 | IDE / dev com IA |
| Claude Code (Anthropic) | 110 – 118 | Agente de dev com IA |
| VPS Hostinger (renovação) | 71 – 108 | Hospedagem (provável n8n) |
| Google One (×2 assinaturas) | ~20 (10 × 2) | Armazenamento |
| Canva | 35 | Design (aparece 1x — confirmar se é mensal ou anual rateado) |
| Hospedagem Hostinger (item separado da VPS) | ~52 | A confirmar se é serviço distinto da VPS |
| Domínio (mercadoaraujo.com) | ~51 | Registro anual, aparece como parcela |

**Estimativa de piso mensal só nesta categoria: ~R$ 400–470/mês** (soma das faixas baixas). Não é número fechado — falta confirmar duplicidades (ex.: "VPS Hostinger" vs. "Hospedagem Hostinger" podem ser a mesma coisa contabilizada 2x).

## 2. Capacitação — Cursos (sem código COGS/OPEX ainda — sugestão: 6004 ou nova conta "Capacitação")

| Curso | Valor | Padrão |
|---|---:|---|
| Nocode | R$ 157,53/mês | Recorrente, parece assinatura/parcelamento longo (visto em 6+ meses) |
| Arkad | R$ 156,32 | Parcelado 1/2, 2/2 — **não é recorrente contínuo**, projeto vai terminar |

Este é o material-base do `metodo-influencia-digital.md` e `business-opportunities.md` do squad Marketing/Intelligence — o investimento em aprendizado já está gerando ativo de conteúdo documentado.

## 3. Marketing — Tráfego Pago (6003, variável por natureza)

Facebook Ads: valores irregulares, de R$ 6 a R$ 225 por lançamento de campanha. **Não é custo fixo** — depende de decisão ativa de investir em campanha. Sem padrão mensal fixo identificado ainda; Marketing/Pietro deve reportar cada campanha lançada para o Finance rastrear ROI por campanha.

## 4. Investimento Pontual — Aquisições Empreendimento (não é OPEX recorrente)

Gastos físicos ligados à validação do piloto Araújo — ringlight, luminária, prateleira, impressões de material. Tratar como investimento pontual de validação de produto/mercado, não como custo estrutural do negócio. Não entra no cálculo de "custo fixo mensal".

---

## Pendências para fechar a estrutura

- [ ] Confirmar se "VPS Hostinger" e "Hospedagem Hostinger" são cobranças duplicadas ou serviços distintos
- [ ] Confirmar valor da reserva/capital próprio disponível
- [ ] Definir se Nocode (curso recorrente) continua sendo pago indefinidamente ou tem prazo de encerramento
- [ ] Consolidar todos os meses de 2026 (a planilha mostrada cobre parte do ano) para ter média mensal real, não só faixa
- [ ] Criar conta própria no chart-of-accounts.md para "Capacitação/Cursos" — hoje não tem código dedicado

## Active Priorities

<!-- O que Lorenzo deve focar agora -->
- Fechar a média mensal real de custo fixo (pendência acima) antes de qualquer cálculo de margem no primeiro produto pago
