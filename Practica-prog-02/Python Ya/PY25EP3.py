# Confeccionar una función que calcule la superficie de un rectángulo y la retorne, la función recibe como parámetros los valores de dos de sus lados:

def retornar_superficie(lado1, lado2):
    superficie = lado1 * lado2
    return superficie

lado1 = float(input("Ingresa la longitud del primer lado del rectángulo: "))
lado2 = float(input("Ingresa la longitud del segundo lado del rectángulo: "))

resultado = retornar_superficie(lado1, lado2)
print(f"La superficie del rectángulo es: {resultado}")
