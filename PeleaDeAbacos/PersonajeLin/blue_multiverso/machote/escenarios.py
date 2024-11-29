import pygame as py 
from OpenGL.GLU import *
from OpenGL.GL import *
from OpenGL.GLUT import *
from pygame.locals import *
from PIL import Image

py.init()
py.mixer.init()

def load_texture(filename):
    im = Image.open(filename)
    ix, iy, image = im.size[0], im.size[1], im.tobytes("raw","RGBX",0,-1)
    texture_id = glGenTextures(1)
    glBindTexture(GL_TEXTURE_2D, texture_id)
    glPixelStorei(GL_UNPACK_ALIGNMENT,1)
    glTexImage2D(GL_TEXTURE_2D,0,GL_RGB,ix,iy,0,GL_RGBA,GL_UNSIGNED_BYTE,image)
    glTexParameterf(GL_TEXTURE_2D, GL_TEXTURE_WRAP_S, GL_REPEAT) 
    glTexParameterf(GL_TEXTURE_2D, GL_TEXTURE_WRAP_T, GL_REPEAT) 
    glTexParameterf(GL_TEXTURE_2D, GL_TEXTURE_MAG_FILTER, GL_LINEAR) 
    glTexParameterf(GL_TEXTURE_2D, GL_TEXTURE_MIN_FILTER, GL_LINEAR) 
    return texture_id

def draw_e5(fileimage,suelo,cielo):
    # Cargar texturas para suelo y cielo
    tex_suelo = load_texture(suelo)
    tex_cielo = load_texture(cielo)

    # Dibujar suelo
    glEnable(GL_TEXTURE_2D)
    glBindTexture(GL_TEXTURE_2D, tex_suelo)
    glBegin(GL_QUADS)
    glColor(1, 1, 1)
    glTexCoord2f(0, 0)
    glVertex3f(-50, 0, 50)  # esquina inf izq
    glTexCoord2f(1, 0)
    glVertex3f(100, 0, 50)  # inf der
    glTexCoord2f(1, 1)
    glVertex3f(100, 0, -100)  # sup der
    glTexCoord2f(0, 1)
    glVertex3f(-50, 0, -100)  # sup izq
    glEnd()
    glDisable(GL_TEXTURE_2D)

    # Dibujar cielo
    glEnable(GL_TEXTURE_2D)
    glBindTexture(GL_TEXTURE_2D, tex_cielo)
    glBegin(GL_QUADS)
    glColor(1, 1, 1)
    glTexCoord2f(0, 0)
    glVertex3f(-50, 100, -50)  # esquina inf izq
    glTexCoord2f(1, 0)
    glVertex3f(100, 100, -50)  # inf der
    glTexCoord2f(1, 1)
    glVertex3f(100, 100, 50)  # sup der
    glTexCoord2f(0, 1)
    glVertex3f(-50, 100, 50)  # sup izq
    glEnd()
    glDisable(GL_TEXTURE_2D)
#-----------------------------------------
    #Paredes:
    glEnable(GL_TEXTURE_2D)
    glBindTexture(GL_TEXTURE_2D, load_texture(fileimage))
    glBegin(GL_QUADS)
    glColor(1,1,1)
    glTexCoord2f(0,0)
    glVertex3f(-50,0,50) #esquina inf izq
    glTexCoord2f(1,0)
    glVertex3f(100,0,50) #inf der
    glTexCoord2f(1,1)
    glVertex3f(100,100,50) # sup der
    glTexCoord2f(0,1)
    glVertex3f(-50,100,50) #sup izq
    glEnd()
    #----2-------------------------
    glBegin(GL_QUADS)
    glColor(1,1,1)
    glTexCoord2f(0,0)
    glVertex3f(50,0,50) #esquina inf izq
    glTexCoord2f(1,0)
    glVertex3f(50,0,-100) #inf der
    glTexCoord2f(1,1)
    glVertex3f(50,100,-100) # sup der
    glTexCoord2f(0,1)
    glVertex3f(50,100,50) #sup izq
    glEnd()
    #----3-------------------------
    glBegin(GL_QUADS)
    glColor(1,1,1)
    glTexCoord2f(0,0)
    glVertex3f(50,0,-50) #esquina inf izq
    glTexCoord2f(1,0)
    glVertex3f(-50,0,-100) #inf der
    glTexCoord2f(1,1)
    glVertex3f(-50,100,-100) # sup der
    glTexCoord2f(0,1)
    glVertex3f(50,100,-50) #sup izq
    glEnd()
    #------4----------------------------
    glBegin(GL_QUADS)
    glColor(1,1,1)
    glTexCoord2f(0,0)
    glVertex3f(-50,0,-100) #esquina inf izq
    glTexCoord2f(1,0)
    glVertex3f(-50,0,50) #inf der
    glTexCoord2f(1,1)
    glVertex3f(-50,100,50) # sup der
    glTexCoord2f(0,1)
    glVertex3f(-50,100,-100) #sup izq
    glEnd()

    glDisable(GL_TEXTURE_2D)