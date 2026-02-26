def calcular_edad_futura(edad: int, anios: int = 10) -> int:
    """
    Calcula la edad futura sumando un número de años.
    
    :param edad: Edad actual
    :param anios: Cantidad de años a sumar (por defecto 10)
    :return: Edad futura
    """

    # Validación de tipos
    if not isinstance(edad, int):
        raise TypeError("La edad debe ser un entero.")

    if not isinstance(anios, int):
        raise TypeError("Los años deben ser un entero.")

    # Validación de reglas de negocio
    if edad < 0:
        raise ValueError("La edad no puede ser negativa.")

    resultado = edad + anios

    if resultado < 0:
        raise ValueError("La edad resultante no puede ser menor que cero.")

    return resultado
  