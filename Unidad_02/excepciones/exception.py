texto = ""
try:
    f = open("archivo.txt", "w")
    texto = f.read()
    f.write("Nueva línea de texto.")
except IOError as e:
    print("Error de E/S: ", e)
else:
    print("Contenido del archivo:")
    print(texto)
