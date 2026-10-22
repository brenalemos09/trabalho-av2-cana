import sys
from pathlib import Path

sys.path.append(str(Path(__file__).parent.parent / "src"))

from pontos_proximos import forca_bruta_pontos, divisao_conquista_pontos


def testar(nome, pontos, distancia_esperada):
    distancia_bruta, par_bruta = forca_bruta_pontos(pontos)
    distancia_divisao, par_divisao = divisao_conquista_pontos(pontos)

    assert abs(distancia_bruta - distancia_esperada) < 0.000001
    assert abs(distancia_divisao - distancia_esperada) < 0.000001
    assert par_bruta is not None
    assert par_divisao is not None

    print(f"{nome}: OK")


def main():
    testar(
        "Dois pontos",
        [(0, 0), (3, 4)],
        5.0,
    )

    testar(
        "Pontos proximos",
        [(0, 0), (10, 10), (2, 2), (2, 3)],
        1.0,
    )

    testar(
        "Pontos negativos",
        [(-5, -5), (-2, -1), (-2, -2)],
        1.0,
    )

    testar(
        "Pontos repetidos",
        [(1, 1), (4, 5), (1, 1)],
        0.0,
    )

    testar(
        "Pontos na mesma linha",
        [(0, 0), (5, 0), (2, 0), (10, 0)],
        2.0,
    )

    testar(
        "Pontos espalhados",
        [(1, 8), (15, 20), (7, 4), (8, 4), (30, 2)],
        1.0,
    )

    testar(
        "Coordenadas decimais",
        [(0.5, 0.5), (1.5, 0.5), (8.0, 9.0)],
        1.0,
    )

    print("\nTodos os testes passaram.")


if __name__ == "__main__":
    main()