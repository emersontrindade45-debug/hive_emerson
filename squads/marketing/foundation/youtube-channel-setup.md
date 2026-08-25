# Setup do Canal — Checklist de Criação

> Criado 2026-08-25. O canal ainda não existe. Roteiro do vídeo 1 está pronto (`data/roteiros/video-01-resposta-ruim.md`), marco C2 (primeiro vídeo publicado) vence **11/09**. Este arquivo é o que falta entre "roteiro pronto" e "vídeo no ar".
>
> Não reabre nicho, público ou tom — isso está decidido em `creator-profile.md`, `mapa-teste-publico.md` e `brand-voice.md`. Este arquivo é só o que existe *tecnicamente* no YouTube Studio.

---

## O que já está decidido (não escolher de novo aqui)

| Decisão | Onde está |
|---|---|
| Eixo do canal | "IA aplicada a trabalho que já existe" — `creator-profile.md` |
| Tom | Direto e sem hype — `brand-voice.md` |
| Público | Em teste, 5 hipóteses, sem ICP fechado até o 8º vídeo — `mapa-teste-publico.md` |
| Formato/duração | YouTube 5–10min, Reels ~1min — `creator-profile.md` |
| Vídeo 1 | Roteiro pronto, ângulo #7, pilar 3, público P3 — `data/roteiros/video-01-resposta-ruim.md` |

---

## Decisões do Emerson — ✅ FECHADAS 25/08/2026

Todas resolvidas. Textos prontos para colar em [`canal-identidade.md`](./canal-identidade.md).

- [x] **Nome da marca:** Impulso IA
- [x] **Handle:** ✅ **`@emerson.impulsoia`** — criado 25/08 (ficou o fallback; mesmo handle do Instagram)
- [x] **Nome de exibição:** decidido `Emerson | Impulso IA` — ⚠️ **está `ImpulsoIA` no canal**, trocar (10s, editável sempre)
- [x] **Conta Google:** `emerson.impulsoia@gmail.com` — já criada, dedicada

⚠️ **Risco de marca registrado (não bloqueia):** existe IMPULSO DIGITAL TECNOLOGIA E INTELIGENCIA ARTIFICIAL LTDA (CNPJ 60.475.559/0001-08) no mesmo CNAE. Não impede o canal; pode impedir registro INPI. Detalhe em `canal-identidade.md`.

---

## Checklist técnico — YouTube Studio

### 1. Conta e canal
- [x] ✅ Conta Google dedicada **já existe**: `emerson.impulsoia@gmail.com` — logar com ela
- [ ] Ativar **verificação em 2 etapas** nessa conta — ela é o único ponto de falha do canal
- [x] ✅ **Canal criado 25/08** — https://www.youtube.com/@emerson.impulsoia
- [ ] ⚠️ **Corrigir nome de exibição:** está `ImpulsoIA`, trocar para **`Emerson | Impulso IA`** em Studio → Personalização → Informações básicas. Não afeta URL nem inscritos
- [x] ✅ Handle reivindicado: **`@emerson.impulsoia`**
- [ ] Categoria do canal: **Educação** (decidido 25/08)
- [ ] País: Brasil / Idioma: Português

### 2. Identidade visual
- [ ] Foto de perfil (800×800px) — **foto real do Emerson**, não logo. Spec completa em `canal-identidade.md`
- [ ] Banner (2560×1440px, área segura 1546×423px) — linha única **"IA aplicada a trabalho que já existe"**. Spec e o que evitar em `canal-identidade.md`
- [ ] Watermark de inscrição (150×150px) — aparece nos vídeos, opcional mas recomendado desde o vídeo 1

### 3. Descrição e metadados do canal
- [ ] Descrição do canal — **texto pronto para colar em `canal-identidade.md`**, sem placeholder pendente
- [ ] Links do canal: LinkedIn `linkedin.com/in/emerson-trindade-8001` + Instagram `@emerson.impulsoia` — tabela com ordem em `canal-identidade.md`
- [ ] Adicionar `emerson.impulsoia@gmail.com` como **e-mail secundário no LinkedIn** (perfil está numa conta Hotmail pessoal — sem isso, perder o Hotmail = perder o perfil e os contatos)
- [x] ✅ E-mail de contato: `emerson.impulsoia@gmail.com` (mesmo da conta dona por ora — separar quando houver domínio)
- [ ] Palavras-chave do canal (Configurações → Canal → Palavras-chave básicas) — **lista pronta em `canal-identidade.md`**

### 4. Configurações antes do primeiro upload
- [ ] Ativar monetização não é possível ainda (exige 500 inscritos + 3.000h watch time ou 3M views Shorts em 90 dias — regra 2026) — não é bloqueio para publicar, só não gera receita ainda
- [x] ✅ Template de descrição de vídeo **completo** — `canal-identidade.md`, sem placeholder
- [x] ✅ Template de tags padrão **escrito** — `canal-identidade.md`
- [ ] Ativar/testar Estúdio de Legendas — vídeo 1 é "Help" educacional, legenda ajuda retenção (régua 1 de `mapa-teste-publico.md`)

### 5. Primeiro upload (vídeo 1)
- [ ] Título — testar 2-3 variantes com `/write-headline` antes de decidir
- [ ] Thumbnail — coerente com "sem hype": nada de emoji de choque ou seta vermelha genérica; usar print de tela real (o roteiro já usa demonstração de tela) ou rosto + texto curto
- [ ] Descrição usando o template do item 4
- [ ] Card/tela final apontando para o próximo vídeo (mesmo que ainda não exista — linkar playlist do canal)
- [ ] Verificar: vídeo público, não "não listado", data de publicação alinhada ao marco C2 (11/09)

### 6. Depois do primeiro vídeo no ar
- [ ] Criar playlist **"IA sem enrolação"** (nome decidido 25/08) — vídeo 1 entra nela já no upload
- [ ] Registrar **Channel ID** (`UC...`, em Configurações → Canal → Configurações avançadas) + URL do canal e do vídeo 1 em `memory/STATE.md` L1
- [ ] Atualizar `data/social-analytics/` (ver `foundation/social-analytics-glossary.md`) com o Channel ID assim que existir — é o que destrava o worker de analytics

---

## Ordem recomendada

1. ~~Decidir nome + handle~~ ✅ feito 25/08 — ver `canal-identidade.md`
2. Criar canal + identidade visual (item 1-3) — pode ser feito em paralelo à gravação
3. Configurar templates (item 4) — uma vez só, reutiliza para sempre
4. Publicar vídeo 1 (item 5)
5. Playlist + registro de STATE (item 6)

**Não bloqueia a gravação.** Filmar (câmera/áudio/luz, já na grade de 27/08) pode acontecer antes do canal existir — só o upload final depende do canal criado.
