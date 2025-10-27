import sys

lista = [10, 20, 50]

try:
    for n in range(5):
        print(lista[n])
except IndexError as e:
    print("Error: ", e)
else:
    print("Proceso finalizado sin errores.")
finally:
    sys.exit(0)
