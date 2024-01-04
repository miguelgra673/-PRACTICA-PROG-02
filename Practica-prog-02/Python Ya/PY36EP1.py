# Crear un diccionario en Python para almacenar los datos de empleados de una empresa. La clave será su número de legajo y en su valor almacenar una lista con el nombre, profesión y sueldo.
# Desarrollar las siguientes funciones:
# 1) Carga de datos de empleados.
# 2) Permitir modificar el sueldo de un empleado. Ingresamos su número de legajo para buscarlo.
# 3) Mostrar todos los datos de empleados que tienen una profesión de "analista de sistemas"

def cargar_empleados():
    empleados = {}

    cantidad_empleados = int(input("Ingresa la cantidad de empleados: "))
    for _ in range(cantidad_empleados):
        legajo = input("\nIngresa el número de legajo del empleado: ")
        nombre = input("Ingresa el nombre del empleado: ")
        profesion = input("Ingresa la profesión del empleado: ")
        sueldo = float(input("Ingresa el sueldo del empleado: "))

        datos_empleado = [nombre, profesion, sueldo]
        empleados[legajo] = datos_empleado

    return empleados

def modificar_sueldo(empleados, legajo_modificar, nuevo_sueldo):
    if legajo_modificar in empleados:
        empleados[legajo_modificar][2] = nuevo_sueldo
        print(f"\nSueldo del empleado con legajo {legajo_modificar} modificado correctamente.")
    else:
        print("\nNo se ha encontado ningún empleado con ese número de legajo.")

def mostrar_analistas_sistemas(empleados):
    print("\nEmpleados con profesión de 'analista de sistemas':")
    for legajo, datos_empleado in empleados.items():
        if datos_empleado[1].lower() == "analista de sistemas":
            print(f"\nNúmero de Legajo: {legajo}")
            print(f"Nombre: {datos_empleado[0]}")
            print(f"Profesión: {datos_empleado[1]}")
            print(f"Sueldo: {datos_empleado[2]}")

#Ejemplo
empleados_dict = cargar_empleados()

legajo_a_modificar = input("\nIngresa el número de legajo para modificar el sueldo: ")
nuevo_sueldo = float(input("Ingresa el nuevo sueldo: "))
modificar_sueldo(empleados_dict, legajo_a_modificar, nuevo_sueldo)

mostrar_analistas_sistemas(empleados_dict)
