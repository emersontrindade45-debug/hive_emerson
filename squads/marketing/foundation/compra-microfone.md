# Compra do microfone — levantamento e decisão

> **Divisão:** `[M3]` Operações e Análise de Marketing · **Squad:** Marketing (Pietro)
> **Criado:** 2026-08-29 · **Contexto:** único item que falta do kit de gravação (`setup-gravacao.md` § Kit de compra). Ring light e tripé já existem.
> **Orçamento:** R$120–250, gasto de bolso do Emerson — **fora do caixa MEI** (folga ~R$5,79/mês, ver `../../finance/memory/STATE.md`).
> **Entrada do celular confirmada (29/08): USB-C.** Isso descarta qualquer modelo Lightning.

⚠️ **Preços verificados em 29/08/2026 via pesquisa de mercado. Preço de eletrônico no Brasil oscila muito** — conferir na hora da compra. O que não muda é a leitura de faixa abaixo.

---

## As 3 faixas reais do mercado

O mercado se divide em três degraus, e o degrau do meio é onde está o orçamento.

| Faixa | Preço | O que é | Serve para o canal? |
|---|---|---|---|
| **Genérico sem marca** | ~R$40 | Kit duplo USB-C plug&play, 10h de bateria | ⚠️ Serve, com ressalva séria — ver abaixo |
| **Marca de entrada** | R$150–200 | Boya, Ulanzi — marca estabelecida, redução de ruído real | ✅ **É a faixa do orçamento** |
| **Semi-profissional** | R$350–950 | Hollyland Lark A1/M2, Maono, Comica | ❌ Fora do orçamento, e desnecessário agora |

---

## Recomendação: **Boya BY-V10** (~R$181)

**Por que este:**

1. **USB-C nativo** — bate com a entrada do celular, sem adaptador. Adaptador é ponto de falha e ruído.
2. **Boya é marca estabelecida em áudio**, não fabricante genérico de marketplace. Importa para peça que vai ser usada em todos os vídeos do trimestre, não uma vez.
3. **Redução de ruído com filtro anti-atrito** — o atrito da roupa no transmissor é o defeito mais comum de lapela, e é exatamente o que estraga take em vídeo sentado/falando parado.
4. **Cabe no orçamento com folga** (R$181 de R$250), sem forçar o teto.

**Alternativa se o BY-V10 estiver esgotado ou acima de R$220:** qualquer **Boya da linha V (BY-V2, BY-V20) ou Mini** em USB-C, na mesma faixa. A linha inteira entrega o mesmo padrão; o que muda é número de transmissores e autonomia.

⚠️ **Ulanzi J12 (~R$159) aparece muito em lista de recomendação — verificar a versão antes de comprar.** Existem duas: a **Lightning (iOS)** e a **USB-C**. A mais divulgada e barata costuma ser a Lightning, que **não serve** aqui. Comprar J12 só confirmando "USB-C" na descrição do anúncio.

---

## Sobre o genérico de ~R$40

Não é golpe e funciona — mas tem limitação documentada que importa para este caso específico:

- **Captação de agudos abafada** e **compressão audível em ambiente silencioso**
- Quarto fechado, à noite, com janela coberta por cobertor (que é exatamente o setup definido em `setup-gravacao.md` §1.5) **é ambiente silencioso** — é onde esse defeito mais aparece

**Veredito:** o genérico é a escolha certa para quem tem R$40 e nada mais. Não é a escolha certa aqui, porque o orçamento existe e o item é de uso recorrente. **Mas se o dinheiro estiver curto no dia, comprar o genérico e gravar é infinitamente melhor que adiar a compra e não gravar** — a diferença entre genérico e Boya é menor que a diferença entre gravar e não gravar.

---

## O que NÃO comprar agora

| Item | Por quê |
|---|---|
| **Hollyland Lark M2** (R$659–910) | Melhor microfone da categoria, e irrelevante — 3× o orçamento para ganho que não aparece em vídeo falado em quarto |
| **Hollyland Lark A1** (R$354–373) | Mais próximo, ainda acima do teto. Reavaliar só se o canal virar receita |
| **LED adicional** | Ring light já resolve (`setup-gravacao.md` §2). Testar antes de comprar mais luz |
| **Espuma acústica** | Só depois de testar as 4 medidas grátis contra vazamento (§1.5) |

---

## Checagem antes de finalizar a compra (30 segundos)

- [ ] Descrição do anúncio diz **USB-C** (não Lightning, não P2, não micro-USB)
- [ ] Vendedor com reputação — ⚠️ marketplace tem genérico anunciado com foto de marca
- [ ] Vem com **estojo de carregamento** se possível (recarrega o transmissor entre takes)
- [ ] Sobra do orçamento **não vira compra extra** — guardar (`setup-gravacao.md` § Kit)

---

## Depois que chegar

Rodar `teste-gravacao-30s.md` completo — checagens 1–3 (áudio) são as que só podem ser validadas com o microfone em mãos.

⚠️ **Não esperar a entrega para fazer o teste.** As checagens 4–7 (foco, exposição, fundo, enquadramento) rodam hoje com o áudio do próprio celular.

---

## Fontes consultadas (29/08/2026)

- [TechTudo — 6 microfones de lapela sem fio que valem a pena (fev/2026)](https://www.techtudo.com.br/listas/2026/02/microfone-de-lapela-sem-fio-modelos-que-valem-super-a-pena-edqualcomprarie.ghtml) — preços do BY-V10 e J12
- [TechKnow — comparativo Hollyland Lark M1/M2/M2s/C1](https://www.techknow.com.br/post/melhor-microfone-lapela-sem-fio) — faixa semi-profissional
- [Mundo do Microfone — análise do lapela USB-C duplo genérico](https://mundodomicrofone.com.br/microfone-lapela-usb-c-duplo-generico/) — limitações do genérico
- [Techinter — 10 melhores lapela sem fio 2026](https://techinter.com.br/audio-e-video/microfones/microfone-de-lapela-sem-fio/) — Ulanzi J12, Boya Mini, Kaidi

---

# REVISÃO 29/08 — critério novo: **discrição**

⚠️ **O Emerson corrigiu o pedido depois da primeira versão:** quer algo **parecido com o Hollyland Lark M2** — transmissor minúsculo, fixação magnética, que não apareça como "microfone de verdade" preso na roupa. **E grava se movimentando pelo quarto**, não parado.

Isso muda o critério de escolha. A primeira versão otimizou preço/marca; esta otimiza **tamanho + fixação magnética**, mantendo o teto de R$250.

## O que faz o Lark M2 parecer discreto

Três coisas, e nenhuma é o preço:

| Atributo | Lark M2 | Por que importa aqui |
|---|---|---|
| **Peso/tamanho** | 9g, sem clipe saliente | Some contra a camiseta em plano médio |
| **Fixação magnética** | Imã prende por trás do tecido | Sem presilha visível na gola — é o que denuncia "microfone" |
| **Sem cabo** | Transmissor é o microfone | Cabo pendurado é mais visível que o microfone |

**A fixação magnética é o item que mais entrega o efeito** — clipe de presilha aparece mesmo em microfone pequeno.

## Preços verificados 29/08 — a faixa mudou

⚠️ **Correção da primeira versão:** o BY-V10 apareceu a **R$223** (Amazon), não R$181. Preço de eletrônico oscila — o levantamento anterior pegou uma cotação mais barata. Isso aperta o teto de R$250.

| Modelo | Preço | Fixação | Peso | Veredito |
|---|---|---|---|---|
| **Kaidi KMF6-C** | **~R$39–56** | ✅ **Clipes magnéticos** | Compacto, duplo | ✅ **Único magnético dentro do orçamento** |
| Boya BY-V10 | ~R$181–223 | ❌ Clipe | Pequeno | Bom áudio, mas **não resolve o pedido** |
| Boya Mini / Mini-14 | R$387–456 | Clipe | **5g** (menor que o Lark) | Fora do teto |
| Boya BY-V20 | R$330–338 | Clipe | Pequeno | Fora do teto |
| Hollyland Lark M1 | — | — | — | **Esgotado** (KaBuM, 29/08) |
| Hollyland Lark A1 | ~R$354–390 | Magnética | Leve | Fora do teto, o mais próximo do M2 |
| **Hollyland Lark M2** | **R$659–910** | ✅ Magnética | 9g | ❌ 3× o orçamento |

## O conflito honesto

**Não existe, hoje, no Brasil, um clone barato e bom do Lark M2.** O mercado se parte em dois:

- **R$39–56:** tem o imã e o tamanho, mas o áudio é o ponto fraco — reviews do Kaidi KMF6-C relatam captação **"metalizada"** e bateria de só 4-5h
- **R$350+:** tem o imã e o áudio bom (Lark A1), mas estoura o teto

O que existe entre R$150-250 (linha Boya V) tem **áudio melhor e clipe visível** — resolve o áudio, não a discrição.

## Recomendação revisada

**Duas saídas legítimas. A escolha é sua, e depende de qual incômodo pesa mais.**

### Opção A — Kaidi KMF6-C (~R$39–56) · *se discrição é inegociável*
✅ Magnético, compacto, duplo, USB-C, dentro do orçamento com muita sobra
⚠️ Áudio "metalizado" relatado · bateria 4-5h (suficiente para uma sessão de gravação, não para o dia todo)
→ **Sobra R$200 do orçamento.** Se o áudio decepcionar no `teste-gravacao-30s.md`, você ainda tem verba para trocar — e aí já sabe exatamente o que não serve.

### Opção B — Guardar e comprar o Hollyland Lark A1 (~R$354–390) · *se quer resolver de uma vez*
✅ Magnético, leve, áudio de marca, 54h de bateria — é o Lark de entrada, mesma família do M2
❌ **Estoura o teto em ~R$100–140** e adia a gravação até juntar a diferença
→ ⚠️ **Adiar a compra adia o vídeo 1, e faltam 13 dias para o marco C2.** Só vale se você tiver a diferença hoje.

**Recomendo a A.** Não porque o Kaidi seja bom — é o mínimo aceitável. Mas porque ele: (1) atende o critério que você pediu, (2) custa 1/7 do orçamento, (3) permite gravar esta semana, e (4) deixa verba intacta para corrigir se falhar. O áudio "metalizado" de um lapela magnético perto da boca ainda é melhor que o microfone do celular a 1 metro de distância.

⚠️ **Se escolher a A, a checagem 1 do `teste-gravacao-30s.md` (áudio limpo) deixa de ser formalidade e vira o teste decisivo** — é ela que diz se os R$39 bastaram.

## Detalhe que importa porque você se movimenta

Você grava **andando pelo quarto**. Isso reforça duas coisas:

1. **Sem fio é obrigatório** (já era a premissa) — cabo P2 estaria descartado de qualquer forma
2. **Alcance não é problema** — o Kaidi faz 15-25m; um quarto tem menos de 5m. Alcance é o spec que menos importa no seu caso, ignore-o na comparação
3. ⚠️ **Atrito de roupa vira o risco nº1** — movimento faz o tecido roçar no transmissor. Fixar o imã **por baixo da gola da camiseta**, não no meio do peito onde o tecido dobra ao andar

## Fontes desta revisão (29/08/2026)

- [TechTudo — melhor microfone de lapela, do barato ao profissional (fev/2026)](https://www.techtudo.com.br/listas/2026/02/melhor-microfone-de-lapela-modelos-do-barato-ao-profissional-edqualcomprarie.ghtml) — Kaidi KMF6-C, fixação magnética
- [Zoom — comparativo de preços Boya USB-C](https://www.zoom.com.br/busca/microfone+boya+mini+usb-c) — BY-V10 a R$223, Mini-14 a R$387+
- [Hollyland — LARK M2 oficial](https://www.hollyland.com/product/lark-m2) — 9g, clipes magnéticos, especificação de referência
- [KaBuM — Hollyland Lark M1](https://www.kabum.com.br/produto/512122/sistema-de-microfone-lapela-sem-fio-hollyland-lark-m1-preto) — esgotado em 29/08

---

# REVISÃO 2 — 29/08 · **com ímã E com par de transmissores**

Pergunta do Emerson: *"tem algum outro com ímã? e com um par?"* — a revisão anterior tratou o Kaidi KMF6-C como se fosse a única saída magnética. **Não é.** Existem pelo menos 3 opções com ímã + 2 transmissores, e uma delas resolve o problema de áudio que fazia o KMF6-C ser uma recomendação com ressalva.

⚠️ **Boa notícia:** quase todo lapela sem fio de mercado vem **em par** (2 TX + 1 RX) por padrão — o par não é o item raro. O item raro é **par + ímã + áudio decente + dentro do teto**.

## As 4 opções com ímã e par, ordenadas por preço

| Modelo | Preço | TX | Ímã | Bateria | Estojo | Nota |
|---|---|---|---|---|---|---|
| **Kaidi KMF6-C** | ~R$39–56 | 2 | ✅ | 4–5h | ❌ | Áudio "metalizado" relatado |
| **Kaidi KMF4-C** | **R$85–90** | 2 | ✅ | 3–4h | ❌ | Mesma família, mais caro, bateria pior |
| **Kaidi KMF4-A** | **R$114** | 2 | ✅ **2 ímãs + 2 clipes** | 4–5h | ❌ | ⚠️ **Não serve p/ iPhone 15/16** (irrelevante aqui, é Android) |
| **Boya Omic-U** | **R$253** (ML, promo) a R$364 (oficial) | 2 | ✅ ímã **ou** clipe | **12h** | ✅ **case com zíper** | ✅ **Marca de áudio + review de usuário elogiando o ímã** |

## A opção que mudou a recomendação: **Boya Omic-U**

É o que faltava na revisão anterior — tem **as duas coisas ao mesmo tempo**:

- ✅ **Ímã** (usuário relata explicitamente *"possibilidade de usar com ímã ou clipe"*)
- ✅ **Par de transmissores** (2 microfones)
- ✅ **Marca de áudio de verdade** (Boya), não fabricante genérico
- ✅ **12h de bateria** — 3× o Kaidi
- ✅ **Case com zíper** incluso
- ✅ Cancelamento de ruído profissional, 2.4GHz, proteção contra vento

⚠️ **O preço é o problema, e depende de onde comprar:**

| Onde | Preço | Situação |
|---|---|---|
| Mercado Livre (promoção registrada) | **R$253** | ✅ Praticamente no teto — **é a compra certa se estiver nesse preço** |
| Loja oficial Boya do Brasil | R$346–364 | ❌ Estoura o teto em ~R$100 |

⚠️ **Vários anúncios do Omic-U aparecem como indisponíveis no ML (29/08).** Verificar estoque antes de contar com ele.

## Recomendação revisada (substitui a da revisão 1)

**Ordem de preferência, de cima para baixo — comprar o primeiro que estiver disponível no preço:**

1. 🥇 **Boya Omic-U a ≤R$260** — resolve tudo de uma vez: ímã, par, áudio de marca, 12h, case. É a compra que não vai precisar ser refeita.
2. 🥈 **Kaidi KMF4-A (~R$114)** — se o Omic-U estiver esgotado ou acima de R$280. Vem com **2 ímãs E 2 clipes** (escolhe na hora qual usar), bateria 4-5h. Custa metade do teto e ainda deixa R$130 de folga.
3. 🥉 **Kaidi KMF6-C (~R$39–56)** — só se o orçamento apertar de verdade no dia. Funciona, com a ressalva de áudio já registrada.

⚠️ **O que NÃO fazer:** pagar R$346 no Omic-U na loja oficial. É o mesmo produto por R$100 a mais — e nessa faixa o Hollyland Lark A1 (R$354) vira concorrente direto.

## Por que o KMF4-A subiu na lista

Ele traz **ímã e clipe juntos na caixa** (1 receptor, 2 microfones, 2 clips, 2 ímãs, 1 cabo). Como você grava **se movimentando**, poder testar as duas fixações no mesmo teste de 30s é vantagem real — se o ímã escorregar com movimento, o clipe está ali sem precisar comprar de novo.

⚠️ **Limitação declarada do KMF4-A:** incompatível com iPhone 15/16. **Não afeta você** — é Android USB-C.

## Fontes desta revisão (29/08/2026)

- [KaBuM — Kaidi KMF4-A, R$113,91](https://www.kabum.com.br/produto/872556/microfone-lapela-duplo-tipo-c-redondo-ima-sem-fio-anti-ruido-preto) — conteúdo da caixa: 2 ímãs + 2 clipes
- [Ion Cabos — Kaidi KMF4-C, R$89,90](https://www.ioncabos.com.br/microfone-duplo-de-lapela-usb-c-wireless-kmf4c) — clipes magnéticos integrados
- [Boya do Brasil — Omic-U oficial, R$346–364](https://boyadobrasil.com.br/produto/sistema-microfone-sem-fio-boya-omic-u-usb-c-lapela-preto/)
- [Pelando — Omic-U por R$253](https://www.pelando.com.br/d/microfone-sem-fio-boya-omic-u-usb-c-lapela-branco-9bb4) — preço promocional registrado
- [Mercado Livre — Boya Omic-U](https://lista.mercadolivre.com.br/microfone-lapela-boya-omic-u) — verificar estoque

---

# ⚠️ RISCO DE COMPATIBILIDADE ANDROID — verificar ANTES de comprar (29/08)

Pergunta do Emerson: *"o meu é Android, será que a opção 1 resolve?"* — pergunta certa, e revelou um risco que **nenhuma das revisões anteriores tinha mapeado**.

## O problema real (vale para QUALQUER lapela USB-C, não só o Omic-U)

Microfone USB-C em Android **não é plug-and-play universal**, apesar de todo anúncio dizer que é. O gargalo **não é o microfone — é o app de câmera nativo do celular**:

| Marca | Comportamento |
|---|---|
| **Samsung** | ✅ Reconhecimento **nativo e automático** (ex.: Galaxy A55 exibe confirmação na tela) |
| **Motorola** | ⚠️ **Problemático** — modelos recentes não reconhecem microfone USB no app de câmera padrão |
| **Xiaomi / marcas chinesas** | ⚠️ Mesmos relatos de falha |

⚠️ **É limitação de software, não defeito de hardware.** O app de câmera padrão dessas marcas simplesmente não tem o código que prioriza fonte de áudio externa. O microfone funciona — o app é que ignora ele.

## ✅ A solução já está no nosso setup

**O `Open Camera` — que `setup-gravacao.md` §1 já manda instalar por outro motivo (travar foco e exposição) — resolve isso em 99% dos casos.**

**Caminho:** Open Camera → Configurações → Configurações de vídeo → **Fonte de áudio** → selecionar **"Microfone externo (se disponível)"**.

Isso contorna a limitação do app nativo independentemente da marca do celular. **O Open Camera passa de "recomendado" a obrigatório** — ele agora resolve dois problemas, não um.

## Resposta direta: a opção 1 resolve?

✅ **Sim, com uma condição operacional.** O Boya Omic-U é explicitamente compatível com Android USB-C (Samsung, LG, Pixel, tablets Android). O risco não é do Omic-U — é da combinação "qualquer lapela USB-C + app de câmera nativo de marca não-Samsung".

**Duas ações que eliminam o risco:**

1. **Ativar OTG** — Configurações → Sobre o telefone → buscar "OTG". Maioria dos Android recentes já vem ativo.
2. **Gravar pelo Open Camera com fonte de áudio externa selecionada** — nunca pelo app nativo.

⚠️ **Isso vira checagem obrigatória do `teste-gravacao-30s.md`:** a primeira coisa a conferir ao plugar o microfone é se o áudio está vindo **dele** e não do microfone interno do celular. É um erro silencioso — o vídeo grava normalmente, só que com o áudio errado, e só se descobre ao ouvir.

## Teste de 30 segundos para detectar o erro silencioso

Com o microfone plugado e o Open Camera configurado:

1. Gravar 10s falando normal
2. **Tapar o microfone de lapela com a mão** e continuar falando
3. Ouvir: se o áudio **abafar** → ✅ está usando o lapela. Se continuar igual → ❌ está usando o microfone do celular, refazer a configuração

## Fontes (29/08/2026)

- [TecnoUp — microfone USB-C não funciona no celular](https://www.tecnoup.net.br/como-usar-microfone-usb-tipo-c-em-qualquer-celular-android/) — Open Camera resolve 99% dos casos; Motorola e chinesas problemáticas, Samsung nativa
- [Comunidade Samsung — microfone externo não reconhecido](https://r1.community.samsung.com/t5/galaxy-a/microfone-externo-n%C3%A3o-reconhecido-pela-c%C3%A2mera/td-p/24163415) — relatos reais, inclusive quebra após atualização
- [Amazon — Boya Omic-U](https://www.amazon.com/BOYA-Microphone-Smartphone-Recording-Streaming/dp/B0CM3GN2DG) — compatibilidade Android declarada

---

# 🔴 REVISÃO 3 — 29/08 · **celular identificado: Motorola Moto E7** — a recomendação muda

O Emerson informou o aparelho: **Motorola Moto E7**. Isso resolve a dúvida "a opção 1 resolve?" e **inverte parte da recomendação anterior**. Ficha confirmada em duas fontes:

| Spec do Moto E7 | Valor | Consequência |
|---|---|---|
| Entrada USB | ✅ **USB-C** | Lapela USB-C é fisicamente compatível |
| **Entrada P2 3,5mm** | ✅ **TEM** | 🔑 **Abre a saída mais segura — ver abaixo** |
| OTG | ✅ Suportado | Necessário para lapela USB-C |
| Android de fábrica | **Android 10** | ⚠️ Antigo, mas **melhor** que 14/15 para este caso |
| Gravação de vídeo | **1080p Full HD** | ✅ Suficiente — bate com o alvo de `setup-gravacao.md` §1 |
| Processador / RAM | Helio G25 / 2–4GB | ⚠️ Entrada. Não gravar 4K (já era a regra) |

## ⚠️ O risco concreto: Motorola é a marca-problema

A pesquisa de compatibilidade (seção anterior) já apontava Motorola como problemática. Com o aparelho identificado, o risco deixa de ser hipotético:

- **Reclame Aqui tem reclamações formais contra a Motorola** especificamente sobre *"não grava microfone externo"* e *"Motorola não aceita microfone externo"*
- O app de câmera nativo da Motorola **não prioriza fonte de áudio externa** — limitação de software, não de hardware
- ✅ **Um ponto a favor:** os relatos mais graves são de **Android 14/15**. O Moto E7 roda **Android 10**, anterior a essa quebra

## 🔑 A saída que o Moto E7 tem e os celulares novos não: **entrada P2**

Celular topo de linha moderno eliminou a entrada de fone. **O Moto E7 tem.** Isso torna disponível uma opção que eu havia descartado na primeira revisão por assumir USB-C como único caminho:

**Microfone de lapela COM FIO, P2 (~R$40–90)** — plugado direto na entrada de fone:

| | Lapela P2 com fio | Lapela USB-C sem fio |
|---|---|---|
| Funciona no Moto E7 | ✅ **Sem depender de OTG nem de app** | ⚠️ Depende de OTG + Open Camera |
| Risco de não reconhecer | ✅ **Praticamente zero** | ⚠️ Real (Motorola é a marca-problema) |
| Discrição | ✅ Cápsula minúscula | ✅ Transmissor pequeno |
| ❌ **Cabo** | ❌ **Tem cabo** | ✅ Sem cabo |
| Preço | R$40–90 | R$114–253 |

⚠️ **Mas o Emerson grava se movimentando pelo quarto** — e é exatamente aí que o cabo P2 perde. Cabo de 1,5m prende o celular ao corpo.

## Recomendação final para o Moto E7

**A opção 1 (Boya Omic-U) resolve? ✅ Sim — mas com risco não-zero e teto de preço apertado.** Considerando o aparelho real, a ordem muda:

### 🥇 **Kaidi KMF4-A (~R$114)** — passa a ser a primeira escolha

Motivos que valem especificamente para o Moto E7:

1. **Risco financeiro proporcional.** Se o Moto E7 não reconhecer o microfone USB-C mesmo com Open Camera, você perdeu **R$114**, não R$253. O risco de compatibilidade é real o bastante para não apostar o teto do orçamento nele.
2. **Vem com 2 ímãs E 2 clipes** — resolve a discrição pedida e permite testar as duas fixações gravando em movimento.
3. **Sobram ~R$135 do orçamento** — se falhar, ainda dá para comprar o lapela P2 com fio como plano B, sem gastar nada além do previsto.
4. Bateria 4–5h é suficiente para sessão de gravação (não é uso de dia inteiro).

### 🥈 **Boya Omic-U a ≤R$260** — se você aceitar o risco por 12h de bateria e áudio de marca
Melhor produto, sem dúvida. Mas ⚠️ **é o teto inteiro do orçamento apostado num aparelho cuja marca tem reclamação formal sobre microfone externo.**

### 🥉 **Lapela P2 com fio (~R$40–90)** — o plano B garantido
⚠️ **É a única opção com risco de compatibilidade praticamente zero**, porque não passa por OTG nem por app. O cabo atrapalha quem se movimenta — mas **um vídeo gravado com cabo é infinitamente melhor que um microfone sem fio que o celular não reconhece.**

## ✅ Teste obrigatório no dia da entrega (5 minutos)

**Antes de gravar qualquer coisa**, e enquanto o prazo de devolução ainda está aberto:

1. Plugar o microfone no Moto E7
2. Abrir **Open Camera** → Configurações → Configurações de vídeo → **Fonte de áudio** → **"Microfone externo (se disponível)"**
3. Gravar 10s falando normal
4. **Tapar o microfone de lapela com a mão** e continuar falando
5. **Ouvir:** áudio abafou → ✅ funcionou. Áudio continuou igual → ❌ **o celular está usando o microfone interno — acionar devolução imediatamente**

⚠️ **O erro é silencioso** — o vídeo grava normalmente, só que com o áudio errado. Sem esse teste, você só descobre depois de gravar o vídeo 1 inteiro.

## Fontes desta revisão (29/08/2026)

- [EpicGeek — ficha técnica Moto E7](https://epicgeek.com.br/ficha/motorola-moto-e7/) — USB-C, entrada de fone, Android 10
- [TechTudo — Moto E7](https://www.techtudo.com.br/tudo-sobre/moto-e7/) — gravação 1080p, Helio G25
- [Reclame Aqui — "não grava microfone externo" (Motorola)](https://www.reclameaqui.com.br/motorola/nao-grava-microfone-externo_-1Ducs3ZiUFgvU8k/) — reclamações formais
- [The Khris — microfone externo em Moto G](https://www.thekhris.com/2020/03/22/como-fazer-microfone-externo-funcionar-no-moto-g/) — app alternativo resolve

---

# ANÁLISE — "Microfone Lapela Profissional J6 Imã Sem Fio Lightning/Tipo C" (29/08)

Anúncio trazido pelo Emerson. **Veredito curto: serve, com 3 ressalvas — e é preciso escolher a variante certa.**

## ⚠️ Achado nº1: a marca do anúncio não é confiável

O **mesmo produto J6** é vendido sob nomes diferentes conforme o vendedor:

| Como é anunciado | Onde |
|---|---|
| "**Xiaomi** J6" | Shopee, TikTok Shop, blogs de review |
| "**ZCCO** J6" | Mercado Livre, Shopee, Amazon |
| "J6" sem marca / "**Profissional**" | Mercado Livre (o anúncio do Emerson) |

⚠️ **"Xiaomi J6" é quase certamente rotulagem falsa de marketplace** — a Xiaomi não lista esse produto na linha oficial dela. **ZCCO é o fabricante real** (marca chinesa de acessórios, existe de verdade, mas não é marca de áudio no nível de Boya/Hollyland).

⚠️ **A palavra "Profissional" no título é marketing, não especificação.** Vale para este anúncio e para metade do marketplace.

**Consequência prática:** não pagar preço de marca por ele. É produto genérico bom, não produto de marca.

## ⚠️ Achado nº2: a faixa de preço é absurdamente ampla — R$34,90 a R$359

O mesmo J6 aparece de **R$34,90 a R$359,13**, dependendo do vendedor. Isso é 10× de variação no mesmo produto.

⚠️ **Pagar acima de ~R$120 num J6 é jogar dinheiro fora** — nessa faixa o Kaidi KMF4-A (R$114) e o Boya Omic-U (R$253, marca de áudio real) são escolhas melhores. **O J6 só faz sentido na faixa barata dele.**

## ⚠️ Achado nº3: conflito nas fontes sobre transmissor duplo

- Anúncios do ZCCO J6 dizem **"duplo"** (2 transmissores) ✅
- Um review descreve que *"o receptor trabalha com apenas um transmissor por vez"* ❌

**Provável explicação:** existem **variantes diferentes** (J6 e J6-F, versões solo e duo). ⚠️ **Conferir no anúncio específico se vem 2 transmissores E se funcionam simultaneamente** — para o caso do Emerson (grava sozinho) **isso não importa**, mas o "par" foi um critério declarado.

## O que ele acerta — e é bastante

| Critério do Emerson | J6 |
|---|---|
| **Ímã** | ✅ Sim — magnético, formato "moeda redonda" |
| **Discreto** | ✅ Sim — é o formato redondinho pequeno, similar ao conceito do Lark M2 |
| **Par** | ⚠️ Depende da variante — confirmar no anúncio |
| **USB-C (Moto E7)** | ✅ Sim — **mas ver a armadilha abaixo** |
| **Preço** | ✅ Na faixa barata, cabe folgado |
| **Bateria** | ✅ 8h declaradas (melhor que os 4-5h do Kaidi) |
| **Alcance** | ✅ Até 50m declarado (irrelevante — o quarto tem 5m) |

## 🔴 A armadilha do título: "Lightning **/** Tipo C"

O título anuncia **as duas conexões**. Isso significa uma de duas coisas, e **muda tudo**:

1. **Vem os dois receptores na caixa** (alguns kits J6 vêm) → ✅ ótimo
2. **É uma variante que você escolhe na compra** → 🔴 **selecionar TIPO C**. Comprar a Lightning por engano = inútil no Moto E7

⚠️ **Antes de finalizar: confirmar na página do anúncio qual variante está sendo comprada.** É o mesmo erro que eu já sinalizei no Ulanzi J12.

## Defeitos relatados nos reviews

- **Suscetível a interferência eletromagnética** — relevante: você grava perto de computador/roteador; se der chiado, afastar o receptor
- **Construção plástica frágil** — não é para uso pesado
- **Sem processamento de áudio avançado** (filtro/equalização)
- Qualidade descrita como **"boa para o segmento de preço"** — não como boa em absoluto

## Veredito para o caso do Emerson

✅ **É uma compra defensável, e melhor que o Kaidi KMF6-C** — mesma categoria de genérico, mas com bateria maior (8h vs 4-5h) e reviews mais numerosos e positivos.

⚠️ **Mas não muda o problema central do Moto E7:** o J6 é USB-C e depende de OTG + Open Camera exatamente como os outros. **O teste da mão tapando o microfone continua obrigatório no dia da entrega.**

**Onde ele entra na ordem de compra:**

1. 🥇 **Kaidi KMF4-A (~R$114)** — mantém a 1ª posição: vem com **ímã E clipe** na caixa (o J6 é só ímã), e a marca é rastreável
2. 🥈 **J6 / ZCCO J6 — se estiver abaixo de ~R$80** — bateria melhor, formato mais discreto. **Boa compra pelo preço, desde que seja a variante Tipo C**
3. 🥉 Boya Omic-U ≤R$260 — se aceitar apostar o teto do orçamento
4. Lapela P2 com fio — plano B de risco zero

⚠️ **Se o J6 estiver a R$34-60, ele vira a escolha mais racional** — custa 1/3 do Kaidi KMF4-A, entrega o mesmo tipo de resultado, e deixa praticamente todo o orçamento livre para corrigir o rumo se o Moto E7 não cooperar.

## Fontes (29/08/2026)

- [Mercado Livre — ZCCO J6 magnético duplo Type-C](https://www.mercadolivre.com.br/microfone-lapela-magnetica-duplo-zcco-j6-antiruido-typec/up/MLBU3698804101) — 8h de bateria, 50m, 4.9★, 1000+ vendidos
- [Mundo do Microfone — review do "Xiaomi J6"](https://mundodomicrofone.com.br/microfone-lapela-sem-fio-xiaomi-j6/) — limitações: interferência, plástico, 1 TX por vez
- [Shopee — ZCCO J6-F](https://shopee.com.br/ZCCO-J6-F-Microfone-Lapela-Sem-Fio-Profissional-Magn%C3%A9tico-Cancelamento-Ru%C3%ADdo-Capta%C3%A7%C3%A3o-360%C2%B0-Compat%C3%ADvel-iPhone-iOS-i.1558330058.22094559816) — variante J6-F

---

# ✅ DECISÃO — 29/08 · Emerson escolheu ficar com a linha Boya (Omic-U)

Pergunta de checagem: existe Boya mais barato com o mesmo perfil (ímã + par)? **Resposta: não, dentro da marca Boya.** Mapeamento completo da linha:

| Modelo Boya | Preço | Ímã? | Par (2 TX)? | Veredito |
|---|---|---|---|---|
| **BY-V10** | ~R$246–268 | ❌ Só clipe | ❌ **Solo, 1 transmissor** | Mais caro E pior que o Omic-U no critério pedido |
| **BY-V20** | ~R$330–338 | ❌ Clipe | ✅ Par | Mais caro que o Omic-U, sem ímã |
| **Omic-D** | **R$685** | ⚠️ Não confirmado (descrito só como "clipe na roupa") | ⚠️ Não especificado | Muito mais caro, pior documentado |
| **Mini-14 / Mini 2** | R$387–456 | ❌ Clipe | ✅ Par | Mais caro que o Omic-U |
| **Omic-U** | **R$253 (ML) / R$346–364 (oficial)** | ✅ **Sim** | ✅ **Par** | ✅ **É o mais barato da marca que tem os dois critérios juntos** |

**Conclusão: dentro da Boya, o Omic-U não é só a melhor opção — é a ÚNICA que combina ímã + par.** Os modelos mais baratos da marca (BY-V10) abrem mão do par; os que têm par (BY-V20, Mini) abrem mão do ímã e ainda custam mais. Não existe "Boya mais barato com o mesmo perfil" — o Omic-U já é esse ponto.

## Fechando a compra

✅ **Comprar no Mercado Livre, não na loja oficial** — a mesma unidade custa **R$253 no ML** contra **R$346–364 no site da Boya do Brasil**. R$100+ de diferença pelo mesmo produto.

⚠️ **Checar estoque antes** — vários anúncios do Omic-U apareciam indisponíveis no ML em 29/08.

⚠️ **Não esquecer o teste obrigatório no dia que chegar, com o prazo de devolução aberto:**
1. Plugar → Open Camera → Configurações de vídeo → Fonte de áudio → "Microfone externo"
2. Gravar 10s falando normal → **tapar o microfone com a mão** e continuar falando
3. Áudio abafou → ✅ funcionou. Áudio igual → ❌ está no microfone interno do Moto E7 → **devolver**

Isso é o que garante que os R$253 não viram R$253 perdidos numa incompatibilidade de Motorola.

---

# ✅ COMPRA REALIZADA — 29/08 · Emerson comprou o Hollyland Lark A1 Mini USB-C

⚠️ **Mudança de decisão em relação ao registrado acima.** A recomendação anterior era o Boya Omic-U; o Emerson comprou o **Hollyland Lark A1 Mini USB-C Preto** — modelo que a Revisão 3 já havia mapeado como "o mais próximo do Lark M2", mas tinha sido descartado por estourar o teto de R$250. **Decisão do Emerson, não recomendação minha** — e é uma compra objetivamente boa, superior ao Omic-U em quase todo critério.

## Specs confirmadas (29/08)

| Critério | Lark A1 Mini | Comparado ao Omic-U (não comprado) |
|---|---|---|
| **Peso/discrição** | **8g, 0,9cm de espessura** — cabe por dentro da camisa | ✅ Muito mais discreto — era exatamente o critério original do Emerson |
| **Fixação** | ✅ Magnética | Empate |
| **Par** | ✅ 2 transmissores | Empate |
| **Bateria** | **54h** | 12h — Lark A1 é **4,5× maior** |
| **Alcance** | 200m (irrelevante — quarto tem 5m) | 50m (também irrelevante) |
| **Cancelamento de ruído** | 3 níveis adaptativos | Sim, sem graduação especificada |
| **USB-C** | ✅ Confirma compatibilidade com Moto E7 | ✅ |
| **Preço pago** | Verificar nota fiscal — mercado varia R$354-600 | Teria sido ~R$253 |
| **Acessórios** | 2 ímãs, 2 protetores de vento felpudos, base de carregamento, bolsa | Case com zíper |

## Por que essa compra é boa, apesar de estourar o teto original

1. **É o mesmo formato do Lark M2** (a referência de discrição que o Emerson pediu desde o início) — 8g contra 9g do M2, praticamente idêntico
2. **54h de bateria elimina uma preocupação operacional inteira** — não precisa recarregar entre sessões de gravação por semanas
3. **Marca com histórico melhor documentado** que Boya na faixa de lapela ultracompacto — Hollyland é referência no segmento
4. ⚠️ **O risco de compatibilidade Android/Motorola mapeado nas revisões anteriores continua valendo igual** — é risco do USB-C em geral, não do modelo específico

## ⚠️ O teste segue exatamente o mesmo, e agora é ainda mais importante

Pagou mais caro → o teste de validação no dia da chegada, com prazo de devolução aberto, importa mais, não menos:

1. Plugar → Open Camera (ou FiLMiC Pro) → selecionar fonte de áudio externa
2. Gravar 10s falando normal
3. **Tapar o transmissor com a mão** e continuar falando
4. Áudio abafou → ✅ funcionou. Áudio igual → ❌ Moto E7 não reconheceu, **devolver**

Rodar isso junto com o `teste-gravacao-30s.md` completo antes de contar com o microfone no vídeo 1.

## Atualização de status

**Compra de microfone: ✅ CONCLUÍDA.** Próximo bloqueio do checklist de `setup-gravacao.md` deixa de ser "comprar microfone" e passa a ser **rodar o teste de validação** — é o próximo passo natural.

## Fontes (29/08/2026)

- [Amazon — Hollyland Lark A1 Combo](https://www.amazon.com.br/Hollyland-LARK-Combo-Microfone-Carregamento/dp/B0F3DC7WWM) — specs completas, 8g, 0,9cm, 54h
- [Oficina da Net — Review Hollyland Lark A1](https://www.oficinadanet.com.br/audio/62177-review-hollyland-lark-a1)
- [Kenny Douglas — Hollyland Lark A1](https://kennydouglas.com.br/hollyland-lark-a1-microfone/)

---

# Funções do Lark A1 — o que ele faz além de captar áudio (29/08)

Pergunta do Emerson: quais funções novas ele ganha com esse microfone. Levantamento das funções reais, com o que muda na prática do canal.

## 🔑 A função que mais importa: gravação offline no próprio transmissor

**3 toques no microfone = ele grava um backup de áudio internamente**, independente do celular. Isso é seguro extra que o Kaidi/Boya baratos não têm.

⚠️ **Por que isso importa MUITO no seu caso específico:** é a rede de segurança contra o risco de compatibilidade Android/Motorola que mapeamos em toda a análise anterior. **Se o Moto E7 falhar em captar o áudio via USB-C** (o risco real que ainda não testamos), **o Lark A1 já gravou tudo sozinho por dentro** — você recupera depois plugando ele num PC. Nenhuma outra opção que analisamos (Kaidi, Boya) tinha essa rede de segurança.

## Controles físicos (nos botões do próprio microfone)

| Toques | Função |
|---|---|
| **1 clique** | Ativa/ajusta cancelamento de ruído |
| **2 cliques** | Muta o microfone |
| **3 cliques** | Inicia gravação offline (backup interno) |

## App companion: **LarkSound** (instalar no celular)

O app abre um painel de controle que os concorrentes baratos não têm:

| Recurso do app | O que faz | Uso prático pra você |
|---|---|---|
| **Equalização (3 perfis: Balance, Low, Bright)** | Muda o timbre da voz captada | Testar os 3 no `teste-gravacao-30s.md` e escolher o que soar mais natural na sua voz |
| **Cancelamento de ruído (3 níveis)** | Ajusta intensidade do filtro | Nível baixo/médio é mais seguro — nível alto pode distorcer a voz (mesmo problema que já expliquei sobre apps de ruído em geral) |
| **Reverb (3 níveis)** | Adiciona eco artificial | ⚠️ **Não usar** — quarto não precisa de reverb, e vídeo educacional pede voz seca e clara |
| **Mono/Estéreo** | Como os 2 transmissores gravam | Mono é suficiente pra 1 pessoa falando sozinha |
| **Controle de LED** | Liga/desliga a luzinha indicadora do transmissor | ⚠️ **Relevante pra discrição** — desligar o LED torna o microfone ainda mais invisível no vídeo, era exatamente seu pedido original |
| **Controle de ganho (6 níveis)** | Volume de entrada do microfone | Ajustar até a voz não estourar nem ficar baixa — testar durante o teste de 30s |

## Modo PC direto (bônus, fora do celular)

O receptor USB-C funciona **direto num computador** como microfone externo — útil se algum dia você quiser gravar um vídeo direto do PC (webinar, tela+voz) sem passar pelo celular.

## O que ele NÃO tem

⚠️ **Sem saída de monitoramento de áudio em tempo real** — não dá pra plugar fone no receptor e ouvir exatamente o que está sendo captado enquanto grava. Não é um problema para o seu uso (você confia no teste de 30s antes de gravar de verdade, não em ficar ouvindo ao vivo).

## Ação recomendada antes do vídeo 1

1. Instalar o app **LarkSound** no Moto E7
2. Desligar o **LED** do transmissor (discrição)
3. Deixar cancelamento de ruído em **nível baixo/médio**, sem reverb, modo **mono**
4. Rodar o `teste-gravacao-30s.md` com essas configurações
5. **Testar a gravação offline** (3 toques) uma vez, só pra confirmar que sabe ativar — é o seu plano B se o Android falhar
