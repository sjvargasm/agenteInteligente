import json
from random import randrange


class Habitacion:
    """
    Clase que representa una habitación en el mundo.
    """
    index = 0
    nivelDeSuciedad = 0
    estado = "Limpio"
    nombre = ""

    def __init__(self, nombre):
        self.nombre = nombre

    def __str__(self):
        self_info = {
            "Indice": self.index,
            "Nombre": self.nombre,
            "Estado": self.estado,
            "Nivel de suciedad": self.nivelDeSuciedad,
        }
        return json.dumps(self_info, indent=2)

    def ensuciar(self):
        """
        Aumenta el nivel de suciedad de la habitación en 1 ("Ensucia la habitación"). 
        Si el estado de la habitación era `"Limpio"`, lo cambia a `"Sucio"` cuando ` nivelDeSuciedad > 0`.
        """
        self.nivelDeSuciedad += 1
        if self.nivelDeSuciedad > 0:
            self.estado = "Sucio"

    def limpiar(self):
        """
        Disminuye el nivel de suciedad de la habitación en 1 ("Limpia la habitación"). 
        Si el estado de la habitación era `"Sucio"`, lo cambia a `"Limpio"` cuando `nivelDeSuciedad <= 0`.
        """
        self.nivelDeSuciedad -= 1
        if self.nivelDeSuciedad <= 0:
            self.estado = "Limpio"
            self.nivelDeSuciedad = 0

    def getIndex(self):
        """
        Devuelve el índice de la habitación (Su ubicación en la lista de habitaciones).
        """
        return self.index

    def setIndex(self, index):
        """
        Configura el índice de la habitación (Su ubicación en la lista de habitaciones).
        """
        self.index = index


class Mundo:
    """
    Es el entorno donde el agente se desenvuelve. Contiene una lista de habitaciones.
    Características: Totalmente observable - Determinista - Secuencal - Dinámico - Discreto - Individual
    """
    def __init__(self, habitaciones=[Habitacion("A"), Habitacion("B")]):
        self.numeroDeHabitaciones = len(habitaciones)
        self.habitaciones = habitaciones
        self.ordenarHabitaciones()

    def __str__(self):
        habitacionesList = []
        for habitacion in self.habitaciones:
            habitacionesList.append(json.loads(habitacion.__str__()))

        self_info = {
            "Numero habitaciones": self.numeroDeHabitaciones,
            "Habitaciones": habitacionesList,
        }

        return json.dumps(self_info, indent=2)

    def ensuciarHabitacion(self, habitacion=-1):
        """
        Ensucia la habitacion `habitacion`. Si dicho parámetro no se especifica, se ensucia una habitación aleatoria
        """
        if habitacion <= 0:
            numeroDeHabitacion = randrange(0, len(self.habitaciones))
            self.habitaciones[numeroDeHabitacion].ensuciar()
        else:
            self.habitaciones[habitacion].ensuciar()

    def ordenarHabitaciones(self):
        """
        Se asigna a cada habitación un número que indica su ubicación en el mundo
        """
        i = 0
        for habitacion in self.habitaciones:
            habitacion.setIndex(i)
            i += 1
