calificaciones_correctas = False
while not calificaciones_correctas:
    try:
        nota1 = float(input("Ingrese la primera calificación (0-10): "))
        nota2 = float(input("Ingrese la segunda calificación (0-10): "))
        nota3 = float(input("Ingrese la tercera calificación (0-10): "))

        if 0 <= nota1 <= 10 and 0 <= nota2 <= 10 and 0 <= nota3 <= 10:
            calificaciones_correctas = True
        else:
            print("Las calificaciones deben estar entre 0 y 10. Intente de nuevo.")
    except ValueError:
        print("Entrada inválida. Por favor, ingrese números válidos.")

promedio = (nota1 + nota2 + nota3) / 3
print(f"La nota media es: {promedio:.2f}")
