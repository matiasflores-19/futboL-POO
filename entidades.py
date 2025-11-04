from datetime import datetime, date
from enums import *

class Jugador:
    def __init__(self, dni, nombre, apellido, fecha_nacimiento, posicion):
        self.dni, self.nombre, self.apellido = dni, nombre, apellido
        self.fecha_nacimiento, self.posicion = fecha_nacimiento, posicion
        self.goles = self.amarillas = self.rojas = 0
        self.equipo = None
    def agregar_gol(self): self.goles += 1
    def __str__(self): return f"{self.nombre} {self.apellido}"

class Equipo:
    def __init__(self, nombre, categoria, año_fundacion, entrenador):
        self.nombre, self.categoria, self.año_fundacion, self.entrenador = nombre, categoria, año_fundacion, entrenador
        self.jugadores, self.puntos, self.gf, self.gc, self.pj = [], 0, 0, 0, 0
    def agregar_jugador(self, jugador):
        if jugador not in self.jugadores:
            self.jugadores.append(jugador)
            jugador.equipo = self
    def dg(self): return self.gf - self.gc
    def __str__(self): return self.nombre

class Estadio:
    def __init__(self, nombre, ubicacion, capacidad, tipo_cesped):
        self.nombre, self.ubicacion, self.capacidad, self.tipo_cesped = nombre, ubicacion, capacidad, tipo_cesped

class Arbitro:
    def __init__(self, id_arbitro, nombre, apellido, años_experiencia):
        self.id_arbitro, self.nombre, self.apellido, self.años_experiencia = id_arbitro, nombre, apellido, años_experiencia

class Partido:
    def __init__(self, fecha, estadio, local, visitante, arbitro):
        self.fecha, self.estadio, self.local, self.visitante, self.arbitro = fecha, estadio, local, visitante, arbitro
        self.gl, self.gv, self.finalizado, self.eventos = 0, 0, False, []
    
    def gol(self, equipo, jugador, minuto):
        if equipo == self.local: self.gl += 1
        elif equipo == self.visitante: self.gv += 1
        jugador.agregar_gol()
        self.eventos.append(f"Gol de {jugador} (min {minuto})")
    
    def finalizar(self): self.finalizado = True
    def __str__(self): return f"{self.local} {self.gl}-{self.gv} {self.visitante}"

class Torneo:
    def __init__(self, nombre, fecha_inicio, fecha_fin, categoria, formato):
        self.nombre, self.fecha_inicio, self.fecha_fin, self.categoria, self.formato = nombre, fecha_inicio, fecha_fin, categoria, formato
        self.equipos, self.partidos, self.tabla = [], [], {}
    
    def agregar_equipo(self, equipo):
        self.equipos.append(equipo)
        self.tabla[equipo] = {'pts': 0, 'pj': 0, 'gf': 0, 'gc': 0, 'dg': 0}
    
    def agregar_partido(self, partido): self.partidos.append(partido)
    
    def actualizar_tabla(self, partido):
        if not partido.finalizado: return
        
        loc, vis = partido.local, partido.visitante
        self.tabla[loc]['gf'] += partido.gl; self.tabla[loc]['gc'] += partido.gv
        self.tabla[vis]['gf'] += partido.gv; self.tabla[vis]['gc'] += partido.gl
        self.tabla[loc]['pj'] += 1; self.tabla[vis]['pj'] += 1
        
        if partido.gl > partido.gv: self.tabla[loc]['pts'] += 3
        elif partido.gl < partido.gv: self.tabla[vis]['pts'] += 3
        else: self.tabla[loc]['pts'] += 1; self.tabla[vis]['pts'] += 1
        
        self.tabla[loc]['dg'] = self.tabla[loc]['gf'] - self.tabla[loc]['gc']
        self.tabla[vis]['dg'] = self.tabla[vis]['gf'] - self.tabla[vis]['gc']
    
    def mostrar_tabla(self):
        tabla_ordenada = sorted(self.tabla.items(), key=lambda x: (x[1]['pts'], x[1]['dg']), reverse=True)
        print("TABLA DE POSICIONES:")
        for i, (equipo, stats) in enumerate(tabla_ordenada, 1):
            print(f"{i}. {equipo} - Pts: {stats['pts']} | DG: {stats['dg']}")