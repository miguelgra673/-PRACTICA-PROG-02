# Confeccionar una clase que administre una agenda personal. Se debe almacenar el nombre de la persona, teléfono y mail
# Debe mostrar un menú con las siguientes opciones:
# 1- Carga de un contacto en la agenda.
# 2- Listado completo de la agenda.
# 3- Consulta ingresando el nombre de la persona.
# 4- Modificación de su teléfono y mail.
# 5- Finalizar programa.

class Contacto:
    def __init__(self, nombre, telefono, mail):
        self.nombre = nombre
        self.telefono = telefono
        self.mail = mail

class AgendaPersonal:
    def __init__(self):
        self.contactos = []

    def cargar_contacto(self):
        nombre = input("Ingresa el nombre del contacto: ")
        telefono = input("Ingresa el teléfono del contacto: ")
        mail = input("Ingresa el mail del contacto: ")

        nuevo_contacto = Contacto(nombre, telefono, mail)
        self.contactos.append(nuevo_contacto)
        print(f"Contacto '{nombre}' cargado correctamente.")

    def listar_agenda(self):
        print("\nListado completo de la agenda:")
        for contacto in self.contactos:
            print(f"Nombre: {contacto.nombre}")
            print(f"Teléfono: {contacto.telefono}")
            print(f"Mail: {contacto.mail}")
            print("------------------------")

    def consultar_contacto(self, nombre_consulta):
        for contacto in self.contactos:
            if contacto.nombre.lower() == nombre_consulta.lower():
                print(f"\nContacto encontrado:")
                print(f"Nombre: {contacto.nombre}")
                print(f"Teléfono: {contacto.telefono}")
                print(f"Mail: {contacto.mail}")
                return
        print(f"\nNo se ha encontrado ningún contacto con el nombre '{nombre_consulta}'.")

    def modificar_contacto(self, nombre_modificar):
        for contacto in self.contactos:
            if contacto.nombre.lower() == nombre_modificar.lower():
                print(f"\nModificación del contacto '{nombre_modificar}':")
                nuevo_telefono = input("Ingresa el nuevo teléfono: ")
                nuevo_mail = input("Ingresa el nuevo mail: ")

                contacto.telefono = nuevo_telefono
                contacto.mail = nuevo_mail
                print(f"Contacto modificado correctamente.")
                return
        print(f"\nNo se encontró ningún contacto con el nombre '{nombre_modificar}'.")

def menu():
    print("\nMenú de la Agenda Personal:")
    print("1- Carga de un contacto en la agenda.")
    print("2- Listado completo de la agenda.")
    print("3- Consulta ingresando el nombre de la persona.")
    print("4- Modificación de su teléfono y mail.")
    print("5- Finalizar programa.")

# Programa principal
agenda = AgendaPersonal()

while True:
    menu()
    opcion = input("\nIngresa la opción deseada (1-5): ")

    if opcion == "1":
        agenda.cargar_contacto()
    elif opcion == "2":
        agenda.listar_agenda()
    elif opcion == "3":
        nombre_consulta = input("Ingresa el nombre a consultar: ")
        agenda.consultar_contacto(nombre_consulta)
    elif opcion == "4":
        nombre_modificar = input("Ingresa el nombre a modificar: ")
        agenda.modificar_contacto(nombre_modificar)
    elif opcion == "5":
        print("Programa finalizado.")
        break
    else:
        print("Opción no válida. Por favor, ingresa una opción válida (1-5).")
