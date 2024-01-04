# Crea un programa llamado Loteria.py que le pida al usuario que introduzca los 6 números que
# juega a la lotería (separados por espacios). Entonces, deberá crear una lista con ellos, ordenarla ascendentemente e imprimirla en pantalla. Además, el programa debe indicar si es una lista válida (es
# decir, los números deben estar entre 1 y 49, inclusive, sin repetirse).

def validar_lista(numeros):
    if any(num < 1 or num > 49 for num in numeros):
        return False
    
    if len(numeros) != len(set(numeros)):
        return False
    
    return True

if __name__ == "__main__":
    entrada_usuario = input("Introduce los 6 números de la lotería separados por espacios: ")

    try:
        numeros_loteria = [int(num) for num in entrada_usuario.split()]
    except ValueError:
        print("Ingresa números válidos.")
        exit(1)

    if validar_lista(numeros_loteria):
        numeros_loteria.sort()
        print(f"Lista ordenada: {numeros_loteria}")
    else:
        print("La lista no es válida:")
        if any(num < 1 or num > 49 for num in numeros_loteria):
            print("Hay números menores que 1 o mayores que 49")
        if len(numeros_loteria) != len(set(numeros_loteria)):
            print("Hay números repetidos")
