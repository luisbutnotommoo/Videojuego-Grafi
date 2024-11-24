from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *
from PIL import Image
import PersonajeLuis.AccionesLuis.recursos as recursos


# Carga la imagen y renderiza un cuadrado con dicha imagen, esto en el viewport que creamos en render_pop_up

menu = recursos.menu
creditos = recursos.creditos

def mostrar_imagen(ruta):
    if ruta == 0:
        dibujar_imagen(cargar_textura(menu))
    if ruta == 1:
        dibujar_imagen(cargar_textura(creditos))

def cargar_textura(filename):
    im = Image.open(filename)
    img_width, img_height = im.size
    imagen = im.convert("RGBA").tobytes("raw", "RGBA", 0, -1)

    texture_id = glGenTextures(1)
    glBindTexture(GL_TEXTURE_2D, texture_id)

    glTexParameteri(GL_TEXTURE_2D, GL_TEXTURE_MIN_FILTER, GL_LINEAR)
    glTexParameteri(GL_TEXTURE_2D, GL_TEXTURE_MAG_FILTER, GL_LINEAR)
    glTexParameteri(GL_TEXTURE_2D, GL_TEXTURE_WRAP_S, GL_CLAMP)
    glTexParameteri(GL_TEXTURE_2D, GL_TEXTURE_WRAP_T, GL_CLAMP)
    
    glTexImage2D(
        GL_TEXTURE_2D,0,GL_RGBA,img_width,img_height,0,GL_RGBA,GL_UNSIGNED_BYTE,imagen)
    return texture_id

def dibujar_imagen(textura_id):
    glEnable(GL_TEXTURE_2D)
    glEnable(GL_BLEND)
    glBlendFunc(GL_SRC_ALPHA, GL_ONE_MINUS_SRC_ALPHA)
    
    glBindTexture(GL_TEXTURE_2D, textura_id)
    
    glColor4f(1.0, 1.0, 1.0, 1.0)
    glBegin(GL_QUADS)
    glTexCoord2f(0.0, 1.0)  
    glVertex2f(0.0, 0.0)
    
    glTexCoord2f(1.0, 1.0) 
    glVertex2f(600.0, 0.0)
    
    glTexCoord2f(1.0, 0.0)  
    glVertex2f(600.0, 600.0)
    
    glTexCoord2f(0.0, 0.0)  
    glVertex2f(0.0, 600.0)
    glEnd()
    
    glDisable(GL_BLEND)
    glDisable(GL_TEXTURE_2D)