import os
import time
import uuid
import random
import requests
from datetime import datetime, timezone
from dotenv import load_dotenv

load_dotenv()

SUPABASE_URL = os.getenv("SUPABASE_URL", "").rstrip("/")
SUPABASE_KEY = os.getenv("SUPABASE_KEY", "")
JOGO_NOME = os.getenv("JOGO_NOME", "Show do Milhão Python")
PREMIOS = [1000, 5000, 10000, 25000, 50000, 100000, 200000, 500000, 1000000]
ORDEM = ["facil"] * 3 + ["media"] * 3 + ["dificil"] * 3
HEADERS = {
    "apikey": SUPABASE_KEY,
    "Authorization": f"Bearer {SUPABASE_KEY}",
    "Content-Type": "application/json",
    "Prefer": "return=representation",
}

def configurado():
    return bool(SUPABASE_URL and SUPABASE_KEY)

def requisicao(method, tabela, **kwargs):
    if not configurado():
        raise RuntimeError("Configure SUPABASE_URL e SUPABASE_KEY no arquivo .env.")
    url = f"{SUPABASE_URL}/rest/v1/{tabela}"
    resposta = requests.request(method, url, headers=HEADERS, timeout=15, **kwargs)
    resposta.raise_for_status()
    return resposta.json() if resposta.text.strip() else []

def obter_jogo_id():
    jogos = requisicao("GET", "jogos", params={"nome": f"eq.{JOGO_NOME}", "select": "id"})
    if jogos:
        return jogos[0]["id"]
    criado = requisicao("POST", "jogos", json={"nome": JOGO_NOME})
    return criado[0]["id"]

def buscar_perguntas(dificuldade):
    return requisicao("GET", "perguntas", params={
        "select": "id,enunciado,alternativa_a,alternativa_b,alternativa_c,alternativa_d,correta,dificuldade",
        "dificuldade": f"eq.{dificuldade}"
    })

def calcular_premio(acertos):
    return PREMIOS[acertos - 1] if acertos else 0

def jogar():
    apelido = input("Digite seu apelido: ").strip()
    while not apelido:
        print("O apelido não pode ficar vazio.")
        apelido = input("Digite seu apelido: ").strip()

    try:
        perguntas = []
        for nivel in ("facil", "media", "dificil"):
            disponiveis = buscar_perguntas(nivel)
            if len(disponiveis) < 3:
                print(f"Banco insuficiente: são necessárias 3 perguntas {nivel}.")
                return
            perguntas.extend(random.sample(disponiveis, 3))
    except Exception as erro:
        print(f"Não foi possível consultar as perguntas: {erro}")
        return

    partida_id = str(uuid.uuid4())
    acertos = 0
    premio = 0
    motivo = "concluida"
    inicio = time.perf_counter()

    print("\n=== SHOW DO MILHÃO ===")
    for indice, pergunta in enumerate(perguntas):
        print(f"\nPergunta {indice + 1}/9 | Prêmio em jogo: R$ {PREMIOS[indice]:,.2f}")
        print(pergunta["enunciado"])
        for letra in "abcd":
            print(f"  {letra.upper()}) {pergunta['alternativa_' + letra]}")
        while True:
            resposta = input("Sua resposta (A/B/C/D) ou S para sair: ").strip().lower()
            if resposta in ("a", "b", "c", "d", "s"):
                break
            print("Entrada inválida. Digite A, B, C, D ou S.")
        if resposta == "s":
            motivo = "desistencia"
            break
        if resposta != pergunta["correta"].lower():
            motivo = "erro"
            print(f"Resposta incorreta. A correta era {pergunta['correta'].upper()}.")
            break
        acertos += 1
        premio = calcular_premio(acertos)
        print(f"Correto! Prêmio atual: R$ {premio:,.2f}")
    else:
        motivo = "nove_acertos"

    duracao = round(time.perf_counter() - inicio, 2)
    print(f"\nFim da partida! {apelido}, você ganhou R$ {premio:,.2f}.")
    print(f"Acertos: {acertos} | Tempo: {duracao:.2f} segundos | Motivo: {motivo}")

    resultado = {
        "id": partida_id,
        "jogo_id": obter_jogo_id(),
        "apelido": apelido,
        "valor_ganho": premio,
        "tempo_segundos": duracao,
        "acertos": acertos,
        "motivo_encerramento": motivo,
        "data_hora": datetime.now(timezone.utc).isoformat()
    }
    salvar_com_retentativa(resultado)

def salvar_com_retentativa(resultado):
    while True:
        try:
            requisicao("POST", "partidas", json=resultado)
            print("Resultado salvo no banco online.")
            return
        except Exception as erro:
            print(f"Falha ao salvar (o resultado continua guardado nesta execução): {erro}")
            tentar = input("Tentar novamente? (S/N): ").strip().lower()
            if tentar != "s":
                print("Resultado não foi enviado. Anote o ID para referência:", resultado["id"])
                return

def consultar_ranking():
    try:
        jogos = requisicao("GET", "jogos", params={"select": "id,nome", "order": "nome"})
        if not jogos:
            print("Ainda não há jogos cadastrados.")
            return
        for i, jogo in enumerate(jogos, 1):
            print(f"{i}. {jogo['nome']}")
        escolha = input("Escolha o número do jogo: ").strip()
        if not escolha.isdigit() or not 1 <= int(escolha) <= len(jogos):
            print("Opção inválida.")
            return
        jogo_id = jogos[int(escolha)-1]["id"]
        partidas = requisicao("GET", "partidas", params={
            "select": "*", "jogo_id": f"eq.{jogo_id}", "order": "valor_ganho.desc,tempo_segundos.asc,data_hora.asc,id.asc"
        })
        melhores = {}
        for p in partidas:
            chave = p["apelido"].casefold()
            if chave not in melhores:
                melhores[chave] = p
        print("\n=== RANKING ===")
        for pos, p in enumerate(list(melhores.values())[:10], 1):
            print(f"{pos:2}. {p['apelido']} — R$ {p['valor_ganho']:,.2f} — {p['tempo_segundos']}s")
    except Exception as erro:
        print(f"Falha ao consultar ranking: {erro}")

def main():
    while True:
        print("\n1 - Iniciar partida\n2 - Consultar ranking\n3 - Sair")
        opcao = input("Escolha: ").strip()
        if opcao == "1":
            jogar()
        elif opcao == "2":
            consultar_ranking()
        elif opcao == "3":
            print("Até mais!")
            break
        else:
            print("Opção inválida.")

if __name__ == "__main__":
    main()
