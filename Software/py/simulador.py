from random import randrange
import sched, time, json
from os import system

class Simulador:
    """
    # Simulador del mundo
    ## Funcionamiento
    El scheduler `scheduler` es el motor del mundo, cada ciertos intervalos, alguna acción ocurre:
    - En un intervalo aleatorio, entre 0 y `retardoMaximoParaEnsuciar`, se ejecuta el método `mundo.ensuciarHabitacion()`
    - En un intervalo de `intervaloDeLimpieza`, se ejecuta el método `agente.run()`

    ## Configuración
    Las configuraciones del simulador se reciben como un diccionario, parámetro del método constructor, con las siguientes claves:
    - `"mundo"`: Objeto `Mundo` que representa el mundo donde el agente se desenvuelve.
    - `"agente"`: Objeto `Agente` que representa el agente en cuestión.
    - `"intervaloDeLimpieza"`: Intervalo en segundos cada cual se ejecuta `agente.run()`
    - `"retardoMaximoParaEnsuciar"`: Tiempo máximo en segundos que puede tardar el simulador en ejecutar `mundo.ensuciarHabitacion()`

    ## Problemas conocidos
    - Es posible que el scheduler sufra de time-drifting.
    """
    scheduler = sched.scheduler(time.monotonic)
    def __init__(self, config):

        # Parámetros de simulación
        self.mundo = config["mundo"]
        self.agente = config["agente"]
        self.intervaloDeLimpieza = config["intervaloDeLimpieza"]
        self.retardoMaximoParaEnsuciar = config["retardoMaximoParaEnsuciar"]

        # Definición de intervalos
        self.scheduler.enter(0, 1, self.ensuciarHabitacion)
        self.scheduler.enter(0, 2, self.limpiarHabitacion)

    def __str__(self):
        infoMundo = json.loads(self.mundo.__str__())
        infoAgente = json.loads(self.agente.__str__())
        self_info = {
            "Mundo" : infoMundo,
            "Agente": infoAgente
        }
        return json.dumps(self_info, indent = 2)

    def ensuciarHabitacion(self):
        """
        En un intervalo aleatorio entre o y `retardoMaximoParaEnsuciar` segundos, el simulador ensucia el mundo
        """
        self.scheduler.enter(randrange(0, self.retardoMaximoParaEnsuciar), 1, self.ensuciarHabitacion)
        self.mundo.ensuciarHabitacion()
        print(self)

    def limpiarHabitacion(self):
        """
        En un intervalo de `intervaloDeLimpieza` segundos, el simulador limpia el mundo
        """
        self.scheduler.enter(self.intervaloDeLimpieza, 2, self.limpiarHabitacion)
        self.agente.run()
        print(self)

    def run(self):
        """
        Inicia el scheduler y con ello la simulación del sistema.
        """
        self.scheduler.run()