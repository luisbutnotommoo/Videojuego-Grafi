import pygame
from pygame.locals import *
from OpenGL.GL import *
from OpenGL.GLU import *

def draw_cube():
    # Vertices del cubo (cuerpo y cabeza)
    vertices = [
        (1, -1, -1), (1, 1, -1), (-1, 1, -1), (-1, -1, -1),   # Cara trasera
        (1, -1, 1), (1, 1, 1), (-1, 1, 1), (-1, -1, 1)        # Cara delantera
    ]
    
    # Lados del cubo
    edges = (
        (0, 1, 2, 3),  # Atrás
        (3, 7, 6, 2),  # Izquierda
        (7, 6, 5, 4),  # Adelante
        (0, 4, 5, 1),  # Derecha
        (1, 5, 6, 2),  # Arriba
        (0, 3, 7, 4),  # Abajo
    )

    glBegin(GL_QUADS)
    for edge in edges:
        for vertex in edge:
            glVertex3fv(vertices[vertex])
    glEnd()

def draw_character():
    # Cuerpo
    glPushMatrix()
    glScalef(0.25, 0.5, 0.10)  # Escalar para alargar el cubo a un cuerpo
    draw_cube()
    glPopMatrix()

    # Cabeza
    glPushMatrix()
    glTranslatef(0, 0.5, 0)  # Mover la cabeza hacia arriba
    glScalef(0.25, 0.25, 0.25)  # Escalar la cabeza más pequeña
    draw_cube()
    glPopMatrix()

def draw_face():
    # Dibujar una cara simple en el frente de la cabeza
    glColor3f(0.9, 0.8, 0.6)  # BBeige
    glBegin(GL_QUADS)
    
    # Ojo izquierdo
    glVertex3f(-0.3, 0.2, 1.01)
    glVertex3f(-0.1, 0.2, 1.01)
    glVertex3f(-0.1, 0.4, 1.01)
    glVertex3f(-0.3, 0.4, 1.01)

    # Ojo derecho
    glVertex3f(0.1, 0.2, 1.01)
    glVertex3f(0.3, 0.2, 1.01)
    glVertex3f(0.3, 0.4, 1.01)
    glVertex3f(0.1, 0.4, 1.01)

    # Boca
    glVertex3f(-0.2, -0.1, 1.01)
    glVertex3f(0.2, -0.1, 1.01)
    glVertex3f(0.2, -0.3, 1.01)
    glVertex3f(-0.2, -0.3, 1.01)

    glEnd()

def init():
    glClearColor(0.0, 0.0, 0.0, 1.0)
    gluPerspective(45, (800/600), 0.1, 50.0)
    glTranslatef(0.0, 0.0, -5)

def main():
    pygame.init()
    display = (800, 600)
    pygame.display.set_mode(display, DOUBLEBUF | OPENGL)
    init()

    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
        
        draw_character()  # Dibujar cuerpo y cabeza
        draw_face()       # Dibujar cara en la cabeza
        
        pygame.display.flip()
        pygame.time.wait(10)

    pygame.quit()

if __name__ == "__main__":
    main()
