# Confeccionar una función que reciba entre 2 y 5 enteros. La misma nos debe retornar la suma de dichos valores. Debe tener tres parámetros por defecto.

def suma_valores(valor1, valor2, valor3=0, valor4=0, valor5=0):
    suma = valor1 + valor2 + valor3 + valor4 + valor5
    return suma

resultado1 = suma_valores(1, 2)
resultado2 = suma_valores(1, 2, 3)
resultado3 = suma_valores(1, 2, 3, 4)
resultado4 = suma_valores(1, 2, 3, 4, 5)

print(f"Resultado 1: {resultado1}")
print(f"Resultado 2: {resultado2}")
print(f"Resultado 3: {resultado3}")
print(f"Resultado 4: {resultado4}")
