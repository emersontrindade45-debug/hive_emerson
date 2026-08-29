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
