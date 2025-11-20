numero_valido: bool = False
numero: int = 0
while not numero_valido:
    try:
        numero: int = int(input("Por favor, ingresa un número entero: "))
    except ValueError:
        print("Entrada inválida. Asegúrate de ingresar un número entero.")
    else:
        numero_valido = True

if numero == 0:
    print("El número es 0")
else:
    es_par: bool = numero % 2 == 0
    es_mult3: bool = numero % 3 == 0
    if es_par and es_mult3:
        print("El número es par y múltiplo de 3")
    elif es_par and not es_mult3:
        print("El número es par pero no es múltiplo de 3")
    elif not es_par and es_mult3:
        print("El número es impar pero es múltiplo de 3")
    else:
        print("El número es impar y no es múltiplo de 3")
