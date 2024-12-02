import pygame
from OpenGL.GLU import *
from OpenGL.GL import *
from OpenGL.GLUT import *
from pygame.locals import *
import Acciones.texto as txt

class ViewPortPreguntas:
    def __init__(self, display_inicial):
        """
        Inicializa el ViewPort con las dimensiones de la pantalla.
        
        :param display_inicial: Tupla con el ancho y alto de la pantalla
        """
        self.display = display_inicial

    def _calcular_dimensiones_texto(self, texto, tamano_fuente):
        """
        Calcula las dimensiones estimadas del texto.
        
        :param texto: Cadena de texto a renderizar
        :param tamano_fuente: Tamaño de la fuente
        :return: Tupla de (ancho estimado, alto estimado)
        """
        # Estimación aproximada del ancho y alto del texto
        # Ajusta estos multiplicadores según tu fuente específica
        ancho_estimado = len(texto) * (tamano_fuente * 0.3)  # Ajusta el multiplicador según sea necesario
        alto_estimado = tamano_fuente * 9  # Estimación de la altura de línea
        
        return ancho_estimado, alto_estimado

    def draw_viewport(self, objeto_pregunta, tamano_fuente=18, relleno=40):
        """
        Dibuja un viewport dinámico que se ajusta al texto de la pregunta.
        
        :param objeto_pregunta: Texto de la pregunta a mostrar
        :param tamano_fuente: Tamaño de la fuente
        :param relleno: Relleno adicional alrededor del texto
        """
        if objeto_pregunta is None:
            return

        # Cambiar a vista 2D sin borrar la pantalla
        objeto_pregunta="\n"+objeto_pregunta
        glMatrixMode(GL_PROJECTION)
        glPushMatrix()
        glLoadIdentity()
        gluOrtho2D(0, self.display[0], 0, self.display[1])
        glMatrixMode(GL_MODELVIEW)
        glPushMatrix()
        glLoadIdentity()

        # Calcular dimensiones del texto
        ancho_texto, alto_texto = self._calcular_dimensiones_texto(objeto_pregunta, tamano_fuente)

        # Definir dimensiones del viewport dinámicamente
        ancho_viewport = min(
            max(ancho_texto + relleno, self.display[0] // 3.3),  # Ancho mínimo
            self.display[0] * 2  # Ancho máximo
        )
        alto_viewport = min(
            max(alto_texto + relleno, self.display[1] // 5),  # Alto mínimo
            self.display[1] * 0.4  # Alto máximo
        )

        # Centrar el viewport
        x_offset = (self.display[0] - ancho_viewport) // 2
        y_offset = (self.display[1] * 2 // 3)

        # Dibujar el fondo del cuadro de texto
        glColor3f(1.0, 0.87, 0.77)  # Color piel
        glBegin(GL_QUADS)
        glVertex2f(x_offset, y_offset)
        glVertex2f(x_offset + ancho_viewport, y_offset)
        glVertex2f(x_offset + ancho_viewport, y_offset - alto_viewport)
        glVertex2f(x_offset, y_offset - alto_viewport)
        glEnd()

        # Dibujar el texto de la pregunta
        text_x = x_offset + relleno // 2
        text_y = y_offset - relleno // 2
        txt.textos().display_text(objeto_pregunta, text_x, text_y, tamano_fuente)

        # Restaurar las matrices
        glMatrixMode(GL_PROJECTION)
        glPopMatrix()
        glMatrixMode(GL_MODELVIEW)
        glPopMatrix()
    


