import sys
from pathlib import Path

sys.path.append(str(Path(__file__).parent.parent / "src"))

from subarranjo import forca_bruta, divisao_conquista


def testar(nome, valores, esperado):
    resultado_bruta = forca_bruta(valores)
    resultado_divisao = divisao_conquista(valores)

    assert resultado_bruta == esperado
    assert resultado_divisao == esperado

    print(f"{nome}: OK")


def main():
    testar(
        "Caso comum",
        [-2, 4, -1, 3, -5],
        (6, 1, 3),
    )

    testar(
        "Somente negativos",
        [-8, -3, -6, -2, -5, -4],
        (-2, 3, 3),
    )

    testar(
        "Vetor de tamanho 1 positivo",
        [7],
        (7, 0, 0),
    )

    testar(
        "Vetor de tamanho 1 negativo",
        [-5],
        (-5, 0, 0),
    )

    testar(
        "Empate de soma",
        [2, -2, 2],
        (2, 0, 0),
    )

    testar(
        "Todos positivos",
        [1, 2, 3, 4],
        (10, 0, 3),
    )

    testar(
        "Valores mistos",
        [-4, 2, 3, -2, 3, -7],
        (6, 1, 4),
    )

    testar(
        "Melhor intervalo no inicio",
        [5, 4, -10, 2],
        (9, 0, 1),
    )

    testar(
        "Melhor intervalo no final",
        [-10, 1, -5, 6, 4],
        (10, 3, 4),
    )

    testar(
        "Vetor com zero",
        [0],
        (0, 0, 0),
    )

    print("\nTodos os testes passaram.")


if __name__ == "__main__":
    main()