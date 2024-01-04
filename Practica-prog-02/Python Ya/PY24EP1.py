# Desarrollar una funcion que reciba un string como parametro y nos muestre la cantidad de vocales.
# Llamarla desde el bloque principal del programa 3 veces con string distintos.
def contar_vocales(cadena):
    vocales = "aeiouAEIOU"
    cantidad_vocales = sum(1 for char in cadena if char in vocales)
    print(f"La cantidad de vocales en '{cadena}' es: {cantidad_vocales}")


cadena1 = input("Ingresa un string para contar las vocales: ")
contar_vocales(cadena1)

cadena2 = input("Ingresa otro string para contar las vocales: ")
contar_vocales(cadena2)

cadena3 = input("Ingresa un tercer string para contar las vocales: ")
contar_vocales(cadena3)
