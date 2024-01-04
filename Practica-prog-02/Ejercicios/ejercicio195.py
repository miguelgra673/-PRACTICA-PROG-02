class GestionAlumnos:

    def __init__(self):
        self.nombres_alumnos = []
        self.notas_alumnos = []

    def menu(self):
        opcion = 0
        while opcion != 4:
            print("1- Cargar alumnos")
            print("2- Listar alumnos")
            print("3- Listado de alumnos con notas mayores o iguales a 7")
            print("4- Finalizar programa")
            opcion = int(input("Ingrese su opción:"))
            if opcion == 1:
                self.cargar_alumnos()
            elif opcion == 2:
                self.listar_alumnos()
            elif opcion == 3:
                self.notas_altas()

    def cargar_alumnos(self):
        for _ in range(5):
            nombre = input("Ingrese nombre del alumno:")
            self.nombres_alumnos.append(nombre)
            nota = int(input("Nota del alumno:"))
            self.notas_alumnos.append(nota)

    def listar_alumnos(self):
        print("Listado completo de alumnos")
        for i in range(5):
            print(self.nombres_alumnos[i], self.notas_alumnos[i])
        print("_____________________")

    def notas_altas(self):
        print("Alumnos con notas superiores o iguales a 7")
        for i in range(5):
            if self.notas_alumnos[i] >= 7:
                print(self.nombres_alumnos[i], self.notas_alumnos[i])
        print("_____________________")

gestion_alumnos = GestionAlumnos()
gestion_alumnos.menu()
