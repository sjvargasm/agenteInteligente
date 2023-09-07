#!/usr/bin/python3

from simulador import Simulador
from ambiente import Mundo, Habitacion
from agente import AgenteReactivoSimple as Agente

from time import sleep
from datetime import datetime
from os import system

# Configuración de mundo
listaHabitaciones = [
    Habitacion("Sala"),
    Habitacion("Cocina"),
    Habitacion("Comedor"),
    Habitacion("Dormitorio"),
    Habitacion("Sotano"),
    Habitacion("Atico")
]
mundo = Mundo(listaHabitaciones)

# Configuración del agente
configAgent = {
    "nombre": "Wall-E",
    "mundo": mundo,
    "rendimientoPorLimpiar": 3,
    "rendimientoPorPaso": -2,
    "rendimientoPorCasa": -1000
}
agente = Agente(configAgent)

# Configuración de la simulación
configSim = {
    "intervaloDeLimpieza": 2,
    "retardoMaximoParaEnsuciar": 5,
    "mundo": mundo,
    "agente": agente,
    "listaHabitaciones": listaHabitaciones
}
sim = Simulador(configSim)

# Inicio
simThread = sim.run()
while True:
    system("clear")
    print(datetime.now())
    print(sim)
    sleep(1/20)
