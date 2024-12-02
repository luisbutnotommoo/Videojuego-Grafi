from OpenGL.GLU import *
from OpenGL.GL import *
from OpenGL.GLUT import *
from pygame.locals import *
from PIL import Image

from PersonajeLuis2.AccionesL import recursos
escenario=recursos.ambiente[0]

def set_escenario(index):
    global escenario
    escenario=recursos.ambiente[index]

def load_texture(filename):
    im = Image.open(filename)
    ix, iy, image = im.size[0], im.size[1], im.tobytes("raw","RGBX",0,-1)
    print(f"Tamaño de la imagen: {im.size}")  # Verifica el tamaño de la imagen
    texture_id = glGenTextures(1)
    glBindTexture(GL_TEXTURE_2D, texture_id)
    glPixelStorei(GL_UNPACK_ALIGNMENT,1)
    glTexImage2D(GL_TEXTURE_2D,0,GL_RGB,ix,iy,0,GL_RGBA,GL_UNSIGNED_BYTE,image)
    glTexParameterf(GL_TEXTURE_2D, GL_TEXTURE_WRAP_S, GL_REPEAT) 
    glTexParameterf(GL_TEXTURE_2D, GL_TEXTURE_WRAP_T, GL_REPEAT) 
    glTexParameterf(GL_TEXTURE_2D, GL_TEXTURE_MAG_FILTER, GL_LINEAR) 
    glTexParameterf(GL_TEXTURE_2D, GL_TEXTURE_MIN_FILTER, GL_LINEAR) 
    return texture_id


def render_escenario():
    # Cargar texturas para suelo y cielo
    tex_pared=load_texture(escenario[0])
    tex_suelo = load_texture(escenario[1])

    # Dibujar suelo
    glEnable(GL_TEXTURE_2D)
    glBindTexture(GL_TEXTURE_2D, tex_suelo)
    glBegin(GL_QUADS)
    glColor(1, 1, 1)
    glTexCoord2f(0, 0)
    glVertex3f(-20, 0, 20)  # esquina inf izq
    glTexCoord2f(1, 0)
    glVertex3f(40, 0, 20)  # inf der
    glTexCoord2f(1, 1)
    glVertex3f(40, 0, -40)  # sup der
    glTexCoord2f(0, 1)
    glVertex3f(-20, 0, -40)  # sup izq
    glEnd()
    glDisable(GL_TEXTURE_2D)

#-----------------------------------------
    #Paredes:
    glEnable(GL_TEXTURE_2D)
    glBindTexture(GL_TEXTURE_2D, tex_pared)
    glBegin(GL_QUADS)
    glColor(1,1,1)
    glTexCoord2f(0,0)
    glVertex3f(-20,0,20) #esquina inf izq
    glTexCoord2f(1,0)
    glVertex3f(40,0,20) #inf der
    glTexCoord2f(1,1)
    glVertex3f(40,40,20) # sup der
    glTexCoord2f(0,1)
    glVertex3f(-20,40,20) #sup izq
    glEnd()
    #----2-------------------------
    glBegin(GL_QUADS)
    glColor(1,1,1)
    glTexCoord2f(0,0)
    glVertex3f(20,0,20) #esquina inf izq
    glTexCoord2f(1,0)
    glVertex3f(20,0,-40) #inf der
    glTexCoord2f(1,1)
    glVertex3f(20,40,-40) # sup der
    glTexCoord2f(0,1)
    glVertex3f(20,40,20) #sup izq
    glEnd()
    #----3-------------------------
    glBegin(GL_QUADS)
    glColor(1,1,1)
    glTexCoord2f(0,0)
    glVertex3f(20,0,-20) #esquina inf izq
    glTexCoord2f(1,0)
    glVertex3f(-20,0,-40) #inf der
    glTexCoord2f(1,1)
    glVertex3f(-20,40,-40) # sup der
    glTexCoord2f(0,1)
    glVertex3f(20,40,-20) #sup izq
    glEnd()
    #------4----------------------------
    glBegin(GL_QUADS)
    glColor(1,1,1)
    glTexCoord2f(0,0)
    glVertex3f(-20,0,-40) #esquina inf izq
    glTexCoord2f(1,0)
    glVertex3f(-20,0,20) #inf der
    glTexCoord2f(1,1)
    glVertex3f(-20,40,20) # sup der
    glTexCoord2f(0,1)
    glVertex3f(-20,40,-40) #sup izq
    glEnd()

    glDisable(GL_TEXTURE_2D)
