from edad import calcular_edad_futura

def obtener_edad() -> int:
    """
    Solicita al usuario su edad y valida la entrada.
    
    :return: Edad válida como entero
    """
    while True:
        try:
            edad = int(input("¿Cuál es tu edad? "))
            if edad < 0:
                print("La edad no puede ser negativa.")
                continue
            return edad
        except ValueError:
            print("Error: Introduce un número válido.")


def imprimir_resultados(nombre: str, edad: int, edad_futura: int) -> None:
    """
    Imprime los resultados al usuario.
    """
    print(f"\nHola, {nombre}")
    print(f"Tu edad actual es: {edad}")
    print(f"En 10 años tendrás: {edad_futura}")


def main() -> None:
    nombre = input("¿Cuál es tu nombre? ")
    edad = obtener_edad()
    edad_futura = calcular_edad_futura(edad)
    imprimir_resultados(nombre, edad, edad_futura)


if __name__ == "__main__":
    main()