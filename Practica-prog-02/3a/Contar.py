# Crea un programa llamado Contar.py que reciba como parámetros del programa principal dos datos
# (numéricos) y realice un conteo desde el primero hasta el segundo. Si no se reciben los dos datos
# mostraremos un mensaje de error y finalizaremos.

def realizar_conteo(desde, hasta):
    for i in range(desde, hasta + 1):
        print(i)

if __name__ == "__main__":
    import sys

    if len(sys.argv) != 3:
        print("Debes proporcionar dos números como argumentos.")
        sys.exit(1)

    try:
        num1 = int(sys.argv[1])
        num2 = int(sys.argv[2])
    except ValueError:
        print("Los argumentos deben ser números enteros.")
        sys.exit(1)

    realizar_conteo(num1, num2)
