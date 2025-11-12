def promedio(*numeros):
    return sum(numeros) / len(numeros) if numeros else 0


def media(num1, num2):
    return (num1 + num2) / 2


numeros_validos = False

while not numeros_validos:
    try:
        n = int(input("¿Cuántos números desea ingresar para calcular el promedio? "))
        if n <= 0:
            print("Por favor, ingrese un número positivo.")
            continue

        numeros = []
        for i in range(n):
            numero = float(input(f"Ingrese el número {i + 1}: "))
            numeros.append(numero)

    except ValueError:
        print("Entrada inválida. Por favor, ingrese un número válido.")

    else:
        numeros_validos = True


if n == 2:
    resultado = media(numeros[0], numeros[1])
    print(f"La media de los dos números es: {resultado}")
else:
    resultado = promedio(*numeros)
    print(f"El promedio de los {n} números es: {resultado}")
