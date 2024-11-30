import pygame
from OpenGL.GLU import*
from OpenGL.GL import*
from OpenGL.GLUT import*
from pygame.locals import*
from PIL import*
import Acciones.objetosTextura as obj
import Acciones.escenario as esc
import Acciones.viewPortPreguntas as view
import Acciones.bancoPreguntas as bp
from Acciones.boceto import  PersonajesDeTodos
import Acciones.boceto as b
from Acciones.colisionRectangular import RectangularCollision3D
from Acciones.texto import textos as tx

class Propiedades:
    def __init__(self, personaje1, personaje2):
        self.estado_emma=0
        self.estado_luis=0
        personajesAElegir=[
            #Personaje emma izquuierda
           {"nombre": "Emma", "estado": 0, "objeto": PersonajesDeTodos("Emma", b.figuraEmma(0),posicion=(-25, -10, 0), rotacion=30, escala=(0.6, 0.6, 0.6))},
           #Personaje emma derecha
           {"nombre": "Emma", "estado": 0, "objeto": PersonajesDeTodos("Emma", b.figuraEmma(0),posicion=(10, -10, 0), rotacion=-10, escala=(0.6, 0.6, 0.6))},
           #Personaje lin izquierda
           {"nombre": "Lin", "estado": 0, "objeto": PersonajesDeTodos("Lin", b.figuraLin(0),posicion=(38, -8, 0), rotacion=-10, escala=(1.1, 1.1, 1.1))},
           #Personaje Lin derecha
           {"nombre": "Lin", "estado": 0, "objeto": PersonajesDeTodos("Lin", b.figuraLin(0),posicion=(5, -8, 0), rotacion=-10, escala=(1.1, 1.1, 1.1))},
            #Personaje Luis Izquierda
            {"nombre": "Luis", "estado": 0, "objeto": PersonajesDeTodos("Luis", b.figuraLuis(0),posicion=(-18, -9, 0), escala=(3.5, 3.5, 3.5))},
           #Personaje luis derecha
           {"nombre": "Luis", "estado": 0, "objeto": PersonajesDeTodos("Luis", b.figuraLuis(0),posicion=(18, -9, 0), escala=(3.5, 3.5, 3.5))},
           #Personaje starenka Izquierda
            {"nombre": "Star", "estado": 0, "objeto": PersonajesDeTodos("Star", b.figuraStar(0),posicion=(-23, -10, 0), rotacion=30, escala=(0.6, 0.6, 0.6))},
           #Personaje starenka derecha
           {"nombre": "Star", "estado": 0, "objeto": PersonajesDeTodos("Star", b.figuraStar(0),posicion=(20, -10, 0), rotacion=0, escala=(0.6, 0.6, 0.6))}
        ]
        self.personajesJugables=[]
        self.personaje=0
        for i in personajesAElegir:
            if personaje1==i:
                self.personajesJugables.append(personajesAElegir[i])
            if personaje2==i:
                self.personajesJugables.append(personajesAElegir[i])

   