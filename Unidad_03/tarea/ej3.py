# Autor: Juan Rangel
# Fecha: 2024-06-12
# Descripcion: Programa que solicita dos numeros y una operacion, luego muestra el resultado de la operacion.

valores_validos = False
while not valores_validos:
    try:
        print("Vamos a realizar una operacion entre 2 numeros")
        n1 = float(input("Ingrese el primer numero: "))
        n2 = float(input("Ingrese el segundo numero: "))

        # Solicitamos la operación a realizar mostrando las opciones disponibles
        operacion = input("Ingrese la operacion a realizar (+, -, *, /): ")

        # Validamos que la operacion ingresada sea correcta
        if operacion not in ["+", "-", "*", "/"]:
            print("Operacion invalida. Por favor, ingrese una operacion valida.")
            continue

    except ValueError:
        print("Entrada invalida. Por favor, ingrese un numero valido.")

    else:
        valores_validos = True


# Realizamos la operacion correspondiente
if operacion == "+":
    resultado = n1 + n2
elif operacion == "-":
    resultado = n1 - n2
elif operacion == "*":
    resultado = n1 * n2
elif operacion == "/":
    if n2 == 0:
        resultado = "Error: Division por cero no es permitida."
    else:
        resultado = n1 / n2

print(f"El resultado de la operacion {n1} {operacion} {n2} es: {resultado}")
