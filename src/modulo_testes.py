"""Executa medições das versões v0 a v6 de Somas em Intervalos.

Uso:
    python modulo_testes.py

Selecione o cenário e a versão pelo menu interativo.
"""

import importlib.util
import random
import statistics
import time
from pathlib import Path

CENARIOS = (1_000, 2_000, 5_000, 10_433, 20_000, 30_000, 50_000, 100_000_00)
REPETICOES = 5
SEMENTE = 42
DIRETORIO = Path(__file__).resolve().parent


def selecionar_opcao(pergunta, minimo, maximo):
    while True:
        resposta = input(pergunta).strip()
        if resposta.isdigit() and minimo <= int(resposta) <= maximo:
            return int(resposta)
        print(f"Opção inválida. Escolha um número entre {minimo} e {maximo}.")


def carregar_funcao(versao):
    """Carrega def somas() do arquivo da versão escolhida."""
    caminho = DIRETORIO / f"soma_em_intervalos_v{versao}.py"
    if not caminho.is_file():
        raise FileNotFoundError(
            f"Arquivo não encontrado: {caminho.name}. "
            "Crie o arquivo da versão na mesma pasta do módulo de testes."
        )

    spec = importlib.util.spec_from_file_location(f"soma_em_intervalos_v{versao}", caminho)
    if spec is None or spec.loader is None:
        raise ImportError(f"Não foi possível carregar {caminho.name}.")

    modulo = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(modulo)
    funcao = getattr(modulo, "somas", None)
    if not callable(funcao):
        raise AttributeError(f"{caminho.name} precisa conter def somas(v, n, ini, fim, q, resp).")
    return funcao


def gerar_entrada(n, semente):
    """Usa n = q e intervalos que cobrem o vetor inteiro (pior caso da v0)."""
    gerador = random.Random(semente)
    vetor = [gerador.randint(-100, 100) for _ in range(n)]
    q = n
    inicios = [0] * q
    finais = [n - 1] * q
    return vetor, inicios, finais, q


def executar(cenario, versao, semente=SEMENTE):
    n = CENARIOS[cenario - 1]
    q = n

    if versao == 0 and n >= 5_000:
        print(
            f"\nAVISO: a v0 faz {n * q:,} verificações por execução, "
            f"e serão feitas {REPETICOES} repetições.\n"
            "Esse teste pode levar muito tempo em Python."
        )
        if input("Digite SIM para continuar: ").strip() != "SIM":
            print("Teste cancelado.")
            return

    algoritmo = carregar_funcao(versao)
    vetor, inicios, finais, q = gerar_entrada(n, semente)
    esperado = [sum(vetor)] * q  # Todas as consultas são [0, n - 1].

    print(f"\nVersão: v{versao} | Teste: {cenario} | n = {n:,} | q = {q:,}")
    print(f"Semente: {semente} | Repetições: {REPETICOES}")

    tempos = []
    for numero in range(1, REPETICOES + 1):
        respostas = [0] * q  # Preparação fora do cronômetro.
        inicio = time.perf_counter()
        algoritmo(vetor, n, inicios, finais, q, respostas)
        duracao = time.perf_counter() - inicio

        # Verificação fora do cronômetro; não substitui os 1.000 testes do trabalho.
        if respostas != esperado:
            raise AssertionError(
                f"A versão v{versao} produziu respostas incorretas na repetição {numero}."
            )

        tempos.append(duracao)
        print(f"Repetição {numero}: {duracao:.6f} s")

    mediana = statistics.median(tempos)
    print(f"\nMediana: {mediana:.6f} s")
    # Todas as consultas geradas cobrem [0, n - 1], portanto a soma é a mesma.
    print(f"Resultado da soma do intervalo [0, {n - 1}]: {respostas[0]}")


def main():
    print("Cenários de teste (n = q):")
    for indice, n in enumerate(CENARIOS, start=1):
        print(f"  {indice}. n = {n:,}".replace(",", "."))

    cenario = selecionar_opcao(
        f"\nSelecione o teste (1-{len(CENARIOS)}): ", 1, len(CENARIOS)
    )
    versao = selecionar_opcao("Selecione a versão (0-6): ", 0, 6)

    try:
        executar(cenario, versao)
    except (FileNotFoundError, ImportError, AttributeError, AssertionError) as erro:
        print(f"Erro: {erro}")
        raise SystemExit(1) from erro


if __name__ == "__main__":
    main()
