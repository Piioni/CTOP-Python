# Autor: Juan Rangel
# Fecha: 2024-06-12
# Descripcion: Programa que solicita un numero entero positivo y muestra todos los numeros desde 1 hasta ese numero.

numero_valido = False
while not numero_valido:
    try:
        numero = int(input("Ingrese un número entero positivo: "))
        # Validamos que el numero sea positivo
        if numero <= 0:
            print("El número debe ser positivo. Intente nuevamente.")
            # Continuamos el bucle para pedir un nuevo número
            continue
    except ValueError:
        print("Entrada inválida. Por favor, ingrese un número entero válido.")
    else:
        numero_valido = True

# Mostramos los numeros desde 1 hasta el numero ingresado
print(f"Números desde 1 hasta {numero}:")
for i in range(1, numero + 1):
    print(i, end=" ")
