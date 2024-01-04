# Definir una lista de enteros por asignación en el bloque principal. 
# Llamar a una función que reciba la lista y nos retorne el producto de todos sus elementos. Mostrar dicho producto en el bloque principal de nuestro programa.

def calcular_producto(lista):
    producto = 1
    for elemento in lista:
        producto *= elemento
    return producto

lista_enteros = [2, 3, 5, 7, 11]

resultado_producto = calcular_producto(lista_enteros)

print(f"El producto de los elementos en la lista es: {resultado_producto}")
