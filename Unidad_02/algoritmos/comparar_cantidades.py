numeros_validos = False
while not numeros_validos:
    try:
        primero = int(input("Ingrese el primer número entero: "))
        segundo = int(input("Ingrese el segundo número entero: "))
    except:
        print("Error: No has introducido un valor de tipo numerico.")
    else:
        numeros_validos = True


if primero > segundo:
    print(f"El primer número ({primero}) es mayor que el segundo número ({segundo}).")
elif segundo > primero:
    print(f"El segundo número ({segundo}) es mayor que el primer número ({primero}).")
else:
    print("Ambos números son iguales.")
