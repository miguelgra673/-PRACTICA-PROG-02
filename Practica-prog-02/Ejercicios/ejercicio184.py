from math import sqrt as obtener_raiz, pow as elevar_potencia

valor_ingresado = int(input("Ingrese un valor entero:"))
raiz_cuadrada = obtener_raiz(valor_ingresado)
cubo = elevar_potencia(valor_ingresado, 3)
print("La raíz cuadrada es", raiz_cuadrada)
print("El cubo es", cubo)
