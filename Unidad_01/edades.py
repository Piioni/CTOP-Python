while True:
    edad = int(input("Ingresa tu edad: (Comprendida entre 0 y 120) "))
    if edad >= 0 and edad <= 120:
        break
    print("Edad no valida. Intenta de nuevo.")

if edad < 16:
    print("Eres niño.")

elif edad >= 16 and edad <= 21:
    print("Eres adolescente.")

elif edad >= 22 and edad <= 35:
    print("Eres joven.")

elif edad >= 36 and edad <= 50:
    print("Eres maduro.")

elif edad >= 51 and edad <= 60:
    print("Eres de mediana edad.")

elif edad >= 61 and edad <= 80:
    print("Eres de mayor.")

elif edad >= 81 and edad <= 100:
    print("Eres viejo.")

else:
    print("Eres centenario.")
