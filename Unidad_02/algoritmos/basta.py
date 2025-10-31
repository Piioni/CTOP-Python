palabra = ""
terminaciones = ["basta"]

while True:
    palabra = input("Ingrese una palabra (o 'basta' para terminar): ")
    print(f"Has ingresado: {palabra}")
    if palabra == "" or palabra.lower() in terminaciones:
        break

print("Programa terminado")
