# Se tiene que cargar los votos obtenidos por tres candidatos a una elección.
# En una lista cargar en la primer componente el nombre del candidato y en la segunda componente cargar una lista con componentes de tipo tupla con el nombre de la provincia y la cantidad de votos obtenidos en dicha provincia.
# Se deben cargar los datos por teclado, pero si se cargaran por asignación tendría una estructura similar a esta:

def cargar_votos():
    candidatos = []

    for i in range(3):
        nombre_candidato = input("Ingresa el nombre del candidato: ")

        provincias_votos = []
        cantidad_provincias = int(input("Ingresa la cantidad de provincias votadas para este candidato: "))

        for j in range(cantidad_provincias):
            nombre_provincia = input("Ingresa el nombre de la provincia: ")
            votos_provincia = int(input(f"Ingresa la cantidad de votos en {nombre_provincia}: "))

            tupla_provincia_votos = (nombre_provincia, votos_provincia)
            provincias_votos.append(tupla_provincia_votos)

        tupla_candidato_votos = (nombre_candidato, provincias_votos)
        candidatos.append(tupla_candidato_votos)

    return candidatos

candidatos = cargar_votos()

print("Datos cargados:")
print(candidatos)
