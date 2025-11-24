from typing import Any


persona: dict[str, Any] = {
    "nombre": "Juan",
    "edad": 21,
    "estudiante": True,
}

persona2: dict[str, Any] = {
    "nombre": "Erick",
    "edad": 37,
    "estudiante": True,
}

persona3: dict[str, Any] = {
    "nombre": "Alejandro",
    "edad": 13,
    "estudiante": False,
}


def imprimir_edad(persona: dict[str, Any]) -> None:
    nombre: str = persona["nombre"]
    edad: int = persona["edad"]
    if edad < 18:
        print(f"{nombre} es menor de edad.")
    elif 18 <= edad < 26:
        print(f"{nombre} eres muy joven.")
    elif 26 <= edad < 41:
        print(f"{nombre} eres joven.")
    else:
        print(f"{nombre} ya no eres tan joven.")


imprimir_edad(persona)
imprimir_edad(persona2)
imprimir_edad(persona3)
