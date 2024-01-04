# Confeccionar un programa que permita:
# 1) Cargar una lista de 10 elementos enteros.
# 2) Generar dos listas a partir de la primera. En una guardar los valores positivos y en otra los negativos.
# 3) Imprimir las dos listas generadas.

def cargar_lista():
    lista = []
    for i in range(10):
        valor = int(input(f"Ingrese el elemento {i + 1}: "))
        lista.append(valor)
    return lista

def generar_listas_positivos_negativos(lista):
    positivos = [valor for valor in lista if valor > 0]
    negativos = [valor for valor in lista if valor < 0]
    return positivos, negativos

lista_enteros = cargar_lista()

positivos, negativos = generar_listas_positivos_negativos(lista_enteros)

print("\nLista de valores positivos:", positivos)
print("Lista de valores negativos:", negativos)
