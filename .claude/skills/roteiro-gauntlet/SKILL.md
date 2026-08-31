---
name: roteiro-gauntlet
description: Use para LAPIDAR um roteiro, título ou thumbnail que já existe em rascunho, comparando-o às cegas contra um vídeo real que funcionou. Não escreve do zero — isso é a `roteiro-youtube`. Dispara em "gauntlet", "compara com", "está bom o suficiente?", "lapida esse roteiro", "melhora o roteiro", "barra de qualidade", "critica esse roteiro".
---

# Gauntlet — lapidar contra uma barra real

**Squad:** Marketing (Pietro) · **Divisão:** `[M1]` Conteúdo e Editorial
**Origem:** técnica *gauntlet-loop* (RoboNuggets, a partir do projeto Claude of Duty do Matt Shumer), CC BY 4.0. **Adaptada em 31/08/2026 com uma mudança deliberada — ver § Teto.**

## A ideia

> *"Uma rubrica pede pro agente se dar nota contra palavras que ele mesmo escreveu. Uma barra faz ele comparar com algo que já existe e é inegavelmente bom."*

O `youtube-playbook.md` é uma rubrica: fui eu que o destilei, e avaliar um roteiro contra ele é me autoavaliar. Esta skill troca isso por uma **comparação cega contra um vídeo real**.

## Escopo — sem restrição

**Decisão do Emerson, 31/08/2026:** esta skill roda em qualquer entrega, a qualquer momento, sem exceção de fase ou de marco.

Uma versão anterior trazia três travas de escopo propostas pelo agente (não usar em gravar/editar/publicar, não usar no vídeo 1 antes do marco C2, não usar sem teto). **Foram removidas a pedido do Emerson.** Não reintroduzir sem ele pedir.

O teto de rodadas do § Teto continua valendo — é parâmetro do método, não restrição de escopo.

## Passo 0 — Pré-requisito

O rascunho já existe. Se não existe, a skill errada foi acionada: use `roteiro-youtube` para escrever, **depois** volte aqui. Ordem: playbook escreve → gauntlet lapida.

## Passo 1 — Escolher a barra

A barra é o truque inteiro. Precisa passar nos 3 testes:

| Teste | Significa |
|---|---|
| **Nomeada** | "O vídeo do Starbucks dos Nerds", não "um vídeo bom de caso" |
| **Obtenível** | Transcrição no disco, ou baixável agora |
| **Comparável** | Mesmo formato e mesma intenção do rascunho |

⚠️ **O terceiro teste é o que mais falha aqui.** O acervo de Marketing é quase todo *meta-conteúdo sobre YouTube* (algoritmo, regras, crescimento). Comparar um roteiro Help sobre IA contra um vídeo sobre o algoritmo do YouTube não é comparação — é ruído.

**Barras já no disco** (`squads/marketing/data/youtube-intel/transcripts/`):

| Barra | Serve para |
|---|---|
| *How to Script Viral Videos 10x Faster* (102k views) | Estrutura e ritmo de Help |
| *Beginner's Guide to YouTube Script Writing* (64k, 52k palavras) | Referência longa de estrutura |
| *10 técnicas de STORYTELLING* (76k) | Micro-história dentro do roteiro |
| *O ALGORITMO DO YOUTUBE MUDOU* (273k) | Só para pauta sobre YouTube |

**Se nada no disco for comparável, baixe a barra certa** — é 1 comando e vale mais que forçar uma barra ruim:

```bash
python _core/youtube-fetch-video.py --dir squads/marketing/data/youtube-intel <URL>
```

Candidato forte já mapeado: **RoboNuggets** (`@robonuggets`) — formato Help sobre IA aplicada, que é exatamente o eixo do canal. Em inglês: serve de barra de **estrutura e ritmo**, nunca de pauta (ver ressalva de mercado no relatório de 26/08).

Se o Emerson não indicou a barra, **proponha 2-3 candidatas e pare para ele escolher.** Não redija nada antes disso.

## Passo 2 — Fatiar

Quebre o rascunho nas menores peças que possam ser julgadas sozinhas. Para roteiro, tipicamente: **hook · promessa · corpo (cada bloco) · CTA**. Peça grande esconde defeito.

## Passo 3 — Comparação cega

1. Extraia da barra o trecho **equivalente** à peça (o hook da barra contra o seu hook).
2. Monte os dois textos como **A** e **B**, sem identificar qual é qual, e **sorteie a ordem**.
3. O crítico roda como **subagente com contexto novo** — não pode ter visto o rascunho sendo escrito, nem saber qual texto é seu.
4. O crítico devolve exatamente duas coisas: **qual venceu (A ou B, binário — nunca nota de 0 a 10)** e **a maior lacuna que resta**, em uma frase.
5. A lacuna volta para quem escreve. Nova rodada.

**O crítico é duro. Elogio não serve para nada.** Se ele empatar ou hesitar, o veredito é derrota.

## Passo 4 — Teto ⬅️ a mudança deliberada

**Máximo de 3 rodadas por peça, ou 40 minutos no total — o que vier primeiro.**

Isto **contraria a regra central da técnica original**, de propósito. O autor escreveu para builds de software, onde iterar é barato e não há vergonha de aparecer envolvida. Aqui o custo de uma rodada extra não é token: é mais um dia sem vídeo publicado.

**Quando o teto estourar e o rascunho ainda perder:**

1. **Entrega assim mesmo.** O roteiro segue para gravação.
2. **Registre a lacuna** em `squads/marketing/foundation/youtube-playbook.md`, com a barra nomeada e a frase do crítico.
3. A lacuna vira entrada de playbook — o **próximo** roteiro já nasce com ela resolvida.

Perder para a barra não bloqueia nada. Vira ativo.

## Passo 5 — Travas do canal continuam valendo

Antes de entregar, o resultado ainda passa pelo Passo 2 da `roteiro-youtube`: eixo fixo, tom sem hype, 4 pilares, servir primeiro, altitude baixa até o 8º vídeo. **A barra não revoga as travas.** Se vencer a comparação custou o tom do canal, a rodada foi perdida.

Número que for ao ar continua passando pela `dados-verificados`.

## Modos de falha (do autor, todos válidos aqui)

- Barra vaga → o crítico inventa a comparação
- Quem escreveu julgando o próprio texto
- Crítico macio, elogiando incremento
- Sair por contagem de rodada em vez de por qualidade — **aqui é o inverso: sair por teto é permitido e previsto**
- Especificar demais e sufocar o julgamento do agente

## ⚠️ Não copie o prompt do repositório original

O template de lá termina com `/loop on each piece` e `Fan out subagents and ultracode`. **Neste ambiente `ultracode` não existe, e `/loop` significa outra coisa** — roda um comando em intervalo recorrente. Colado literalmente, ele agenda tarefa repetida em vez de iterar. Use os passos desta skill.
