import sys


def sumar(*args: float) -> float:
    return sum(args)


def restar(minuendo: float, sustraendo: float) -> float:
    return minuendo - sustraendo


def multiplicar(*args: float) -> float:
    resultado = 1.0
    for num in args:
        resultado *= num
    return resultado


def dividir(dividendo: float, divisor: float) -> float:
    if divisor == 0:
        raise ValueError("El divisor no puede ser cero.")
    return dividendo / divisor


def potenciar(base: float, exponente: int) -> float:
    return base**exponente


if __name__ == "__main__":
    print("Estas ejecutando el modulo directamente.")
    sys.exit(0)
else:
    print("Estas importando el modulo de forma correcta.")
