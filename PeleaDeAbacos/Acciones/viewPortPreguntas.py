import pygame
from OpenGL.GLU import*
from OpenGL.GL import*
from OpenGL.GLUT import*
from pygame.locals import*
from PIL import*
import Acciones.objetos as obj
import Acciones.texto as txt
import random as ran
import Acciones.bancoPreguntas as bp
class viewPort:

    def __init__(self, displayInicial):
        self.display = displayInicial

        

    def draw_viewport(self,objetoPregunta):
        # Cambiar a vista 2D sin borrar la pantalla
        glMatrixMode(GL_PROJECTION)
        glPushMatrix()  # Guardar la proyección actual
        glLoadIdentity()
        gluOrtho2D(0, self.display[0], 0, self.display[1])
        glMatrixMode(GL_MODELVIEW)
        glPushMatrix()  # Guardar la matriz de vista actual
        glLoadIdentity()

        # Dibujar el fondo del cuadro de texto (más pequeño y movido hacia arriba)
        glColor3f(1.0, 0.87, 0.77)  # Color piel
        # Ajustamos el tamaño y la posición del rectángulo (más pequeño y más arriba)
        viewport_width = self.display[0] // 3.3  # 33% del ancho de la pantalla
        viewport_height = self.display[1] // 5  # 10% del alto de la pantalla
        x_offset = self.display[0] // 3  # Centrar más estrecho
        y_offset = 2 * self.display[1] // 3 # Moverlo hacia arriba

        glBegin(GL_QUADS)
        glVertex2f(x_offset, y_offset)
        glVertex2f(x_offset + viewport_width, y_offset)
        glVertex2f(x_offset + viewport_width, y_offset - viewport_height)
        glVertex2f(x_offset, y_offset - viewport_height)
        glEnd()

         # Dibujar el texto de la pregunta
        if objetoPregunta.preguntaActual:
            text_x = x_offset + 20  # Ajuste horizontal
            text_y = y_offset - 30  # Ajuste vertical
            txt.textos().display_text(objetoPregunta.preguntaActual, text_x, text_y, 18)


        # Restaurar las matrices
        glMatrixMode(GL_PROJECTION)
        glPopMatrix()
        glMatrixMode(GL_MODELVIEW)
        glPopMatrix()
    
    def draw_viewport2(self,objetoPregunta):
        # Cambiar a vista 2D sin borrar la pantalla
        glMatrixMode(GL_PROJECTION)
        glPushMatrix()  # Guardar la proyección actual
        glLoadIdentity()
        gluOrtho2D(0, self.display[0], 0, self.display[1])
        glMatrixMode(GL_MODELVIEW)
        glPushMatrix()  # Guardar la matriz de vista actual
        glLoadIdentity()

        # Dibujar el fondo del cuadro de texto (más pequeño y movido hacia arriba)
        glColor3f(1.0, 0.87, 0.77)  # Color piel
        # Ajustamos el tamaño y la posición del rectángulo (más pequeño y más arriba)
        viewport_width = self.display[0] // 3.3  # 33% del ancho de la pantalla
        viewport_height = self.display[1] // 5  # 10% del alto de la pantalla
        x_offset = self.display[0] // 3  # Centrar más estrecho
        y_offset = 2 * self.display[1] // 3 # Moverlo hacia arriba

        glBegin(GL_QUADS)
        glVertex2f(x_offset, y_offset)
        glVertex2f(x_offset + viewport_width, y_offset)
        glVertex2f(x_offset + viewport_width, y_offset - viewport_height)
        glVertex2f(x_offset, y_offset - viewport_height)
        glEnd()

         # Dibujar el texto de la pregunta
        if objetoPregunta.preguntaActual:
            text_x = x_offset + 20  # Ajuste horizontal
            text_y = y_offset - 25  # Ajuste vertical
            txt.textos().display_text(objetoPregunta.preguntaActual, text_x, text_y, 16)


        # Restaurar las matrices
        glMatrixMode(GL_PROJECTION)
        glPopMatrix()
        glMatrixMode(GL_MODELVIEW)
        glPopMatrix()
    


