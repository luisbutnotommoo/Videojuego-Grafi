import pygame
from OpenGL.GLU import *
from OpenGL.GL import *
from OpenGL.GLUT import *
from pygame.locals import *
from PIL import *

from actionsEV import luces as lc
from actionsEV import objetos as obj

PosX_objeto1 = 3
PosY_objeto1 = 6
PosZ_objeto1 = 4
objeto1_height = 1

def draw(moveX,moveY):
    global PosX_objeto1, PosY_objeto1
    PosX_objeto1 = PosX_objeto1+moveX
    PosY_objeto1 = PosY_objeto1+moveY
    glEnable(GL_DEPTH_TEST)
    glPushMatrix()
    glTranslatef(PosX_objeto1,PosY_objeto1,PosZ_objeto1)
    lc.iluminacion(0.0,1.0,0.0)
    obj.draw_cube()
    glDisable(GL_LIGHTING)
    glDisable(GL_LIGHT0)
    glPopMatrix()

# Primer dibujo
PosX_objeto2 = 8
PosY_objeto2 = 6
PosZ_objeto2 = 4

objeto2_height = 1
objeto2_width = 1
objeto2_deept = 1

def draw2():
    glEnable(GL_DEPTH_TEST)
    glPushMatrix()
    glTranslatef(PosX_objeto2, PosY_objeto2, PosZ_objeto2)
    lc.iluminacion(0.0, 0.0, 0.0)
    obj.draw_sphere(2,40,40)
    glDisable(GL_LIGHTING)
    glDisable(GL_LIGHT0)
    glPopMatrix()

posCabezaX = 7
posCabezaY = 7
posCabezaZ = 7

def draw_cabeza():
    glEnable(GL_DEPTH_TEST)
    glPushMatrix()
    glTranslatef(posCabezaX, posCabezaY, posCabezaZ)
    lc.iluminacion(0.0, 1.0, 0.0)
    obj.draw_sphere(2,40,40)
    glDisable(GL_LIGHTING)
    glDisable(GL_LIGHT0)
    glPopMatrix()

posCuerpoX = 7
posCuerpoY = 2
posCuerpoZ = 7
def draw_cuerpo():
    glEnable(GL_DEPTH_TEST)
    glPushMatrix()
    glTranslatef(posCuerpoX, posCuerpoY, posCuerpoZ)
    lc.iluminacion(0.0, 1.0, 0.0)
    obj.draw_sphere(4,40,40)
    glDisable(GL_LIGHTING)
    glDisable(GL_LIGHT0)
    glPopMatrix()