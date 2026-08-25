# Identidade visual do canal — como produzir

> Criado 2026-08-25. Canal: https://www.youtube.com/@emerson.impulsoia
> Direção estética decidida em `foundation/canal-identidade.md`. Aqui é execução.

---

## 1. Banner — `banner-canal.html`

**Como usar:** abrir o arquivo no Chrome → botão **"Exportar PNG 2560×1440"** → sobe em Studio → Personalização → Imagem de marca.

Se a exportação falhar (varia por navegador), o fallback está no próprio alerta: ocultar guias → `Ctrl+Shift+P` no Chrome → "Capture node screenshot".

**As guias tracejadas são referência de tela** — nunca entram no PNG.

### Por que assim
- **Área segura 1546×423 respeitada.** Fora dela o YouTube corta no celular, que é onde a maioria vê. Todo o texto está dentro.
- **Grafite + âmbar (`#16181D` / `#F2A03D`).** Fuga deliberada do azul-ciano-degradê que é o uniforme de canal de IA. Se o banner parece com os outros, contradiz o "sem hype" antes de qualquer palavra.
- **Sem robô, cérebro ou circuito.** `brand-voice.md`: concreto, não futurista.
- **Grade técnica discreta** sugere sistema/planilha — o trabalho real — não ficção científica.
- **Subtítulo cita o que quebrou.** É o diferencial declarado no `creator-profile.md`, e quase ninguém escreve isso num banner.

### Editar
Tudo em texto no HTML. Cores nas variáveis `:root` do topo. Frase principal no `<h1>`. Se trocar o texto, **confira que continua dentro da moldura tracejada laranja**.

---

## 2. Foto de perfil — 800×800px

**Não dá pra terceirizar: precisa ser você.** A autoridade do canal vem de "quem já fez" (`brand-voice.md`) — logo abstrato apaga exatamente isso.

### O teste que reprova a maioria das fotos boas
A foto aparece a **48×48 pixels** na maior parte das telas (comentário, lista de inscrições, sugestão). Antes de subir: reduza a imagem para o tamanho de uma unha do polegar e olhe.

**Se você não reconhece o rosto nesse tamanho, a foto está errada** — por mais bonita que esteja em tamanho cheio. Esse é o único critério que importa de verdade.

### Como tirar em 10 minutos com celular
1. **Luz:** de frente para uma janela, de dia. Nunca com a janela atrás — vira silhueta. Sem luz de teto direto (sombra sob os olhos).
2. **Fundo:** parede lisa, 1,5m atrás de você. Sem bagunça, sem porta, sem cama. Fundo neutro faz o rosto saltar a 48px.
3. **Câmera traseira**, não a frontal — mais nitidez. Celular apoiado, timer de 3s, na altura dos olhos.
4. **Enquadramento:** cabeça e ombros. Rosto ocupando ~60% do quadro. Corte acima do peito.
5. **Expressão:** neutra-confiante ou meio sorriso. Sorriso largo demais destoa do tom direto.
6. **Roupa:** cor lisa, sem estampa nem listra fina (cria ruído ao reduzir). Evitar branco puro e preto puro.
7. **Tire 20 fotos**, escolha depois. A primeira nunca é a boa.
8. **Recorte quadrado 800×800**, rosto centralizado, e **faça o teste dos 48px.**

### Não faça
- Foto de festa recortada — o corte aparece
- Óculos escuros, boné, ou terceiros no quadro
- Filtro pesado ou beleza automática — contradiz "sem hype"
- Logo no lugar do rosto
- Foto antiga que não parece mais com você — quem te encontra na reunião precisa reconhecer

---

## 3. Watermark — 150×150px, PNG com fundo transparente

Aparece sobreposto no canto do vídeo o tempo todo. Precisa funcionar **pequeno e monocromático**.

- Versão simplificada da marca: `II` ou `Impulso IA` em uma linha, âmbar `#F2A03D` ou branco
- **Nunca a foto de perfil** — vira borrão nesse tamanho
- Fundo obrigatoriamente transparente
- Opcional; se travar, pule. Não bloqueia publicar.

---

## Ordem

1. Banner (pronto, é só exportar) — **5 min**
2. Foto (tirar + testar 48px) — **15 min**
3. Watermark — opcional, depois

Foto e banner são o que dá ao canal cara de coisa séria antes do primeiro vídeo. Watermark é refino.
