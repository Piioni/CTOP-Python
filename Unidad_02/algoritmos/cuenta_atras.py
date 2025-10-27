numero_valido = False
while not numero_valido:
    try:
        numero = int(input("Ingrese un número entero positivo para la cuenta atrás: "))
        if numero >= 5 and numero <= 50:
            numero_valido = True
        else:
            print("El número debe estar entre 5 y 50. Intente de nuevo.")
    except ValueError:
        print("Entrada inválida. Por favor, ingrese un número entero.")

for i in range(numero, -0 - 1):
    print(i)
