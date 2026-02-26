import pytest
from src.edad import calcular_edad_futura


def test_edad_futura_normal():
    assert calcular_edad_futura(20) == 30


def test_edad_futura_con_parametro_personalizado():
    assert calcular_edad_futura(20, 5) == 25


def test_edad_negativa():
    with pytest.raises(ValueError):
        calcular_edad_futura(-1)


def test_no_permitir_edad_menor_a_cero():
    with pytest.raises(ValueError):
        calcular_edad_futura(5, -10)

def test_edad_no_entera():
    with pytest.raises(TypeError):
        calcular_edad_futura("20", 10)


def test_anios_no_entero():
    with pytest.raises(TypeError):
        calcular_edad_futura(20, "10")


def test_edad_float():
    with pytest.raises(TypeError):
        calcular_edad_futura(20.5, 5)