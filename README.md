# Trabalho Prático - Divisão e Conquista

Trabalho desenvolvido para a disciplina de Construção e Análise de Algoritmos.

O projeto implementa e compara algoritmos de força bruta e divisão e conquista para dois problemas:

- Subarranjo máximo
- Par de pontos mais próximos

Também foi implementada uma solução linear para o problema do subarranjo máximo.

## Algoritmos implementados

### Subarranjo máximo

Foram implementadas três soluções:

- Força bruta: O(n²)
- Divisão e conquista: O(n log n)
- Solução linear: O(n)

O resultado contém a soma máxima encontrada e os índices inicial e final do subarranjo.

Em caso de empate de soma, é escolhido o menor intervalo. Se o tamanho também for igual, é escolhido o intervalo que começa primeiro.

### Par de pontos mais próximos

Foram implementadas duas soluções:

- Força bruta: O(n²)
- Divisão e conquista: O(n log n)

Na solução por divisão e conquista, os pontos são ordenados e divididos em duas partes. Após resolver cada metade, é analisada a faixa próxima à divisão.

Foi utilizado o limiar 20 para o caso-base da recursão. Esse valor foi escolhido após testes experimentais com diferentes limiares.

## Estrutura do projeto

```text
Trabalho_AV2_CANA/
├── dados/
│   ├── casos_teste.txt
│   └── configuracao_maquina.txt
├── resultados/
│   ├── grafico_pontos.png
│   ├── grafico_pontos_normal.png
│   ├── grafico_subarranjo.png
│   ├── grafico_subarranjo_normal.png
│   ├── medias_pontos.csv
│   ├── medias_subarranjo.csv
│   ├── tempos_pontos.csv
│   └── tempos_subarranjo.csv
├── src/
│   ├── graficos.py
│   ├── medicoes.py
│   ├── pontos_proximos.py
│   ├── subarranjo.py
│   └── teste_limiar.py
├── testes/
│   ├── test_pontos_proximos.py
│   └── test_subarranjo.py
├── .gitignore
└── README.md
```

## Requisitos

- Python 3
- Matplotlib

Para instalar o Matplotlib:

```bash
python -m pip install matplotlib
```

## Executando os testes

Teste do subarranjo máximo:

```bash
python testes/test_subarranjo.py
```

Teste do par de pontos mais próximos:

```bash
python testes/test_pontos_proximos.py
```

## Executando as medições

Para realizar as medições de tempo:

```bash
python src/medicoes.py
```

Cada algoritmo é executado 5 vezes para cada tamanho de entrada.

Os tamanhos utilizados são:

```text
100, 200, 400, 800, 1600, 3200 e 6400
```

Os tempos obtidos são armazenados em arquivos CSV na pasta `resultados`.

## Gerando os gráficos

Depois das medições, execute:

```bash
python src/graficos.py
```

O programa calcula os tempos médios e gera os gráficos utilizados na análise experimental.

## Testes realizados

Os casos de teste utilizados estão documentados em:

```text
dados/casos_teste.txt
```

Além dos testes definidos no projeto, foram utilizados 500 casos aleatórios para comparar as três implementações do subarranjo máximo e 500 casos aleatórios para comparar as duas implementações do problema dos pontos mais próximos.

A configuração da máquina utilizada nas medições está registrada em:

```text
dados/configuracao_maquina.txt
```

## Resultados

A pasta `resultados` contém:

- Tempos individuais das execuções
- Tempos médios
- Gráficos comparativos
- Resultados em escala normal e logarítmica

Os resultados são utilizados para comparar o comportamento experimental dos algoritmos com suas complexidades teóricas.