# Autor: Juan Rangel
# Fecha: 2024-06-12
# Descripcion: Programa que calcula el area de un rectangulo dada su base y altura.
# Objetivo: Practicar el uso del debugging en Python.


def area_rectangulo(base, altura):
    # Habia un error logico en el calculo del area, se estaba realizando una potencia en lugar de una multiplicacion.
    area = base * altura
    return area


# No se estaba realizando la conversion de los inputs a float, lo que causaba un error al intentar multiplicar cadenas.
base = float(input("Introduce la base: "))
altura = float(input("Introduce la altura: "))
area = area_rectangulo(base, altura)

# El primer error es un error de sintaxis en el print, falta una coma entre las cadenas y la variable.
print("El area es: ", area)
