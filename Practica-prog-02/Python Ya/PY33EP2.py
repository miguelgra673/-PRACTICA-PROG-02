# Almacenar los nombres de 5 productos y sus precios. Utilizar una lista y cada elemento una tupla con el nombre y el precio.
# Desarrollar las funciones:
# 1) Cargar por teclado.
# 2) Listar los productos y precios.
# 3) Imprimir los productos con precios comprendidos entre 10 y 15.

def cargar_productos():
    productos = []

    for _ in range(5):
        nombre = input("Ingrese el nombre del producto: ")
        precio = float(input("Ingrese el precio del producto: "))

        tupla_producto = (nombre, precio)
        productos.append(tupla_producto)

    return productos

def listar_productos_precios(productos):
    print("\nLista de productos y precios:")
    for nombre, precio in productos:
        print(f"{nombre}: ${precio}")

def imprimir_productos_entre_precios(productos, precio_min, precio_max):
    print(f"\nProductos con precios entre ${precio_min} y ${precio_max}:")
    for nombre, precio in productos:
        if precio_min <= precio <= precio_max:
            print(f"{nombre}: ${precio}")

#Puesa en prácitca
productos = cargar_productos()

listar_productos_precios(productos)

precio_minimo = 10
precio_maximo = 15
imprimir_productos_entre_precios(productos, precio_minimo, precio_maximo)
