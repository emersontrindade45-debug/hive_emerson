---
name: vendas
description: Use ao preparar QUALQUER conversa de venda, negociação, proposta, resposta a objeção, precificação ao cliente, qualificação de lead ou definição de ICP — e sempre que o squad Commercial for acionado. Carrega os métodos Contrapeso (preço/desconto), Lavagem Cerebral Antiobjeção, Alicerce (7 etapas do processo) e AIDAS. Dispara em "vender", "venda", "proposta", "negociar", "desconto", "tá caro", "objeção", "preço para o cliente", "lead", "qualificar", "ICP", "pipeline", "prospecção", "fechamento", "reunião com cliente", "Araújo".
---

# Vendas

**Squad:** Commercial (Tatiane) · **Interface:** `modelo-de-negocios` para precificar pelo ROI

## Regra de ativação

Obrigatória antes de qualquer conversa comercial. O marco **A3 (18/09)** — reunião de precificação com o Araújo — é chamado no plano trimestral de "a data de decisão do trimestre".

## Passo 1 — Ler a fonte

**`squads/commercial/foundation/sales-playbook.md`** — 59 transcrições, ~271 mil palavras. Ler a seção que corresponde à tarefa:

| Situação | Seção |
|---|---|
| Cliente disse "tá caro" / pediu desconto | §1 — **Método Contrapeso** + **Estrutura de 4 passos** (empatia → isolar → minimizar → pedir a venda) |
| Antecipar resistência antes que apareça | §1 — **Lavagem Cerebral Antiobjeção** |
| Como dizer o número sem estragar a venda | §1 — **Depois de passar o preço** (5 erros + microdecisões) |
| **Construir o argumento de valor** | **§1B — 10 maneiras de vender valor + regra do sim + fechamento por condição** |
| Atraio curioso e não comprador | §1B — **As 4 causas** (ancoragem, falta de clareza, viver na promoção, conteúdo errado) |
| Usar gatilhos (escassez, urgência, prova social) | §4B — **os 4 gatilhos de Cialdini + aversão à perda** |
| Voz, postura, presença, linguagem não verbal | §4B — 9 elementos da oratória + **método SINCRONIA** |
| **Travado, com medo, insegurança para vender** | **§4C — autodiagnóstico de 8 perguntas + 4 antídotos** |
| **Ansiedade na reunião · recuperar depois do "não"** | **§4D — 3 componentes da emoção · 5 pilares · treinamento de cenário** |
| Não existe processo de venda | §2 — **Método Alicerce** (7 etapas) |
| Atrair, converter, fidelizar (funil inteiro) | §3 — **AIDAS completo** (A·I·D·A·S) |
| Fechar sem parecer desesperado | §4 — **7 erros do fechamento** + **10 formas de induzir** |
| Cliente disse "vou pensar" | §4 — **Cortina de fumaça × cliente analítico** |
| Mentalidade, perfil de cliente | §5 — Os dois pilares |
| Dimensionar meta, contratar vendedor | §6 — Metas de venda |
| Preparar o Araújo (18/09) | § Aplicação ao contexto do Emerson |

## Passo 2 — As 7 regras que mais mudam resultado

1. **Desconto não se dá, se troca.** Toda concessão precisa de contrapartida — fechamento hoje, à vista, contrato longo, indicação, depoimento. *"O que é conquistado, o cérebro valoriza; o que é dado, despreza."*
2. **Contra "tá caro", peso no prato do valor — nunca tirar do prato do preço.** Derrubar o preço no primeiro sinal destrói a âncora e sinaliza que o valor original era mentira.
3. **Custo invisível vence argumento.** Perguntar quanto custa **não** resolver, e ficar calado. O número que o cliente diz vale 10× mais que qualquer coisa que você fale.
4. **Objeção é sinal de interesse.** *"Só tenho objeção de algo que tenho intenção de comprar."* Ordem: acolhe → entende → responde. Nunca vire advogado de defesa.
5. **Isolar antes de conceder.** *"Se eu conseguir esse preço, a gente fecha agora — ou tem mais alguma coisa que impede?"* Sem isso você dá o desconto **e mesmo assim** ouve "vou analisar".
6. **Toda mensagem termina em pergunta — e depois, silêncio.** Preço enviado sem pergunta mata a conversa. Feita a pergunta, **calar**: preencher o silêncio denuncia insegurança.
7. **Nunca perguntar "você tem interesse?"** — nem *"ainda"* tem interesse. Conduza com duas opções ou assuma o fechamento: *"vou anotar seus dados"*.

## Passo 3 — Travas do contexto atual

Ler `squads/commercial/memory/STATE.md` e o STATE do orchestrator antes de agir:

- **Prospecção ativa por ligação está EXCLUÍDA do trimestre** (decisão de 23/08, segue valendo). A base de 238 leads e o script estão intactos, mas parados.
- **O Araújo não paga nada hoje** — é piloto gratuito e preço **nunca** foi mencionado ao cliente. Os R$ 4.000 são estimativa do Emerson, não sinalização do cliente.
- **A rede do Araújo está fechada** para o Hub falar com o ERP deles — sem isso não há o que precificar. Risco externo, sem data.
- **Plano de contingência em 18/09:** aceita R$4.000 → segue; contrapropõe R$1.500-3.000 → aceitar (receita > preço ideal); < R$1.000 → reduzir escopo ou encerrar; recusa → reabrir prospecção.

⚠️ **A contingência é rede de segurança, não é a âncora.** Pelo Contrapeso, o número que abre a conversa é **R$ 4.000** — abrir em 1.500 destrói a referência da negociação inteira.

## Passo 4 — Antes da reunião, fazer o dever de casa

O Contrapeso exige preparação escrita, não improviso:

1. **Diferenciais** — do Hub **e do Emerson** (a §1B manda listar 5 diferenciais *seus*, não do produto)
2. **Custo invisível do Araújo** — quanto custa por mês o problema continuar. Os dados existem no Supabase (atendimentos, pedidos, horas economizadas) e viram o relatório do marco A2 (11/09). Pela §1B, **não afirmar o ganho: perguntar os números e fazer a conta na frente dele**
3. **3 moedas de troca** — o que aceita conceder e o que exige em troca
4. **A faixa de preço** — ⚠️ o Araújo está em piloto gratuito, então a âncora dele é **zero**. Nunca apresentar R$4.000 sozinho: montar faixa com **R$4.000 no meio, nunca no topo** (§1B, comparação inteligente)
5. **Rodar o autodiagnóstico de 8 perguntas da §4C** — 2 minutos. Duas ou mais respostas "sim" e o problema de 18/09 é emocional, não de argumento
6. **Treinamento de cenário (§4D)** — para cada faixa da contingência (R$4.000 · R$1.500-3.000 · <R$1.000 · recusa), escrever não só a resposta técnica mas **como vai reagir emocionalmente**. E responder antes: *"qual é a pior coisa que acontece se ele não fechar?"*
7. **Juntar a pasta de feedbacks** — todo retorno positivo do Araújo durante o piloto é prova social e munição de valor (§4C)

## Fontes

- **Carol Iasmim** (`@carol.iasmim`, 175k) — 58 vídeos, catálogo completo 2025+2026. 17 anos de vendas, formada em Direito. Canal fixo no radar semanal desde 27/08.
- **Dani Martins** (Sales Prime) via JJ Podcast #219 — ⚠️ só ~15% processado.

## Lacunas — declarar quando a pergunta cair fora do playbook

- **36 das 59 transcrições ainda não destiladas.** O playbook cobre **23 vídeos** (preço/objeção, valor, processo, AIDAS completo, fechamento, gatilhos/autoridade, insegurança, inteligência emocional/mentalidade). As demais cobrem **ler o cliente, pós-venda, prospecção, canais (WhatsApp/ligação), crise, mercados concorridos, rotina**. Se a pergunta cair nesses temas: dizer que o material existe baixado mas não foi destilado, e oferecer destilar antes de responder.
- 📋 **Plano priorizado: `squads/commercial/data/sales-intel/PLANO-DESTILACAO.md`** — 5-7 sessões restantes. ✅ Lotes 1 (valor), 2 (gatilhos) e 3 (emocional) concluídos. **A base do A3 está integralmente coberta**; o próximo é o lote 4 (ler o cliente). Para retomar: *"destilar lote N da Carol"*.
- ⚠️ **`nQBJPfBA-_A` veio com transcrição vazia** — precisa recoletar.
- **JJ #219:** ~15% processado — o resto é gestão de time de vendas, pouco aplicável a quem vende sozinho.
- `squads/commercial/foundation/icp-profile.md` e `squads/commercial/foundation/qualification-criteria.md` seguem em **template genérico** do HIVE (02/06), nunca preenchidos. O Método Alicerce (§2) é o roteiro para preenchê-los.
