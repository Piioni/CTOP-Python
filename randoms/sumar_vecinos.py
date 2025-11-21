matriz = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]


def sumarVecinos(matriz):
    matrizVecina = [[0 for j in range(len(matriz))] for i in range(len(matriz))]
    for i in range(len(matriz)):
        for j in range(len(matriz)):
            sumatoria = 0
            if i - 1 >= 0:
                sumatoria += matriz[i - 1][j]
            if i + 1 < len(matriz):
                sumatoria += matriz[i + 1][j]
            if j - 1 >= 0:
                sumatoria += matriz[i][j - 1]
            if j + 1 < len(matriz):
                sumatoria += matriz[i][j + 1]

            matrizVecina[i][j] = matriz[i][j] + sumatoria

    return matrizVecina


print(sumarVecinos(matriz))
