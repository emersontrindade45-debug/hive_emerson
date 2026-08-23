# /update-youtube

Inteligência semanal de crescimento no YouTube. Raspa os canais monitorados, lê as transcrições e devolve o que mudou + o que aplicar.

## When to use

- Update semanal ("o que rolou no YouTube essa semana")
- Antes de escrever um roteiro — o playbook acumulado é insumo direto
- `/update-youtube` explícito

## Inputs

- `--days N`: janela de coleta (default 7)
- `--max N`: máximo de vídeos por canal (default 10)
- `--skip-collect`: pula a raspagem, analisa só o que já está em cache

---

## Steps

### Step 1 — Coletar

```bash
python squads/marketing/data/youtube-intel/collect.py --days 7
```

**Regra crítica:** sempre caminho absoluto ou relativo à raiz do projeto. Nunca `cd` para a subpasta — os hooks de sessão do HIVE resolvem caminho relativo ao cwd e quebram.

O script tem cache: vídeo já baixado não é rebaixado. Roda em ~15s por vídeo novo (throttle de 2,5s contra HTTP 429).

Se a saída indicar `transcript_status` diferente de `ok`, registre quais vídeos ficaram sem transcrição — a análise abaixo vale só para os que têm.

### Step 2 — Ler as transcrições novas

Leia os `.json` em `squads/marketing/data/youtube-intel/transcripts/` cujo `collected_at` seja desta rodada. Cada arquivo tem `title`, `upload_date`, `view_count`, `description` e `transcript` (texto corrido).

Priorize por `view_count` quando houver muitos: o que performou indica o que a audiência deles quis.

### Step 3 — Produzir o relatório (4 blocos)

Grave em `squads/marketing/data/youtube-intel/reports/YYYY-MM-DD.md`.

Regra de ouro para os quatro blocos: **cite o vídeo de origem em cada afirmação** (título + link). Se os canais não falaram de algo, o bloco fica vazio — escreva "nada novo esta semana". Nunca preencha com conhecimento geral seu sobre YouTube; o valor aqui é ser o que *aqueles* canais disseram.

#### Bloco 1 — Update do algoritmo
O que mudou no YouTube, em bullets. Para cada item: o que mudou, a partir de quando, e o efeito prático. Descarte hype sem substância — se o vídeo só especula, marque como especulação.

#### Bloco 2 — Playbook de roteiro
Técnicas concretas de hook, retenção e estrutura. Só entra o que for **acionável**: "primeiros 30s devem entregar o conflito" entra; "faça conteúdo de qualidade" não entra.

Acumule em `squads/marketing/foundation/youtube-playbook.md` — este arquivo é a base de conhecimento permanente, consultada quando formos escrever um vídeo. Não duplique técnica já registrada; se o novo vídeo refina algo existente, edite a entrada em vez de criar outra.

#### Bloco 3 — Canal como negócio
Monetização, posicionamento, funil, precificação. Separado das técnicas de produção de propósito — é a camada de negócio.

#### Bloco 4 — Ideias de vídeo para o Emerson
Cruze o que os canais falaram com o contexto dele (agência, pré-receita). Leia antes `foundation/icp-audience.md` e `foundation/brand-voice.md`.

Cada ideia precisa de: título provisório, ângulo, e qual insight desta semana a originou. Aplique o teste do `/content-ideas`: se 100 canais pudessem publicar a mesma ideia sem mudar nada além do nome, descarte.

### Step 4 — Propagar

- Atualize `[L1]` em `squads/marketing/memory/STATE.md` com a data do último update e o titular da semana
- Se algo for urgente (mudança de algoritmo que afeta publicação em curso), diga na resposta em vez de só gravar no arquivo

---

## Output

Resposta no chat: máximo 3 parágrafos curtos ou uma tabela. O relatório completo fica no arquivo — não despeje ele inteiro no chat.

Abra sempre pelo que **muda a ação desta semana**. Se nada muda, diga isso na primeira linha.

---

## Gotchas

- `--extractor-args youtube:lang=pt` é obrigatório: sem isso o YouTube devolve títulos auto-traduzidos para inglês
- A legenda correta é `pt-orig` (idioma original). Pedir várias variantes de uma vez dispara HTTP 429
- `-J` do yt-dlp suprime a escrita de arquivos de legenda — por isso `collect.py` faz duas chamadas separadas
- Console do Windows é cp1252 e quebra com emoji nos títulos: todo I/O usa UTF-8 explícito
