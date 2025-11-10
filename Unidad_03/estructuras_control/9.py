numero_valido = False
while not numero_valido:
    try:
        numero = int(input("Ingrese un numero del 1 al 10: "))
        if 1 <= numero <= 10:
            numero_valido = True
        else:
            print("Número fuera de rango. Por favor, ingrese un número del 1 al 10.")
    except ValueError:
        print("Entrada inválida. Por favor, ingrese un número entero válido.")

print("Tabla de multiplicar del", numero)
for i in range(1, 11):
    print(numero, "x", i, "=", numero * i)
