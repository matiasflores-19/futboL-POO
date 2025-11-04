from datetime import datetime, date
from enums import *
from entidades import *

# Crear datos de prueba
estadio = Estadio("Estadio Municipal", "Centro", 5000, TipoCesped.NATURAL)  # CORREGIDO: NATURAL
arbitro = Arbitro("ARB001", "Carlos", "Gonzalez", 10)  # CORREGIDO: ARB001

equipo1 = Equipo("Los Halcones", "Sub-20", 1990, "Roberto Silva")  # CORREGIDO: equipo1
equipo2 = Equipo("Los Tigres", "Sub-20", 1985, "Miguel Ángel")     # CORREGIDO: equipo2

jugador1 = Jugador("12345678", "Luis", "Perez", date(2003, 5, 15), PosicionJugador.DELANTERO)  # CORREGIDO: DELANTERO
jugador2 = Jugador("23456789", "Pedro", "Gomez", date(2002, 8, 20), PosicionJugador.MEDIOCAMPISTA)

equipo1.agregar_jugador(jugador1)  # CORREGIDO: jugador1 (minúscula)
equipo2.agregar_jugador(jugador2)  # CORREGIDO: jugador2 (minúscula)

torneo = Torneo("Torneo Apertura", date(2024, 1, 15), date(2024, 6, 15), "Sub-20", FormatoTorneo.LIGA)
torneo.agregar_equipo(equipo1)  # CORREGIDO: equipo1
torneo.agregar_equipo(equipo2)  # CORREGIDO: equipo2

# Simular partido
partido = Partido(datetime(2024, 2, 1, 16, 0), estadio, equipo1, equipo2, arbitro)  # CORREGIDO: equipo1 vs equipo2
torneo.agregar_partido(partido)

partido.gol(equipo1, jugador1, 25)
partido.gol(equipo2, jugador2, 60)  # CORREGIDO: equipo2
partido.finalizar()

torneo.actualizar_tabla(partido)  # CORREGIDO: actualizar_tabla

# Mostrar resultados
print("=== SISTEMA TORNEOS ===")
print(f"Torneo: {torneo.nombre}")
print(f"Partido: {partido}")
print(f"Goles de {jugador1}: {jugador1.goles}")
print(f"Goles de {jugador2}: {jugador2.goles}")
torneo.mostrar_tabla()