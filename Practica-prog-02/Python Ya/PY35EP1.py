# Se desea almacenar los datos de 3 alumnos. Definir un diccionario cuya clave sea el número de documento del alumno. Como valor almacenar una lista con componentes de tipo tupla donde almacenamos nombre de materia y su nota.
# Crear las siguientes funciones:
# 1) Carga de los alumnos (de cada alumno solicitar su dni y los nombres de las materias y sus notas)
# 2) Listado de todos los alumnos con sus notas
# 3) Consulta de un alumno por su dni, mostrar las materias que cursa y sus notas.

def cargar_alumnos():
    alumnos = {}

    for _ in range(3):
        dni = input("\nIngresa el número de documento del alumno: ")
        materias_notas = []

        cantidad_materias = int(input("Ingresa la cantidad de materias que cursa el alumno: "))
        for _ in range(cantidad_materias):
            materia = input("Ingresa el nombre de la materia: ")
            nota = float(input(f"Ingresa la nota de {materia}: "))

            tupla_materia_nota = (materia, nota)
            materias_notas.append(tupla_materia_nota)

        alumnos[dni] = materias_notas

    return alumnos

def listar_alumnos_notas(diccionario):
    print("\nListado de todos los alumnos con sus notas:")
    for dni, materias_notas in diccionario.items():
        print(f"\nNúmero de Documento: {dni}")
        print("Materias y Notas:")
        for materia, nota in materias_notas:
            print(f"- {materia}: {nota}")

def consultar_alumno_por_dni(diccionario, dni_consulta):
    if dni_consulta in diccionario:
        materias_notas = diccionario[dni_consulta]
        print(f"\nAlumno con número de documento {dni_consulta}:")
        print("Materias y Notas:")
        for materia, nota in materias_notas:
            print(f"- {materia}: {nota}")
    else:
        print("\nNo se encontró ningún alumno con ese número de documento.")

alumnos_dict = cargar_alumnos()

listar_alumnos_notas(alumnos_dict)

dni_a_consultar = input("\nIngresa el número de documento para consultar al alumno: ")
consultar_alumno_por_dni(alumnos_dict, dni_a_consultar)
