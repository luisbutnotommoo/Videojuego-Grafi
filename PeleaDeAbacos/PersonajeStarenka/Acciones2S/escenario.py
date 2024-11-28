import pygame
from OpenGL.GLU import*
from OpenGL.GL import*
from OpenGL.GLUT import*
from pygame.locals import*
from PIL import Image

def load_texture(FileName):
    #Abre la imagen del archivo que se dio.
    im = Image.open(FileName)
    #Obtiene el ancho y el alto de la imagen
    ix, iy = im.size 
    # Convertimos la imagen a bytes en formato RGB
    image = im.tobytes("raw", "RGBX", 0, -1)
        
    #Identificador de la textura    
    texture_id = glGenTextures(1)
    #Vincula la textura con el identificador a una textura 2D
    glBindTexture(GL_TEXTURE_2D, texture_id)
    #Establece la alineación de los bytes de la textura
    glPixelStorei(GL_UNPACK_ALIGNMENT, 1)

    # Cambiamos el formato de la textura a GL_RGBA para que coincida con los bytes de la imagen
    glTexImage2D(GL_TEXTURE_2D, 0, GL_RGBA, ix, iy, 0, GL_RGBA, GL_UNSIGNED_BYTE, image)
   
    glTexParameterf(GL_TEXTURE_2D, GL_TEXTURE_WRAP_S, GL_REPEAT)
    glTexParameterf(GL_TEXTURE_2D, GL_TEXTURE_WRAP_T, GL_REPEAT)
    glTexParameterf(GL_TEXTURE_2D, GL_TEXTURE_MAG_FILTER, GL_LINEAR)
    glTexParameterf(GL_TEXTURE_2D, GL_TEXTURE_MIN_FILTER, GL_LINEAR)

    return texture_id


def draw_e(fileImage):
    #Habilita el uso de texturas 2D en OpenGL
    glEnable(GL_TEXTURE_2D)
    #Vincula la textura la imagen que mandamos
    glBindTexture(GL_TEXTURE_2D, load_texture(fileImage))
    
    #Inicia el dibujo-
    #GL_QUADS(indica que sera compuesto por cuadrilateros)
    glBegin(GL_QUADS)
    
    # Cara frontal
    glColor3f(1, 1, 1)
    glTexCoord2f(0, 0)
    glVertex3f(-50, -50, 50)
    glTexCoord2f(1, 0)
    glVertex3f(50, -50, 50)
    glTexCoord2f(1, 1)
    glVertex3f(50, 50, 50)
    glTexCoord2f(0, 1)
    glVertex3f(-50, 50, 50)
    
    # Cara trasera
    glTexCoord2f(0, 0)
    glVertex3f(-50, -50, -50)
    glTexCoord2f(1, 0)
    glVertex3f(50, -50, -50)
    glTexCoord2f(1, 1)
    glVertex3f(50, 50, -50)
    glTexCoord2f(0, 1)
    glVertex3f(-50, 50, -50)
    
    # Cara izquierda
    glTexCoord2f(0, 0)
    glVertex3f(-50, -50, -50)
    glTexCoord2f(1, 0)
    glVertex3f(-50, -50, 50)
    glTexCoord2f(1, 1)
    glVertex3f(-50, 50, 50)
    glTexCoord2f(0, 1)
    glVertex3f(-50, 50, -50)
    
    # Cara derecha
    glTexCoord2f(0, 0)
    glVertex3f(50, -50, -50)
    glTexCoord2f(1, 0)
    glVertex3f(50, -50, 50)
    glTexCoord2f(1, 1)
    glVertex3f(50, 50, 50)
    glTexCoord2f(0, 1)
    glVertex3f(50, 50, -50)
    
    # Cara superior
    glTexCoord2f(0, 0)
    glVertex3f(-50, 50, -50)
    glTexCoord2f(1, 0)
    glVertex3f(50, 50, -50)
    glTexCoord2f(1, 1)
    glVertex3f(50, 50, 50)
    glTexCoord2f(0, 1)
    glVertex3f(-50, 50, 50)
    
    # Cara inferior
    glTexCoord2f(0, 0)
    glVertex3f(-50, -50, -50)
    glTexCoord2f(1, 0)
    glVertex3f(50, -50, -50)
    glTexCoord2f(1, 1)
    glVertex3f(50, -50, 50)
    glTexCoord2f(0, 1)
    glVertex3f(-50, -50, 50)


    glEnd()
    glDisable(GL_TEXTURE_2D)
    
