try:
    num = int(input("Ingrese un número entero: "))

except ValueError:
    print("Error: Entrada inválida. Por favor, ingrese un número entero.")
except Exception as e:
    print("Ocurrió un error inesperado: ", e)
else:
    if num > 0:
        print("El número es positivo.")
    elif num < 0:
        print("El número es negativo.")
    else:
        print("El número es cero.")
finally:
    print("Fin del programa.")
