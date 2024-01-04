def cargar_contactos():
    lista_contactos = {}
    continuar = "s"
    while continuar == "s":
        nombre = input("Ingrese el nombre del contacto:")
        telefono = input("Ingrese el numero de telefono:")
        lista_contactos[nombre] = telefono
        continuar = input("¿Desea ingresar otro contacto? [s/n]:")
    return lista_contactos


def modificar_telefono_contacto(lista_contactos):
    nombre = input("Ingrese el nombre del contacto para modificar el telefono:")
    if nombre in lista_contactos:
        nuevo_telefono = input("Ingrese el nuevo numero telefonico:")
        lista_contactos[nombre] = nuevo_telefono
    else:
        print("No existe un contacto con el nombre ingresado.")


def imprimir_contactos(lista_contactos):
    print("Listado de todos los contactos:")
    for nombre, telefono in lista_contactos.items():
        print(f"{nombre}: {telefono}")


# Bloque principal

contactos = cargar_contactos()
modificar_telefono_contacto(contactos)
imprimir_contactos(contactos)
