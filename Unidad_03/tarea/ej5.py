from time import time

# Autor: Juan Rangel
# Fecha: 2024-06-12
# Descripcion: Programa que compara el tiempo de ejecución de un bucle for y un bucle while para sumar los primeros 1,000,000 números.

# Inicialiamos la sumatoria y el tiempo de inicio
sumatoria = 0
inicio_for = time()
for i in range(1000000):
    sumatoria += i

fin_for = time()
print("Usando for:")
print(f"La sumatoria de los primeros 1,000,000 números es: {sumatoria}")
# Calculamos y mostramos el tiempo de ejecución
print(f"Tiempo de ejecución con for: {fin_for - inicio_for} segundos.")


# Versión usando while
sumatoria = 0
i = 0
inicio_while = time()
while i < 1000000:
    sumatoria += i
    i += 1
fin_while = time()

print("Usando while:")
print(f"La sumatoria de los primeros 1,000,000 números es: {sumatoria}")
print(f"Tiempo de ejecución con while: {fin_while - inicio_while} segundos.")
