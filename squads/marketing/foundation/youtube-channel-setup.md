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

## Pendente do Emerson — decisões que faltam

Nenhuma tem resposta certa; são as únicas coisas que este arquivo não pode decidir sozinho.

- [ ] **Nome do canal** — precisa refletir o eixo ("IA aplicada a trabalho que já existe"), não o público P1-P5 em teste. Evitar nome que amarre a um público só (ex.: nada com "comércio" ou "varejo" — mataria a leitura de P3/P4). Testar se o nome funciona pronunciado em vídeo ("se inscreve no canal ___").
- [ ] **Handle (@usuario)** — precisa estar livre no YouTube e, se possível, coerente com Instagram/LinkedIn/TikTok para quando esses canais entrarem (mesmo handle em todas as plataformas evita fragmentar marca pessoal).
- [ ] **Nome de exibição do criador** — usar nome real (Emerson) ou nome de canal? Dado o tom "conversa de quem já fez" (`brand-voice.md`), nome real tende a reforçar credibilidade — mas é decisão do Emerson.

---

## Checklist técnico — YouTube Studio

### 1. Conta e canal
- [ ] Criar/usar conta Google dedicada (separar do Gmail pessoal se o Emerson preferir isolar)
- [ ] Criar canal em [youtube.com/create_channel](https://www.youtube.com/create_channel)
- [ ] Definir nome do canal (ver pendência acima)
- [ ] Reivindicar handle @ (ver pendência acima) — [youtube.com/handle](https://www.youtube.com/handle)
- [ ] Categoria do canal: **Educação** ou **Como fazer e estilo** (mais aderente a "Help/tutorial" que é 50-40% do conteúdo por `creator-profile.md`)
- [ ] País: Brasil / Idioma: Português

### 2. Identidade visual
- [ ] Foto de perfil (800×800px mín.) — coerente com tom "direto e sem hype": preferir foto real a logo abstrato, dado que autoridade vem de "quem já fez" (`brand-voice.md`)
- [ ] Banner do canal (2560×1440px, área segura 1546×423px) — comunicar o eixo em 1 linha ("IA aplicada a trabalho que já existe" ou variação)
- [ ] Watermark de inscrição (150×150px) — aparece nos vídeos, opcional mas recomendado desde o vídeo 1

### 3. Descrição e metadados do canal
- [ ] Descrição do canal (primeiras 2 linhas aparecem sem "ver mais" — usar o eixo + prova, não slogan)
- [ ] Links: site/LinkedIn/Instagram (mesmo sem conteúdo lá ainda, reserva o espaço)
- [ ] E-mail de contato comercial (separado do pessoal, para parcerias)
- [ ] Palavras-chave do canal (Configurações → Canal → Palavras-chave básicas): usar vocabulário de `brand-voice.md` seção "Usar" — *automação, WhatsApp, n8n, IA para negócio* — não jargão técnico puro

### 4. Configurações antes do primeiro upload
- [ ] Ativar monetização não é possível ainda (exige 500 inscritos + 3.000h watch time ou 3M views Shorts em 90 dias — regra 2026) — não é bloqueio para publicar, só não gera receita ainda
- [ ] Definir template de descrição de vídeo (reutilizável): resumo + timestamps + links + CTA — escrever 1 vez, reaplicar
- [ ] Definir template de tags/categoria padrão
- [ ] Ativar/testar Estúdio de Legendas — vídeo 1 é "Help" educacional, legenda ajuda retenção (régua 1 de `mapa-teste-publico.md`)

### 5. Primeiro upload (vídeo 1)
- [ ] Título — testar 2-3 variantes com `/write-headline` antes de decidir
- [ ] Thumbnail — coerente com "sem hype": nada de emoji de choque ou seta vermelha genérica; usar print de tela real (o roteiro já usa demonstração de tela) ou rosto + texto curto
- [ ] Descrição usando o template do item 4
- [ ] Card/tela final apontando para o próximo vídeo (mesmo que ainda não exista — linkar playlist do canal)
- [ ] Verificar: vídeo público, não "não listado", data de publicação alinhada ao marco C2 (11/09)

### 6. Depois do primeiro vídeo no ar
- [ ] Criar playlist única (ex. "Automação sem enrolação") — vídeos futuros entram nela desde o início
- [ ] Registrar URL do canal e do vídeo 1 em `memory/STATE.md` L1
- [ ] Atualizar `data/social-analytics/` (ver `foundation/social-analytics-glossary.md`) com o Channel ID assim que existir — é o que destrava o worker de analytics

---

## Ordem recomendada

1. Decidir nome + handle (única dependência real — trava tudo abaixo)
2. Criar canal + identidade visual (item 1-3) — pode ser feito em paralelo à gravação
3. Configurar templates (item 4) — uma vez só, reutiliza para sempre
4. Publicar vídeo 1 (item 5)
5. Playlist + registro de STATE (item 6)

**Não bloqueia a gravação.** Filmar (câmera/áudio/luz, já na grade de 27/08) pode acontecer antes do canal existir — só o upload final depende do canal criado.
