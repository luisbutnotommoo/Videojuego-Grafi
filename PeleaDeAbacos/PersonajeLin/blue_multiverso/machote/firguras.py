import pygame
from pygame.locals import *
from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import *
import math


def rectangle():
    glBegin(GL_QUADS)
    
    glColor3f(1.0, 1.0, 1.0)
    glVertex3f(2, 1, -1)
    glVertex3f(-2, 1, -1)
    glVertex3f(-2, -1, -1)
    glVertex3f(2, -1, -1)
    
    glVertex3f(2, 1, 1)
    glVertex3f(-2, 1, 1)
    glVertex3f(-2, -1, 1)
    glVertex3f(2, -1, 1)
    
    glVertex3f(2, 1, -1)
    glVertex3f(2, 1, 1)
    glVertex3f(2, -1, 1)
    glVertex3f(2, -1, -1)
    
    glVertex3f(-2, 1, 1)
    glVertex3f(-2, 1, -1)
    glVertex3f(-2, -1, -1)
    glVertex3f(-2, -1, 1)
    
    glVertex3f(2, 1, 1)
    glVertex3f(-2, 1, 1)
    glVertex3f(-2, 1, -1)
    glVertex3f(2, 1, -1)
    
    glVertex3f(2, -1, -1)
    glVertex3f(-2, -1, -1)
    glVertex3f(-2, -1, 1)
    glVertex3f(2, -1, 1)
    
    glEnd()



def draw_oval(center_x, center_y, center_z, radius_x, radius_y, depth, slices=50):
    glBegin(GL_TRIANGLE_FAN)
    glColor3f(1.0, 1.0, 1.0)
    glVertex3f(center_x, center_y, center_z)  # Centro del óvalo
    for i in range(slices+1):
        angle = i * 2.0 * math.pi / slices
        x = center_x + (radius_x * math.cos(angle))
        y = center_y + (radius_y * math.sin(angle))
        glVertex3f(x, y, center_z)
    glEnd()

    # Lados del óvalo
    glBegin(GL_QUAD_STRIP)
    glColor3f(1.0, 1.0, 1.0)
    for i in range(slices+1):
        angle = i * 2.0 * math.pi / slices
        x = center_x + (radius_x * math.cos(angle))
        y = center_y + (radius_y * math.sin(angle))
        glVertex3f(x, y, center_z)
        glVertex3f(x, y, center_z - depth)
    glEnd() 


def draw_oval2(center_x, center_y, center_z, radius_x, radius_y, depth, slices=50):
    glBegin(GL_TRIANGLE_FAN)
    glColor3f(1.0, 1.0, 0.0)
    glVertex3f(center_x, center_y, center_z)  # Centro del óvalo
    for i in range(slices+1):
        angle = i * 2.0 * math.pi / slices
        x = center_x + (radius_x * math.cos(angle))
        z = center_z + (radius_y * math.sin(angle))  # Usamos radius_y para la coordenada z
        glVertex3f(x, center_y, z)  # Intercambiamos x y center_y
    glEnd()

    # Lados del óvalo
    glBegin(GL_QUAD_STRIP)
    glColor3f(1.0, 1.0, 0.0)
    for i in range(slices+1):
        angle = i * 2.0 * math.pi / slices
        x = center_x + (radius_x * math.cos(angle))
        z = center_z + (radius_y * math.sin(angle))  # Usamos radius_y para la coordenada z
        glVertex3f(x, center_y, center_z)
        glVertex3f(x, center_y, z)  # Intercambiamos x y center_y para la coordenada z
    glEnd()    


def draw_cylinder(center_x, center_y, center_z, radius, depth, slices=50):
    glBegin(GL_QUAD_STRIP)
    glColor3f(0.0, 1.0, 0.0)
    for i in range(slices+1):
        angle = i * 2.0 * math.pi / slices
        x = center_x + (radius * math.cos(angle))
        y = center_y + (radius * math.sin(angle))
        glVertex3f(x, y, center_z)
        glVertex3f(x, y, center_z - depth)
        
    glEnd()

    
    for z in (center_z, center_z - depth):
        glBegin(GL_TRIANGLE_FAN)
        glVertex3f(center_x, center_y, z)
        for i in range(slices+1):
            angle = i * 2.0 * math.pi / slices
            x = center_x + (radius * math.cos(angle))
            y = center_y + (radius * math.sin(angle))
            glVertex3f(x, y, z)
        glEnd()



def draw_cone(center_x, center_y, center_z, radius_base, height, slices=50):
    glColor3f(1.0, 1.0, 0.0)
    glBegin(GL_TRIANGLE_FAN)
    glVertex3f(center_x, center_y + height, center_z)  # Punto superior del cono
    for i in range(slices+1):
        angle = i * 2.0 * math.pi / slices
        x = center_x + (radius_base * math.cos(angle))
        z = center_z + (radius_base * math.sin(angle))
        glVertex3f(x, center_y, z)  # Puntos en la base del cono
    glEnd()

    glBegin(GL_TRIANGLE_FAN)
    glVertex3f(center_x, center_y, center_z)  # Centro de la base del cono
    for i in range(slices+1):
        angle = i * 2.0 * math.pi / slices
        x = center_x + (radius_base * math.cos(angle))
        z = center_z + (radius_base * math.sin(angle))
        glVertex3f(x, center_y, z)  # Puntos en la base del cono
    glEnd()
    
    # Lados del cono
    glBegin(GL_TRIANGLE_STRIP)
    for i in range(slices+1):
        angle = i * 2.0 * math.pi / slices
        x = center_x + (radius_base * math.cos(angle))
        z = center_z + (radius_base * math.sin(angle))
        glVertex3f(x, center_y, z)  # Punto en la base del cono
        glVertex3f(center_x, center_y + height, center_z)  # Punto en el vértice del cono
    glEnd()



def draw_cylinderpata(center_x, center_y, center_z, radius, height, slices=50):
    # Lados del cilindro
    glBegin(GL_TRIANGLE_STRIP)
    glColor3f(1.0, 0.0, 0.0) 
    for i in range(slices, -1, -1):  # Recorremos en orden inverso para dibujar al revés
        angle = i * 2.0 * math.pi / slices
        x = center_x + (radius * math.cos(angle))
        z = center_z + (radius * math.sin(angle))
        glVertex3f(x, center_y + height, z)  # Punto en la parte superior del cilindro
        glVertex3f(x, center_y, z)  # Punto en la parte inferior del cilindro
    glEnd()

    # Tapas del cilindro
    glColor3f(1.0, 0.0, 0.0)   # Color rojo

    # Tapa inferior del cilindro
    glBegin(GL_TRIANGLE_FAN)
    glVertex3f(center_x, center_y + height, center_z)  # Centro de la tapa inferior
    for i in range(slices, -1, -1):
        angle = i * 2.0 * math.pi / slices
        x = center_x + (radius * math.cos(angle))
        z = center_z + (radius * math.sin(angle))
        glVertex3f(x, center_y + height, z)  # Puntos en la tapa inferior
    glEnd()

    # Tapa superior del cilindro
    glBegin(GL_TRIANGLE_FAN)
    glVertex3f(center_x, center_y, center_z)  # Centro de la tapa superior
    for i in range(slices+1):
        angle = i * 2.0 * math.pi / slices
        x = center_x + (radius * math.cos(angle))
        z = center_z + (radius * math.sin(angle))
        glVertex3f(x, center_y, z)  # Puntos en la tapa superior
    glEnd()



def draw_square():
   # Plano XY
    glBegin(GL_QUADS)
    glColor3f(0.1, 0.1, 0.1)  # Color negro claro
    glVertex3f(-1.5, -1, 1.1)
    glVertex3f(1.5, -1, 1.1)
    glVertex3f(1.5, 1, 1.1)
    glVertex3f(-1.5, 1, 1.1)
    glEnd()




def draw_star(x, y, radius, num_points):
    glColor3f(1.0,0.0,0.0)
    glBegin(GL_TRIANGLE_FAN)
    glVertex2f(x, y)  # Centro de la estrella
    for i in range(num_points * 2 + 1):
        angle = i * math.pi / num_points
        if i % 2 == 0:
            glVertex2f(x + radius * math.cos(angle), y + radius * math.sin(angle))  # Punto exterior
        else:
            glVertex2f(x + radius / 2 * math.cos(angle), y + radius / 2 * math.sin(angle))  # Punto interior
    glEnd()    

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

def draw_piernaDemov():
    glBegin(GL_QUADS)
 # Front Face
 
    glVertex3f(-1.5,-2.5,0.0)  # 1
    glVertex3f(-1.5,-3.5,0.0)  # 2
    glVertex3f(-0.5,-3.5,0.0)  # 3
    glVertex3f(-0.5,-3.5,0.0)  # 4
    
    # Back Face
 
    glVertex3f(-1.5, -2.5, 2.0)  # 5
    glVertex3f(-1.5,-3.5,2.0)  # 6
    glVertex3f(-0.5,-3.5,2.0)  # 7
    glVertex3f(-0.5, -2.5, 2.0)  # 8
    
    # Side Faces
    # Side 1
   
    glVertex3f(-1.5,-2.5,0.0)  # 1
    glVertex3f(-1.5, -2.5, 2.0)  # 5
    glVertex3f(-1.5,-3.5,2.0)  # 6
    glVertex3f(-1.5,-3.5,0.0)  # 2
    
    # Side 2

    glVertex3f(-0.5,-2.5,0.0)  # 4
    glVertex3f(-0.5, -2.5, 2.0)  # 8
    glVertex3f(-0.5,-3.5,2.0)  # 7
    glVertex3f(-0.5,-3.5,0.0)  # 3

    #cara inferior

    glVertex3f(-1.5,-2.5,0.0)  # 1
    glVertex3f(-0.5,-2.5,0.0)  # 4
    glVertex3f(-0.5, -2.5, 2.0)  # 8
    glVertex3f(-1.5, -2.5, 2.0)  # 5

    #cara posterior

    glVertex3f(-1.5,-3.5,0.0)  # 2
    glVertex3f(-0.5,-3.5,0.0)  # 3
    glVertex3f(-0.5,-3.5,2.0)  # 7
    glVertex3f(-1.5,-3.5,2.0)  # 6


    glEnd()

def draw_piernaIzmov():
    glBegin(GL_QUADS)
 # Front Face
 
    glVertex3f(1.5,-2.5,0.0)  # 1
    glVertex3f(1.5,-3.5,0.0)  # 2
    glVertex3f(0.5,-3.5,0.0)  # 3
    glVertex3f(0.5,-3.5,0.0)  # 4
    
    # Back Face
 
    glVertex3f(1.5, -2.5, 2.0)  # 5
    glVertex3f(1.5,-3.5,2.0)  # 6
    glVertex3f(0.5,-3.5,2.0)  # 7
    glVertex3f(0.5, -2.5, 2.0)  # 8
    
    # Side Faces
    # Side 1
   
    glVertex3f(1.5,-2.5,0.0)  # 1
    glVertex3f(1.5, -2.5, 2.0)  # 5
    glVertex3f(1.5,-3.5,2.0)  # 6
    glVertex3f(1.5,-3.5,0.0)  # 2
    
    # Side 2

    glVertex3f(0.5,-2.5,0.0)  # 4
    glVertex3f(0.5, -2.5, 2.0)  # 8
    glVertex3f(0.5,-3.5,2.0)  # 7
    glVertex3f(0.5,-3.5,0.0)  # 3

    #cara inferior

    glVertex3f(1.5,-2.5,0.0)  # 1
    glVertex3f(0.5,-2.5,0.0)  # 4
    glVertex3f(0.5, -2.5, 2.0)  # 8
    glVertex3f(1.5, -2.5, 2.0)  # 5

    #cara posterior

    glVertex3f(1.5,-3.5,0.0)  # 2
    glVertex3f(0.5,-3.5,0.0)  # 3
    glVertex3f(0.5,-3.5,2.0)  # 7
    glVertex3f(1.5,-3.5,2.0)  # 6


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

def brazo_Der_up():
    glBegin(GL_QUADS)
 # Front Face

    glVertex3f(-3.0,-2.2,7.0)  # 1
    glVertex3f(-3.0,-3.2,7.0)  # 2
    glVertex3f(-1.5,-2.5,5.0)  # 3
    glVertex3f(-1.5,-1.5,5.0)  # 4
    
    # Back Face

    glVertex3f(-3.0,-2.2,8.0)  # 5
    glVertex3f(-3.0,-3.2,8.0)  # 6
    glVertex3f(-1.5,-2.5,6.0)  # 7
    glVertex3f(-1.5,-1.5,6.0)  # 8
    
    # Side Faces
    # Side 1

    glVertex3f(-3.0,-2.2,7.0)  # 1
    glVertex3f(-3.0,-2.2,8.0)  # 5
    glVertex3f(-3.0,-3.2,8.0)  # 6
    glVertex3f(-3.0,-3.2,7.0)  # 2
    
    # Side 2

    glVertex3f(-1.5,-1.5,5.0)  # 4
    glVertex3f(-1.5,-1.5,6.0)  # 8
    glVertex3f(-1.5,-2.5,6.0) # 7
    glVertex3f(-1.5,-2.5,5.0)  # 3

    #cara inferior
 
    glVertex3f(-3.0,-2.2,7.0)  # 1
    glVertex3f(-1.5,-1.5,5.0)  # 4
    glVertex3f(-1.5,-1.5,6.0)  # 8
    glVertex3f(-3.0,-2.2,8.0)  # 5

    #cara posterior 
    glVertex3f(-3.0,-3.2,7.0)  # 2
    glVertex3f(-1.5,-2.5,5.0)  # 3
    glVertex3f(-1.5,-2.5,6.0)  # 7
    glVertex3f(-3.0,-3.2,8.0)  # 6


    glEnd()    
def brazo_Iz_up():
    glBegin(GL_QUADS)
 # Front Face

    glVertex3f(3.0,-2.2,7.0)  # 1
    glVertex3f(3.0,-3.2,7.0)  # 2
    glVertex3f(1.5,-2.5,5.0)  # 3
    glVertex3f(1.5,-1.5,5.0)  # 4
    
    # Back Face

    glVertex3f(3.0,-2.2,8.0)  # 5
    glVertex3f(3.0,-3.2,8.0)  # 6
    glVertex3f(1.5,-2.5,6.0)  # 7
    glVertex3f(1.5,-1.5,6.0)  # 8
    
    # Side Faces
    # Side 1

    glVertex3f(3.0,-2.2,7.0)  # 1
    glVertex3f(3.0,-2.2,8.0)  # 5
    glVertex3f(3.0,-3.2,8.0)  # 6
    glVertex3f(3.0,-3.2,7.0)  # 2
    
    # Side 2

    glVertex3f(1.5,-1.5,5.0)  # 4
    glVertex3f(1.5,-1.5,6.0)  # 8
    glVertex3f(1.5,-2.5,6.0) # 7
    glVertex3f(1.5,-2.5,5.0)  # 3

    #cara inferior
 
    glVertex3f(3.0,-2.2,7.0)  # 1
    glVertex3f(1.5,-1.5,5.0)  # 4
    glVertex3f(1.5,-1.5,6.0)  # 8
    glVertex3f(3.0,-2.2,8.0)  # 5

    #cara posterior 
    glVertex3f(3.0,-3.2,7.0)  # 2
    glVertex3f(1.5,-2.5,5.0)  # 3
    glVertex3f(1.5,-2.5,6.0)  # 7
    glVertex3f(3.0,-3.2,8.0)  # 6


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

def mov_Cuello():
    glBegin(GL_QUADS)
 # Front Face

    glVertex3f(-0.5,-1.5,6.0)  # 1
    glVertex3f(-0.5,-2.5,6.0)  # 2
    glVertex3f(0.5,-2.5,6.0)  # 3
    glVertex3f(0.5,-1.5,6.0)  # 4
    
    # Back Face
 
    glVertex3f(-0.5, -1.5, 7.5)  # 5
    glVertex3f(-0.5,-2.5,7.5)  # 6
    glVertex3f(0.5,-2.5,7.5)  # 7
    glVertex3f(0.5,-1.5,7.5)  # 8
    
    # Side Faces
    # Side 1

    glVertex3f(-0.5,-1.5,6.0)  # 1
    glVertex3f(-0.5, -1.5, 7.5) # 5
    glVertex3f(-0.5,-2.5,7.5)  # 6
    glVertex3f(-0.5,-2.5,6.0)  # 2
    
    # Side 2

    glVertex3f(0.5,-1.5,6.0)  # 4
    glVertex3f(0.5,-1.5,7.5)  # 8
    glVertex3f(0.5,-2.5,7.5)  # 7
    glVertex3f(0.5,-2.5,6.0)  # 3

    #cara inferior

    glVertex3f(-0.5,-1.5,6.0)  # 1
    glVertex3f(0.5,-1.5,6.0)  # 4
    glVertex3f(0.5,-1.5,7.5)  # 8
    glVertex3f(-0.5, -1.5, 7.5)  # 5

    #cara posterior

    glVertex3f(-0.5,-2.5,6.0)  # 2
    glVertex3f(0.5,-2.5,6.0)  # 3
    glVertex3f(0.5,-2.5,7.5)  # 7
    glVertex3f(-0.5,-2.5,7.5)  # 6


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

def mov_Cabeza():
    glBegin(GL_QUADS)
 # Front Face
    # Beige
    glVertex3f(-1.5,-1.5,7.5)  # 1
    glVertex3f(-1.5,-2.5,7.5)  # 2
    glVertex3f(1.5,-2.5,7.5)  # 3
    glVertex3f(1.5,-1.5,7.5)  # 4
    
    # Back Face
     # Beige
    glVertex3f(-1.5,-1.5,9.5)  # 5
    glVertex3f(-1.5,-2.5,9.5)  # 6
    glVertex3f(1.5, -2.5, 9.5)  # 7
    glVertex3f(1.5,-1.5,9.5)  # 8
    
    # Side Faces
    # Side 1
     # Beige
    glVertex3f(-1.5,-1.5,7.5)  # 1
    glVertex3f(-1.5,-1.5,9.5)  # 5
    glVertex3f(-1.5,-2.5,9.5)  # 6
    glVertex3f(-1.5,-2.5,7.5)  # 2
    
    # Side 2
     # Beige
    glVertex3f(1.5,-1.5,7.5)  # 4
    glVertex3f(1.5,-1.5,9.5)  # 8
    glVertex3f(1.5, -2.5, 9.5) # 7
    glVertex3f(1.5,-2.5,7.5)  # 3

    #cara inferior
      # Beige
    glVertex3f(-1.5,-1.5,7.5)  # 1
    glVertex3f(1.5,-1.5,7.5)  # 4
    glVertex3f(1.5,-1.5,9.5)  # 8
    glVertex3f(-1.5,-1.5,9.5)  # 5

    #cara posterior
      # Beige
    glVertex3f(-1.5,-2.5,7.5)  # 2
    glVertex3f(1.5,-2.5,7.5)  # 3
    glVertex3f(1.5, -2.5, 9.5)  # 7
    glVertex3f(-1.5,-2.5,9.5)  # 6
   

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

    
def mov_draw_ojos():
    glBegin(GL_QUADS)
    glColor3f(0.0, 0.0, 0.0)
    glVertex3f(-1.3,-2.6,8.6)#1
    glVertex3f(-.4,-2.6,8.6)#4
    glVertex3f(-.4,-2.6,8.7)#5
    glVertex3f(-1.3,-2.6,8.7)#8

    glVertex3f(.4,-2.6,8.6)#1
    glVertex3f(1.3,-2.6,8.6)#4
    glVertex3f(1.3,-2.6,8.7)#5
    glVertex3f(.4,-2.6,8.7)#8

    

    glEnd()

def draw_ojos_asco():
    glBegin(GL_QUADS)
    glColor3f(0.0, 0.0, 0.0)
    glVertex3f(-1.3,-2.6,7.6)#1
    glVertex3f(-.4,-2.6,7.6)#4
    glVertex3f(-.4,-2.6,7.7)#5
    glVertex3f(-1.3,-2.6,7.7)#8

    glVertex3f(.4,-2.6,7.6)#1
    glVertex3f(1.3,-2.6,7.6)#4
    glVertex3f(1.3,-2.6,7.7)#5
    glVertex3f(.4,-2.6,7.7)#8

    glColor3f(0.0, 0.0, 0.0)
    glVertex3f(-1.3,-2.6,8.0)#1
    glVertex3f(-.4,-2.6,7.6)#4
    glVertex3f(-.4,-2.6,7.7)#5
    glVertex3f(-1.3,-2.6,8.0)#8

    glVertex3f(.4,-2.6,7.6)#1
    glVertex3f(1.3,-2.6,8.0)#4
    glVertex3f(1.3,-2.6,8.0)#5
    glVertex3f(.4,-2.6,7.7)#8

    

    glEnd()    

def draw_enojo():
    glBegin(GL_QUADS)

    glVertex3f(-.7,-2.6,6.9)#1
    glVertex3f(-.7,-2.6,7.2)#5
    glVertex3f(.77,-2.6,6.9)#4
    glVertex3f(.7,-2.6,7.2)#8
    glEnd()

def draw_feliz():
    glBegin(GL_QUADS)
    glColor3f(1.0, 1.0, 1.0)
    glVertex3f(-.7,-2.52,6.9)#1
    glVertex3f(.7,-2.52,6.9)#4
    glVertex3f(.7,-2.52,7.2)#8
    glVertex3f(-.7,-2.52,7.2)#5
    
    
    glEnd()


def asombro():
    glBegin(GL_QUADS)
    glColor3f(1.0, 1.0, 1.0)
    glVertex3f(-.3,-2.52,6.9)#1
    glVertex3f(.3,-2.52,6.9)#4
    glVertex3f(.3,-2.52,7.2)#8
    glVertex3f(-.3,-2.52,7.2)#5
    
    
    glEnd()

def draw_triste():
    glColor3f(0.0, 0.0, 0.0)
    glBegin(GL_QUADS)
    glVertex3f(-.7,-2.52,6.9)#1
    glVertex3f(.7,-2.52,6.9)#4
    glVertex3f(.7,-2.52,7.0)#8
    glVertex3f(-.7,-2.52,7.0)#5

    
    glVertex3f(.58,-2.52,6.8)#1
    glVertex3f(.7,-2.52,6.8)#4
    glVertex3f(.7,-2.52,7.0)#8
    glVertex3f(.58,-2.52,7.0)#5

    glVertex3f(-.58,-2.52,6.8)#1
    glVertex3f(-.7,-2.52,6.8)#4
    glVertex3f(-.7,-2.52,7.0)#8
    glVertex3f(-.58,-2.52,7.0)#5
    
    
    glEnd()

def lagrimas():
    glBegin(GL_QUADS)
    glColor3f(0.0, 0.0, 1.0)
    glVertex3f(-1.3,-2.6,7.7)#1
    glVertex3f(-1.2,-2.6,7.7)#4
    glVertex3f(-1.2,-2.6,7.5)#5
    glVertex3f(-1.3,-2.6,7.5)#8

    glVertex3f(1.2,-2.6,7.7)#1
    glVertex3f(1.3,-2.6,7.7)#4
    glVertex3f(1.3,-2.6,7.5)#5
    glVertex3f(1.2,-2.6,7.5)#8

    
    glColor3f(0.0, 0.0, 1.0)
    glVertex3f(-1.3,-2.6,7.4)#1
    glVertex3f(-1.2,-2.6,7.4)#4
    glVertex3f(-1.2,-2.6,7.2)#5
    glVertex3f(-1.3,-2.6,7.2)#8

    glVertex3f(1.2,-2.6,7.4)#1
    glVertex3f(1.3,-2.6,7.4)#4
    glVertex3f(1.3,-2.6,7.2)#5
    glVertex3f(1.2,-2.6,7.2)#8

    glColor3f(0.0, 0.0, 1.0)
    glVertex3f(-1.3,-2.6,7.1)#1
    glVertex3f(-1.2,-2.6,7.1)#4
    glVertex3f(-1.2,-2.6,6.9)#5
    glVertex3f(-1.3,-2.6,6.9)#8

    glVertex3f(1.2,-2.6,7.1)#1
    glVertex3f(1.3,-2.6,7.1)#4
    glVertex3f(1.3,-2.6,6.9)#5
    glVertex3f(1.2,-2.6,6.9)#8

    glEnd()

def dientes():
    glBegin(GL_QUADS)
    glColor3f(0.0, 0.0, 0.0)  # Color negro
    # Definir los vértices para la línea
    glVertex3f(-0.7, -2.56, 7.05)  # 1
    glVertex3f(0.7, -2.56, 7.05)   # 4
    glVertex3f(0.7, -2.53, 7.05)  # 8
    glVertex3f(-0.7, -2.53, 7.05) # 5

    # Línea 1
    glVertex3f(0.0, -2.56, 6.9)   # 1
    glVertex3f(0.0, -2.56, 7.2)   # 4
    glVertex3f(0.0, -2.53, 7.2)  # 8
    glVertex3f(0.0, -2.53, 6.9)  # 5

    # Línea 2
    glVertex3f(-0.35, -2.56, 6.9)  # 1
    glVertex3f(-0.35, -2.56, 7.2)  # 4
    glVertex3f(-0.35, -2.53, 7.2) # 8
    glVertex3f(-0.35, -2.53, 6.9) # 5

    # Línea 3
    glVertex3f(0.35, -2.56, 6.9)  # 1
    glVertex3f(0.35, -2.56, 7.2)  # 4
    glVertex3f(0.35, -2.53, 7.2) # 8
    glVertex3f(0.35, -2.53, 6.9) # 5

   
    glVertex3f(-.71,-2.51,6.9)#1
    glVertex3f(.71,-2.51,6.9)#4
    glVertex3f(.71,-2.51,7.2)#8
    glVertex3f(-.71,-2.51,7.2)#5
   

    glEnd()


#def draw_cube():
    glBegin(GL_QUADS)

    # Cara frontal
    glVertex3f(-5.0, -5.0, 5.0)
    glVertex3f(5.0, -5.0, 5.0)
    glVertex3f(5.0, 5.0, 5.0)
    glVertex3f(-5.0, 5.0, 5.0)

    # Cara trasera
    glVertex3f(-5.0, -5.0, -5.0)
    glVertex3f(5.0, -5.0, -5.0)
    glVertex3f(5.0, 5.0, -5.0)
    glVertex3f(-5.0, 5.0, -5.0)

    # Caras laterales
    glVertex3f(-5.0, -5.0, 5.0)
    glVertex3f(5.0, -5.0, 5.0)
    glVertex3f(5.0, -5.0, -5.0)
    glVertex3f(-5.0, -5.0, -5.0)

    glVertex3f(-5.0, 5.0, 5.0)
    glVertex3f(5.0, 5.0, 5.0)
    glVertex3f(5.0, 5.0, -5.0)
    glVertex3f(-5.0, 5.0, -5.0)

    glVertex3f(-5.0, -5.0, 5.0)
    glVertex3f(-5.0, 5.0, 5.0)
    glVertex3f(-5.0, 5.0, -5.0)
    glVertex3f(-5.0, -5.0, -5.0)

    glVertex3f(5.0, -5.0, 5.0)
    glVertex3f(5.0, 5.0, 5.0)
    glVertex3f(5.0, 5.0, -5.0)
    glVertex3f(5.0, -5.0, -5.0)

    glEnd()


#def draw_cube():
    glBegin(GL_QUADS)

    #cara frontal
    glVertex3f(-10.0,-10.0,10.0)
    glVertex3f(10.0,-10.0,10.0)
    glVertex3f(10.0,10.0,10.0)
    glVertex3f(-10.0,10.0,10.0)
    #cara trasera
    glVertex3f(-10.0,-10.0,-10.0)
    glVertex3f(10.0,-10.0,-10.0)
    glVertex3f(10.0,10.0,-10.0)
    glVertex3f(-10.0,-10.0,-10.0)
    #caras laterales:
    glVertex3f(-10.0,-10.0,10.0)
    glVertex3f(10.0,-10.0,10.0)
    glVertex3f(10.0,-10.0,-10.0)
    glVertex3f(-10.0,-10.0,-10.0)

    glVertex3f(-10.0,10.0,10.0)
    glVertex3f(10.0,10.0,10.0)
    glVertex3f(10.0,10.0,-10.0)
    glVertex3f(-10.0,10.0,-10.0)

    glVertex3f(-10.0,-10.0,10.0)
    glVertex3f(-10.0,10.0,10.0)
    glVertex3f(-10.0,10.0,-10.0)
    glVertex3f(-10.0,-10.0,-10.0)

    glVertex3f(10.0,-10.0,10.0)
    glVertex3f(10.0,10.0,10.0)
    glVertex3f(10.0,10.0,-10.0)
    glVertex3f(10.0,-10.0,-10.0)

    glEnd()
    
def draw_sphere(radius,num_slices,num_segments):
    for i in range(num_slices+1):
        lat0=math.pi * (-0.5 +(i-1)/num_slices)
        z0=radius * math.sin(lat0)
        zr0=radius * math.cos(lat0)
 
        lat1=math.pi * (-0.5 + i /num_slices)
        z1=radius * math.sin(lat1)
        zr1=radius * math.cos(lat1)
 
        glBegin(GL_QUAD_STRIP)
        for j in range(num_segments+1):
            lng=2*math.pi * j / num_segments
            x=zr0 * math.cos(lng)
            y=zr0 * math.sin(lng)
 
            glNormal3f(x,y,z0)
            glVertex3f(x,y,z0)
 
            x=zr1 * math.cos(lng)
            y=zr1 * math.sin(lng)
 
            glNormal3f(x,y,z1)
            glVertex3f(x,y,z1)
 
        glEnd()    


def draw_cylinder(radius, height, num_segments):
    glBegin(GL_QUAD_STRIP)
    for i in range(num_segments + 1):
        theta = i * (2 * math.pi / num_segments)
        x = radius * math.cos(theta)
        z = radius * math.sin(theta)
 
        glVertex3f(x, height / 2, z)
        glVertex3f(x, -height /2, z)
    glEnd()

def draw_cube():
    glBegin(GL_QUADS)
 
    #cara frontal
    glVertex3f(-1.0, -1.0, 1.0)
    glVertex3f(1.0, -1.0, 1.0)
    glVertex3f(1.0, 1.0, 1.0)
    glVertex3f(-1.0, 1.0, 1.0)
 
    #cara trasera
    glVertex3f(-1.0, -1.0, -1.0)
    glVertex3f(1.0, -1.0, -1.0)
    glVertex3f(1.0, 1.0, -1.0)
    glVertex3f(-1.0, 1.0, -1.0)
 
    #caras laterales
    glVertex3f(-1.0, -1.0, 1.0)
    glVertex3f(1.0, -1.0, 1.0)
    glVertex3f(1.0, -1.0, -1.0)
    glVertex3f(-1.0, -1.0, -1.0)
 
    glVertex3f(-1.0, 1.0, 1.0)
    glVertex3f(1.0, 1.0, 1.0)
    glVertex3f(1.0, 1.0, -1.0)
    glVertex3f(-1.0, 1.0, -1.0)
 
    glVertex3f(-1.0, -1.0, 1.0)
    glVertex3f(-1.0, 1.0, 1.0)
    glVertex3f(-1.0, 1.0, -1.0)
    glVertex3f(-1.0, -1.0, -1.0)
 
    glVertex3f(1.0, -1.0, 1.0)
    glVertex3f(1.0, 1.0, 1.0)
    glVertex3f(1.0, 1.0, -1.0)
    glVertex3f(1.0, -1.0, -1.0)
 
    glEnd()