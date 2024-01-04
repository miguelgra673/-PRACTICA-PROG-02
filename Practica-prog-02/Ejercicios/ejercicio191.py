class Punto:

    def __init__(self, coordenada_x, coordenada_y):
        self.coordenada_x = coordenada_x
        self.coordenada_y = coordenada_y

    def imprimir(self):
        print("Coordenada del punto")
        print("(", self.coordenada_x, ",", self.coordenada_y, ")")

    def imprimir_cuadrante(self):
        if self.coordenada_x > 0 and self.coordenada_y > 0:
            print("Primer cuadrante")
        elif self.coordenada_x < 0 and self.coordenada_y > 0:
            print("Segundo cuadrante")
        elif self.coordenada_x < 0 and self.coordenada_y < 0:
            print("Tercer cuadrante")
        elif self.coordenada_x > 0 and self.coordenada_y < 0:
            print("Cuarto cuadrante")


punto_1 = Punto(10, -2)
punto_1.imprimir()
punto_1.imprimir_cuadrante()
