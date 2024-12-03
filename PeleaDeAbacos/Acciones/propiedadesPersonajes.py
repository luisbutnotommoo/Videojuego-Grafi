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
from Acciones.boceto2 import  PersonajesDeTodos
import Acciones.boceto2 as b
from Acciones.colisionRectangular import RectangularCollision3D
from Acciones.textos import textos as tx

class Propiedades:
    def __init__(self, personajes=[]):
        self.estado_emma=0
        self.estado_luis=0
        self.personajesJugables=[]
        self.arregloPersonajes=personajes
        self.personajesAElegir=[
            #Personaje emma izquuierda
           {"nombre": "Emma", "estado": 0, "objeto": PersonajesDeTodos("Emma", b.figuraEmma(0),posicion=(-25, -10, 0), rotacion=30, escala=(0.6, 0.6, 0.6))},
            #Personaje Luis Izquierda
            {"nombre": "Luis", "estado": 0, "objeto": PersonajesDeTodos("Luis", b.figuraLuis(0),posicion=(-18, -9, 0), escala=(3.5, 3.5, 3.5))},
            #Personaje lin izquierda
             {"nombre": "LinDer", "estado": 0, "objeto": PersonajesDeTodos("Lin", b.figuraLin(0),posicion=(5, -8, 0), rotacion=-10, escala=(1.1, 1.1, 1.1))},
           
           
            #Personaje starenka Izquierda
            {"nombre": "Star", "estado": 0, "objeto": PersonajesDeTodos("Star", b.figuraStar(0),posicion=(-23, -10, 0), rotacion=30, escala=(0.7, 0.7, 0.7))}, 
           #Personaje emma derecha
           
           {"nombre": "EmmaDer", "estado": 0, "objeto": PersonajesDeTodos("Emma", b.figuraEmma(0),posicion=(10, -10, 0), rotacion=-10, escala=(0.6, 0.6, 0.6))},
          #Personaje luis derecha
           {"nombre": "LuisDer", "estado": 0, "objeto": PersonajesDeTodos("Luis", b.figuraLuis(0),posicion=(18, -9, 0), escala=(3.5, 3.5, 3.5))},
           #Personaje Lin derecha
          {"nombre": "Lin", "estado": 0, "objeto": PersonajesDeTodos("Lin", b.figuraLin(0),posicion=(38, -8, 0), rotacion=-10, escala=(1.1, 1.1, 1.1))},
           
           #Personaje starenka derecha
           {"nombre": "StarDer", "estado": 0, "objeto": PersonajesDeTodos("Star", b.figuraStar(0),posicion=(20, -10, 0), rotacion=0, escala=(0.7, 0.7, 0.7))}
        ]

        
        
        print("Personajes Jugables dentro de propiedades:", self.arregloPersonajes)
        for i in range(2):
            for j in range(len(self.personajesAElegir)):
                if(self.arregloPersonajes[i]==j):

                    self.personajesJugables.append(self.personajesAElegir[j])
                    print("Personaje almacenado ", self.personajesJugables[i])
