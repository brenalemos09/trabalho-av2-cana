import math


def distancia(ponto1, ponto2):
    x1, y1 = ponto1
    x2, y2 = ponto2

    return math.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)


def forca_bruta_pontos(pontos):
    if len(pontos) < 2:
        raise ValueError("São necessários pelo menos dois pontos.")

    menor_distancia = float("inf")
    melhor_par = None

    for i in range(len(pontos)):
        for j in range(i + 1, len(pontos)):
            atual = distancia(pontos[i], pontos[j])

            if atual < menor_distancia:
                menor_distancia = atual
                melhor_par = (pontos[i], pontos[j])

    return menor_distancia, melhor_par


def dividir_pontos(pontos_x, pontos_y):
    if len(pontos_x) <= 20:
        return forca_bruta_pontos(pontos_x)

    meio = len(pontos_x) // 2
    esquerda_x = pontos_x[:meio]
    direita_x = pontos_x[meio:]

    limite_x = pontos_x[meio][0]

    esquerda_y = []
    direita_y = []

    pontos_esquerda = set(esquerda_x)

    for ponto in pontos_y:
        if ponto in pontos_esquerda:
            esquerda_y.append(ponto)
        else:
            direita_y.append(ponto)

    distancia_esquerda, par_esquerda = dividir_pontos(
        esquerda_x, esquerda_y
    )

    distancia_direita, par_direita = dividir_pontos(
        direita_x, direita_y
    )

    if distancia_esquerda <= distancia_direita:
        menor_distancia = distancia_esquerda
        melhor_par = par_esquerda
    else:
        menor_distancia = distancia_direita
        melhor_par = par_direita

    faixa = [
        ponto
        for ponto in pontos_y
        if abs(ponto[0] - limite_x) < menor_distancia
    ]

    for i in range(len(faixa)):
        limite = min(i + 8, len(faixa))

        for j in range(i + 1, limite):
            atual = distancia(faixa[i], faixa[j])

            if atual < menor_distancia:
                menor_distancia = atual
                melhor_par = (faixa[i], faixa[j])

    return menor_distancia, melhor_par


def divisao_conquista_pontos(pontos):
    if len(pontos) < 2:
        raise ValueError("São necessários pelo menos dois pontos.")

    pontos_x = sorted(
        pontos,
        key=lambda ponto: (ponto[0], ponto[1]),
    )

    pontos_y = sorted(
        pontos,
        key=lambda ponto: (ponto[1], ponto[0]),
    )

    return dividir_pontos(pontos_x, pontos_y)