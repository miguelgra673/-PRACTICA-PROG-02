# Implementar la clase Operaciones. Se deben cargar dos valores enteros por teclado en el método __init__, 
# calcular su suma, resta, multiplicación y división, cada una en un método, imprimir dichos resultados.

class Operaciones:
    def __init__(self):
        self.valor1 = int(input("Ingresa el primer valor entero: "))
        self.valor2 = int(input("Ingresa el segundo valor entero: "))

    def suma(self):
        resultado = self.valor1 + self.valor2
        return resultado

    def resta(self):
        resultado = self.valor1 - self.valor2
        return resultado

    def multiplicacion(self):
        resultado = self.valor1 * self.valor2
        return resultado

    def division(self):
        if self.valor2 != 0:
            resultado = self.valor1 / self.valor2
            return resultado
        else:
            return "No se puede dividir por cero."

    def imprimir_resultados(self):
        print(f"Suma: {self.suma()}")
        print(f"Resta: {self.resta()}")
        print(f"Multiplicación: {self.multiplicacion()}")
        print(f"División: {self.division()}")


operaciones = Operaciones()

operaciones.imprimir_resultados()
