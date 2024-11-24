from OpenGL.GLU import *
from OpenGL.GL import *
from OpenGL.GLUT import *

def iluminacion(R, G, B):
    glEnable(GL_LIGHTING) #Habilita la iluminacion
    glEnable(GL_LIGHT0) #Fuente de luz
    glEnable(GL_DEPTH_TEST) #Habilitar primer fuente de luz

    # Propiedades de la fuente de luz
    posicion_luz = (30.0, 5.0, 5.0, 1.0)
    luz_ambiental = (1.0, 0.7, 0.2, 1.0) #Color RGB
    difusion = (R,G,B, 1.0)

    glLightfv(GL_LIGHT0, GL_POSITION, posicion_luz)
    glLightfv(GL_LIGHT0, GL_AMBIENT, luz_ambiental)
    glLightfv(GL_LIGHT0, GL_DIFFUSE, difusion)