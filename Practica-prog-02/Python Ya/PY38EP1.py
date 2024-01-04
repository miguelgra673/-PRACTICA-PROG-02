# Cargar una cadena de caracteres por teclado. Mostrar la cadena del final al principio utilizando subíndices negativos.

def mostrar_al_reves(cadena):
    cadena_al_reves = cadena[::-1]
    print(f"Cadena al revés: {cadena_al_reves}")

cadena_ingresada = input("Ingresa una cadena de caracteres: ")

mostrar_al_reves(cadena_ingresada)
