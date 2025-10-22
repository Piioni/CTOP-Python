numero_valido = False
while not numero_valido:
    try:
        numero = int(input("Ingrese un numero entero: "))
        if numero > 0:
            numero_valido = True
        else:
            print("El numero debe ser positivo. Intente de nuevo.")
    except ValueError:
        print("Entrada no valida. Por favor, ingrese un numero entero positivo.")

suma_pares = 0
lista_pares = []
for i in range(2, numero + 1, 2):
    suma_pares += i
    lista_pares.append(i)
print("La suma de los numeros pares es:", suma_pares)
print("Los numeros pares son:", lista_pares)
