#!/usr/bin/env python3
"""
Cliente da API do Neotriad para o HIVE.

Le a ChaveAPI do .env (nunca commitado), troca por um access_token e consulta
os endpoints. O token vale ~30 dias e fica cacheado em _core/.neotriad-token.json.

Uso como script:
    python _core/neotriad.py status      # resumo do dia: triade, tarefas, compromissos
    python _core/neotriad.py papeis      # lista os papeis
    python _core/neotriad.py hoje        # o que esta agendado para hoje

Uso como modulo:
    from neotriad import Neotriad
    api = Neotriad()
    tarefas = api.tarefas("2026-08-23", "2026-08-30")

DESCOBERTAS que a documentacao oficial NAO traz (testado em 2026-08-23):
  1. POST /token exige corpo form-urlencoded ("grant_type=password").
     A doc diz JSON — com JSON a API responde 400 unsupported_grant_type.
  2. Um User-Agent de navegador e obrigatorio: sem ele o Cloudflare
     devolve 403 (error code 1010) antes de a chave ser avaliada.
  3. As respostas vem como {"data": {"Quantidade": N, "<Recurso>": [...]}},
     nao como lista direta.

DESCOBERTAS DE ESCRITA (testado em 2026-08-27):
  4. POST/PUT/DELETE /api/tarefas operam em LOTE: o corpo e sempre uma LISTA,
     mesmo para uma tarefa so. A doc mostra os campos de UMA tarefa e nao diz
     isso; objeto solto devolve 400 "A lista de tarefas nao pode ser vazia".
  5. A resposta de escrita e por item:
     {"data": {"Itens": [{"Sucesso": bool, "id_tarefa": "...", "Mensagem": ...}]}}
     Um 201 no envelope NAO garante que todos os itens passaram — checar Sucesso.
  6. PAPEL so funciona no POST, e o formato e Papel:[{"id_papel": "<guid>"}]
     — LISTA DE OBJETOS, nao lista de GUIDs. Passar Papel:["<guid>"] e aceito
     com 201 e IGNORADO em silencio: a tarefa nasce sem papel e sem erro.
     No PUT nenhum formato funciona (objeto -> "Object must implement
     IConvertible"; escalar -> "Invalid cast from System.String to
     ICollection<Neotriad.Model.Papel>"). Consequencia pratica: para corrigir
     o papel de uma tarefa existente, recriar e apagar a antiga.
  7. NAO existe endpoint de METAS nem de PROJETOS na API — so tarefas,
     compromissos, papeis e categorias. O campo id_meta existe na tarefa, mas
     a meta em si so pode ser criada pela interface web.
"""

import io
import json
import os
import sys
import urllib.error
import urllib.parse
import urllib.request
from datetime import datetime, timedelta

REPO = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
ENV_FILE = os.path.join(REPO, ".env")
TOKEN_CACHE = os.path.join(REPO, "_core", ".neotriad-token.json")

# Sem isto o Cloudflare bloqueia com 403/1010.
USER_AGENT = (
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 "
    "(KHTML, like Gecko) Chrome/128.0 Safari/537.36"
)

TRIADE = {"I": "Importante", "U": "Urgente", "C": "Circunstancial"}


def ler_env():
    if not os.path.exists(ENV_FILE):
        raise SystemExit(
            "ERRO: .env nao encontrado. Copie .env.example para .env e "
            "preencha NEOTRIAD_CHAVE_API."
        )
    env = {}
    for linha in io.open(ENV_FILE, encoding="utf-8"):
        linha = linha.strip()
        if linha and not linha.startswith("#") and "=" in linha:
            chave, valor = linha.split("=", 1)
            env[chave.strip()] = valor.strip()
    return env


class Neotriad:
    def __init__(self):
        env = ler_env()
        self.chave = env.get("NEOTRIAD_CHAVE_API", "")
        self.base = env.get(
            "NEOTRIAD_BASE_URL", "https://apibeta.neotriad.com"
        ).rstrip("/")
        if not self.chave:
            raise SystemExit("ERRO: NEOTRIAD_CHAVE_API vazio no .env")
        self._token = None

    # -- autenticacao ------------------------------------------------------
    def _token_do_cache(self):
        if not os.path.exists(TOKEN_CACHE):
            return None
        try:
            dados = json.load(io.open(TOKEN_CACHE, encoding="utf-8"))
            expira = datetime.fromisoformat(dados["expira_em"])
            # margem de 1 dia para nao usar token quase vencido
            if expira - timedelta(days=1) > datetime.now():
                return dados["access_token"]
        except (OSError, json.JSONDecodeError, KeyError, ValueError):
            pass
        return None

    def token(self):
        if self._token:
            return self._token
        cacheado = self._token_do_cache()
        if cacheado:
            self._token = cacheado
            return cacheado

        # A doc diz JSON, mas a API so aceita form-urlencoded aqui.
        corpo = urllib.parse.urlencode({"grant_type": "password"}).encode()
        req = urllib.request.Request(self.base + "/token", method="POST", data=corpo)
        req.add_header("ChaveAPI", self.chave)
        req.add_header("Content-Type", "application/x-www-form-urlencoded")
        req.add_header("User-Agent", USER_AGENT)
        try:
            with urllib.request.urlopen(req, timeout=30) as resp:
                dados = json.loads(resp.read().decode())
        except urllib.error.HTTPError as exc:
            raise SystemExit(
                f"ERRO ao autenticar ({exc.code}): {exc.read().decode()[:200]}"
            )

        self._token = dados["access_token"]
        try:
            expira = datetime.now() + timedelta(seconds=int(dados["expires_in"]))
            json.dump(
                {"access_token": self._token, "expira_em": expira.isoformat()},
                io.open(TOKEN_CACHE, "w", encoding="utf-8"),
            )
        except (OSError, KeyError, ValueError):
            pass  # cache e otimizacao, nao requisito
        return self._token

    # -- chamadas ----------------------------------------------------------
    def _get(self, caminho, params=None):
        url = self.base + caminho
        if params:
            url += "?" + urllib.parse.urlencode(params)
        req = urllib.request.Request(url)
        req.add_header("Authorization", "Bearer " + self.token())
        req.add_header("User-Agent", USER_AGENT)
        req.add_header("Accept", "application/json")
        try:
            with urllib.request.urlopen(req, timeout=45) as resp:
                return json.loads(resp.read().decode())
        except urllib.error.HTTPError as exc:
            corpo = exc.read().decode()[:200]
            raise SystemExit(f"ERRO {exc.code} em {caminho}: {corpo}")

    def _post(self, caminho, corpo):
        """POST com corpo JSON. Escrita testada em 2026-08-27 (POST /api/tarefas)."""
        dados = json.dumps(corpo).encode("utf-8")
        req = urllib.request.Request(self.base + caminho, method="POST", data=dados)
        req.add_header("Authorization", "Bearer " + self.token())
        req.add_header("Content-Type", "application/json")
        req.add_header("User-Agent", USER_AGENT)
        req.add_header("Accept", "application/json")
        try:
            with urllib.request.urlopen(req, timeout=45) as resp:
                bruto = resp.read().decode()
                return json.loads(bruto) if bruto else {}
        except urllib.error.HTTPError as exc:
            raise SystemExit(
                f"ERRO {exc.code} em POST {caminho}: {exc.read().decode()[:300]}"
            )

    def criar_tarefa(self, nome, data_inicio, id_triade="I",
                     duracao_prevista=None, papeis=None, id_meta=None,
                     descricao=None):
        """Cria uma tarefa. Obrigatorios pela API: nome (<=255) e data_inicio."""
        corpo = {"nome": nome[:255], "data_inicio": data_inicio}
        if id_triade:
            corpo["id_triade"] = id_triade
        if duracao_prevista:
            corpo["duracao_prevista"] = duracao_prevista
        if papeis:
            # LISTA DE OBJETOS. Lista de GUIDs e ignorada em silencio (ver 6).
            corpo["Papel"] = [
                p if isinstance(p, dict) else {"id_papel": p} for p in papeis
            ]
        if id_meta:
            corpo["id_meta"] = id_meta
        if descricao:
            corpo["descricao"] = descricao
        return self.criar_tarefas([corpo])

    def criar_tarefas(self, tarefas):
        """POST /api/tarefas recebe uma LISTA, nunca um objeto solto.

        A doc oficial mostra os campos de UMA tarefa e nao diz isso; enviar o
        objeto direto devolve 400 "A lista de tarefas nao pode ser vazia".
        Resposta: {"data": {"Itens": [{"Sucesso": bool, "id_tarefa": ...}]}}
        """
        return self._post("/api/tarefas", list(tarefas))

    def excluir_tarefas(self, ids):
        """DELETE /api/tarefas?ids=<guid>,<guid>"""
        url = self.base + "/api/tarefas?" + urllib.parse.urlencode(
            {"ids": ",".join(ids)}
        )
        req = urllib.request.Request(url, method="DELETE")
        req.add_header("Authorization", "Bearer " + self.token())
        req.add_header("User-Agent", USER_AGENT)
        req.add_header("Accept", "application/json")
        try:
            with urllib.request.urlopen(req, timeout=45) as resp:
                bruto = resp.read().decode()
                return json.loads(bruto) if bruto else {}
        except urllib.error.HTTPError as exc:
            raise SystemExit(
                f"ERRO {exc.code} em DELETE /api/tarefas: {exc.read().decode()[:300]}"
            )

    @staticmethod
    def _itens(resposta, nome_recurso):
        """A API devolve {"data": {"Quantidade": N, "<Recurso>": [...]}}."""
        data = resposta.get("data") or {}
        return data.get(nome_recurso) or []

    def papeis(self):
        return self._itens(self._get("/api/papeis"), "Papeis")

    def categorias(self):
        return self._itens(self._get("/api/categorias"), "Categorias")

    def tarefas(self, inicio, termino):
        r = self._get("/api/tarefas", {"inicio": inicio, "termino": termino})
        return self._itens(r, "Tarefas")

    def compromissos(self, inicio, termino):
        r = self._get("/api/compromissos", {"inicio": inicio, "termino": termino})
        return self._itens(r, "Compromissos")


# -- relatorios -----------------------------------------------------------
def _distribuicao_triade(tarefas):
    """Conta tarefas e minutos por esfera da triade."""
    contagem = {"I": 0, "U": 0, "C": 0, "?": 0}
    minutos = {"I": 0, "U": 0, "C": 0, "?": 0}
    for t in tarefas:
        esfera = (t.get("id_triade") or "?").upper()
        if esfera not in contagem:
            esfera = "?"
        contagem[esfera] += 1
        minutos[esfera] += t.get("duracao_prevista") or 0
    return contagem, minutos


def cmd_status(api):
    hoje = datetime.now()
    ini = (hoje - timedelta(days=7)).strftime("%Y-%m-%d")
    fim = (hoje + timedelta(days=7)).strftime("%Y-%m-%d")
    tarefas = api.tarefas(ini, fim)
    contagem, minutos = _distribuicao_triade(tarefas)
    total = sum(contagem.values()) or 1
    total_min = sum(minutos.values()) or 1

    print(f"Neotriad — janela {ini} a {fim}")
    print(f"Tarefas: {len(tarefas)}")
    print()
    print("Distribuicao da Triade (alvo: 70% I / 20% U / 10% C)")
    alvo = {"I": 70, "U": 20, "C": 10, "?": 0}
    for esfera in ("I", "U", "C", "?"):
        if not contagem[esfera]:
            continue
        pct = contagem[esfera] * 100 / total
        pct_min = minutos[esfera] * 100 / total_min
        nome = TRIADE.get(esfera, "Sem classificacao")
        marca = ""
        if esfera in ("I", "U", "C"):
            delta = pct - alvo[esfera]
            marca = f" (alvo {alvo[esfera]}%, {delta:+.0f})"
        print(
            f"  {nome:18} {contagem[esfera]:4} tarefas  {pct:5.1f}%"
            f"  | {minutos[esfera]:6} min {pct_min:5.1f}%{marca}"
        )


def cmd_hoje(api):
    hoje = datetime.now().strftime("%Y-%m-%d")
    tarefas = api.tarefas(hoje, hoje)
    compromissos = api.compromissos(hoje, hoje)
    print(f"Hoje ({hoje})")
    print(f"\nTarefas: {len(tarefas)}")
    for t in tarefas[:20]:
        esfera = TRIADE.get((t.get("id_triade") or "?").upper(), "?")[:1]
        dur = t.get("duracao_prevista") or 0
        print(f"  [{esfera}] {(t.get('nome') or '')[:56]} ({dur}min)")
    print(f"\nCompromissos: {len(compromissos)}")
    for c in compromissos[:20]:
        print(f"  - {(c.get('nome') or '')[:56]}")


def cmd_papeis(api):
    papeis = api.papeis()
    print(f"Papeis: {len(papeis)}")
    for p in papeis:
        if p.get("lixeira"):
            continue
        ideal = p.get("minutos_ideal") or 0
        extra = f" (ideal {ideal}min)" if ideal else ""
        print(f"  - {p.get('nome')}{extra}")


def main():
    comando = sys.argv[1] if len(sys.argv) > 1 else "status"
    api = Neotriad()
    if comando == "status":
        cmd_status(api)
    elif comando == "hoje":
        cmd_hoje(api)
    elif comando == "papeis":
        cmd_papeis(api)
    else:
        print(f"comando desconhecido: {comando}")
        print("use: status | hoje | papeis")
        sys.exit(1)


if __name__ == "__main__":
    main()
