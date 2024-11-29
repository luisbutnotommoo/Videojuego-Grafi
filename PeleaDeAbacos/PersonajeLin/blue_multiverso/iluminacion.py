from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import *
from personaje import *


def init_lighting():
    # Habilitar la iluminación
    glEnable(GL_LIGHTING)
    glEnable(GL_LIGHT0)
    glEnable(GL_COLOR_MATERIAL)
    
    # Configurar la fuente de luz
    light_position = [1.0, 1.0, 1.0, 0.0]
    glLightfv(GL_LIGHT0, GL_POSITION, light_position)
    
    # Configurar el ambiente, difuso y especular de la luz
    light_ambient = [0.2, 0.2, 0.2, 1.0]
    light_diffuse = [0.8, 0.8, 0.8, 1.0]
    light_specular = [1.0, 1.0, 1.0, 1.0]
    
    glLightfv(GL_LIGHT0, GL_AMBIENT, light_ambient)
    glLightfv(GL_LIGHT0, GL_DIFFUSE, light_diffuse)
    glLightfv(GL_LIGHT0, GL_SPECULAR, light_specular)
    
    # Materiales
    mat_specular = [1.0, 1.0, 1.0, 1.0]
    mat_shininess = 50.0
    glMaterialfv(GL_FRONT, GL_SPECULAR, mat_specular)
    glMaterialf(GL_FRONT, GL_SHININESS, mat_shininess)

def display():
    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
    glLoadIdentity()
    
    # Configuración de cámara
    gluLookAt(0, 0, 5, 0, 0, 0, 0, 1, 0)
    
    # Dibujar partes del personaje con iluminación Phong
    draw_piernaIz()
    draw_piernaDe()
    draw_BrazoDe()
    draw_BrazoIz()
    
    glutSwapBuffers()

# Definir otras funciones de dibujo del personaje aquí (draw_piernaIz, draw_piernaDe, etc.)

def main():
    glutInit()
    glutInitDisplayMode(GLUT_DOUBLE | GLUT_RGB | GLUT_DEPTH)
    glutInitWindowSize(500, 500)
    glutCreateWindow(b"Modelo Phong en OpenGL")
    
    init_lighting()
    glEnable(GL_DEPTH_TEST)
    glutDisplayFunc(display)
    glutMainLoop()

main()
