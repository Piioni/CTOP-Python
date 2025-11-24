import operaciones as ops


def test_suma():
    assert ops.sumar(2, 3) == 5
    assert ops.sumar(-1, 1) == 0
    assert ops.sumar(0, 0) == 0


def test_resta():
    assert ops.restar(5, 3) == 2
    assert ops.restar(0, 0) == 0
    assert ops.restar(-1, -1) == 0


def test_multiplicacion():
    assert ops.multiplicar(2, 3) == 6
    assert ops.multiplicar(-1, 1) == -1
    assert ops.multiplicar(0, 5) == 0


def test_division():
    assert ops.dividir(6, 3) == 2
    assert ops.dividir(-6, -3) == 2
    try:
        ops.dividir(5, 0)
    except ValueError as e:
        assert str(e) == "El divisor no puede ser cero."


def test_potenciacion():
    assert ops.potenciar(2, 3) == 8
    assert ops.potenciar(5, 0) == 1
    assert ops.potenciar(3, 2) == 9


if __name__ == "__main__":
    test_suma()
    test_resta()
    test_multiplicacion()
    test_division()
    test_potenciacion()
    print("Todas las pruebas pasaron correctamente.")
