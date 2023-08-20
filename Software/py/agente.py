import json

class AgenteReactivoSimple:
    """
    # Agente reactivo simple
    ## Configuración
    Las configuraciones del agente se reciben como un diccionario, parámetro del método constructor, con las siguientes claves:
    - `"mundo"`: Objeto mundo donde se desenvolverá el agente
    - `"nombre"`: Nombre del agente
    - `"rendimientoPorLimpiar"`: Puntuación por limpiar una habitación
    - `"rendimientoPorPaso"`: Puntuación por cambiar de habitación (o dar un paso)
    - `"rendimientoPorCasa"`: Puntuación por volver a casa (Aun no se utiliza)
    """
    def __init__(self, config):
        self.rendimiento = 0
        self.mundo = config["mundo"]
        self.habitacionActual = self.mundo.habitaciones[0]
        self.nombre = config["nombre"]
        self.indicadoresDeRendimiento = {
            "rendimientoPorLimpiar": config["rendimientoPorLimpiar"],
            "rendimientoPorPaso": config["rendimientoPorPaso"],
            "rendimientoPorCasa": config["rendimientoPorCasa"]
        }
    
    def __str__(self):
        habitacionActualInfo = json.loads(self.habitacionActual.__str__())
        self_info = {
            "Nombre": self.nombre,
            "Rendimiento": self.rendimiento,
            "Ubicacion": habitacionActualInfo
        }
        return json.dumps(self_info, indent=2)

    def verificarSensor(self):
        """
        Revisa el estado actual de la habitación en el que el agente se encuentra.
        """
        return self.habitacionActual.estado

    def limpiar(self):
        """
        Ejecuta el método `limpiar()` del a habitación donde se encuentra. 
        También agrega al rendimiento del agente su puntuación por limpiar.
        """
        self.habitacionActual.limpiar()
        self.rendimiento += self.indicadoresDeRendimiento["rendimientoPorLimpiar"]

    def cambiarHabitacion(self):
        """
        Cambia a la siguiente habitación de la lista. Volviendo al principio cuando se llega al final de la lista. 
        También agrega al rendimiento del agente su puntuación por cambiar de habitación.
        """
        indiceHabitacionNueva = self.habitacionActual.getIndex() + 1
        if indiceHabitacionNueva >= len(self.mundo.habitaciones):
            indiceHabitacionNueva = 0
        self.habitacionActual = self.mundo.habitaciones[indiceHabitacionNueva]
        self.rendimiento += self.indicadoresDeRendimiento["rendimientoPorPaso"]

    def run(self):
        """
        Corre un ciclo del agente:
        1. Verifica los sensores del agente con `verificarSensor()`.
        2. Si el estado del sensor es diferente de `"Limpio"`, ejecuta su método `limpiar()`.
        3. En caso contrario, cambia a la siguiente habitación de la lista.
        
        Retorna la acción realizada
        """
        if self.verificarSensor() != "Limpio":
            self.limpiar()
            accion = "Limpiar"
        else:
            self.cambiarHabitacion()
            accion = "Siguiente"

        return accion