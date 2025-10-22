numero_valido = False
while not numero_valido:
    try:
        numero = int(input("Ingrese un número entero positivo para la cuenta atrás: "))
        if numero >= 0:
            numero_valido = True
        else:
            print("El número debe ser positivo. Intente de nuevo.")
    except ValueError:
        print("Entrada inválida. Por favor, ingrese un número entero.")

for i in range(numero, -1, -1):
    print(i)
