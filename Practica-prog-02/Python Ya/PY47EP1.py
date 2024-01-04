# Declarar una clase Cuenta y dos subclases CajaAhorra y PlazoFijo. Definir los atributos y métodos comunes entre una caja de ahorro y un plazo fijo y agruparlos en la clase Cuenta.
# Una caja de ahorro y un plazo fijo tienen un nombre de titular y un monto. Un plazo fijo añade un plazo de imposición en días y una tasa de interés. Hacer que la caja de ahorro no genera intereses.
# En el bloque principal del programa definir un objeto de la clase CajaAhorro y otro de la clase PlazoFijo.

class Cuenta:
    def __init__(self, titular, monto):
        self.titular = titular
        self.monto = monto

    def mostrar_informacion(self):
        print(f"Titular: {self.titular}")
        print(f"Monto: ${self.monto:.2f}")


class CajaAhorro(Cuenta):
    def __init__(self, titular, monto):
        super().__init__(titular, monto)
        self.intereses = 0

    def mostrar_informacion(self):
        super().mostrar_informacion()
        print("Tipo de cuenta: Caja de Ahorro")
        print(f"Intereses generados: ${self.intereses:.2f}")


class PlazoFijo(Cuenta):
    def __init__(self, titular, monto, plazo, tasa_interes):
        super().__init__(titular, monto)
        self.plazo = plazo
        self.tasa_interes = tasa_interes

    def calcular_intereses(self):
        self.intereses = self.monto * (self.tasa_interes / 100) * (self.plazo / 365)

    def mostrar_informacion(self):
        super().mostrar_informacion()
        print("Tipo de cuenta: Plazo Fijo")
        print(f"Plazo de imposición: {self.plazo} días")
        print(f"Tasa de interés: {self.tasa_interes}%")
        print(f"Intereses generados: ${self.intereses:.2f}")


# Bloque principal del programa
caja_ahorro = CajaAhorro("Miguel Ángel", 1000)
caja_ahorro.mostrar_informacion()

plazo_fijo = PlazoFijo("Pepito Martínez", 5000, 90, 5)
plazo_fijo.calcular_intereses()
plazo_fijo.mostrar_informacion()
