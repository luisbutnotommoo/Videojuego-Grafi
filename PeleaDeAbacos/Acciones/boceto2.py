from OpenGL.GLU import *
from OpenGL.GL import *
from OpenGL.GLUT import *
from pygame.locals import *
from PIL import Image
# from Acciones import objetos as obj
from PersonajeLuis.dibujaPersonajeLuisEmocion import Personaje
from PersonajeEmma.emocioneJuegoEmma import NewtJuego
from PersonajeStarenka.clasePintar import PintarPersonajeStar
from PersonajeLin.blue_multiverso.dibujaPersonajeJuegoEmocion import pesonajeLinEmocionesJuego as PersonajeLin
import math

class PersonajesDeTodos:
    def __init__(self, nombre, funciones_dibujo, posicion=(0, 0, 0), rotacion=0, escala=(1.0, 1.0, 1.0), emocion=0):
        self.nombre = nombre
        self.funciones_dibujo = funciones_dibujo
        self.posicion = posicion
        self.escala = escala
        self.rotacion = rotacion
        self.jumping = False
        self.jump_height = 5.0
        self.jump_speed = 0.5
        self.initial_y = self.posicion[1]
        self.estado_emocion = emocion  # Agregar un atributo para el estado de la emoción

    def set_position(self, x, y, z):
        self.posicion = (x, y, z)

    def set_scale(self, x, y, z):
        self.escala = (x, y, z)

    def render(self):
        x, y, z = self.posicion
        glPushMatrix()
        glTranslatef(x, y, z)
        glRotatef(self.rotacion, 0, 1, 0)
        glScalef(self.escala[0], self.escala[1], self.escala[2])
        
         
        for i, funcion in enumerate(self.funciones_dibujo):
            funcion(self.estado_emocion)  # Pass the current emotion state
        glPopMatrix()

    def jump(self):
        if self.jumping:
            if self.posicion[1] < self.initial_y + self.jump_height:
                self.posicion = (self.posicion[0], self.posicion[1] + self.jump_speed, self.posicion[2])
            else:
                self.jumping = False
        else:
            if self.posicion[1] > self.initial_y:
                self.posicion = (self.posicion[0], self.posicion[1] - self.jump_speed, self.posicion[2])
            else:
                self.posicion = (self.posicion[0], self.initial_y, self.posicion[2])

    def start_jump(self):
        if not self.jumping:
            self.jumping = True

    # Nuevo método para actualizar la emoción del personaje
    def set_emotion(self, emocion):
        self.estado_emocion = emocion  # Cambiar el estado de la emoción


# Función para generar los personajes con lambdas para manejar emociones
def figuraLuis(emocion):
    temp = Personaje(emocion)
    return [lambda emocion=emocion: temp.render_personaje(emocion)]  # Capture emotion correctly

def figuraEmma(emocion):
    temp2 = NewtJuego(emocion)
    return [lambda emocion=emocion: temp2.personaje(emocion)]  # Capture emotion correctly

def figuraLin(emocion):
    temp3 = PersonajeLin(emocion)
    return [lambda emocion=emocion: temp3.personaje(emocion)]  # Capture emotion correctly

def figuraStar(emocion):
    temp4 = PintarPersonajeStar(emocion)
    return [lambda emocion=emocion: temp4.Personaje(emocion)]  # Capture emotion correctly


