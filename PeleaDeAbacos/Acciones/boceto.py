from OpenGL.GLU import*
from OpenGL.GL import*
from OpenGL.GLUT import*
from pygame.locals import*
from PIL import*
#from Acciones import objetos as obj
from PersonajeLuis.AccionesLuis.personaje import Personaje
from PersonajeEmma.actionsEV.clasePersonaje import Newt
#from PersonajeLin.machote.clasePersonajeBlue import PersonajeLin
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
#------Personaje Starenka----------------
"""def draw_pie_izq():
    glEnable(GL_DEPTH_TEST)
    glColor3f(0.306, 0.204, 0.181)
    glPushMatrix()
    glTranslatef(0,0,0)
    obj.draw_cube()
    glPopMatrix()

def draw_pie_der():
    glEnable(GL_DEPTH_TEST)
    glColor3f(0.306, 0.204, 0.181)
    glPushMatrix()
    glTranslatef(3,0,0)
    obj.draw_cube()
    glPopMatrix()

def draw_pierna_izq():
    glEnable(GL_DEPTH_TEST)
    glColor3f(0.31, 0.396, 0.537)
    glPushMatrix()
    glTranslatef(-1,0,0)
    obj.draw_rectangle(0,1,1,2 ,5,2)
    glPopMatrix()

def draw_pierna_der():
    glEnable(GL_DEPTH_TEST)
    glColor3f(0.31, 0.396, 0.537)
    glPushMatrix()
    glTranslatef(2,0,0)
    obj.draw_rectangle(0,1,1,2 ,5,2)
    glPopMatrix()

def draw_bajoSup():
    glEnable(GL_DEPTH_TEST)
    glColor3f(0.502, 0, 0.502)
    glPushMatrix()
    glTranslatef(0,5.5,0)
    obj.draw_rectangle(-1,0,2,5 ,3,4)
    glPopMatrix()

def draw_brazoIzquierdo():
    glEnable(GL_DEPTH_TEST)
    glColor3f(0.024, 0.239, 0.482)
    glPushMatrix()
    glTranslatef(0,6,0)
    obj.draw_rectangle(-3,1,1,2 ,6,2)
    glPopMatrix()

def draw_brazoDerecho():
    glEnable(GL_DEPTH_TEST)
    glColor3f(0.024, 0.239, 0.482)
    glPushMatrix()
    glTranslatef(7,6,0)
    obj.draw_rectangle(-3,1,1,2 ,6,2)
    glPopMatrix()

def draw_torso():
    glEnable(GL_DEPTH_TEST)
    glColor3f(0.502, 0, 0.502)
    glPushMatrix()
    glTranslatef(0,6,0)
    obj.draw_rectangle(-1,0,2,5 ,7,4)
    glPopMatrix()

def draw_cabeza():
    glEnable(GL_DEPTH_TEST)
    glColor3f(1.0, 0.8784, 0.7412)
    glPushMatrix()
    glTranslatef(0.9,17,0)
    obj.draw_sphere(4,30,30)
    glPopMatrix()

def draw_pelo():
    glEnable(GL_DEPTH_TEST)
    glColor3f(0.2353, 0.1569, 0.0)
    glPushMatrix()
    glTranslatef(-1.5,19,3)
    obj.draw_rectangle(0,0,0,6,8,6)
    glPopMatrix()

def draw_ojoDer():
    glEnable(GL_DEPTH_TEST)
    glColor3f(0.2353, 0.1569, 0.0)
    glPushMatrix()
    glTranslatef(0,16.2,-4)
    obj.draw_arc(1,0,360,1)
    glPopMatrix()
    
def draw_ojoIzq():
    glEnable(GL_DEPTH_TEST)
    glColor3f(0.2353, 0.1569, 0.0)
    glPushMatrix()
    glTranslatef(3,17,-4)
    obj.draw_arc(1,0,180,1)
    glPopMatrix()

def draw_bocaNom():
    glEnable(GL_DEPTH_TEST)
    glColor3f(0.2353, 0.1569, 0.0)
    glPushMatrix()
    glTranslatef(3,15,-3)
    obj.draw_arc(1,0,60,2)
    glPopMatrix()

def caraOrg():
    draw_ojoDer
    draw_bocaNom
    draw_ojoIzq

#Figura Original
def original():
    funciones_dibujo = [
        draw_pierna_der,    # Sin paréntesis para no ejecutar la función
        draw_pie_der,
        draw_pie_izq,
        draw_pierna_izq,
        draw_bajoSup,
        draw_torso,
        draw_brazoIzquierdo,
        draw_brazoDerecho,
        draw_cabeza,
        draw_pelo,
        draw_ojoDer,
        draw_bocaNom,
        draw_ojoIzq
    ]
    return funciones_dibujo"""

#Figura Luis
def figuraLuis(emocion):
    temp=Personaje(emocion)
    funcion_dibujo=[temp.render_personaje]
    return funcion_dibujo

def figuraEmma(emocion):
    temp2=Newt(emocion)
    funcion_dibujo2=[temp2.personaje]
    return funcion_dibujo2

"""def figuraLin():
    temp3=PersonajeLin()
    funcion_dibujo3=[temp3.draw]
    return funcion_dibujo3"""
