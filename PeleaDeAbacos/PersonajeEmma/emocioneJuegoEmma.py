from OpenGL.GLU import *
from OpenGL.GL import *
from OpenGL.GLUT import *
from PersonajeEmma.actionsEV import escenario as esc
from PersonajeEmma.actionsEV import draw2 as dr

class NewtJuego():
    
    def __init__(self, emocion):
        print(f"NewtJuego drawing with emotion: {emocion}")

        self.emocion=emocion

    def convertColor(r, g, b, a=255):
        return (r / 255.0, g / 255.0, b / 255.0, a / 255.0)

#Normal
    def personaje(self, emocion):
        self.emocion=emocion
        if emocion == 0:
            dr.cabeza(195,159,129,10, 25, 7)
            dr.ojos()
            dr.boca(10,24.5,4,0,0,0,0)
            dr.ceja(9,26.5,3.85,8,26.5,3.85) #IZQUIERDA
            dr.ceja(11,26.5,3.85,12,26.5,3.85) #DERECHA
            dr.cuerpo()
            dr.piernaR(90)
            dr.piernaL(90)
            dr.brazoL(90,1,0,0)
            dr.brazoR(90,1,0,0)
            dr.baston()


        #Expresiones 1-5
        if emocion == 2: #Enojado

            dr.cabeza(255,0,0,10, 25, 7)
            dr.ojos()
            dr.ceja(9,26.5,3.85,8,27,3.85) #IZQUIERDA
            dr.ceja(11,26.5,3.85,12,27,3.85) #DERECHA
            dr.boca(10,22.5,3.5,180,0,0,1)
            dr.cuerpo()
            dr.piernaR(90)
            dr.piernaL(90)
            dr.brazoL(90,1,0,0)
            dr.brazoR(180,1,0,0)
            dr.baston()

        

        if emocion == 1: # SONRIENTE FELiii
            glPushMatrix()

            
            dr.cabeza(195,159,129,10, 25, 7)
            dr.boca_risa(10,24,3.55)
            dr.ojos()
            dr.ceja(9,27,3.8,8,27,3.8) #IZQUIERDA
            dr.ceja(11,27,3.85,12,27,3.85) #DERECHA
            dr.cuerpo()
            dr.piernaR(90)
            dr.piernaL(90)
            dr.brazoL(90,1,0,0)
            dr.brazoR(90,1,0,0)
            dr.baston()
                
            glPopMatrix()
