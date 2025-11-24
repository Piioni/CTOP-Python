# Unidad_03/estructuras_control/Tipos de datos.py

decimal_valido = False
while not decimal_valido:
    entrada = input("Ingrese un número decimal: ")
    try:
        numero_decimal = float(entrada)
    except ValueError:
        print("Entrada inválida. Por favor, ingrese un número decimal válido.")
    else:
        decimal_valido = True
        print(f"Número decimal ingresado: {numero_decimal}")
        print(f"Convertido a entero: {int(numero_decimal)}")
        print(f'Convertido a cadena: "{str(numero_decimal)}"')
