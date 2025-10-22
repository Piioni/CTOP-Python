cadena = "Hola, aqui programando en python"
vocales = "aeiou"

contador = 0
for char in cadena:
    if char.lower() in vocales:
        contador += 1

print("Cantidad de vocales:", contador)
