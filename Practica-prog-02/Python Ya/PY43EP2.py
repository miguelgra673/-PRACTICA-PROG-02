# Desarrollar un programa que cargue los lados de un triángulo e implemente los siguientes métodos: 
# inicializar los atributos, imprimir el valor del lado mayor y otro método que muestre si es equilátero o no. El nombre de la clase llamarla Triangulo.

class Triangulo:
    def __init__(self):
        self.a = 0
        self.b = 0
        self.c = 0

    def cargar_lados(self):
        self.a = float(input("Ingresa el lado a: "))
        self.b = float(input("Ingresa el lado b: "))
        self.c = float(input("Ingresa el lado c: "))

    def imprimir_lado_mayor(self):
        lado_mayor = max(self.a, self.b, self.c)
        print(f"El lado mayor del triángulo es: {lado_mayor}")

    def es_equilatero(self):
        if self.a == self.b == self.c:
            print("El triángulo es equilátero.")
        else:
            print("El triángulo no es equilátero.")


triangulo = Triangulo()

triangulo.cargar_lados()

triangulo.imprimir_lado_mayor()

triangulo.es_equilatero()
