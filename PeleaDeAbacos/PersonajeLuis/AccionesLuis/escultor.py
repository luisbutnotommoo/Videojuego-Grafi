from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import *

def render_prismas(tupla_prismas,lista_colores):
    #recibimos el arreglo de puntos que se suponen son prismas (incluyendo cubos) y los colores con los que se deben pintar
    itera_color=0 #controla que color pinta el renderizado
    for matriz_extremidad in tupla_prismas:     
        if len(matriz_extremidad)==2:
            vertices=matriz_extremidad[0]
            caras=matriz_extremidad[1]
            glBegin(GL_QUADS) 
            glColor3f(*lista_colores[itera_color])
            for cara in caras:
                for vertice in cara:
                    glVertex3fv(vertices[vertice])
            glEnd()
        itera_color+=1

def render_piramides(tupla_piramides, lista_colores):
    # Hace lo mismo que el otro pero con piramides
    itera_color=0
    for matriz_extremidad in tupla_piramides:
        if len(matriz_extremidad) == 2:
            vertices = matriz_extremidad[0]
            caras = matriz_extremidad[1]
        
            glColor3f(*lista_colores[itera_color])
        
            glBegin(GL_TRIANGLES)
            for cara in caras:
                for i in range(1, len(cara)):
                    glVertex3fv(vertices[cara[0]])
                    glVertex3fv(vertices[cara[i]])
                    glVertex3fv(vertices[cara[(i + 1) % len(cara)]])
            glEnd()

            # Pintamos las aristas de negro (lo añadí porque se perdia la oreja color blanco con la cabeza)
            glColor3f(0, 0, 0)
            glBegin(GL_LINES)
            for cara in caras:
                for i in range(len(cara)):
                    glVertex3fv(vertices[cara[i]])
                    glVertex3fv(vertices[cara[(i + 1) % len(cara)]])
            glEnd()
        itera_color+=1


def render_esfera(centro,radio,color,expresion):
    glPushMatrix() 
    glTranslatef(*centro) 
    glColor3f(*color)
    esfera = gluNewQuadric() 
    gluSphere(esfera, radio, 32, 16)
    
    glPopMatrix()  
    dibujar_lineas(expresion)


def dibujar_lineas(cara):
    #recorremos el array asociado a la expresion y lo pintamos con 0.5 de grosor
    if cara is not None:
        for faccion in cara:
            for i in range(len(faccion)-1):
                glLineWidth(9)
                glBegin(GL_LINES)
                glColor3f(0.0, 0.0, 0.0)
                glVertex3f(*faccion[i]) 
                glVertex3f(*faccion[i+1])  
                glEnd()
        glLineWidth(0.5)
