import random
import time

from pontos_proximos import distancia


def forca_bruta_local(pontos):
    menor = float("inf")

    for i in range(len(pontos)):
        for j in range(i + 1, len(pontos)):
            atual = distancia(pontos[i], pontos[j])

            if atual < menor:
                menor = atual

    return menor


def dividir(pontos_x, pontos_y, limiar):
    if len(pontos_x) <= limiar:
        return forca_bruta_local(pontos_x)

    meio = len(pontos_x) // 2
    esquerda_x = pontos_x[:meio]
    direita_x = pontos_x[meio:]

    limite_x = pontos_x[meio][0]
    pontos_esquerda = set(esquerda_x)

    esquerda_y = []
    direita_y = []

    for ponto in pontos_y:
        if ponto in pontos_esquerda:
            esquerda_y.append(ponto)
        else:
            direita_y.append(ponto)

    menor = min(
        dividir(esquerda_x, esquerda_y, limiar),
        dividir(direita_x, direita_y, limiar),
    )

    faixa = [
        ponto
        for ponto in pontos_y
        if abs(ponto[0] - limite_x) < menor
    ]

    for i in range(len(faixa)):
        for j in range(i + 1, min(i + 8, len(faixa))):
            menor = min(menor, distancia(faixa[i], faixa[j]))

    return menor


def executar(pontos, limiar):
    pontos_x = sorted(pontos, key=lambda p: (p[0], p[1]))
    pontos_y = sorted(pontos, key=lambda p: (p[1], p[0]))

    return dividir(pontos_x, pontos_y, limiar)


def main():
    random.seed(42)

    pontos = [
        (
            random.uniform(-10000, 10000),
            random.uniform(-10000, 10000),
        )
        for _ in range(6400)
    ]

    limiares = [3, 5, 10, 20, 50]
    repeticoes = 5

    for limiar in limiares:
        tempos = []

        for _ in range(repeticoes):
            inicio = time.perf_counter()
            executar(pontos, limiar)
            fim = time.perf_counter()

            tempos.append(fim - inicio)

        media = sum(tempos) / len(tempos)

        print(
            f"Limiar {limiar}: "
            f"{media:.6f} segundos"
        )


if __name__ == "__main__":
    main()