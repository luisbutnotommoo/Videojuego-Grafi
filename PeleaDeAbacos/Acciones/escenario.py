import pygame
from OpenGL.GLU import*
from OpenGL.GL import*
from OpenGL.GLUT import*
from pygame.locals import*
from PIL import*
import Acciones.objetos as obj

class escenario:
    def __init__(self,pisoTextura, paredTextura):
        # Cargar texturas
        self.floor_texture = self.load_texture(pisoTextura)

        self.wall_texture = self.load_texture(paredTextura)

    def dibujar_piso_pared(self):
            glEnable(GL_TEXTURE_2D)

            # Configurar material para las texturas con un filtro neutral
            glMaterialfv(GL_FRONT, GL_SPECULAR, [0.2, 0.2, 0.2, 1.0])
            glMaterialf(GL_FRONT, GL_SHININESS, 16.0)

            # Dibujar el piso (bajado a -10.0 en el eje Y)
            glBindTexture(GL_TEXTURE_2D, self.floor_texture)
            glColor3f(0.6, 0.6, 0.6)
            glBegin(GL_QUADS)
            glNormal3f(0.0, 1.0, 0.0)
            glTexCoord2f(0, 0); glVertex3f(-50.0, -10.0, -50.0)
            glTexCoord2f(1, 0); glVertex3f(50.0, -10.0, -50.0)
            glTexCoord2f(1, 1); glVertex3f(50.0, -10.0, 50.0)
            glTexCoord2f(0, 1); glVertex3f(-50.0, -10.0, 50.0)
            glEnd()

            # Dibujar la pared frontal (incrementada a 80.0 en el eje Y)
            glBindTexture(GL_TEXTURE_2D, self.wall_texture)
            glColor3f(0.8, 0.8, 0.8)
            glBegin(GL_QUADS)
            glNormal3f(0.0, 0.0, 1.0)
            glTexCoord2f(0, 0); glVertex3f(-50.0, -10.0, -50.0)
            glTexCoord2f(1, 0); glVertex3f(50.0, -10.0, -50.0)
            glTexCoord2f(1, 1); glVertex3f(50.0, 80.0, -50.0)
            glTexCoord2f(0, 1); glVertex3f(-50.0, 80.0, -50.0)
            glEnd()

            # Dibujar la pared trasera (incrementada a 80.0 en el eje Y)
            glBegin(GL_QUADS)
            glNormal3f(0.0, 0.0, -1.0)
            glTexCoord2f(0, 0); glVertex3f(-50.0, -10.0, 50.0)
            glTexCoord2f(1, 0); glVertex3f(50.0, -10.0, 50.0)
            glTexCoord2f(1, 1); glVertex3f(50.0, 80.0, 50.0)
            glTexCoord2f(0, 1); glVertex3f(-50.0, 80.0, 50.0)
            glEnd()

            # Dibujar la pared izquierda (incrementada a 80.0 en el eje Y)
            glBegin(GL_QUADS)
            glNormal3f(1.0, 0.0, 0.0)
            glTexCoord2f(0, 0); glVertex3f(-50.0, -10.0, -50.0)
            glTexCoord2f(1, 0); glVertex3f(-50.0, -10.0, 50.0)
            glTexCoord2f(1, 1); glVertex3f(-50.0, 80.0, 50.0)
            glTexCoord2f(0, 1); glVertex3f(-50.0, 80.0, -50.0)
            glEnd()

            # Dibujar la pared derecha (incrementada a 80.0 en el eje Y)
            glBegin(GL_QUADS)
            glNormal3f(-1.0, 0.0, 0.0)
            glTexCoord2f(0, 0); glVertex3f(50.0, -10.0, -50.0)
            glTexCoord2f(1, 0); glVertex3f(50.0, -10.0, 50.0)
            glTexCoord2f(1, 1); glVertex3f(50.0, 80.0, 50.0)
            glTexCoord2f(0, 1); glVertex3f(50.0, 80.0, -50.0)
            glEnd()

            glDisable(GL_TEXTURE_2D)

    def load_texture(self, path):
            texture_surface = pygame.image.load(path)
            texture_data = pygame.image.tostring(texture_surface, "RGB", 1)
            width, height = texture_surface.get_rect().size

            texture_id = glGenTextures(1)
            glBindTexture(GL_TEXTURE_2D, texture_id)
            glTexImage2D(GL_TEXTURE_2D, 0, GL_RGB, width, height, 0, GL_RGB, GL_UNSIGNED_BYTE, texture_data)
            glTexParameterf(GL_TEXTURE_2D, GL_TEXTURE_MIN_FILTER, GL_LINEAR)
            glTexParameterf(GL_TEXTURE_2D, GL_TEXTURE_MAG_FILTER, GL_LINEAR)
            return texture_id