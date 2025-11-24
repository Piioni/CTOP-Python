edad_valida = False
while not edad_valida:
    try:
        edad = int(input("Introduce tu edad: "))
        if 0 <= edad <= 120:
            edad_valida = True
        else:
            print("Edad no válida. Por favor, inténtalo de nuevo.")

    except ValueError:
        print("Entrada no válida. Por favor, introduce un número entero.")

if edad < 18:
    print("Eres menor de edad.")
elif edad < 65:
    print("Eres adulto.")
else:
    print("Eres mayor.")
