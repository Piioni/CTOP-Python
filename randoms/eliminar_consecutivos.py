arr = [1, 2, 2, 3, 3, 3, 4, 4, 5, 5, 5, 5, 6]


def eliminar_consecutivos(lista: list[int]) -> list[int]:
    if not lista:
        return []

    lista_sin_consecutivos: list[int] = [lista[0]]

    for i in range(1, len(lista)):
        if lista[i] != lista[i - 1]:
            lista_sin_consecutivos.append(lista[i])

    return lista_sin_consecutivos
