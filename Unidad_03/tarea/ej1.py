# Autor: Juan Rangel
# Fecha: 2024-06-12
# Descripcion: Programa que solicita tres numeros y muestra el mayor de ellos.

numeros_validos = False
# Bucle para asegurar que se ingresen numeros validos
while not numeros_validos:
    try:
        print("Vamos a calcular el mayor numero entre 3")
        n1 = float(input("Ingrese el primer numero: "))
        n2 = float(input("Ingrese el segundo numero: "))
        n3 = float(input("Ingrese el tercer numero: "))

    # Manejo de excepciones para entradas invalidas
    except ValueError:
        print("Entrada inválida. Por favor, ingrese un número válido.")

    else:
        numeros_validos = True

# Si n1 es mayor o igual que n2 y n3, entonces n1 es el mayor
if n1 >= n2 and n1 >= n3:
    mayor = n1
# Si n2 es mayor o igual que n3, entonces n2 es el mayor
elif n2 >= n3:
    mayor = n2
else:
    mayor = n3

print(f"El mayor numero es: {mayor}")
