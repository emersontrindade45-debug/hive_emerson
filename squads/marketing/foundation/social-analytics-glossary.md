# Glossário de Métricas — Análise de Dados Sociais

> Criado 2026-08-25. Cobre YouTube (ativo). Instagram, LinkedIn, Facebook, TikTok, X e Google AdSense entram quando cada plataforma for priorizada — mesma estrutura, seção nova por plataforma.
>
> Este arquivo existe para dar significado ao que o worker de analytics vai coletar (`workers/youtube-analytics.py`, a construir quando o canal existir). Sem ele, número vira ruído — não vira decisão.

---

## YouTube

### Métricas de canal

| Métrica | O que mede | Onde ver |
|---|---|---|
| **Inscritos** | Pessoas que optaram por ver mais. Vaidosa se isolada — inscrito que não assiste não vale nada | YouTube Studio → Público |
| **Views (visualizações)** | **Mudou em 24/08/2026** — conta a partir do primeiro frame, não mais ~30s assistidos. Infla comparação com dado histórico pré-24/08 | YouTube Studio → Visão geral |
| **Engaged views** | A métrica que substitui view como proxy de atenção real, pós-mudança de 24/08. Usar esta, não view bruta, para julgar se um vídeo prendeu alguém | YouTube Studio → Alcance |
| **Watch time (tempo de exibição)** | Soma de minutos assistidos. YouTube usa isso — não views — para decidir recomendação | YouTube Studio → Alcance |
| **Retenção média (%)** | Da duração total, quanto a média de quem clicou assistiu. É a régua 1 de `mapa-teste-publico.md`: retenção alta = o vídeo estava sendo útil | YouTube Studio → Envolvimento |
| **CTR da thumbnail (%)** | De quem viu a thumbnail no feed/busca, quantos clicaram. Mede a promessa, não a entrega | YouTube Studio → Alcance |
| **RPM (receita por mil views)** | Só existe após monetização ativa (500 inscritos + 3.000h watch time ou 3M views Shorts/90 dias). Não aplicável ainda | YouTube Studio → Receita |

### Metas realistas — canal novo (0 a 8 vídeos)

Não comparar com canais estabelecidos. `mapa-teste-publico.md` já define a régua certa para esta fase — este bloco só traduz em número de referência, não meta rígida:

| Métrica | Faixa "canal novo saudável" | O que preocupa |
|---|---|---|
| Retenção média | 40%+ em vídeo de 5-10min | Abaixo de 25% — hook ou promessa da thumbnail não bate com o conteúdo |
| CTR thumbnail | 4-8% | Abaixo de 2% — thumbnail/título não comunica o que o vídeo entrega |
| Comentário com contexto | Qualquer volume > 0 nos primeiros vídeos | Views alta + zero comentário de contexto = ninguém foi servido de verdade (regra explícita de `mapa-teste-publico.md`) |

**Não existe meta de inscritos ou views nesta fase.** O `mapa-teste-publico.md` é explícito: a régua dos primeiros 8 vídeos é "eu ajudei alguém de verdade?", não volume. Aplicar meta de crescimento agora contradiz a decisão de 24/08.

### Onde este glossário se conecta

- **`mapa-teste-publico.md`** define a régua (o que medir e por quê) — este arquivo define o dado bruto por trás de cada sinal da régua
- **`/analyze-channel`** (skill, a criar quando o canal existir) lê o snapshot do worker e aplica esta régua
- **`workers/youtube-analytics.py`** (a criar) só grava número — nunca decide o que ele significa

---

## Instagram — placeholder

_A preencher quando priorizado. Métricas candidatas: alcance, contas engajadas, salvamentos (proxy de valor prático, coerente com o princípio "servir primeiro"), taxa de resposta em DM._

## LinkedIn — placeholder

_A preencher quando priorizado. Métricas candidatas: impressões, taxa de engajamento, cliques em perfil (proxy de autoridade B2B — relevante para P2/P3 de `mapa-teste-publico.md`)._

## Facebook — placeholder

_A preencher quando priorizado._

## TikTok — placeholder

_A preencher quando priorizado. Formato já coberto em parte por `creator-profile.md` (Reels/Shorts ~1min, CAM³+C)._

## X (Twitter) — placeholder

_A preencher quando priorizado._

## Google AdSense — placeholder

_A preencher quando priorizado. Só relevante após monetização do YouTube ativa (ver requisito acima) — provavelmente a última plataforma a ganhar worker próprio._

---

- **Última atualização:** 2026-08-25
- **Dono:** Pietro (Marketing)
