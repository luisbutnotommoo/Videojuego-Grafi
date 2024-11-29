import pygame as py
import math
from OpenGL.GLU import *
from OpenGL.GL import *
from OpenGL.GLUT import *
from pygame.locals import *
from PIL import *


def draw_piernaIz():
    glBegin(GL_QUADS)
    # Front Face
    #glColor3f(0.9, 0.8, 0.6)  # Beige
    glColor3f(0.0, 0.0, 1.0)
    glVertex3f(0.5, -1.5, 0.0)  # 1
    glVertex3f(0.5, -2.5, 0.0)  # 2
    glVertex3f(1.5, -2.5, 0.0)  # 3
    glVertex3f(1.5, -1.5, 0.0)  # 4
    
    # Back Face
    glColor3f(0.0, 0.0, 1.0)
    glVertex3f(0.5, -1.5, 2.0)  # 5
    glVertex3f(0.5, -2.5, 2.0)  # 6
    glVertex3f(1.5, -2.5, 2.0)  # 7
    glVertex3f(1.5, -1.5, 2.0)  # 8
    
    # Side Faces
    # Side 1
    glColor3f(0.0, 0.0, 1.0)
    glVertex3f(0.5, -1.5, 0.0)  # 1
    glVertex3f(0.5, -1.5, 2.0)  # 5
    glVertex3f(0.5, -2.5, 2.0)  # 6
    glVertex3f(0.5, -2.5, 0.0)  # 2
    
    # Side 2
    glColor3f(0.0, 0.0, 1.0)
    glVertex3f(1.5, -1.5, 0.0)  # 4
    glVertex3f(1.5, -1.5, 2.0)  # 8
    glVertex3f(1.5, -2.5, 2.0)  # 7
    glVertex3f(1.5, -2.5, 0.0)  # 3

    #cara inferior
    glColor3f(0.0, 0.0, 1.0)
    glVertex3f(0.5, -1.5, 0.0)  # 1
    glVertex3f(1.5, -1.5, 0.0)  # 4
    glVertex3f(1.5, -1.5, 2.0)  # 8
    glVertex3f(0.5, -1.5, 2.0)  # 5

    #cara posterior
    glColor3f(0.0, 0.0, 1.0)
    glVertex3f(0.5, -2.5, 0.0)  # 2
    glVertex3f(1.5, -2.5, 0.0)  # 3
    glVertex3f(1.5, -2.5, 2.0)  # 7
    glVertex3f(0.5, -2.5, 2.0)  # 6
    
    
    glEnd()

def draw_piernaDe():
    glBegin(GL_QUADS)
 # Front Face
    glColor3f(0.0, 0.0, 1.0)  # Beige
    glVertex3f(-1.5,-1.5,0.0)  # 1
    glVertex3f(-1.5,-2.5,0.0)  # 2
    glVertex3f(-0.5,-2.5,0.0)  # 3
    glVertex3f(-0.5,-1.5,0.0)  # 4
    
    # Back Face
    glColor3f(0.0, 0.0, 1.0)  # Beige
    glVertex3f(-1.5, -1.5, 2.0)  # 5
    glVertex3f(-1.5,-2.5,2.0)  # 6
    glVertex3f(-0.5,-2.5,2.0)  # 7
    glVertex3f(-0.5, -1.5, 2.0)  # 8
    
    # Side Faces
    # Side 1
    glColor3f(0.0, 0.0, 1.0)  # Beige
    glVertex3f(-1.5,-1.5,0.0)  # 1
    glVertex3f(-1.5, -1.5, 2.0)  # 5
    glVertex3f(-1.5,-2.5,2.0)  # 6
    glVertex3f(-1.5,-2.5,0.0)  # 2
    
    # Side 2
    glColor3f(0.0, 0.0, 1.0)  # Beige
    glVertex3f(-0.5,-1.5,0.0)  # 4
    glVertex3f(-0.5, -1.5, 2.0)  # 8
    glVertex3f(-0.5,-2.5,2.0)  # 7
    glVertex3f(-0.5,-2.5,0.0)  # 3

    #cara inferior
    glColor3f(0.0, 0.0, 1.0)  # Beige
    glVertex3f(-1.5,-1.5,0.0)  # 1
    glVertex3f(-0.5,-1.5,0.0)  # 4
    glVertex3f(-0.5, -1.5, 2.0)  # 8
    glVertex3f(-1.5, -1.5, 2.0)  # 5

    #cara posterior
    glColor3f(0.0, 0.0, 1.0)  # Beige
    glVertex3f(-1.5,-2.5,0.0)  # 2
    glVertex3f(-0.5,-2.5,0.0)  # 3
    glVertex3f(-0.5,-2.5,2.0)  # 7
    glVertex3f(-1.5,-2.5,2.0)  # 6


    glEnd()

def draw_BrazoDe():
    glBegin(GL_QUADS)
 # Front Face
    glColor3f(0.9, 0.8, 0.6)  # Beige
    glVertex3f(-2.7,-1.5,4.0)  # 1
    glVertex3f(-2.7,-2.5,4.0)  # 2
    glVertex3f(-1.5,-2.5,5.0)  # 3
    glVertex3f(-1.5,-1.5,5.0)  # 4
    
    # Back Face
    glColor3f(0.9, 0.8, 0.6)  # Beige
    glVertex3f(-2.7,-1.5,5.0)  # 5
    glVertex3f(-2.7,-2.5,5.0)  # 6
    glVertex3f(-1.5,-2.5,6.0)  # 7
    glVertex3f(-1.5,-1.5,6.0)  # 8
    
    # Side Faces
    # Side 1
    glColor3f(0.9, 0.8, 0.6)  # Beige
    glVertex3f(-2.7,-1.5,4.0)  # 1
    glVertex3f(-2.7,-1.5,5.0)  # 5
    glVertex3f(-2.7,-2.5,5.0)  # 6
    glVertex3f(-2.7,-2.5,4.0)  # 2
    
    # Side 2
    glColor3f(0.9, 0.8, 0.6)  # Beige
    glVertex3f(-1.5,-1.5,5.0)  # 4
    glVertex3f(-1.5,-1.5,6.0)  # 8
    glVertex3f(-1.5,-2.5,6.0) # 7
    glVertex3f(-1.5,-2.5,5.0)  # 3

    #cara inferior
    glColor3f(0.9, 0.8, 0.6)  # Beige
    glVertex3f(-2.7,-1.5,4.0)  # 1
    glVertex3f(-1.5,-1.5,5.0)  # 4
    glVertex3f(-1.5,-1.5,6.0)  # 8
    glVertex3f(-2.7,-1.5,5.0)  # 5

    #cara posterior
    glColor3f(0.9, 0.8, 0.6)  # Beige
    glVertex3f(-2.7,-2.5,4.0)  # 2
    glVertex3f(-1.5,-2.5,5.0)  # 3
    glVertex3f(-1.5,-2.5,6.0)  # 7
    glVertex3f(-2.7,-2.5,5.0)  # 6


    glEnd()  

def draw_BrazoIz():
    glBegin(GL_QUADS)
 # Front Face
    glColor3f(0.9, 0.8, 0.6)  # Beige
    glVertex3f(2.7,-1.5,4.0)  # 1
    glVertex3f(2.7,-2.5,4.0)  # 2
    glVertex3f(1.5,-2.5,5.0)  # 3
    glVertex3f(1.5,-1.5,5.0)  # 4
    
    # Back Face
    glColor3f(0.9, 0.8, 0.6)  # Beige
    glVertex3f(2.7,-1.5,5.0)  # 5
    glVertex3f(2.7,-2.5,5.0)  # 6
    glVertex3f(1.5,-2.5,6.0)  # 7
    glVertex3f(1.5,-1.5,6.0)  # 8
    
    # Side Faces
    # Side 1
    glColor3f(0.9, 0.8, 0.6)  # Beige
    glVertex3f(2.7,-1.5,4.0)  # 1
    glVertex3f(2.7,-1.5,5.0)  # 5
    glVertex3f(2.7,-2.5,5.0)  # 6
    glVertex3f(2.7,-2.5,4.0)  # 2
    
    # Side 2
    glColor3f(0.9, 0.8, 0.6)  # Beige
    glVertex3f(1.5,-1.5,5.0)  # 4
    glVertex3f(1.5,-1.5,6.0)  # 8
    glVertex3f(1.5,-2.5,6.0) # 7
    glVertex3f(1.5,-2.5,5.0)  # 3

    #cara inferior
    glColor3f(0.9, 0.8, 0.6)  # Beige
    glVertex3f(2.7,-1.5,4.0)  # 1
    glVertex3f(1.5,-1.5,5.0)  # 4
    glVertex3f(1.5,-1.5,6.0)  # 8
    glVertex3f(2.7,-1.5,5.0)  # 5

    #cara posterior
    glColor3f(0.9, 0.8, 0.6)  # Beige
    glVertex3f(2.7,-2.5,4.0)  # 2
    glVertex3f(1.5,-2.5,5.0)  # 3
    glVertex3f(1.5,-2.5,6.0)  # 7
    glVertex3f(2.7,-2.5,5.0)  # 6

    glEnd()

def draw_Torzo():
    glBegin(GL_QUADS)
    
    # Front Face
    glColor3f(0.0, 0.0, 1.0)  # Azul
    glVertex3f(-1.5, -1.5, 6.0)  # Vértice superior izquierdo (frontal)
    glVertex3f(-1.5, -2.5, 6.0)  # Vértice inferior izquierdo (frontal)
    glVertex3f(1.5, -2.5, 6.0)   # Vértice inferior derecho (frontal)
    glVertex3f(1.5, -1.5, 6.0)   # Vértice superior derecho (frontal)
    
    # Back Face
    glColor3f(0.0, 0.0, 1.0)  # Azul
    glVertex3f(-1.5, -1.5, 2.0)  # Vértice superior izquierdo (trasero)
    glVertex3f(-1.5, -2.5, 2.0)  # Vértice inferior izquierdo (trasero)
    glVertex3f(1.5, -2.5, 2.0)   # Vértice inferior derecho (trasero)
    glVertex3f(1.5, -1.5, 2.0)   # Vértice superior derecho (trasero)

    # Side Face 1 (lado izquierdo)
    glColor3f(0.0, 0.0, 1.0)  # Azul
    glVertex3f(-1.5, -1.5, 6.0)  # Frontal superior izquierdo
    glVertex3f(-1.5, -2.5, 6.0)  # Frontal inferior izquierdo
    glVertex3f(-1.5, -2.5, 2.0)  # Trasero inferior izquierdo
    glVertex3f(-1.5, -1.5, 2.0)  # Trasero superior izquierdo

    # Side Face 2 (lado derecho)
    glColor3f(0.0, 0.0, 1.0)  # Azul
    glVertex3f(1.5, -1.5, 6.0)  # Frontal superior derecho
    glVertex3f(1.5, -2.5, 6.0)  # Frontal inferior derecho
    glVertex3f(1.5, -2.5, 2.0)  # Trasero inferior derecho
    glVertex3f(1.5, -1.5, 2.0)  # Trasero superior derecho

    # Bottom Face (inferior)
    glColor3f(0.0, 0.0, 1.0)  # Azul
    glVertex3f(-1.5, -2.5, 6.0)  # Frontal inferior izquierdo
    glVertex3f(1.5, -2.5, 6.0)   # Frontal inferior derecho
    glVertex3f(1.5, -2.5, 2.0)   # Trasero inferior derecho
    glVertex3f(-1.5, -2.5, 2.0)  # Trasero inferior izquierdo

    # Top Face (superior)
    glColor3f(0.0, 0.0, 1.0)  # Azul
    glVertex3f(-1.5, -1.5, 6.0)  # Frontal superior izquierdo
    glVertex3f(1.5, -1.5, 6.0)   # Frontal superior derecho
    glVertex3f(1.5, -1.5, 2.0)   # Trasero superior derecho
    glVertex3f(-1.5, -1.5, 2.0)  # Trasero superior izquierdo

    glEnd()



def Cuello():
    glBegin(GL_QUADS)
 # Front Face
    glColor3f(0.9, 0.8, 0.6)  # Beige
    glVertex3f(-0.5,-1.5,6.0)  # 1
    glVertex3f(-0.5,-2.5,6.0)  # 2
    glVertex3f(0.5,-2.5,6.0)  # 3
    glVertex3f(0.5,-1.5,6.0)  # 4
    
    # Back Face
    glColor3f(0.9, 0.8, 0.6)  # Beige
    glVertex3f(-0.5, -1.5, 6.5)  # 5
    glVertex3f(-0.5,-2.5,6.5)  # 6
    glVertex3f(0.5,-2.5,6.5)  # 7
    glVertex3f(0.5,-1.5,6.5)  # 8
    
    # Side Faces
    # Side 1
    glColor3f(0.9, 0.8, 0.6)  # Beige
    glVertex3f(-0.5,-1.5,6.0)  # 1
    glVertex3f(-0.5, -1.5, 6.5) # 5
    glVertex3f(-0.5,-2.5,6.5)  # 6
    glVertex3f(-0.5,-2.5,6.0)  # 2
    
    # Side 2
    glColor3f(0.9, 0.8, 0.6)  # Beige
    glVertex3f(0.5,-1.5,6.0)  # 4
    glVertex3f(0.5,-1.5,6.5)  # 8
    glVertex3f(0.5,-2.5,6.5)  # 7
    glVertex3f(0.5,-2.5,6.0)  # 3

    #cara inferior
    glColor3f(0.9, 0.8, 0.6)  # Beige
    glVertex3f(-0.5,-1.5,6.0)  # 1
    glVertex3f(0.5,-1.5,6.0)  # 4
    glVertex3f(0.5,-1.5,6.5)  # 8
    glVertex3f(-0.5, -1.5, 6.5)  # 5

    #cara posterior
    glColor3f(0.9, 0.8, 0.6)  # Beige
    glVertex3f(-0.5,-2.5,6.0)  # 2
    glVertex3f(0.5,-2.5,6.0)  # 3
    glVertex3f(0.5,-2.5,6.5)  # 7
    glVertex3f(-0.5,-2.5,6.5)  # 6


    glEnd() 
def draw_Cabeza():
    glBegin(GL_QUADS)
 # Front Face
    glColor3f(0.9, 0.8, 0.6)  # Beige
    glVertex3f(-1.5,-1.5,6.5)  # 1
    glVertex3f(-1.5,-2.5,6.5)  # 2
    glVertex3f(1.5,-2.5,6.5)  # 3
    glVertex3f(1.5,-1.5,6.5)  # 4
    
    # Back Face
    glColor3f(0.9, 0.8, 0.6)  # Beige
    glVertex3f(-1.5,-1.5,8.5)  # 5
    glVertex3f(-1.5,-2.5,8.5)  # 6
    glVertex3f(1.5, -2.5, 8.5)  # 7
    glVertex3f(1.5,-1.5,8.5)  # 8
    
    # Side Faces
    # Side 1
    glColor3f(0.9, 0.8, 0.6)  # Beige
    glVertex3f(-1.5,-1.5,6.5)  # 1
    glVertex3f(-1.5,-1.5,8.5)  # 5
    glVertex3f(-1.5,-2.5,8.5)  # 6
    glVertex3f(-1.5,-2.5,6.5)  # 2
    
    # Side 2
    glColor3f(0.9, 0.8, 0.6)  # Beige
    glVertex3f(1.5,-1.5,6.5)  # 4
    glVertex3f(1.5,-1.5,8.5)  # 8
    glVertex3f(1.5, -2.5, 8.5) # 7
    glVertex3f(1.5,-2.5,6.5)  # 3

    #cara inferior
    glColor3f(0.9, 0.8, 0.6)  # Beige
    glVertex3f(-1.5,-1.5,6.5)  # 1
    glVertex3f(1.5,-1.5,6.5)  # 4
    glVertex3f(1.5,-1.5,8.5)  # 8
    glVertex3f(-1.5,-1.5,8.5)  # 5

    #cara posterior
    glColor3f(0.9, 0.8, 0.6)  # Beige
    glVertex3f(-1.5,-2.5,6.5)  # 2
    glVertex3f(1.5,-2.5,6.5)  # 3
    glVertex3f(1.5, -2.5, 8.5)  # 7
    glVertex3f(-1.5,-2.5,8.5)  # 6
   

    glEnd()

    
def draw_ojos():
    glBegin(GL_QUADS)

    glVertex3f(-1.3,-2.6,7.6)#1
    glVertex3f(-.4,-2.6,7.6)#4
    glVertex3f(-.4,-2.6,7.7)#5
    glVertex3f(-1.3,-2.6,7.7)#8

    glVertex3f(.4,-2.6,7.6)#1
    glVertex3f(1.3,-2.6,7.6)#4
    glVertex3f(1.3,-2.6,7.7)#5
    glVertex3f(.4,-2.6,7.7)#8

    glEnd()         