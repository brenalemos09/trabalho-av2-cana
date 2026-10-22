def melhor_resultado(atual, novo):
    if novo[0] > atual[0]:
        return novo

    if novo[0] == atual[0]:
        tamanho_atual = atual[2] - atual[1]
        tamanho_novo = novo[2] - novo[1]

        if tamanho_novo < tamanho_atual:
            return novo

        if tamanho_novo == tamanho_atual and novo[1] < atual[1]:
            return novo

    return atual


def forca_bruta(valores):
    if not valores:
        raise ValueError("O vetor não pode estar vazio.")

    melhor = (valores[0], 0, 0)

    for inicio in range(len(valores)):
        soma = 0

        for fim in range(inicio, len(valores)):
            soma += valores[fim]
            candidato = (soma, inicio, fim)
            melhor = melhor_resultado(melhor, candidato)

    return melhor


def melhor_cruzando_meio(valores, esquerda, meio, direita):
    soma = 0
    melhor_esquerda = (float("-inf"), meio, meio)

    for i in range(meio, esquerda - 1, -1):
        soma += valores[i]
        candidato = (soma, i, meio)
        melhor_esquerda = melhor_resultado(
            melhor_esquerda,
            candidato,
        )

    soma = 0
    melhor_direita = (float("-inf"), meio + 1, meio + 1)

    for i in range(meio + 1, direita + 1):
        soma += valores[i]
        candidato = (soma, meio + 1, i)
        melhor_direita = melhor_resultado(
            melhor_direita,
            candidato,
        )

    return (
        melhor_esquerda[0] + melhor_direita[0],
        melhor_esquerda[1],
        melhor_direita[2],
    )


def dividir(valores, esquerda, direita):
    if esquerda == direita:
        return valores[esquerda], esquerda, direita

    meio = (esquerda + direita) // 2

    melhor_esquerda = dividir(valores, esquerda, meio)
    melhor_direita = dividir(valores, meio + 1, direita)

    melhor_meio = melhor_cruzando_meio(
        valores,
        esquerda,
        meio,
        direita,
    )

    melhor = melhor_resultado(
        melhor_esquerda,
        melhor_direita,
    )

    melhor = melhor_resultado(
        melhor,
        melhor_meio,
    )

    return melhor


def divisao_conquista(valores):
    if not valores:
        raise ValueError("O vetor não pode estar vazio.")

    return dividir(valores, 0, len(valores) - 1)


def linear(valores):
    if not valores:
        raise ValueError("O vetor não pode estar vazio.")

    soma_atual = valores[0]
    inicio_atual = 0
    melhor = (valores[0], 0, 0)

    for fim in range(1, len(valores)):
        if valores[fim] >= soma_atual + valores[fim]:
            soma_atual = valores[fim]
            inicio_atual = fim
        else:
            soma_atual += valores[fim]

        candidato = (
            soma_atual,
            inicio_atual,
            fim,
        )

        melhor = melhor_resultado(
            melhor,
            candidato,
        )

    return melhor