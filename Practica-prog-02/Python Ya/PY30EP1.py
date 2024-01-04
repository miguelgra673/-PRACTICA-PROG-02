# Confeccionar una función que reciba una serie de edades y me retorne la cantidad que son mayores o iguales a 18 (como mínimo se envía un entero a la función)

def contar_edades_mayores_18(*edades):
    mayores_18 = sum(1 for edad in edades if edad >= 18)
    return mayores_18

edades = (15, 22, 17, 30, 19, 18, 25)

cantidad_mayores_18 = contar_edades_mayores_18(*edades)

print(f"La cantidad de edades mayores o iguales a 18 es: {cantidad_mayores_18}")
