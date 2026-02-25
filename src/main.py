# main.py
def calcula_edad_en_10_anios(edad):
    edad_en_10_anios = edad + 10
    return edad_en_10_anios

def obtener_edad():
    while True:
        try:
            edad = int(input("¿Cuál es tu edad? "))
            break  # Salir del bucle si la entrada es válida
        except ValueError:
            print("Error: Por favor, introduce un número válido para la edad.")

    edad = calcula_edad_en_10_anios(edad)
    return edad

def main():
    nombre = input("¿Cuál es tu nombre? ")
    edad_en_10_anios = obtener_edad()    

    print("Hola,", nombre)
    print("En 10 años tendrás :", edad_en_10_anios)

if __name__ == "__main__":
    main()