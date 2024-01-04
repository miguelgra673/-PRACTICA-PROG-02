# Crear un diccionario en Python que defina como clave el número de documento de una persona y como valor un string con su nombre.
# Desarrollar las siguientes funciones:
# 1) Cargar por teclado los datos de 4 personas.
# 2) Listado completo del diccionario.
# 3) Consulta del nombre de una persona ingresando su número de documento.

def cargar_personas():
    personas = {}

    for _ in range(4):
        documento = input("Ingrese el número de documento: ")
        nombre = input("Ingrese el nombre de la persona: ")

        personas[documento] = nombre

    return personas

def listar_personas(diccionario):
    print("\nListado completo del diccionario:")
    for documento, nombre in diccionario.items():
        print(f"Número de Documento: {documento}, Nombre: {nombre}")

def consultar_nombre(diccionario, documento_consulta):
    if documento_consulta in diccionario:
        nombre = diccionario[documento_consulta]
        print(f"\nNombre de la persona con documento {documento_consulta}: {nombre}")
    else:
        print("\nNo se encontró ninguna persona con ese número de documento.")

personas_dict = cargar_personas()

listar_personas(personas_dict)

documento_a_consultar = input("\nIngrese el número de documento para consultar el nombre: ")
consultar_nombre(personas_dict, documento_a_consultar)
