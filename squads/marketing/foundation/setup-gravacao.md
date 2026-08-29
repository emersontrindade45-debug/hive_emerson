# Setup de Gravação — Câmera, Áudio, Luz, Tela

> Criado 27/08/2026. Cobre o que `youtube-channel-setup.md` não cobre: equipamento físico e software para gravar o vídeo 1 (e os seguintes) no quarto do Emerson, sem estrutura pré-existente. Divisão responsável: **M3 · Operações e Análise de Marketing** (setup técnico é escopo M3, ver `../CLAUDE.md`).
>
> **Contexto assumido:** celular Android intermediário/básico, orçamento pontual de R$150-300 (investimento único, fora do fluxo mensal — a folga de caixa da empresa é ~R$5,79/mês, ver `../../finance/memory/STATE.md`; isso é gasto de bolso do Emerson, não do caixa MEI). Ambiente: quarto, zero estrutura.
>
> **Atualizado 27/08/2026 — inventário real do Emerson:** já tem ring light e tripé de celular. **Falta comprar:** microfone (orçamento inteiro do kit sobra pra isso) e, se necessário, LEDs adicionais. **Pendências novas a resolver:** vazamento de áudio de gravação para os vizinhos, e parede de fundo do quarto malpintada/sem acabamento. Seções abaixo atualizadas para refletir isso.

---

## Por que "Diretor de Estúdio" não vira divisão nova

O Emerson sugeriu nomear isso como divisão de algum squad. Não cabe pelos 3 testes já definidos em `../../../CLAUDE.md` § "Condição para replicar a outros squads":

- **Teste 1 (Volume):** setup de gravação é 1 tarefa pontual (montar o ambiente uma vez), não um fluxo recorrente com múltiplos itens abertos
- **Teste 2 (Função distinta):** já existe função dona — M3 (Operações e Análise de Marketing) cobre "setup de canal" no próprio mapa de divisões
- **Teste 3 (Bloqueio independente):** não há um segundo motivo de bloqueio além de "ainda não foi montado"

Fica registrado como checklist dentro de M3, não como divisão nova. Revisar se, depois de vários vídeos, surgir uma frente contínua de produção (edição, motion, thumbnail em série) que justifique subdividir — não é o caso agora.

---

## 1. Celular — apps para melhorar imagem e áudio

Celular Android intermediário/básico grava pior que o hardware permite quando usa o app de câmera padrão em automático. Ganho maior vem de configuração e app, não de comprar celular novo.

### ⚠️ ATUALIZAÇÃO 29/08 — Emerson já usa FiLMiC Pro, não Open Camera

O Emerson informou que já usa o **FiLMiC Pro** e vai gravar pela **câmera frontal** (mais fácil manter contato visual com a lente, sendo iniciante). Isso substitui a recomendação de Open Camera abaixo — mantida só como alternativa gratuita caso o FiLMiC pareça complexo demais ou tenha custo que não valha.

**Sobre o FiLMiC Pro:**
- Controles manuais de foco, exposição, ISO, temperatura de cor, velocidade do obturador — mesmo propósito do Open Camera, mais completo
- Tem botão dedicado para **trocar entre câmera frontal e traseira**, inclusive mapeável em atalho personalizado
- ⚠️ **Ressalva real:** câmera frontal de celular de entrada (Moto E7) tem menos sensor e menos controle exposto que a traseira — é limitação de hardware, não do app. Os controles manuais aparecem na tela, mas o efeito prático pode ser mais limitado do que seria na câmera traseira.
- ⚠️ **Gravando pela frontal, a checagem de foco/exposição do `teste-gravacao-30s.md` vale ainda mais** — é onde a limitação de hardware mais aparece

**Configuração mínima (vale para qualquer app de câmera manual, inclusive FiLMiC):**
- Resolução 1080p a 30fps (não 4K — pesado demais pro Moto E7 processar)
- Travar foco manual no rosto antes de falar
- Lente limpa

### App de câmera — alternativa gratuita (Open Camera)
**Open Camera** (grátis, Android, sem anúncio, open source) — permite travar foco e exposição manualmente, o que o app padrão da maioria das marcas intermediárias não deixa fazer direito. Trava o problema mais comum de celular básico: a câmera "respira" (muda exposição sozinha) toda vez que algo se move no fundo.

**Configuração mínima antes de gravar:**
- Resolução: 1080p a 30fps (não usar 4K — arquivo pesado demais pro celular processar e pro upload, sem ganho real de qualidade percebida no YouTube)
- Travar foco manual no rosto antes de começar a falar
- Limpar a lente com pano (poeira/gordura na lente do celular é a causa nº1 de imagem "borrada" em vídeo amador — mais barato que qualquer software)

### App de áudio (gravação separada, depois sincroniza)
Áudio de celular gravado junto com o vídeo é sempre pior que áudio gravado separado e sincronizado depois — é a maior diferença perceptível entre "vídeo caseiro" e "vídeo profissional", mais que a câmera.

**Se comprar microfone de lapela (ver seção física abaixo):** grava direto no celular via cabo P2/USB-C, sem app extra.

**⚠️ Se decidir gravar SEM comprar microfone algum (nem lapela, nem segundo celular) — limite real, não hipotético (29/08):**

Não existe app que resolva isso de verdade. Cancelamento de ruído "em tempo real" de app genérico funciona por dois métodos, e nenhum dos dois substitui microfone físico perto da boca:

1. **Onda inversa (ativo):** o app escuta o ruído de fundo e gera uma onda oposta para cancelar — é a mesma técnica de fone com ANC. Em gravação de voz falada, isso **distorce a própria voz** junto com o ruído, porque os dois estão na mesma faixa de frequência (voz humana). Funciona bem para ruído constante e grave (ventilador, ar-condicionado); funciona mal para o que mais atrapalha aqui, que é ruído de rua/vizinho.
2. **Filtro de frequência (passivo):** corta faixas onde normalmente não tem voz. Ajuda um pouco, mas é o mesmo processamento que qualquer editor de vídeo (inclusive gratuito) já faz DEPOIS de gravado — rodar em tempo real no Moto E7 (Helio G25, 2-4GB RAM) ainda arrisca travar a gravação.

**Recomendação honesta: não usar app de cancelamento de ruído durante a captura.** Gravar o áudio o mais limpo possível na fonte (as 5 medidas grátis do §1.5 — janela fechada, cobertor, tom de voz normal, horário) e, se sobrar ruído, tratar DEPOIS na edição (CapCut, gratuito, tem redução de ruído em pós — mas isso é edição, não captura). Aplicar redução de ruído ao vivo raramente ajuda mais do que atrapalha, e é conselho recorrente até entre quem já usa microfone dedicado.

**O único ganho real de app, sem comprar nada:** o app nativo de gravador de voz do Android (ou "Diretor de Som") gravando em modo avião, o mais perto possível da boca, como fonte de áudio separada — que é a opção "sem microfone dedicado" já registrada acima. Não é um app "melhorando" o microfone do celular; é usar o próprio celular COMO microfone, posicionado direito. É esse posicionamento — 30-40cm da boca — que faz toda a diferença, não o app.

**Se ainda não tiver microfone dedicado:** usar um segundo celular (ou o próprio, em modo avião pra não ter interrupção) só para gravar áudio, o mais perto possível da boca (30-40cm), com o app **Diretor de Som** ou o gravador de voz nativo do Android em qualidade alta — depois sincronizar no editor batendo a palma no início da gravação (marca visual e sonora clara pro corte).

---

## 1.5 Vazamento de áudio para os vizinhos

Importante separar dois problemas diferentes, porque as soluções são opostas:

- **Isolamento acústico** (bloquear som de entrar/sair) — caro: lã de rocha, drywall, porta maciça com vedação. É o que resolve "vizinho com música alta incomoda meu quarto".
- **O seu caso é o oposto e mais simples de resolver:** você está *falando* (não tocando instrumento ou ouvindo música alta) e o problema é o **volume da sua própria voz** se propagando, provavelmente por uma janela ou parede fina. Isso não exige obra.

**O que resolve, do mais barato ao mais efetivo:**

1. **Gravar com a janela fechada** (se ainda gravar com ela aberta) — sozinho já reduz bastante a propagação direta pra rua/vizinho lateral.
2. **Cobrir a janela com um cobertor ou edredom pesado durante a gravação** — absorve parte do som que sairia pelo vidro, é a técnica caseira mais usada por quem grava podcast/vídeo em apartamento. Custo zero, só usar o que já tem em casa.
3. **Não gritar/projetar a voz como se estivesse em auditório** — grave com o microfone de lapela perto da boca (30-40cm) e fale em tom de conversa normal. Isso sozinho já reduz o volume de saída porque você para de compensar a falta de microfone bom projetando mais a voz.
4. **Horário:** gravar em horário em que barulho ambiente da rua/vizinhança já é mais alto (fim de tarde/início da noite em dia de semana) camufla melhor do que gravar de madrugada ou cedo demais, quando o silêncio ao redor faz sua voz destacar mais.
5. **Se depois de tudo isso ainda incomodar:** um painel de espuma acústica fina colado na parede que dá para a casa do vizinho (não a sala toda, só essa parede) já ajuda bastante e é relativamente barato (kits de espuma piramidal a partir de ~R$80-150 por poucos m²) — mas só vale investir nisso depois de testar as 4 medidas grátis acima, porque provavelmente já resolvem.

**Não é prioridade de compra agora** — nenhuma dessas 5 medidas exige o orçamento de R$150-300, que fica inteiro para o microfone.

---

## 2. Iluminação — já tem ring light + tripé, falta só usar certo

Emerson já tem ring light e tripé de celular (27/08) — não precisa comprar nada de luz agora. O que falta é posicionamento correto, que é o que separa "tenho ring light" de "uso o ring light direito".

### Como usar o que já existe

1. **Ring light na frente, não do lado** — luz de anel fica de frente pro rosto, na altura dos olhos ou levemente acima, a ~50-80cm de distância. Erro comum é deixar muito perto (estoura a imagem, "lava" o rosto) ou de lado (perde o efeito de preenchimento uniforme que é a vantagem do ring light).
2. **Combinar com luz natural, não substituir** — se o quarto tem janela, posicionar de forma que a luz natural venha de um ângulo (lateral, ~45°) e o ring light complemente de frente. Ring light sozinho num quarto totalmente escuro cria uma luz achatada, sem profundidade no rosto.
3. **Testar a temperatura de cor do ring light** (a maioria tem ajuste quente/neutro/frio + dimmer de intensidade) — combinar com o horário: luz mais neutra/fria durante o dia (combina com luz de janela), mais quente à noite (combina com lâmpada do quarto, evita choque de cor entre as duas fontes).
4. **Rebatedor caseiro ainda vale (R$0):** cartolina branca, isopor ou lençol claro do lado oposto ao ring light, pra suavizar sombra do outro lado do rosto — mesmo com ring light, ainda ajuda.

**Se depois de testar isso a luz ainda ficar ruim:** aí sim considerar 1 painel LED simples adicional como preenchimento lateral — mas testar o que já existe primeiro, provavelmente resolve.

---

## 2.5 Parede de fundo malpintada

Parede com pintura ruim atrás de quem fala é um dos detalhes que mais denuncia "produção amadora" em vídeo, mas resolver não exige pintar a parede de novo.

**Opções sem reforma, do mais simples ao mais trabalhoso:**

1. **Desfoque de fundo (mais simples, R$0):** se a câmera do celular tiver modo retrato/desfoque de fundo (a maioria dos intermediários recentes tem), usar isso já borra a imperfeição da parede sem precisar cobrir nada. Testar se o app de câmera (Open Camera não tem esse recurso — usar o app nativo do celular só para esse teste, ou verificar se há modo retrato em vídeo) preserva nitidez no rosto.
2. **Enquadrar mais fechado (R$0):** aproximar o enquadramento no rosto/tronco (plano médio) em vez de plano aberto — quanto menos parede aparece no quadro, menos o problema chama atenção. Reforça também a regra de "carga cognitiva" do playbook (imagem mais simples de processar).
3. **Cobrir com tecido/pano liso (R$0-30):** um pano ou cortina lisa (cor neutra — cinza, bege, verde escuro) pendurado atrás, cobrindo só a área que entra no enquadramento. Não precisa cobrir a parede inteira, só o retângulo que a câmera captura.
4. **Fundo temático simples (baixo custo):** uma prateleira com poucos itens (livro, planta, luminária) posicionada para tampar parcialmente a parede e dar profundidade — efeito comum em canal de "estúdio caseiro" sem custo de painel.

**Não é prioridade de compra do kit de R$150-300** — as opções 1-3 resolvem com o que já existe em casa ou gasto simbólico. Deixar pintura de parede como melhoria de médio prazo, não bloqueio para gravar o vídeo 1.

---

## 3. Gravação de tela do computador

O roteiro do vídeo 1 (`data/roteiros/video-01-resposta-ruim.md`) tem um bloco de Demonstração (5:30-7:00) que exige gravação de tela.

**Recomendado: OBS Studio** (grátis, open source, Windows/Mac/Linux) — é o que a maioria dos criadores de tutorial usa. Grava tela inteira ou janela específica, permite adicionar webcam em overlay (canto da tela) simultaneamente, e grava áudio do sistema + microfone juntos com controle de volume separado.

**Configuração mínima para o vídeo 1:**
- Cena com "Captura de Janela" (só o navegador/app que está demonstrando, não a área de trabalho inteira — evita mostrar notificação, ícone pessoal etc.)
- Gravar em MP4 direto (evita ter que converter depois)
- Testar 10 segundos antes de gravar de verdade — erro comum é gravar 5 minutos e descobrir que o áudio não foi capturado

**Alternativa mais simples, se OBS parecer complexo de início:** gravador de tela nativo do Windows (Xbox Game Bar, `Win+G`) — mais limitado, mas resolve uma demonstração simples de navegador sem curva de aprendizado.

---

## Checklist de montagem (uma vez só, antes de gravar o vídeo 1)

- [ ] Instalar Open Camera no celular, testar foco/exposição manual
- [ ] Comprar microfone de lapela (ver kit de compra abaixo)
- [ ] Testar 4 medidas grátis contra vazamento de áudio (janela fechada, cobertor na janela, falar em tom normal perto do microfone, horário de gravação) — ver seção 1.5
- [ ] Posicionar ring light de frente ao rosto, ~50-80cm, testar temperatura de cor contra a luz natural do quarto
- [ ] Testar modo retrato/desfoque de fundo do celular OU enquadrar mais fechado para disfarçar a parede malpintada — ver seção 2.5
- [ ] Improvisar rebatedor (cartolina/isopor/lençol branco) do lado oposto ao ring light
- [ ] Instalar OBS Studio no computador, configurar cena de captura de janela, testar 10s de gravação com áudio
- [ ] Gravar teste de 30s completo (câmera + áudio + luz + enquadramento da parede) antes de gravar o vídeo 1 de verdade — conferir tudo junto, não peça por peça

---

## Kit de compra — só falta o microfone

Ring light e tripé já existem (27/08). Orçamento de R$150-300 fica inteiro para o microfone — dá pra comprar uma opção bem melhor que o mínimo.

| Item | Faixa de preço | Nota |
|---|---|---|
| Microfone de lapela com fio (P2 ou USB-C, conforme entrada do celular) | R$40-90 | Resolve o essencial |
| Microfone de lapela sem fio (par transmissor+receptor, tipo os populares de clipe duplo) | R$120-250 | Mais liberdade de movimento, qualidade mais consistente, ainda cabe no orçamento |

**Recomendação:** com o orçamento sobrando, vale considerar o modelo sem fio em vez do com fio — folga de R$150-300 inteira permite um microfone de lapela sem fio de entrada, que evita o cabo enroscando e tem captação mais uniforme. Se sobrar depois da compra do microfone, guardar o restante em vez de gastar em LED adicional — a luz que já existe (ring light) resolve, testado antes de comprar mais.
