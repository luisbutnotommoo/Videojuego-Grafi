import pygame
from OpenGL.GLU import *
from OpenGL.GL import *
from OpenGL.GLUT import *

def drawText(text, posX, posY, posZ, SizeFont, R, G, B, RB, GB, BB):
    font = pygame.font.Font(None, SizeFont)
    textSurface = font.render(text, True, (R,G,B), (RB, GB, BB))
    textData = pygame.image.tostring(textSurface, "RGBA", True)
    glRasterPos3d(posX,posY,posZ)
    glDrawPixels(textSurface.get_width(), textSurface.get_height(), GL_RGBA, GL_UNSIGNED_BYTE, textData)


def render_text_2d(display, text, x, y, font, line_height=18):
    lines = text.split('\n')  # Dividir el texto en líneas donde haya saltos de línea (\n)
    
    for i, line in enumerate(lines):
        # Renderizar cada línea como una imagen de Pygame
        text_surface = font.render(line, True, (255, 255, 255), (0, 0, 0))  # Texto blanco sobre fondo negro
        text_data = pygame.image.tostring(text_surface, "RGBA", True)
        
        # Obtener el ancho y alto de la superficie
        text_width, text_height = text_surface.get_size()
        
        # Cargar la textura en OpenGL
        glEnable(GL_TEXTURE_2D)
        texture_id = glGenTextures(1)
        glBindTexture(GL_TEXTURE_2D, texture_id)
        glTexImage2D(GL_TEXTURE_2D, 0, GL_RGBA, text_width, text_height, 0, GL_RGBA, GL_UNSIGNED_BYTE, text_data)
        
        glTexParameterf(GL_TEXTURE_2D, GL_TEXTURE_MIN_FILTER, GL_LINEAR)
        glTexParameterf(GL_TEXTURE_2D, GL_TEXTURE_MAG_FILTER, GL_LINEAR)
        
        # Cambiar la proyección para dibujar en 2D
        glMatrixMode(GL_PROJECTION)
        glPushMatrix()
        glLoadIdentity()
        glOrtho(0, display[0], 0, display[1], -1, 1)  # Proyección ortográfica 2D
        glMatrixMode(GL_MODELVIEW)
        glPushMatrix()
        glLoadIdentity()

        # Dibujar un cuadrado donde se proyectará la textura (texto)
        glBindTexture(GL_TEXTURE_2D, texture_id)
        glBegin(GL_QUADS)
        glTexCoord2f(0, 0); glVertex2f(x, y - i * line_height)  # Ajustar la posición vertical para cada línea
        glTexCoord2f(1, 0); glVertex2f(x + text_width, y - i * line_height)
        glTexCoord2f(1, 1); glVertex2f(x + text_width, y + text_height - i * line_height)
        glTexCoord2f(0, 1); glVertex2f(x, y + text_height - i * line_height)
        glEnd()
        
        # Limpiar la textura
        glDeleteTextures(int(texture_id))
        
        # Restaurar la proyección
        glPopMatrix()
        glMatrixMode(GL_PROJECTION)
        glPopMatrix()
        glMatrixMode(GL_MODELVIEW)
        glDisable(GL_TEXTURE_2D)