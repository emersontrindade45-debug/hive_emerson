# Onde parei — 31/08/2026

> Arquivo de retomada. Abra uma sessão nova e diga **"leia o RETOMAR.md"** — ou simplesmente **"vamos continuar"**, que o Stamper lê os STATEs.
> Este arquivo é reescrito a cada sessão. Se a data acima não for recente, confie nos STATEs dos squads.

---

## ⏰ O RELÓGIO — leia isto primeiro

| Marco | Prazo | Faltam | Situação real |
|---|---|---|---|
| **C2** — vídeo 1 publicado | **11/09** | **11 dias** | roteiro pronto desde 24/08, microfone comprado, **0 gravado** |
| **A2** — relatório de valor Araújo | 11/09 | 11 dias | dever de casa Contrapeso não feito |
| **A3** — reunião de preço Araújo | 18/09 | 18 dias | depende do A2 |
| **C3** — 4 vídeos publicados | 09/10 | 39 dias | **1 roteiro, 0 vídeos** |

**Nada avançou em gravar desde 27/08.** As entregas de 29/08 e 31/08 foram todas de preparação, análise e ferramenta. O gargalo não mudou.

---

## O que fizemos em 31/08 (6 entregas)

1. **Radar de IA voltou a rodar** — `squads/intelligence/data/radar-semanal-2026-08-31.md`, o primeiro em 12 dias.
2. **Skill `roteiro-gauntlet` criada** — técnica gauntlet-loop (RoboNuggets/Matt Shumer) adaptada, registrada no hook e testada em 6 cenários de roteamento.
3. **RoboNuggets adicionado ao radar** — `channels.json` do Marketing, 18 canais no total. Tabela da skill `radar-youtube` corrigida (dizia 10 canais e listava Commercial como vazio).
4. **Varredura de 30 dias** — `data/youtube-radar/2026-08-31-30d.md`, 49 vídeos de 10 dos 17 canais então monitorados.
5. **Notion — 3 estruturas novas** em `Negócio → Empresa IA → PRODUTO & INOVAÇÃO → Laboratório IA`:
   - **📡 Radar IA — Semanal** (base + 6 views), 12 sinais de IA carregados
   - **📈 Relatório de Nicho** (painel enxuto, só tabelas)
   - **🎬 Conteúdos do Nicho** (base + 4 views), 27 vídeos com veredito "aplica ao negócio?"
6. **Análise de outliers do nicho por cálculo direto** — o filtro do vidIQ falhou duas vezes; refeito sobre o acervo dos canais.

---

## 🔴 O ACHADO QUE MUDA DECISÃO — Meta Business Agent

**A Meta tem um agente de IA nativo no WhatsApp Business, global, com +1 milhão de negócios usando.** Lançado em **03/06/2026** (não é notícia da semana — o achado é que isso tem quase 3 meses e nunca entrou em nenhum STATE). Desde agosto a cobrança é **por token**.

**Consequências que precisam ser tratadas antes de 18/09:**
- O diferencial "atendimento por WhatsApp com IA" do Hub **deixou de ser diferencial** — vem de fábrica.
- A seção "diferenciais do Hub" do dever de casa do **método Contrapeso** (marco A3) precisa ser reescrita sabendo disso. Se o Araújo descobrir na reunião e você não tiver resposta, a âncora de R$4.000 não se sustenta.
- O ângulo do Pilar 1 mudou: não é mais *"dá pra colocar IA no WhatsApp"*, é *"a Meta já colocou — e o que ela não faz"*.
- **Bônus:** o Brasil é **38,9% da busca mundial** por "meta business agent", e nenhum canal do recorte PT-BR fez vídeo sobre isso.

---

## 📊 A DESCOBERTA ESTRATÉGICA — as duas pistas do nicho

Análise de 20 canais PT-BR e 27 vídeos (detalhe completo no Notion):

| | 🅰️ Implementação | 🅱️ Notícia/opinião |
|---|---|---|
| Referência | Guilherme Lazarotto (53k) | Maestros da IA (104k) |
| Tema que vence | n8n + WhatsApp, grátis, passo a passo | Claude, modelo novo, "99% das pessoas" |
| Cadência necessária | **4 vídeos/mês** | **86 vídeos/mês** |
| Validade | Perene (o nº1 rende há 15 meses) | Perecível |
| Maior outlier | **92,7×** a mediana | 5,1× |
| Gera | **Lead qualificado** | Audiência |

**A pista A é a sua.** Prova controlada, mesmo canal e mesma pessoa, só o tema muda: vídeos de n8n/WhatsApp têm mediana de **18.758 views**; vídeos de "ferramenta do momento", **4.459**. O contraexemplo: *"Kimi K3 supera o Fable 5?"* do mesmo criador — **1.436 views**, 588× menos que o nº1 dele.

**Vocabulário dos vencedores:** "GRÁTIS"/"DE GRAÇA"/"sem gastar NADA" · "para Iniciantes"/"Fácil"/"Passo a Passo" · ano no título.

⚠️ **Sobre a meta de 1 milhão de inscritos (pedida em 31/08):** nenhum canal de IA para negócios em PT-BR chegou lá. O teto do nicho é 797k (Grupo Ninja, 12 anos, hoje +1,9%/ano). O crescimento mais rápido já medido custou 86 vídeos/mês. **E é a métrica errada para lead:** Guilherme tem 53k inscritos e 41.321 views médias por vídeo; Bruno Picinini tem 444k e 36.524. A OnsmartAI vende SDR de IA com 84 mil inscritos. Escada real: 8 vídeos → 1k inscritos → 10k → 84k → 1M.

---

## ⏭️ O QUE FAZER NA PRÓXIMA SESSÃO

### Prioridade 1 — Gravar (é a prioridade nº 1 da empresa)

- [x] ~~Comprar o microfone~~ — ✅ **COMPRADO: Hollyland Lark A1 Mini USB-C** (29/08). 8g, 0,9cm, magnético, par de transmissores, 54h de bateria. Não é o Boya que estava recomendado — o Emerson mudou de decisão e a compra é melhor em quase todo critério. Detalhe em `foundation/compra-microfone.md` § Compra Realizada
- [ ] 🔴 **TESTE DA MÃO — fazer no dia que o microfone chegar, com prazo de devolução aberto.** Open Camera → Config → Vídeo → Fonte de áudio → "Microfone externo" → gravar 10s → **tapar o transmissor com a mão** falando. Áudio abafou = ✅ funcionou. Áudio igual = ❌ está no microfone interno do Moto E7 → **devolver**. ⚠️ **O erro é silencioso:** grava normal, com o áudio errado. Risco de Motorola não reconhecer USB-C vale para qualquer modelo
- [ ] **Fazer o teste de 30s** — protocolo pronto em `foundation/teste-gravacao-30s.md`. Custo zero
- [ ] **Gravar o vídeo 1** — roteiro pronto em `data/roteiros/video-01-resposta-ruim.md`. Prazo 11/09

### Prioridade 2 — Araújo (marco A3, 18/09)

- [ ] **Reescrever os diferenciais do Hub** considerando o Meta Business Agent (ver seção 🔴 acima)
- [ ] Custo invisível do Araújo (dados no Supabase) + 3 moedas de troca — a skill `vendas` conduz

### Prioridade 3 — Conteúdo

- [ ] **Roteiro do vídeo 2** — a pauta com melhor evidência é *"O que a IA nativa do WhatsApp NÃO faz"*: resolve conteúdo e o dever de casa do Araújo no mesmo trabalho
- [ ] Escolher os números do radar de 31/08 que valem transcrição (49 candidatos, 15h39 de vídeo total — não cabe num dia)

### Ações manuais só suas

- [x] ~~Comprar microfone~~ ✅ feito 29/08
- [ ] **Setup do canal no YouTube** — guia em `foundation/assets/COLAR-NO-YOUTUBE.md`
- [ ] **Registrar o Channel ID** no STATE do Marketing
- [ ] **2FA** no `emerson.impulsoia@gmail.com`
- [ ] **Automações do Notion** — a API não cria automações; as 3 que valem estão descritas na página do Radar IA

---

## 🐛 Pendências técnicas registradas

- **Bug no hook `userprompt-squad-routing.py`:** casamento por substring sem fronteira de palavra. A chave `api` do squad Dev casa dentro de "l**api**da", "r**ápi**do", "c**api**tal", "ter**api**a". Outras chaves curtas com o mesmo risco: `dev`, `bug`, `crm`, `icp`, `seo`, `bio`, `nps`, `okr`, `sop`, `dns`, `ssl`, `vps`, `mei`, `dre`. Correção mexe na função `detect()`, que serve todos os squads — não foi feita.
- **Radar cego para Shorts:** lê só a aba `/videos`. O RoboNuggets publica ~109 shorts e 7 longos por mês — 94% invisível.
- **Radar não guarda histórico de título:** 4 canais trocaram título de vídeo já publicado em 31/08 (um deles em menos de 6 horas). Cada execução sobrescreve a leitura anterior.
- **Análise de mediana cobre 2 dos 6** canais em crescimento. Faltam onsmartAI, Eli Rigobeli, inventormiguel e Invente com IA.

---

## 📋 Backlog registrado (não urgente)

- Destilar as 51 transcrições restantes da Carol · Completar o AIDAS · 9 transcrições do Joel Jota · 67 de Dev e Infra nunca lidas
- Preencher `icp-profile.md` e `qualification-criteria.md`
- Reclassificar a tríade no Neotriad — **13 de 13 tarefas estão como "I"** (alvo: 70%)
- Raspar canais pendentes: 6 indicados em 26/08 + Oliver Rasmussen e Felipe Borges

---

## 🔁 Rotinas que rodam sozinhas

**Segunda 09:00** — tarefa `HIVE-YouTube-Intel` roda `_core/youtube-radar.py` e gera a lista em `data/youtube-radar/YYYY-MM-DD.md`. **Sem baixar nada.**

**Sexta 14:00** — revisão semanal. Indicador: vídeos publicados (acumulado). Binário.

⚠️ O **radar de IA do Intelligence é manual** — não tem tarefa agendada. Foi por isso que ficou 12 dias parado. Um agente agendado semanal foi oferecido em 31/08 e **não foi aprovado ainda**.

Manual: `python _core/youtube-radar.py --dias 7`

---

## 🧠 Skills (8)

| Você fala sobre | Skill |
|---|---|
| roteiro, hook, título, thumbnail, pauta | `roteiro-youtube` |
| **lapidar/criticar um rascunho que já existe** | **`roteiro-gauntlet`** (nova em 31/08) |
| marca, território, tese, bio | `influencia-digital` |
| qualquer número que vá ao ar | `dados-verificados` |
| meta, trimestre, rotina, Neotriad | `metas-performance` |
| venda, desconto, objeção, Araújo | `vendas` |
| "vale a pena?", precificar | `modelo-de-negocios` |
| radar, o que saiu de novo | `radar-youtube` |

**Dev, Infra, CS, Product, Finance e Quality não têm skill** — não têm acervo destilado.

---

## ⚠️ Travas ativas — não reabrir por engano

- **Conteúdo ganha do Araújo** quando disputarem a mesma hora (26/08)
- **Prospecção ativa por ligação está excluída** do trimestre (23/08) — 238 leads parados de propósito
- **Servir primeiro** — nenhuma régua de lead antes do 8º vídeo
- **2º canal (Concurso com IA) e SaaS do Ciclo EARA:** congelados até 09/10
- **Nada de transcrição baixada automaticamente** — radar lista, você escolhe
- **Nunca rodar `youtube-collect-all.py`** — contraria a decisão de 27/08
- **A âncora do Araújo é R$ 4.000** — a contingência de R$1.500-3.000 é rede de segurança, não ponto de partida
- **A skill `roteiro-gauntlet` não tem restrição de escopo** — decisão do Emerson em 31/08. As 3 travas propostas pelo agente foram removidas a pedido dele. **Não reintroduzir sem ele pedir.**
