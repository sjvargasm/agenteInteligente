from simulador import Simulador
from ambiente import Mundo, Habitacion
from agente import AgenteReactivoSimple as Agente

# Configuración de mundo
listaHabitaciones = [
    Habitacion("Sala"),
    Habitacion("Cocina"),
    Habitacion("Comedor"),
    Habitacion("Dormitorio")
]
mundo = Mundo(listaHabitaciones)

# Configuración del agente
configAgent = {
    "nombre": "Wall-E",
    "mundo": mundo,
    "rendimientoPorLimpiar": 4,
    "rendimientoPorPaso": -1,
    "rendimientoPorCasa": -1000
}
agente = Agente(configAgent)

# Configuración de la simulación
configSim = {
    "intervaloDeLimpieza": 2,
    "retardoMaximoParaEnsuciar": 20,
    "mundo": mundo,
    "agente": agente,
    "listaHabitaciones": listaHabitaciones
}
sim = Simulador(configSim)

sim.run()