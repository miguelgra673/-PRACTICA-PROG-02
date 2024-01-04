# Adapta el ejercicio 2 anterior en un archivo llamado ContarExcepciones.py , y controla el caso en
# que los datos que escriba el usuario como parámetros no sean números enteros, mostrando el mensaje
# "Datos incorrectos" en ese caso.


def realizar_conteo(desde, hasta):
    for i in range(desde, hasta + 1):
        print(i)

if __name__ == "__main__":
    try:
        desde = int(input("Introduce el primer número: "))
        hasta = int(input("Introduce el segundo número: "))

        realizar_conteo(desde, hasta)

    except ValueError:
        print("Datos incorrectos")
