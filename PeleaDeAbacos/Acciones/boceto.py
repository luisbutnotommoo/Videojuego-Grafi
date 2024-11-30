from OpenGL.GLU import*
from OpenGL.GL import*
from OpenGL.GLUT import*
from pygame.locals import*
from PIL import*
#from Acciones import objetos as obj
from PersonajeLuis.AccionesLuis.personaje import Personaje
from PersonajeEmma.actionsEV.clasePersonaje import Newt
from PersonajeStarenka.clasePintar import PintarPersonajeStar
from PersonajeLin.blue_multiverso.dibujaPersonajeJuegoEmocion import pesonajeLinEmocionesJuego as PersonajeLin
import math

class PersonajesDeTodos:
    def __init__(self, nombre, funciones_dibujo, posicion=(0, 0, 0), rotacion=0,escala=(1.0, 1.0, 1.0)):
        self.nombre = nombre
        self.funciones_dibujo = funciones_dibujo
        self.posicion = posicion
        self.escala = escala
        self.rotacion=rotacion
        self.jumping = False
        self.jump_height = 5.0  # Altura máxima del salto
        self.jump_speed = 0.5  # Velocidad del salto
        self.initial_y = self.posicion[1]  # Guardar la altura inicial para el salto

        
    def set_position(self, x, y, z):
        self.posicion = (x, y, z)

    def set_scale(self, x, y, z):
        self.escala = (x, y, z)

    def render(self):
        x, y, z = self.posicion
        glPushMatrix()
        glTranslatef(x, y, z)  # Aplicar la altura del salto
        glRotatef(self.rotacion, 0, 1, 0)
        glScalef(self.escala[0], self.escala[1], self.escala[2])
        for funcion in self.funciones_dibujo:
            funcion()
        glPopMatrix()

    def jump(self):
        if self.jumping:
            # Calcular la nueva posición Y para el salto
            if self.posicion[1] < self.initial_y + self.jump_height:
                self.posicion[1] += self.jump_speed  # Subir
            else:
                self.jumping = False  # Cambiar el estado al caer
        else:
            if self.posicion[1] > self.initial_y:
                self.posicion[1] -= self.jump_speed  # Bajar
            else:
                self.posicion[1] = self.initial_y  # Resetear a la altura inicial

    def start_jump(self):
        if not self.jumping:
            self.jumping = True  # Comenzar el salto


#Figura Luis
def figuraLuis(emocion):
    temp=Personaje(emocion)
    funcion_dibujo=[temp.render_personaje]
    return funcion_dibujo

def figuraEmma(emocion):
    temp2=Newt(emocion)
    funcion_dibujo2=[temp2.personaje]
    return funcion_dibujo2

def figuraLin(emocion):
    temp3=PersonajeLin(emocion)
    funcion_dibujo3=[temp3.personaje]
    return funcion_dibujo3

def figuraStar(emocion):
    temp4=PintarPersonajeStar(emocion)
    funcion_dibujo4=[temp4.Personaje]
    return funcion_dibujo4