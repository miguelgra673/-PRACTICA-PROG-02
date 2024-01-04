# Desarrollar un programa que solicite la carga de tres valores y muestre el menor. 
# Desde el bloque principal del programa llamar 2 veces a dicha función (sin utilizar una estructura repetitiva)

def encontrar_menor(valor1, valor2, valor3):
    menor = min(valor1, valor2, valor3)
    print(f"El menor valor es: {menor}")


print("Ingresa tres valores para encontrar el menor:")
num1 = float(input("Ingrese el primer valor: "))
num2 = float(input("Ingrese el segundo valor: "))
num3 = float(input("Ingrese el tercer valor: "))
encontrar_menor(num1, num2, num3)

print("\nIngresa otros tres valores para encontrar el menor:")
num4 = float(input("Ingrese el primer valor: "))
num5 = float(input("Ingrese el segundo valor: "))
num6 = float(input("Ingrese el tercer valor: "))
encontrar_menor(num4, num5, num6)
