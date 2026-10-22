import csv
import random
import time
from pathlib import Path

from subarranjo import forca_bruta, divisao_conquista, linear
from pontos_proximos import forca_bruta_pontos, divisao_conquista_pontos


REPETICOES = 5
TAMANHOS = [100, 200, 400, 800, 1600, 3200, 6400]


def medir(funcao, entrada):
    inicio = time.perf_counter()
    funcao(entrada)
    fim = time.perf_counter()

    return fim - inicio


def salvar_csv(nome, dados):
    pasta = Path(__file__).parent.parent / "resultados"
    pasta.mkdir(exist_ok=True)

    caminho = pasta / nome

    with open(caminho, "w", newline="", encoding="utf-8") as arquivo:
        escritor = csv.writer(arquivo)
        escritor.writerow(["algoritmo", "tamanho", "execucao", "tempo_segundos"])
        escritor.writerows(dados)


def medir_subarranjo():
    resultados = []

    algoritmos = [
        ("forca_bruta", forca_bruta),
        ("divisao_conquista", divisao_conquista),
        ("linear", linear),
    ]

    for tamanho in TAMANHOS:
        valores = [
            random.randint(-1000, 1000)
            for _ in range(tamanho)
        ]

        for nome, funcao in algoritmos:
            for execucao in range(1, REPETICOES + 1):
                tempo = medir(funcao, valores)

                resultados.append(
                    [nome, tamanho, execucao, tempo]
                )

        print(f"Subarranjo tamanho {tamanho}: concluido")

    salvar_csv("tempos_subarranjo.csv", resultados)


def medir_pontos():
    resultados = []

    algoritmos = [
        ("forca_bruta", forca_bruta_pontos),
        ("divisao_conquista", divisao_conquista_pontos),
    ]

    for tamanho in TAMANHOS:
        pontos = [
            (
                random.uniform(-10000, 10000),
                random.uniform(-10000, 10000),
            )
            for _ in range(tamanho)
        ]

        for nome, funcao in algoritmos:
            for execucao in range(1, REPETICOES + 1):
                tempo = medir(funcao, pontos)

                resultados.append(
                    [nome, tamanho, execucao, tempo]
                )

        print(f"Pontos tamanho {tamanho}: concluido")

    salvar_csv("tempos_pontos.csv", resultados)


def main():
    random.seed(42)

    medir_subarranjo()
    medir_pontos()

    print("\nMedicoes concluidas.")


if __name__ == "__main__":
    main()