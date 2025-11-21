matriz = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]


def rotar_matriz(matriz: list[list[int]]) -> list[list[int]]:
    matriz_rotada = [[0 for _ in range(len(matriz))] for _ in range(len(matriz))]
    for columna in range(len(matriz)):
        for fila in range(len(matriz) - 1, -1, -1):
            matriz_rotada[columna][len(matriz) - 1 - fila] = matriz[fila][columna]

    return matriz_rotada


print(rotar_matriz(matriz))
