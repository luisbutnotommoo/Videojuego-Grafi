import pygame
from OpenGL.GLU import*
from OpenGL.GL import*
from OpenGL.GLUT import*
from pygame.locals import*
from PIL import*
from PersonajeStarenka.Acciones2S import escenario as es
from PersonajeStarenka.Acciones2S import sonido as son
from PersonajeStarenka.Acciones2S import boceto as b


class PintarPersonajeStar():
    def __init__(self, emocion):
        self.emocion=emocion

    def Personaje (self):
        if self.emocion==0:
            b.original()
        if self.emocion==1:
            b.molesto()
        if self.emocion==2: 
            b.felicidad2()
            
            
    