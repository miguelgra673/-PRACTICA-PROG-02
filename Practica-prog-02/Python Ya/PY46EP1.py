# Plantear una clase Club y otra clase Socio.
# La clase Socio debe tener los siguientes atributos: nombre y la antigüedad en el club (en años).
# En el método __init__ de la clase Socio pedir la carga por teclado del nombre y su antigüedad.
# La clase Club debe tener como atributos 3 objetos de la clase Socio.
# Definir una responsabilidad para imprimir el nombre del socio con mayor antigüedad en el club.

class Socio:
    def __init__(self):
        self.nombre = input("Ingresa el nombre del socio: ")
        self.antiguedad = int(input("Ingresa la antigüedad del socio en años: "))

class Club:
    def __init__(self):
        self.socio1 = Socio()
        self.socio2 = Socio()
        self.socio3 = Socio()

    def socio_con_mayor_antiguedad(self):
        socios = [self.socio1, self.socio2, self.socio3]
        socio_mayor_antiguedad = max(socios, key=lambda x: x.antiguedad)
        return socio_mayor_antiguedad

club = Club()

socio_mayor_antiguedad = club.socio_con_mayor_antiguedad()
print(f"\nEl socio con mayor antigüedad en el club es: {socio_mayor_antiguedad.nombre} con {socio_mayor_antiguedad.antiguedad} años de antigüedad.")
