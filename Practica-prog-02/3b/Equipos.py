# Escribe una nueva versión del ejercicio anterior en un programa llamado Equipos.py donde,
# además de la clase Jugador haya una segunda clase llamada Equipo , cuyo único atributo será el
# nombre del equipo (texto), junto con un constructor para darle valor . Haz que cada jugador pueda
# pertenecer a un equipo añadiendo un atributo Equipo a la clase Jugador. En el programa principal, crea
# un jugador y un equipo, y asigna el equipo al jugador. Muestra por pantalla la información del jugador,
# incluyendo el equipo. 

class Jugador:
    def __init__(self, dorsal, nombre):
        self.dorsal = dorsal
        self.nombre = nombre
        self.equipo = None 

    def asignar_equipo(self, equipo):
        self.equipo = equipo

    def mostrar_informacion(self):
        if self.equipo:
            return f"{self.dorsal}. {self.nombre}. Equipo: {self.equipo.nombre_equipo}"
        else:
            return f"{self.dorsal}. {self.nombre}. Sin equipo"


class Equipo:
    def __init__(self, nombre_equipo):
        self.nombre_equipo = nombre_equipo
        self.jugadores = []

    def agregar_jugador(self, jugador):
        self.jugadores.append(jugador)

    def mostrar_jugadores(self):
        print(f"Jugadores del equipo {self.nombre_equipo}:")
        for jugador in self.jugadores:
            print(jugador.mostrar_informacion())

if __name__ == "__main__":
    jugador1 = Jugador(16, "Pau Gasol")
    equipoA = Equipo("Equipo A")

    jugador1.asignar_equipo(equipoA)

    print(jugador1.mostrar_informacion())
