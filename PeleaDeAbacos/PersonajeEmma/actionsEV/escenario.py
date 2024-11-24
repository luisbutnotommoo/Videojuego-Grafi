import pygame
from OpenGL.GLU import *
from OpenGL.GL import *
from OpenGL.GLUT import *
from pygame.locals import *
from PIL import Image

#python -m pip install -U pillow

pygame.init()
pygame.mixer.init()

def load_texture(fileName):
    im = Image.open(fileName)
    ix, iy = im.size
    image = im.tobytes("raw", "RGBX", 0, -1)
    texture_id = glGenTextures(1)
    glBindTexture(GL_TEXTURE_2D, texture_id)
    glPixelStorei(GL_UNPACK_ALIGNMENT, 1)
    glTexImage2D(GL_TEXTURE_2D, 0 ,GL_RGBA, ix, iy, 0, GL_RGBA, GL_UNSIGNED_BYTE, image)
    glTexParameterf(GL_TEXTURE_2D, GL_TEXTURE_WRAP_S, GL_REPEAT)
    glTexParameterf(GL_TEXTURE_2D, GL_TEXTURE_WRAP_T, GL_REPEAT)
    glTexParameterf(GL_TEXTURE_2D, GL_TEXTURE_MAG_FILTER, GL_LINEAR)
    glTexParameterf(GL_TEXTURE_2D, GL_TEXTURE_MIN_FILTER, GL_LINEAR)

    return texture_id

def draw_paredes(FileImage):
    glEnable(GL_TEXTURE_2D)
    glBindTexture(GL_TEXTURE_2D, load_texture(FileImage))
    
    glBegin(GL_QUADS)
    glColor(1,1,1)
    glTexCoord2f(0,0)
    glVertex3f(40, 0, 40) # Esquina inferior izquierda 
    glTexCoord2f(1,0)
    glVertex3f(-18, 0, 40) # Esquina inferior derecha 
    glTexCoord2f(1,1)
    glVertex3f(-18, 60, 40) # Esquina superior derecha
    glTexCoord2f(0,1)
    glVertex3f(40, 60, 40) # Esquina superior izquierda 
    glEnd()
    
    glBegin(GL_QUADS)
    glColor(1,1,1)
    glTexCoord2f(0,0)
    glVertex3f(-18, 0, -40) # Esquina inferior izquierda
    glTexCoord2f(1,0)
    glVertex3f(-18, 0, 40) # Esquina inferior derecha 
    glTexCoord2f(1,1)
    glVertex3f(-18, 60, 40) # Esquina superior derecha
    glTexCoord2f(0,1)
    glVertex3f(-18, 60, -40) # Esquina superior izquierda 
    glEnd()
    
    glBegin(GL_QUADS)
    glColor(1,1,1)
    glTexCoord2f(0,0)
    glVertex3f(40, 0, -40) # Esquina inferior izquierda
    glTexCoord2f(1,0)
    glVertex3f(40, 0, 40) # Esquina inferior derecha 
    glTexCoord2f(1,1)
    glVertex3f(40, 60, 40) # Esquina superior derecha
    glTexCoord2f(0,1)
    glVertex3f(40, 60, -40) # Esquina superior izquierda 
    glEnd()
    
    glDisable(GL_TEXTURE_2D)

def draw_techo():
    glColor4f(0.3, 0.3, 0.3, 1)
    glBegin(GL_QUADS)
    glVertex3f(-18, 60, -40)
    glVertex3f(40, 60, -40)
    glVertex3f(40, 60, 40)
    glVertex3f(-18, 60, 40)
    glEnd()

    glBegin(GL_QUADS)
    glVertex3f(-18, 0, -40)
    glVertex3f(40, 0, -40)
    glVertex3f(40, 0, 40)
    glVertex3f(-18, 0, 40)
    glEnd()
   