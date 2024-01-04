import random

class Dado:

    def lanzar(self):
        self.valor = random.randint(1, 6)

    def imprimir_valor(self):
        print("Valor del dado:", self.valor)

    def obtener_valor(self):
        return self.valor


class JuegoDeDados:

    def __init__(self):
        self.dado1 = Dado()
        self.dado2 = Dado()
        self.dado3 = Dado()

    def jugar(self):
        self.dado1.lanzar()
        self.dado1.imprimir_valor()
        self.dado2.lanzar()
        self.dado2.imprimir_valor()
        self.dado3.lanzar()
        self.dado3.imprimir_valor()
        if self.dado1.obtener_valor() == self.dado2.obtener_valor() == self.dado3.obtener_valor():
            print("Gano")
        else:
            print("Perdio")


juego_dados = JuegoDeDados()
juego_dados.jugar()
