import pygame
from OpenGL.GLU import*
from OpenGL.GL import*
from OpenGL.GLUT import*


def iluminacion(R, G, B):
    glEnable(GL_LIGHTING)  # Habilita la iluminación
    glEnable(GL_LIGHT0)    # Habilita la fuente de luz 0
    glEnable(GL_DEPTH_TEST) # Habilita la prueba de profundidad

    # Propiedades de la fuente de luz
    posicion_luz = (5.0, 5.0, 5.0, 1.0)  # Posición de la luz (x, y, z, w)
    luz_ambiental = (1.0, 0.7, 0.2, 1.0)  # Color de la luz ambiental (RGBA)
    difusion = (R, G, B, 1.0)              # Color de difusión de la luz (RGBA)

    # Configuraciones de la fuente de luz
    glLightfv(GL_LIGHT0, GL_POSITION, posicion_luz)
    glLightfv(GL_LIGHT0, GL_AMBIENT, luz_ambiental)
    glLightfv(GL_LIGHT0, GL_DIFFUSE, difusion)
from OpenGL.GLU import *
from OpenGL.GL import *
from OpenGL.GLUT import *



#3 vectores de iluminación, la ilumn. está en el ambiente



def phong(R, G, B):
    glEnable(GL_LIGHTING) # Habilita las luces
    glEnable(GL_LIGHT0) # Fuente de luz
    glEnable(GL_DEPTH_TEST) # Habilita el z-buffer

    # Propiedades de la fuente de luz
    posicion_luz = (150.0, 250.0, -250.0, 1.0)
    luz_ambiental = (0.1, 0.1, 0.1, 1.0)
    luz_difusa = (R, G, B, 1.0)
    luz_especular = (1.0, 1.0, 1.0, 1.0)
    glLightfv(GL_LIGHT0, GL_POSITION, posicion_luz)
    glLightfv(GL_LIGHT0, GL_AMBIENT, luz_ambiental) 
    glLightfv(GL_LIGHT0, GL_DIFFUSE, luz_difusa)
    glLightfv(GL_LIGHT0, GL_SPECULAR, luz_especular)

    # Material del objeto
    material_ambiente = (0.2, 0.2, 0.2, 1.0)
    material_difuso = (R, G, B, 1.0)
    material_especular = (1.0, 1.0, 1.0, 1.0)
    brillo_especular = 50.0
    glMaterialfv(GL_FRONT, GL_AMBIENT, material_ambiente)
    glMaterialfv(GL_FRONT, GL_DIFFUSE, material_difuso)
    glMaterialfv(GL_FRONT, GL_SPECULAR, material_especular)
    glMaterialfv(GL_FRONT, GL_SHININESS, brillo_especular)

    # Configuración de Phong
    glEnable(GL_COLOR_MATERIAL)
    glColorMaterial(GL_FRONT, GL_AMBIENT_AND_DIFFUSE)

    # Fuentes de luz y modelo de iluminación
    glEnable(GL_LIGHTING)
    glEnable(GL_LIGHT0)
    glEnable(GL_DEPTH_TEST)




def gouraud(R, G, B):
    glEnable(GL_LIGHTING) # Habilita las luces
    glEnable(GL_LIGHT0) # Fuente de luz
    glEnable(GL_DEPTH_TEST) # Habilita el z-buffer

    # Propiedades de la fuente de luz
    posicion_luz = (150.0, 250.0, -250.0, 1.0)
    luz_ambiental = (0.1, 0.1, 0.1, 1.0)
    luz_difusa = (R, G, B, 1.0)
    luz_especular = (1.0, 1.0, 1.0, 1.0)
    glLightfv(GL_LIGHT0, GL_POSITION, posicion_luz)
    glLightfv(GL_LIGHT0, GL_AMBIENT, luz_ambiental) 
    glLightfv(GL_LIGHT0, GL_DIFFUSE, luz_difusa)
    glLightfv(GL_LIGHT0, GL_SPECULAR, luz_especular)

    # Configuración de Gouraud
    glShadeModel(GL_SMOOTH) # Interpolación de colores suaves entre vértices

    # Material del objeto
    material_ambiente = (0.2, 0.2, 0.2, 1.0)
    material_difuso = (R, G, B, 1.0)
    material_especular = (1.0, 1.0, 1.0, 1.0)
    brillo_especular = 50.0
    glMaterialfv(GL_FRONT, GL_AMBIENT, material_ambiente)
    glMaterialfv(GL_FRONT, GL_DIFFUSE, material_difuso)
    glMaterialfv(GL_FRONT, GL_SPECULAR, material_especular)
    glMaterialfv(GL_FRONT, GL_SHININESS, brillo_especular)

    # Fuentes de luz y modelo de iluminación
    glEnable(GL_LIGHTING)
    glEnable(GL_LIGHT0)
    glEnable(GL_DEPTH_TEST)

def interpolado(R, G, B):
    glEnable(GL_LIGHTING) # Habilita las luces
    glEnable(GL_LIGHT0) # Fuente de luz
    glEnable(GL_DEPTH_TEST) # Habilita el z-buffe
    
    #posicion_luz = (150.0, 250.0, -250.0, 1.0)
    posicion_luz = (0.5, 0.5, 0.5, 1.0)
    luz_ambiental = (0.1, 0.1, 0.1, 1.0)
    luz_difusa = (R, G, B, 1.0)
    luz_especular = (1.0, 1.0, 1.0, 1.0)
    glLightfv(GL_LIGHT0, GL_POSITION, posicion_luz)
    glLightfv(GL_LIGHT0, GL_POSITION, posicion_luz)
    glLightfv(GL_LIGHT0, GL_AMBIENT, luz_ambiental) 
    glLightfv(GL_LIGHT0, GL_DIFFUSE, luz_difusa)
    glLightfv(GL_LIGHT0, GL_SPECULAR, luz_especular)
    

    # Configuración de Flat shading (sombreado plano)
    glShadeModel(GL_FLAT)

    # Material del objeto
    material_ambiente = (0.2, 0.2, 0.2, 1.0)
    material_difuso = (R, G, B, 1.0)
    material_especular = (1.0, 1.0, 1.0, 1.0)
    brillo_especular = 50.0
    glMaterialfv(GL_FRONT, GL_AMBIENT, material_ambiente)
    glMaterialfv(GL_FRONT, GL_DIFFUSE, material_difuso)
    glMaterialfv(GL_FRONT, GL_SPECULAR, material_especular)
    glMaterialfv(GL_FRONT, GL_SHININESS, brillo_especular)

    # Fuentes de luz y modelo de iluminación
    glEnable(GL_LIGHTING)
    glEnable(GL_LIGHT0)
    glEnable(GL_DEPTH_TEST)