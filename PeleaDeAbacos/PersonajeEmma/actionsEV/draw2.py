import math as mt
from PersonajeEmma.actionsEV import objetos as obj
from OpenGL.GLU import *
from OpenGL.GL import *
from OpenGL.GLUT import *
from pygame.locals import *
from PIL import *


quad = gluNewQuadric()
gluQuadricNormals(quad, GLU_SMOOTH)

def convertColor(r, g, b, a=255):
    return (r / 255.0, g / 255.0, b / 255.0, a / 255.0)


def ejes():
    glColor4f(*convertColor(255,0,0))
    obj.draw_line(0,0,0,30,0,0)
    glColor4f(*convertColor(0,255,0))
    obj.draw_line(0,0,0,0,30,0)
    glColor4f(*convertColor(0,0,255))
    obj.draw_line(0,0,0,0,0,30)

def cabeza(R,G,B,x,y,z):
    glPushMatrix()
    glTranslatef(x,y,z)
    glColor4f(*convertColor(R,G,B))
    gluSphere(quad, 3.5, 32, 16)
    glPopMatrix()

def ceja(x1,y1,z1,x2,y2,z2):
    glLineWidth(2)
    glColor4f(*convertColor(0,0,0))
    obj.draw_line(x1, y1, z1, x2, y2, z2)

def boca(x,y,z,angle,rx,ry,rz):
    glPushMatrix()
    glTranslatef(x,y,z)
    glRotatef(angle,rx,ry,rz)
    glColor4f(*convertColor(0,0,0))
    obj.draw_arc(1.5,3.66,5.75,20)
    glPopMatrix()

def cuerpo():
    glColor4f(*convertColor(100,100,100))
    glBegin(GL_QUADS) #TAPA ABAJO
    glVertex3f(7, 10, 9)
    glVertex3f(7, 10, 5)
    glVertex3f(13, 10, 5)
    glVertex3f(13, 10, 9)
    glEnd()
    glBegin(GL_QUADS) #TAPA ARRIBA
    glVertex3f(6, 22, 9)
    glVertex3f(6, 22, 5)
    glVertex3f(14, 22, 5)
    glVertex3f(14, 22, 9)
    glEnd()
    glBegin(GL_QUADS) # LATERAL DER
    glVertex3f(7, 10, 9)
    glVertex3f(7, 10, 5)
    glVertex3f(6, 22, 5)
    glVertex3f(6, 22, 9)
    glEnd()
    glBegin(GL_QUADS) # FRENTE
    glVertex3f(7, 10, 5)
    glVertex3f(13, 10, 5)
    glVertex3f(14, 22, 5)
    glVertex3f(6, 22, 5)
    glEnd()
    glBegin(GL_QUADS) # LATERAL IZQ
    glVertex3f(13, 10, 5)
    glVertex3f(13, 10, 9)
    glVertex3f(13, 22, 9)
    glVertex3f(13, 22, 5)
    glEnd()

def piernaR(angle):
    glPushMatrix()
    glTranslatef(11.5, 10, 7)
    glRotatef(angle, 1, 0, 0)
    glColor4f(*convertColor(204,153,0))
    gluCylinder(quad, 1.5, 0.9, 8.0, 32, 16)  # radio 1.0 y altura 8.0
    glPopMatrix()

def piernaL(angle):
    glPushMatrix()
    glTranslatef(8.5, 10, 7)
    glRotatef(angle, 1, 0, 0)
    glColor4f(*convertColor(204,153,0))
    gluCylinder(quad, 1.5, 0.9, 8.0, 32, 16)  # radio 1.0 y altura 8.0
    glPopMatrix()

def ojos():
    glPushMatrix()
    glTranslatef(11.42, 25.53, 3.85)
    glColor4f(*convertColor(0,0,0))
    gluSphere(quad, 0.5, 32, 16)
    glPopMatrix()
        
    glPushMatrix()
    glTranslatef(8.58, 25.53, 3.85)
    glColor4f(*convertColor(0,0,0))
    gluSphere(quad, 0.5, 32, 16)
    glPopMatrix()

def brazoR(angle,rx,ry,rz):
    glPushMatrix()
    glTranslatef(14.5, 20, 7)
    glRotatef(angle, rx, ry, rz)
    glColor4f(*convertColor(100,100,100))
    gluCylinder(quad, 1.3, 0.9, 8.0, 32, 16)
    glPopMatrix()


def brazoL(angle,rx,ry,rz):
    glPushMatrix()
    glTranslatef(5.5, 20, 7)
    glRotatef(angle,rx,ry,rz)
    glColor4f(*convertColor(100,100,100))
    gluCylinder(quad, 1.3, 0.9, 8.0, 32, 16)
    glPopMatrix()

def baston():
    glPushMatrix()
    glTranslatef(5.5, 13, 7)
    glRotatef(90, 1, 0, 0)
    glColor4f(*convertColor(153,102,0))
    gluCylinder(quad, 0.5, 0.5, 11.0, 32, 16)
    glPopMatrix()

def pies():
    glColor4f(*convertColor(50,50,50))
    glBegin(GL_QUADS)
    glVertex3f(11, 1, 5)
    glVertex3f(13, 1, 5)
    glVertex3f(13, 1, 8)
    glVertex3f(11, 1, 8)
    glEnd()
    
    glColor4f(*convertColor(50,50,50))
    glBegin(GL_QUADS)
    glVertex3f(11, 0, 5)
    glVertex3f(13, 0, 5)
    glVertex3f(13, 1, 5)
    glVertex3f(11, 1, 5)
    glEnd()
    
    glColor4f(*convertColor(50,50,50))
    glBegin(GL_QUADS)
    glVertex3f(13, 0, 5)
    glVertex3f(13, 0, 8)
    glVertex3f(13, 1, 8)
    glVertex3f(13, 1, 5)
    glEnd()
    
    glColor4f(*convertColor(50,50,50))
    glBegin(GL_QUADS)
    glVertex3f(13, 0, 8)
    glVertex3f(11, 0, 8)
    glVertex3f(11, 1, 8)
    glVertex3f(13, 1, 8)
    glEnd()
    
    glColor4f(*convertColor(50,50,50))
    glBegin(GL_QUADS)
    glVertex3f(11, 0, 8)
    glVertex3f(11, 0, 5)
    glVertex3f(11, 1, 5)
    glVertex3f(11, 1, 8)
    glEnd()
    
    glColor4f(*convertColor(50,50,50))
    glBegin(GL_QUADS)
    glVertex3f(7, 1, 5)
    glVertex3f(9, 1, 5)
    glVertex3f(9, 1, 8)
    glVertex3f(7, 1, 8)
    glEnd()
    
    glColor4f(*convertColor(50,50,50))
    glBegin(GL_QUADS)
    glVertex3f(7, 0, 5)
    glVertex3f(9, 0, 5)
    glVertex3f(9, 1, 5)
    glVertex3f(7, 1, 5)
    glEnd()
    
    glColor4f(*convertColor(50,50,50))
    glBegin(GL_QUADS)
    glVertex3f(9, 0, 5)
    glVertex3f(9, 0, 8)
    glVertex3f(9, 1, 8)
    glVertex3f(9, 1, 5)
    glEnd()
    
    glColor4f(*convertColor(50,50,50))
    glBegin(GL_QUADS)
    glVertex3f(9, 0, 8)
    glVertex3f(7, 0, 8)
    glVertex3f(9, 1, 8)
    glVertex3f(7, 1, 8)
    glEnd()
    
    glColor4f(*convertColor(50,50,50))
    glBegin(GL_QUADS)
    glVertex3f(7, 0, 8)
    glVertex3f(7, 0, 5)
    glVertex3f(7, 1, 5)
    glVertex3f(7, 1, 8)
    glEnd()

def boca_sorpresa(x,y,z):
    glPushMatrix()
    glTranslatef(x,y,z)
    glColor4f(*convertColor(0,0,0))
    gluDisk(quad, 0.0, 0.8, 32, 2)
    glPopMatrix()

def boca_risa(x,y,z):
    glPushMatrix()
    glTranslatef(x,y,z)
    glColor4f(*convertColor(0,0,0))
    gluPartialDisk(quad, 0.0, 0.8, 32, 1, 90, 180)
    glPopMatrix()

def obj1(R,G,B):
    glPushMatrix()
    glColor4f(*convertColor(R,G,B))
    gluSphere(quad, 3.5, 32, 16)
    glPopMatrix()