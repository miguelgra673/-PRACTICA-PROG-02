# Plantear una clase llamada Jugador.
# Definir en la clase Jugador los atributos nombre y puntaje, y los métodos __init__, imprimir y pasar_tiempo (que debe reducir en uno la variable de clase).
# Declarar dentro de la clase Jugador una variable de clase que indique cuantos minutos falta para el fin de juego (iniciarla con el valor 30)
# Definir en el bloque principal dos objetos de la clase Jugador.
# Reducir dicha variable hasta llegar a cero.

class Jugador:
    tiempo_fin_de_juego = 30

    def __init__(self, nombre, puntaje):
        self.nombre = nombre
        self.puntaje = puntaje

    def imprimir(self):
        print(f"Nombre: {self.nombre}")
        print(f"Puntaje: {self.puntaje}")
        print(f"Tiempo restante: {self.tiempo_fin_de_juego} minutos\n")

    def pasar_tiempo(self):
        Jugador.tiempo_fin_de_juego -= 1


jugador1 = Jugador("Miguel Ángel", 100)
jugador2 = Jugador("Ángel", 150)

while Jugador.tiempo_fin_de_juego > 0:
    jugador1.pasar_tiempo()
    jugador2.pasar_tiempo()

jugador1.imprimir()
jugador2.imprimir()
