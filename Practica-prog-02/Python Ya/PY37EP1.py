# Realizar un programa que contenga las siguientes funciones:
# 1) Carga de una lista de 10 enteros.
# 2) Recibir una lista y retornar otra con la primer mitad (se sabe que siempre llega una lista con una cantidad par de elementos)
# 3) Imprimir una lista.

def cargar_lista():
    lista = []
    for _ in range(10):
        elemento = int(input("Ingresa un entero: "))
        lista.append(elemento)
    return lista

def obtener_primer_mitad(lista):
    mitad = len(lista) // 2
    return lista[:mitad]

def imprimir_lista(lista):
    print("Lista:")
    print(lista)


lista_enteros = cargar_lista()
primer_mitad_lista = obtener_primer_mitad(lista_enteros)
imprimir_lista(primer_mitad_lista)
