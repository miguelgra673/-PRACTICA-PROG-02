class Estudiante:

    def configurar_datos(self, nombre, calificacion):
        self.nombre = nombre
        self.calificacion = calificacion

    def imprimir_informacion(self):
        print("Nombre:", self.nombre)
        print("Calificación:", self.calificacion)

    def mostrar_estado(self):
        if self.calificacion >= 4:
            print("Regular")
        else:
            print("Libre")


# Bloque principal

estudiante1 = Estudiante()
estudiante1.configurar_datos("Diego", 2)
estudiante1.imprimir_informacion()
estudiante1.mostrar_estado()

estudiante2 = Estudiante()
estudiante2.configurar_datos("Ana", 10)
estudiante2.imprimir_informacion()
estudiante2.mostrar_estado()
