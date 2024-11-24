import pygame
from OpenGL.GLU import*
from OpenGL.GL import*
from OpenGL.GLUT import*
from pygame.locals import*
from PIL import*
import Acciones.objetos as obj

class textos:
    def display_text(self, text, x, y,num):
        glColor3f(0, 0, 0)  # Color negro para el texto
        font = pygame.font.SysFont("Arial", num, True)  # Tamaño de fuente reducido a 24
        lines = text.split('\n')  # Dividir el texto por líneas usando '\n'

        # Dibujar cada línea, desplazándola verticalmente
        for i, line in enumerate(lines):
                text_surface = font.render(line, True, (0, 0, 0), (255, 223, 191))
                text_data = pygame.image.tostring(text_surface, "RGBA", True)
                glWindowPos2d(x, y - i * 30)  # Ajustar el espaciado entre líneas (30 píxeles entre líneas)
                glDrawPixels(text_surface.get_width(), text_surface.get_height(), GL_RGBA, GL_UNSIGNED_BYTE, text_data)

    def draw_text2(texto_instrucciones, font, transparencia, pos_x, pos_y, x_inicio=0, y_inicio=0, ancho=800, alto=600):
        # Asegurar que la transparencia esté dentro de un rango válido
        transparencia = max(0, min(255, transparencia))  # Limita el valor entre 0 y 255

        # Crear una superficie transparente en Pygame
        superficie = pygame.Surface((800, 600), pygame.SRCALPHA)
        superficie.fill((0, 0, 0, 0))  # Fondo totalmente transparente

        # Dibujar un rectángulo con fondo semitransparente
        fondo_rect = pygame.Rect(x_inicio, y_inicio, ancho, alto)
        pygame.draw.rect(superficie, (0, 0, 0, transparencia), fondo_rect)

        # Renderizar el texto en la superficie
        y_offset = pos_y  # Iniciar en la posición Y proporcionada
        for linea in texto_instrucciones:
            texto = font.render(linea, True, (255, 255, 255))  # Texto blanco
            superficie.blit(texto, (pos_x, y_offset))  # Dibujar en la posición X, Y
            y_offset += 40  # Incrementar la posición Y para la siguiente línea

        # Convertir la superficie de Pygame a una textura de OpenGL
        textura_data = pygame.image.tostring(superficie, "RGBA", True)
        textura_id = glGenTextures(1)
        glBindTexture(GL_TEXTURE_2D, textura_id)
        glTexImage2D(GL_TEXTURE_2D, 0, GL_RGBA, superficie.get_width(), superficie.get_height(), 0, GL_RGBA, GL_UNSIGNED_BYTE, textura_data)
        glTexParameteri(GL_TEXTURE_2D, GL_TEXTURE_MIN_FILTER, GL_LINEAR)
        glTexParameteri(GL_TEXTURE_2D, GL_TEXTURE_MAG_FILTER, GL_LINEAR)

        # Configuración de OpenGL para renderizar en 2D sin perspectiva
        glMatrixMode(GL_PROJECTION)
        glPushMatrix()
        glLoadIdentity()
        glOrtho(0, 800, 600, 0, -1, 1)
        glMatrixMode(GL_MODELVIEW)
        glPushMatrix()
        glLoadIdentity()

        # Habilitar mezcla y configurar la función de mezcla para transparencia
        glEnable(GL_BLEND)
        glBlendFunc(GL_SRC_ALPHA, GL_ONE_MINUS_SRC_ALPHA)

        # Dibujar el cuadrado de textura de la superficie en pantalla con coordenadas de textura corregidas
        glColor4f(1, 1, 1, 1)  # Color blanco para que la textura conserve sus colores originales
        glEnable(GL_TEXTURE_2D)
        glBindTexture(GL_TEXTURE_2D, textura_id)
        glBegin(GL_QUADS)
        glTexCoord2f(0, 1)
        glVertex2f(0, 0)
        glTexCoord2f(1, 1)
        glVertex2f(800, 0)
        glTexCoord2f(1, 0)
        glVertex2f(800, 600)
        glTexCoord2f(0, 0)
        glVertex2f(0, 600)
        glEnd()
        glDisable(GL_TEXTURE_2D)

        # Restaurar matrices
        glPopMatrix()
        glMatrixMode(GL_PROJECTION)
        glPopMatrix()
        glMatrixMode(GL_MODELVIEW)

        # Liberar la textura temporal
        glDeleteTextures([textura_id])
