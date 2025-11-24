palabra_valida = False
while not palabra_valida:
    # Verificar que solo sea una palabra.
    palabra = input("Ingrese una palabra: ")
    if " " in palabra or palabra == "":
        print("Entrada inválida. Por favor, ingrese una sola palabra sin espacios.")
    else:
        palabra_valida = True


letras = 0
for letra in palabra:
    letras += 1

print("La palabra tiene", letras, "letras.")
