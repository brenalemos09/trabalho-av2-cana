import csv
from collections import defaultdict
from pathlib import Path

import matplotlib.pyplot as plt


PASTA_RESULTADOS = Path(__file__).parent.parent / "resultados"


def calcular_medias(nome_arquivo):
    tempos = defaultdict(list)

    caminho = PASTA_RESULTADOS / nome_arquivo

    with open(caminho, "r", encoding="utf-8") as arquivo:
        leitor = csv.DictReader(arquivo)

        for linha in leitor:
            algoritmo = linha["algoritmo"]
            tamanho = int(linha["tamanho"])
            tempo = float(linha["tempo_segundos"])

            tempos[(algoritmo, tamanho)].append(tempo)

    medias = defaultdict(list)

    for (algoritmo, tamanho), valores in tempos.items():
        media = sum(valores) / len(valores)
        medias[algoritmo].append((tamanho, media))

    for algoritmo in medias:
        medias[algoritmo].sort()

    return medias


def salvar_medias(nome_arquivo, medias):
    caminho = PASTA_RESULTADOS / nome_arquivo

    with open(caminho, "w", newline="", encoding="utf-8") as arquivo:
        escritor = csv.writer(arquivo)
        escritor.writerow(["algoritmo", "tamanho", "tempo_medio_segundos"])

        for algoritmo, valores in medias.items():
            for tamanho, media in valores:
                escritor.writerow([algoritmo, tamanho, media])


def criar_grafico(medias, titulo, nome_arquivo):
    plt.figure(figsize=(9, 6))

    for algoritmo, valores in medias.items():
        tamanhos = [valor[0] for valor in valores]
        tempos = [valor[1] for valor in valores]

        plt.plot(
            tamanhos,
            tempos,
            marker="o",
            label=algoritmo.replace("_", " ").title(),
        )

    plt.xlabel("Tamanho da entrada")
    plt.ylabel("Tempo médio (segundos)")
    plt.yscale("log")
    plt.title(titulo)
    plt.legend()
    plt.grid()
    plt.tight_layout()

    caminho = PASTA_RESULTADOS / nome_arquivo
    plt.savefig(caminho, dpi=300)
    plt.close()


def main():
    medias_subarranjo = calcular_medias(
        "tempos_subarranjo.csv"
    )

    medias_pontos = calcular_medias(
        "tempos_pontos.csv"
    )

    salvar_medias(
        "medias_subarranjo.csv",
        medias_subarranjo,
    )

    salvar_medias(
        "medias_pontos.csv",
        medias_pontos,
    )

    criar_grafico(
        medias_subarranjo,
        "Subarranjo Máximo - Tempo de Execução",
        "grafico_subarranjo.png",
    )

    criar_grafico(
        medias_pontos,
        "Par de Pontos Mais Próximos - Tempo de Execução",
        "grafico_pontos.png",
    )

    print("Médias e gráficos gerados com sucesso.")


if __name__ == "__main__":
    main()