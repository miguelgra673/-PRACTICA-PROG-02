# Crea un programa llamado Funciones.py con las siguientes funciones:
# 1. Una función llamada mcd que reciba dos enteros a y b como parámetros y devuelva el máximo
# común divisor de esos parámetros. El máximo común divisor es el número más alto por el que se
# pueden dividir los dos números.
# 2. Una función llamada esPrimo que reciba un número como parámetro y devuelva un booleano
# indicando si el número es primo o no
# Desde el programa principal, llama a la función mcd para calcular el máximo común divisor de 20 y 12
# (debería dar 4), y usa la función esPrimo para sacar los números primos que haya del 1 al 50.

# Funciones.py

def mcd(a, b):
    while b:
        a, b = b, a % b
    return a

def esPrimo(numero):
    if numero < 2:
        return False
    for i in range(2, int(numero**0.5) + 1):
        if numero % i == 0:
            return False
    return True

num1 = 20
num2 = 12
resultado_mcd = mcd(num1, num2)
print(f"El máximo común divisor de {num1} y {num2} es: {resultado_mcd}")

print("Números primos del 1 al 50:")
for num in range(1, 51):
    if esPrimo(num):
        print(num)