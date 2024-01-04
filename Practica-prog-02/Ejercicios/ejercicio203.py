class Cliente:
    clientes_suspendidos = []

    def __init__(self, codigo, nombre):
        self.codigo_cliente = codigo
        self.nombre_cliente = nombre

    def imprimir_informacion(self):
        print("Código:", self.codigo_cliente)
        print("Nombre:", self.nombre_cliente)
        self.esta_suspendido()

    def esta_suspendido(self):
        if self.codigo_cliente in Cliente.clientes_suspendidos:
            print("Está suspendido")
        else:
            print("No está suspendido")
        print("_____________________________")

    def suspender_cliente(self):
        Cliente.clientes_suspendidos.append(self.codigo_cliente)


cliente_1 = Cliente(1, "Miguel Ángel")
cliente_2 = Cliente(2, "Pedro")
cliente_3 = Cliente(3, "Pila")
cliente_4 = Cliente(4, "Alejandro")

cliente_3.suspender_cliente()
cliente_4.suspender_cliente()

cliente_1.imprimir_informacion()
cliente_2.imprimir_informacion()
cliente_3.imprimir_informacion()
cliente_4.imprimir_informacion()

print(Cliente.clientes_suspendidos)
