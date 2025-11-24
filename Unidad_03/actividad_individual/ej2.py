numero_valido: bool = False
while not numero_valido:
    try:
        num: int = int(input("Ingresa un número entre 5 y 12: "))
        if 5 <= num <= 12:
            numero_valido = True
        else:
            print("El número no está en el rango de 5 a 12. Intenta de nuevo.")

    except ValueError:
        print("Entrada inválida. Por favor, ingresa un número entero.")

print(f"Número válido ingresado: {num}")
for i in range(11):
    resultado: int = num * i
    print(f"{num} x {i} = {resultado}")
