def sumar(*numeros):
    return sum(numeros)


def restar(num1, num2):
    return num1 - num2


def multiplicar(*numeros):
    resultado = 1
    for numero in numeros:
        resultado *= numero
    return resultado


def dividir(num1, num2):
    if num2 == 0:
        raise ValueError("No se puede dividir por cero.")
    return num1 / num2


if __name__ == "__main__":
    print(
        "Haz ejecutado el módulo de operaciones directamente, importalo para usar sus funciones."
    )
