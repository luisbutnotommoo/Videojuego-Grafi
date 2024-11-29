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
