import pygame
from OpenGL.GLU import*
from OpenGL.GL import*
from OpenGL.GLUT import*

#pINTAR TEXTOS
def draw_text(text, posX, posY, posZ, sizeFont, R, G, B, RB, GB, BB):
    font=pygame.font.Font(None, sizeFont)
    text_surface=font.render(text, True, (R,G,B), (RB, GB,BB))
    text_data=pygame.image.tostring(text_surface, "RGBA", True)
    glRasterPos3d(posX, posY, posZ)
    glDrawPixels(text_surface.get_width(),
     text_surface.get_height(),
     GL_RGBA, GL_UNSIGNED_BYTE, text_data)