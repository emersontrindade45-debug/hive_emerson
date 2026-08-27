# Onde parei — 27/08/2026

> Arquivo de retomada. Abra uma sessão nova e diga **"leia o RETOMAR.md"** — ou simplesmente **"vamos continuar"**, que o Stamper lê os STATEs.
> Este arquivo é reescrito a cada sessão. Se a data acima não for recente, confie nos STATEs dos squads.

---

## O que fizemos hoje (5 entregas)

1. **10 marcos do trimestre criados no Neotriad** — C2/C3/C4 (conteúdo), A1–A6 (Araújo) + gatilho de cobrança, todos com papel EMPREENDEDOR e critério de verificação.
2. **6 skills criadas** a partir do acervo, uma por tema, com a regra "squad acionado, skill acionada".
3. **Coleta automática desligada** — virou radar de decisão toda segunda 09:00.
4. **Catálogo completo da Carol Iasmim baixado** — 58 vídeos (2025+2026), 271 mil palavras.
5. **Playbook de vendas destilado** — 4 métodos nomeados.

---

## ⏭️ O QUE FAZER NA PRÓXIMA SESSÃO

### Prioridade 1 — Conteúdo (é a prioridade nº 1 da empresa)

**Meta do trimestre: 4 vídeos publicados até 09/10. Hoje existe 1 roteiro e 0 vídeos gravados.**

- [ ] **Escrever o roteiro do vídeo 2** — é o gargalo real. Diga: *"vamos escrever o roteiro do vídeo 2"* (aciona a skill `roteiro-youtube` automaticamente)
- [ ] **Gravar o vídeo 1** — roteiro pronto desde 24/08 em `squads/marketing/data/roteiros/video-01-resposta-ruim.md`. Prazo: **11/09** (marco C2)

### Prioridade 2 — Preparar a reunião do Araújo (marco A3, 18/09)

- [ ] **Fazer o dever de casa do método Contrapeso** (a skill `vendas` conduz):
  1. Diferenciais do Hub
  2. **Custo invisível do Araújo** — quanto custa por mês o problema continuar (dados estão no Supabase)
  3. **3 moedas de troca** — o que você cede e o que exige em troca
- [ ] Isso alimenta o **relatório de valor** do marco A2 (11/09), que sustenta o A3

### Ações manuais só suas (não consigo fazer)

- [ ] **Setup do canal no YouTube** — guia campo-a-campo pronto em `squads/marketing/data/assets/COLAR-NO-YOUTUBE.md`: corrigir nome de exibição (`ImpulsoIA` → `Emerson | Impulso IA`), colar descrição, subir banner, palavras-chave, links, playlist
- [ ] **Registrar o Channel ID** no STATE do Marketing — desbloqueia o worker de analytics
- [ ] **Comprar microfone** — R$120-250 (ring light e tripé você já tem)
- [ ] **2FA** no `emerson.impulsoia@gmail.com` + adicionar esse e-mail como secundário no LinkedIn
- [ ] **Vincular os marcos a uma Meta no Neotriad** (opcional) — a API não cria metas; se você criar as duas na interface ("Conteúdo" e "Araújo"), eu vinculo via `id_meta`

---

## 📋 Backlog registrado (não urgente)

- **Destilar as 51 transcrições restantes da Carol** — estão baixadas; o playbook cobre 7. Temas pendentes: carisma, prospecção, autoridade, fechamento, gatilhos, atendimento, mentalidade, mercados concorridos
- **Completar o AIDAS** — só a letra A foi destilada (I, D, A, S estão em `9pyipK86Imc.json`)
- **Destilar as 9 transcrições do Joel Jota** (negócios) — nunca lidas
- **67 transcrições de Dev e Infra** — baixadas, nunca lidas, sem playbook
- **Preencher `icp-profile.md` e `qualification-criteria.md`** — em template genérico desde 02/06. O Método Alicerce (§2 do sales-playbook) é o roteiro
- **Reclassificar a tríade no Neotriad** — 100% das tarefas estão como "I" (alvo: 70%). Se tudo é importante, a tríade para de ordenar
- **Raspar canais pendentes** — 6 indicados em 26/08 + Oliver Rasmussen e Felipe Borges

---

## 🔁 Rotina que agora roda sozinha

**Toda segunda 09:00** a tarefa `HIVE-YouTube-Intel` gera o radar em `data/youtube-radar/YYYY-MM-DD.md` — lista os vídeos novos de todos os canais **sem baixar nada**. Você escolhe os números, e só o escolhido vira transcrição.

Para rodar manualmente: `python _core/youtube-radar.py --dias 7`

---

## 🧠 Como as skills funcionam agora

Ao falar de um assunto, a skill do squad dono carrega sozinha:

| Você fala sobre | Skill que dispara |
|---|---|
| roteiro, hook, título, thumbnail, pauta | `roteiro-youtube` |
| marca, território, tese, bio | `influencia-digital` |
| qualquer número/estatística que vá ao ar | `dados-verificados` |
| meta, trimestre, rotina, Neotriad | `metas-performance` |
| venda, desconto, objeção, "tá caro", Araújo | `vendas` |
| "vale a pena?", nova oportunidade, precificar | `modelo-de-negocios` |
| radar, o que saiu de novo, lista da semana | `radar-youtube` |

**Dev, Infra, CS, Product, Finance e Quality não têm skill** — não têm acervo destilado. O hook avisa isso explicitamente em vez de improvisar.

---

## ⚠️ Travas ativas — não reabrir por engano

- **Conteúdo ganha do Araújo** quando disputarem a mesma hora (decisão de 26/08)
- **Prospecção ativa por ligação está excluída** do trimestre (23/08) — 238 leads parados de propósito
- **Servir primeiro** — nenhuma régua de lead antes do 8º vídeo
- **2º canal (Concurso com IA) e SaaS do Ciclo EARA:** congelados até 09/10
- **Nada de transcrição baixada automaticamente** — radar lista, você escolhe
- **A âncora do Araújo é R$ 4.000** — a contingência de R$1.500-3.000 é rede de segurança, não ponto de partida
