# En un hospital hay diferentes tipos de personal: médicos, enfermeros y administrativos. De todos
# guardamos su información básica (dni, nombre, dirección y teléfono), de los médicos almacenamos
# también su especialidad, y de los enfermeros la planta en la que trabajan.
# Al hospital acuden pacientes. De todos ellos se guarda un historial con su dni, nombre, dirección,
# teléfono, y un conjunto de pruebas y consultas que hayan hecho en el hospital. De cada prueba o
# consulta guardamos la fecha en que se hizo, y el médico que le atendió
# Define las clases necesarias para el enunciado propuesto en un programa llamado Hospital.py. Define
# un programa principal que cree un array de personal de hospital con varios médicos y enfermeros.
# Define un paciente con sus datos, y dale de alta diversas pruebas realizadas por varios médicos.
# Finalmente, trata de mostrar por pantalla los datos completos del paciente, incluyendo su historial de
# pruebas.
# Hospital.py

class Persona:
    def __init__(self, dni, nombre, direccion, telefono):
        self.dni = dni
        self.nombre = nombre
        self.direccion = direccion
        self.telefono = telefono

class Medico(Persona):
    def __init__(self, dni, nombre, direccion, telefono, especialidad):
        super().__init__(dni, nombre, direccion, telefono)
        self.especialidad = especialidad

class Enfermero(Persona):
    def __init__(self, dni, nombre, direccion, telefono, planta):
        super().__init__(dni, nombre, direccion, telefono)
        self.planta = planta

class PruebaConsulta:
    def __init__(self, fecha, medico):
        self.fecha = fecha
        self.medico = medico

class Paciente(Persona):
    def __init__(self, dni, nombre, direccion, telefono):
        super().__init__(dni, nombre, direccion, telefono)
        self.historial = []

    def agregar_prueba_consulta(self, prueba_consulta):
        self.historial.append(prueba_consulta)

if __name__ == "__main__":
    personal_hospital = [
        Medico("123456789", "Dr. Pedro Cavadas", "Calle Falsa, 123", "632145267", "Traumatólogo"),
        Enfermero("987654321", "Enfermera Ana Garcia", "Calle Falsa, 123", "61324567", 3),
    ]

    paciente = Paciente("123456789B", "Manolo Lama", "Calle Falsa, 123", "61234567")

    paciente.agregar_prueba_consulta(PruebaConsulta("2024-01-01", personal_hospital[0]))
    paciente.agregar_prueba_consulta(PruebaConsulta("2024-02-01", personal_hospital[1]))

    print(f"Datos del paciente:\nDNI: {paciente.dni}\nNombre: {paciente.nombre}\n"
          f"Dirección: {paciente.direccion}\nTeléfono: {paciente.telefono}\n")

    print("Historial de pruebas y consultas:")
    for prueba in paciente.historial:
        print(f"Fecha: {prueba.fecha}\nMédico: {prueba.medico.nombre} - Especialidad: {getattr(prueba.medico, 'especialidad', 'N/A')}\n")
