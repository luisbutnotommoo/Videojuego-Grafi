import pygame
from OpenGL.GLU import*
from OpenGL.GL import*
from OpenGL.GLUT import*
from pygame.locals import*
from PIL import*
from PersonajeStarenka.Acciones2S import escenario as es
from PersonajeStarenka.Acciones2S import sonido as son
from PersonajeStarenka.Acciones2S import boceto2 as b


class PintarPersonajeStar():
    def __init__(self, emocion):
        self.emocion=emocion

    def Personaje (self, emocion):
        
        if emocion==0:
            
            b.original()
        
        if emocion==2:
            b.molesto()
        if emocion==1: 
            b.felicidad2()
        
            
            
    