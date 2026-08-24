# Plano Trimestral — 23/08 a 31/10/2026

> Gerado 2026-08-23. **Revisado no mesmo dia** após decisão do Emerson: foco em Mercado Araújo + conteúdo no canal; prospecção por ligação excluída do trimestre.
> **Disponibilidade: 20h/semana** — 4h/dia (2h manhã + 2h tarde), seg a sex.
> **Correção 24/08:** datas da Semana 1 deslizadas -1 dia (o rascunho original rotulava "Seg 25/08", mas 25/08/2026 é terça — Semana 1 passa a começar hoje, segunda 24/08).

---

## A decisão que estrutura este plano

Duas frentes, nesta ordem de prioridade:

1. **Mercado Araújo** — converter o piloto gratuito em contrato pago. Potencial estimado: **R$ 4.000/mês**
2. **Conteúdo no canal** — gerar leads inbound, substituindo a prospecção ativa

**Excluído do trimestre:** ligação para os 238 leads. Decisão do Emerson em 23/08.

### O risco, registrado

| Fato | Consequência |
|---|---|
| Araújo **não paga nada hoje** (piloto gratuito) | Não é upgrade de contrato — é a primeira conversa de preço |
| Preço **nunca foi mencionado** ao cliente | A negociação é inédita; pode dar em qualquer número, inclusive zero |
| R$ 4.000 é **estimativa do Emerson**, não sinalização do cliente | Número não validado pela única pessoa que decide: o Araújo |
| Prospecção ativa excluída | Sem plano B ativo. Se o Araújo disser não, a receita segue R$ 0 |
| Conteúdo tem ciclo longo | Não substitui a ligação no prazo deste trimestre |

> Isso não é argumento contra a decisão — é o que precisa estar visível quando a conversa de preço acontecer. **A data da proposta ao Araújo é o marco mais importante do trimestre. Se ela escorregar, o trimestre escorrega junto.**

---

## Grade fixa da semana — 20h

| Bloco | Horário | Dias | h/sem | O quê |
|---|---|---|---:|---|
| **A — Araújo** | 09:00–11:00 | seg–sex | 10h | Entrega, estabilização, negociação |
| **B — Conteúdo** | 14:00–16:00 | seg–qui | 8h | Roteiro, gravação, edição, publicação |
| **Revisão** | 14:00–15:00 | sex | 1h | Indicadores + planejar semana |
| *Folga* | — | — | ~1h | Imprevisto (regra dos 70%) |

**Regra de colisão:** conteúdo nunca invade o bloco do Araújo. O bloco A é o que gera caixa neste trimestre.

---

## Meta 1 — MERCADO ARAÚJO (prioritária)

**Converter piloto gratuito em contrato pago** · prazo **31/10/2026** · Atual R$ 0 · Alvo **R$ 4.000/mês**

**Indicador semanal:** a conversa de preço avançou de etapa? (Diagnóstico → Número apresentado → Proposta → Assinatura)

### Marcos com data

| # | Marco | Prazo | Verificação objetiva |
|---|---|---|---|
| A1 | Sistema estável — zero quedas por 7 dias | **04/09** sex | EME-5 e EME-6 fechadas; log limpo |
| A2 | Relatório de valor entregue ao Araújo | **11/09** sex | PDF: nº de atendimentos, pedidos, horas economizadas |
| A3 | **Reunião de precificação realizada** | **18/09** sex | Reunião feita; número R$ 4.000 apresentado |
| A4 | Proposta formal enviada | **25/09** sex | Contrato com escopo, preço e SLA |
| A5 | **Contrato assinado** | **09/10** sex | Assinatura + data da 1ª cobrança |
| A6 | 1º pagamento recebido | **30/10** sex | Extrato bancário |

> **A2 é o que sustenta o A3.** Não dá para pedir R$ 4.000 sem mostrar, em número, o que o sistema já entregou de graça. Esse relatório é o argumento inteiro da negociação — e os dados já existem no Supabase.

### Semana 1 — 24/08 a 28/08 (detalhada)

| Quando | Tarefa | Feito quando |
|---|---|---|
| **Seg 24/08, 09:00–11:00** | Rotacionar credencial do Postgres + fechar porta 5432 (EME-6) | Senha nova, porta fechada |
| **Ter 25/08, 09:00–11:00** | Corrigir vazamento de conexões em `apps-auth` (EME-5) | Pool estável sob carga |
| **Qua 26/08, 09:00–11:00** | Monitorar n8n + fila de conciliação ERP | Zero quedas registradas |
| **Qui 27/08, 09:00–11:00** | **Extrair métricas do Supabase** — atendimentos, pedidos, tempo de resposta desde o início | Query pronta, números na mão |
| **Sex 28/08, 09:00–11:00** | Montar rascunho do relatório de valor (A2) | Estrutura + números preenchidos |
| **Sex 28/08, 14:00–15:00** | Revisão semanal | Indicadores escritos |

Tardes seg–qui: Bloco B (abaixo).

### Semanas 2 a 10

| Sem | Período | Bloco A — Araújo | Marco |
|---|---|---|---|
| 2 | 31/08–04/09 | Estabilização final + fechar relatório | **A1** |
| 3 | 07–11/09 | Entregar relatório e agendar reunião | **A2** |
| 4 | 14–18/09 | **Reunião de precificação** | **A3** |
| 5 | 21–25/09 | Ajustar escopo conforme reação + enviar proposta | **A4** |
| 6 | 28/09–02/10 | Follow-up da proposta | Resposta obtida |
| 7 | 05–09/10 | Negociação e fechamento | **A5** |
| 8 | 12–16/10 | Formalizar cobrança recorrente | Boleto/PIX programado |
| 9 | 19–23/10 | Entregar o que foi vendido | Escopo cumprido |
| 10 | 26–30/10 | Cobrança + avaliar 2º cliente | **A6** R$ 4.000 |

### Plano de contingência — decidir em 18/09

Se na reunião A3 o Araújo recusar ou oferecer muito abaixo:

| Reação do cliente | Resposta |
|---|---|
| Aceita R$ 4.000 | Segue o plano |
| Contrapropõe R$ 1.500–3.000 | Aceitar. Receita > preço ideal. Ajustar escopo ao valor |
| Oferece < R$ 1.000 | Reduzir escopo drasticamente ou encerrar o gratuito |
| Recusa pagar | **Reabrir prospecção imediatamente** — a base de 238 leads e o script continuam existindo |

> **18/09 é a data de decisão do trimestre.** Até lá não há plano B ativo — foi decisão consciente, tomada em 23/08.

---

## Meta 2 — CONTEÚDO NO CANAL

**Gerar leads inbound por conteúdo** · prazo **31/10/2026** · Atual 0

**Indicador semanal:** nº de vídeos publicados. Secundário: leads que chegaram citando o canal.

Base já existente: `squads/marketing/foundation/youtube-playbook.md` e `metodo-influencia-digital.md`.

### Marcos com data

| # | Marco | Prazo | Verificação |
|---|---|---|---|
| C1 | Linha editorial definida — 10 temas | **28/08** sex | Lista escrita |
| C2 | Primeiro vídeo publicado | **11/09** sex | URL no ar |
| C3 | 4 vídeos publicados | **09/10** sex | 4 URLs |
| C4 | 8 vídeos + 1 lead inbound | **30/10** sex | 8 URLs + 1 contato |

**Ritmo:** 1 vídeo por semana a partir de 11/09. 8h/semana é folgado para isso — se sobrar tempo, volta para o Araújo.

### Semana 1 — Bloco B (tardes seg–qui)

| Quando | Tarefa |
|---|---|
| Seg 24/08, 14:00–16:00 | Definir ICP do canal: para quem eu falo? (comerciante local) |
| Ter 25/08, 14:00–16:00 | Listar 10 temas que esse comerciante pesquisaria no YouTube |
| Qua 26/08, 14:00–16:00 | Escolher formato e escrever roteiro do vídeo 1 |
| Qui 27/08, 14:00–16:00 | Testar setup de gravação (câmera, áudio, luz) |

> **O caso Araújo é o melhor conteúdo que existe.** "Automatizei o atendimento de um mercado" é tema com prova real. Usar — com autorização do cliente.

---

## Meta 3 — SAÚDE (Emerson) · REPACTUADA

**81kg → 73kg** · **30/04 (vencido) → 31/10/2026**

| Marco | Prazo |
|---|---|
| 79 kg | 18/09 |
| 76 kg | 16/10 |
| 73 kg | 30/10 |

Caminhada 30min · **seg/qua/sex 06:30**. Pesar **segunda 06:00**. Fora das 20h do negócio.

## Meta 4 — FAMÍLIA · REPACTUADA

**1 programa/semana** · sábado · **12/06 (vencido) → 31/10/2026** · Alvo 10 programas.
Definido na revisão de sexta. Por isso o plano usa só 5 dias.

---

## Metas pausadas até 01/11

| Meta | Motivo |
|---|---|
| 5. Automatizar as despesas | Economiza 1h/semana; custa mais do que devolve agora |
| 6. Processo de Compras (CMS) | Meta de emprego, não de negócio |
| **Prospecção ativa (238 leads)** | **Excluída do trimestre por decisão de 23/08.** Base e script preservados — reativar se A3 falhar em 18/09 |

---

## Ritual de sexta — 14:00, 1 hora

1. A conversa com o Araújo avançou de etapa? (Diagnóstico → Número → Proposta → Assinatura)
2. Publiquei o vídeo da semana?
3. Bati o marco? (sim/não, sem "quase")
4. Se não: o que travou?
5. Blocos da semana seguinte + programa de sábado

**Regra ao falhar** (Neotriad): falhou um dia → retoma no seguinte. Falhou a semana → revisa o **marco**, nunca a meta.

---

## O que este plano NÃO faz

- ❌ Não liga para os 238 leads (decisão de 23/08)
- ❌ Não cria database novo no Notion
- ❌ Não consolida os 5 databases de tarefas — depois de 31/10
- ✅ Exceção (5 min): fechar os 2 ciclos vencidos como "Cancelado"

**Critério de sucesso: em 31/10, o Araújo paga. Se pagar menos que R$ 4.000, ainda é sucesso — R$ 0 é o número a derrotar.**
