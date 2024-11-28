import pygame
from OpenGL.GLU import*
from OpenGL.GL import*
from OpenGL.GLUT import*
def iluminacion():
    glEnable(GL_LIGHTING)  # Habilitar iluminación
    glEnable(GL_LIGHT0)    # Habilitar la luz 0
    glEnable(GL_COLOR_MATERIAL)  # Permitir que los colores de los materiales interactúen con la luz
    glColorMaterial(GL_FRONT_AND_BACK, GL_AMBIENT_AND_DIFFUSE)

    # Configurar las propiedades de la luz
    light_position = [1.0, 1.0, 1.0, 0.0]  # Posición de la luz
    light_ambient = [0.2, 0.2, 0.2, 1.0]  # Luz ambiental
    light_diffuse = [0.8, 0.8, 0.8, 1.0]  # Luz difusa
    light_specular = [1.0, 1.0, 1.0, 1.0]  # Luz especular (brillo)

    glLightfv(GL_LIGHT0, GL_POSITION, light_position)  # Posición de la luz
    glLightfv(GL_LIGHT0, GL_AMBIENT, light_ambient)    # Luz ambiental
    glLightfv(GL_LIGHT0, GL_DIFFUSE, light_diffuse)    # Luz difusa
    glLightfv(GL_LIGHT0, GL_SPECULAR, light_specular)  # Luz especular


