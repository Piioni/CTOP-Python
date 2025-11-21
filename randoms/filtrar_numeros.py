def filtrar_numero(lista: list[int]) -> list[int]:
    dicc: dict[int, int] = {}
    lista_filtrada: list[int] = []
    for numero in lista:
        if numero in dicc:
            dicc[numero] += 1
        else:
            lista_filtrada.append(numero)
            dicc[numero] = 1

    return lista_filtrada


print(filtrar_numero([1, 2, 2, 3, 4, 4, 5, 1, 6, 3]))
