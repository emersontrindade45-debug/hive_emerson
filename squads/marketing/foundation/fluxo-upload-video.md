# Fluxo de upload automático — celular → nuvem → edição

> **Divisão:** `[M3]` Operações e Análise de Marketing · **Squad:** Marketing (Pietro)
> **Criado:** 2026-08-29 · **Complementa:** `setup-gravacao.md` (câmera/áudio/luz) — este arquivo cobre o que acontece **depois** de gravar: como o vídeo sai do celular e chega pronto no computador para editar.
> **Contexto confirmado com o Emerson (29/08):** edição no computador · Google Drive já é a conta usada · Wi-Fi de casa bom · conta Google com espaço.

---

## O fluxo

```
Celular grava (FiLMiC Pro)
        │
        ▼
App "Google Drive" no Android — upload automático da pasta de vídeo
        │  (sobe sozinho quando conectado no Wi-Fi)
        ▼
Google Drive na nuvem — pasta "Vídeos Brutos"
        │
        ▼
Google Drive para Computador (instalado no PC, modo Espelhamento)
        │  (sincroniza a pasta pro HD automaticamente)
        ▼
Pasta aparece no Windows Explorer, pronta pra abrir no editor
```

**O gatilho é passivo:** gravar → celular pega Wi-Fi de casa → sobe sozinho → PC ligado com Drive rodando puxa automaticamente → arquivo pronto na pasta local. Nenhuma ação manual de "exportar" ou "transferir" no meio.

---

## ⚠️ Por que Google Drive, não Google Fotos

**Google Fotos comprime por padrão.** Mesmo a opção "Alta Qualidade" reprocessa o arquivo (limita a 1080p, que já é a resolução de gravação definida em `setup-gravacao.md` — então tecnicamente não perderia resolução, mas ainda reprocessa/recodifica o vídeo).

**Google Drive não comprime nada** — sobe o arquivo bruto exatamente como o FiLMiC Pro gravou. Para editar, arquivo intacto é o que importa: perda de qualidade em recompressão se acumula a cada etapa (grava → comprime no upload → editor recomprime ao exportar → YouTube recomprime de novo).

⚠️ **Não confundir os dois apps do Google** — "Google Fotos" e "Google Drive" são apps diferentes no Android, mesmo que ambos façam backup de mídia. Configurar o backup automático **no app Google Drive**, não no Google Fotos.

---

## Configuração — 3 partes

### 1. No celular — upload automático
1. Abrir o app **Google Drive** (Android)
2. Configurações → **Fazer upload automático de fotos e vídeos** (ou "Backup")
3. Selecionar a pasta onde o **FiLMiC Pro salva os vídeos** — conferir em FiLMiC Pro → Configurações → local de gravação (geralmente `DCIM/FiLMiC Pro` ou pasta customizada)
4. Ativar **"somente Wi-Fi"** — vídeo de 1-3GB por rede móvel é lento e consome franquia de dados

### 2. No computador — sincronização automática
1. Instalar **Google Drive para Computador** ([drive.google.com/drive/download](https://drive.google.com/drive/download))
2. Configurar em **modo Espelhamento (Mirror)**, não Streaming
   - ⚠️ **Streaming** deixa o arquivo "na nuvem, baixa sob demanda" — problemático para editor de vídeo, que precisa do arquivo físico local para não travar durante a edição
   - **Espelhamento** salva cópia real no HD, sempre disponível offline
3. Escolher a pasta "Vídeos Brutos" do Drive para sincronizar localmente

### 3. Organização da pasta (recomendado, não obrigatório)
Criar a pasta **"Vídeos Brutos"** no Drive antes de gravar o vídeo 1, para não misturar com outros arquivos do Drive pessoal. Nomear por vídeo: `video-01-resposta-ruim/` com os arquivos de câmera + áudio separado (se estiver usando gravação de áudio separada, ver `setup-gravacao.md` §1).

---

## Riscos e limites reais (não hipotéticos)

| Risco | Detalhe | Mitigação |
|---|---|---|
| **Espaço na conta Google** | ✅ Confirmado 29/08: conta paga/quase cheia, com folga | Nenhuma ação agora — revisar se começar a acumular muitos vídeos brutos sem apagar |
| **Vídeo de 7-8min em 1080p pesa 1-3GB** | Upload e download consomem tempo e banda a cada vídeo | ✅ Confirmado: Wi-Fi de casa bom, upload automático viável |
| **PC precisa estar ligado e com Drive aberto** | Se o PC estiver desligado, a sincronização só completa quando ligar de novo | Não é bloqueio — só significa que "pronto para editar" depende de ligar o PC, não é instantâneo se ele estiver desligado |
| **Modo Streaming vs Espelhamento trocado por engano** | Se mudar de Espelhamento pra Streaming depois com arquivos não sincronizados, risco de perda | Configurar Espelhamento desde o início e não mexer nisso sem necessidade |

---

## Teste antes de contar com o fluxo no vídeo 1

Gravar um clipe de teste curto (os mesmos 30s do `teste-gravacao-30s.md` servem) e conferir:
1. Subiu sozinho no Drive do celular sem precisar abrir o app manualmente
2. Apareceu na pasta do Drive no PC sem precisar apertar "sincronizar agora"
3. O arquivo abre normalmente no editor de vídeo escolhido

Só depois desse teste passar, contar com o fluxo automático para o vídeo 1 de verdade.
