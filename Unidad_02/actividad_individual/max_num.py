numeros_correctos = False
while not numeros_correctos:
    try:
        num1 = int(input("Ingrese el primer número entero: "))
        num2 = int(input("Ingrese el segundo número entero: "))
        numeros_correctos = True
    except ValueError:
        print("Entrada inválida. Por favor, ingrese números enteros.")

if num1 > num2:
    print(f"El número mayor es: {num1}")
elif num2 > num1:
    print(f"El número mayor es: {num2}")
else:
    print("Ambos números son iguales.")
