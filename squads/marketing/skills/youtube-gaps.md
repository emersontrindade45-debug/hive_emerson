# /youtube-gaps

Descoberta de **lacuna de conteúdo** no YouTube. Divisão responsável: **M2 · Intelligence**.

## O sinal que este worker persegue

> **Vídeo com muitas views em canal pequeno = demanda validada sem autoridade estabelecida.**

Se um canal de 300 inscritos faz 80k views, o algoritmo não empurrou por causa do canal — empurrou por causa do **tema**. Logo: **a procura existe, a oferta boa não.** Isso é lacuna explorável.

A métrica é a **razão views ÷ inscritos**:

| Ratio | Sinal | Leitura |
|---|---|---|
| ≥ 20x | 🔴 **LACUNA FORTE** | O tema carregou sozinho. Prioridade máxima de pauta |
| 5–20x | 🟠 **LACUNA MÉDIA** | Tema puxou além da base do canal |
| 1,5–5x | 🟡 ACIMA DA BASE | Boa performance, mas dentro do esperado |
| < 1,5x | ⚪ NORMAL | Alcance compatível com o canal — sem sinal |

## Diferença para `/update-youtube`

| | `/update-youtube` | `/youtube-gaps` |
|---|---|---|
| O que faz | **Vigia** canais conhecidos | **Prospecta** por termo |
| Pergunta | "o que meus referenciais publicaram?" | "que tema tem procura e não tem oferta boa?" |
| Saída | Técnica nova no playbook | Pauta candidata com demanda comprovada |

São complementares. Vigilância ensina **como fazer**; prospecção diz **sobre o que fazer**.

## When to use

- Antes de decidir a pauta do próximo vídeo
- Quando o backlog de ângulos esvaziar
- Mensalmente, como varredura de rotina
- `/youtube-gaps` explícito

## Inputs

- `--termos "a,b,c"` — termos avulsos
- `--termos-arquivo` — usa `squads/marketing/data/youtube-intel/termos.json` (10 termos mapeados aos 4 pilares)
- `--max N` — resultados por termo (default 20)
- `--meses N` — janela (default 18)
- `--min-ratio N` — corte do relatório (default 5)

---

## Steps

### Step 1 — Rodar a varredura

```bash
python _core/youtube-gaps.py --termos-arquivo squads/marketing/data/youtube-intel/termos.json --max 20
```

**Regra crítica:** sempre da raiz do repo. Nunca `cd` para subpasta — os hooks de sessão do HIVE quebram.

⏱️ ~1,5s por vídeo (throttle contra HTTP 429). 10 termos × 20 vídeos ≈ 8 min. Para teste rápido, use `--max 5`.

Saída: `squads/marketing/data/youtube-intel/gaps/YYYY-MM-DD.json`

### Step 2 — Ler os achados

Ordenados por ratio decrescente. Para cada LACUNA FORTE/MÉDIA, avaliar:

1. **Cabe no eixo do canal?** "IA aplicada a trabalho que já existe" (`creator-profile.md`). Ratio alto em tema fora do eixo é ruído, não oportunidade.
2. **Cabe em algum dos 4 pilares?** Se não cabe em nenhum, provavelmente não é nosso.
3. **Qual público (P1–P5)?** Ver `mapa-teste-publico.md`.
4. **O que o título promete?** É o formato da promessa que performou, não só o assunto.

### Step 3 — Ler a transcrição do vencedor

Para os 3 melhores achados, puxar a transcrição e ver **como** foi feito:

```bash
python _core/youtube-fetch-video.py <url> --dir squads/marketing/data/youtube-intel
```

Procurar: estrutura do hook, promessa do título vs. entrega, onde o vídeo é fraco. **O ponto fraco do vencedor é a nossa entrada** — se o vídeo de 80k views não mostra o que quebrou, é aí que a régua "sem hype" ganha.

### Step 4 — Converter em ângulo

Achado que passou no filtro vira ângulo novo em `foundation/mapa-teste-publico.md`, com:
- ratio e views de origem (a prova de que há demanda)
- pilar e público
- Hero/Hub/Help
- **o que faremos diferente** do vídeo que performou

### Step 5 — Registrar

Atualizar `memory/STATE.md`, prefixo `[M2]`, com: quantos termos varridos, quantas lacunas fortes, quais viraram ângulo.

---

## Limites conhecidos

- **Canal que oculta inscritos é descartado** — sem denominador não há razão. Perde-se alguns casos legítimos.
- **Ratio alto não garante que o tema seja bom pra você.** Vídeo viral fora do eixo continua fora do eixo. O filtro do Step 2 é obrigatório, não opcional.
- **Vídeo antigo acumula views.** A janela de 18 meses reduz, mas não elimina; comparar sempre com `upload_date`.
- **A busca do YouTube é personalizada e instável.** Duas rodadas do mesmo termo podem diferir. Tendência importa, não o número exato.
- **Não substitui `/update-youtube`.** Prospecção acha tema; vigilância ensina execução.
