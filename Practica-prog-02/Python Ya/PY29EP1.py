# Elaborar una función que muestre la tabla de multiplicar del valor que le enviemos como parámetro.
# Definir un segundo parámetro llamado termino que por defecto almacene el valor 10. Se deben mostrar tantos términos de la tabla de multiplicar como lo indica el segundo parámetro.
# Llamar a la función desde el bloque principal de nuestro programa con argumentos nombrados.

def tabla_multiplicar(valor, termino=10):
    print(f"Tabla de multiplicar del {valor} hasta el término {termino}:\n")
    for i in range(1, termino + 1):
        resultado = valor * i
        print(f"{valor} x {i} = {resultado}")

valor_tabla = 5
termino_tabla = 12

tabla_multiplicar(valor=valor_tabla, termino=termino_tabla)
