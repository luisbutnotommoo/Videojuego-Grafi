from OpenGL.GLU import *
from OpenGL.GL import *
from OpenGL.GLUT import *
from PersonajeEmma.actionsEV import escenario as esc
from PersonajeEmma.actionsEV import draw2 as dr

class Newt():
    def __init__(self):
        # Aquí puedes agregar atributos para guardar información del personaje, como su estado actual.
        self.estado = 0

    def convertColor(r, g, b, a=255):
        return (r / 255.0, g / 255.0, b / 255.0, a / 255.0)

    def personaje(self):
        if self.estado == 0:

            #esc.draw_paredes("images/fondo1.jpg")
            #esc.draw_techo()
        
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

        if self.estado == 11: # SORPRESA

            esc.draw_paredes("images/estadio.jpg")
            esc.draw_techo()

            dr.boca_sorpresa(10,23.5,3.55)
            dr.cabeza(195,159,129,10, 25, 7)
            dr.ojos()
            dr.ceja(9,27,3.8,8,27,3.8) #IZQUIERDA
            dr.ceja(11,27,3.85,12,27,3.85) #DERECHA
            dr.cuerpo()
            dr.piernaR(90)
            dr.piernaL(90)
            dr.brazoL(90,1,0,0)
            dr.brazoR(90,1,0,0)
            dr.baston()

        #Expresiones 1-5
        if self.estado == 1: #Enojado

            esc.draw_paredes("images/callejon.jpg")
            esc.draw_techo()

            dr.cabeza(255,0,0,10, 25, 7)
            dr.ojos()
            dr.ceja(9,26.5,3.85,8,27,3.85) #IZQUIERDA
            dr.ceja(11,26.5,3.85,12,27,3.85) #DERECHA
            dr.boca(10,22.5,3.5,180,0,0,1)
            dr.cuerpo()
            dr.piernaR(90)
            dr.piernaL(90)
            dr.brazoL(90,1,0,0)
            dr.brazoR(90,1,0,0)
            dr.baston()

        if self.estado == 2: #TRISTE

            esc.draw_paredes("images/Ciudad Oscura.jpeg")
            esc.draw_techo()

            dr.cabeza(0,0,255,10, 25, 7)
            dr.ojos()
            dr.boca(10,22.5,3.5,180,0,0,1)
            dr.ceja(9,27,3.85,8,26.5,3.85) #IZQUIERDA
            dr.ceja(11,27,3.85,12,26.5,3.85) #DERECHA
            dr.cuerpo()
            dr.piernaR(90)
            dr.piernaL(90)
            dr.brazoL(90,1,0,0)
            dr.brazoR(90,1,0,0)
            dr.baston()

        if self.estado == 3: #SOSPECHOSO

            esc.draw_paredes("images/crimen.jpg")
            esc.draw_techo()

            dr.cabeza(195,159,129,10, 25, 7)
            glColor4f(*self.convertColor(0,0,0))
            dr.ceja(9, 25.5, 3.6, 8, 25.5, 3.6)
            dr.ceja(11, 25.5, 3.65, 12, 25.5, 3.65)
            dr.ceja(9,23.5,3.65,11,23.5,3.65)
            dr.ceja(9,26.5,3.8,8,26.5,3.8) 
            dr.ceja(11,26.5,3.85,12,26.5,3.85) 
            dr.cuerpo()
            dr.piernaR(90)
            dr.piernaL(90)
            dr.brazoL(90,1,0,0)
            dr.brazoR(90,1,0,0)
            dr.baston()
            
        if self.estado == 4: #INDIFERENTE

            esc.draw_paredes("images/indiferencia.jpg")
            esc.draw_techo()

            dr.cabeza(195,159,129,10, 25, 7)
            dr.ojos()
            dr.ceja(9,23.5,3.65,11,23.5,3.65) #BOCA
            dr.ceja(9,26.5,3.8,8,26.5,3.8) #IZQUIERDA
            dr.ceja(11,26.5,3.85,12,26.5,3.85) #DERECHA
            dr.cuerpo()
            dr.piernaR(90)
            dr.piernaL(90)
            dr.brazoL(90,1,0,0)
            dr.brazoR(90,1,0,0)
            dr.baston()

        if self.estado == 5: #LEVANTANDO CEJA

            esc.draw_paredes("images/pregunta.jpg")
            esc.draw_techo()

            dr.cabeza(195,159,129,10, 25, 7)
            dr.ojos()
            dr.ceja(9,23.5,3.65,11,23.5,3.65) #BOCA
            dr.ceja(9,27.5,3.8,8,26.5,3.8) #IZQUIERDA
            dr.ceja(11,26.5,3.85,12,26.5,3.85) #DERECHA
            dr.cuerpo()
            dr.piernaR(90)
            dr.piernaL(90)
            dr.brazoL(90,1,0,0)
            dr.brazoR(90,1,0,0)
            dr.baston()


        if self.estado == 12: # SONRIENTE

            esc.draw_paredes("images/playa.jpg")
            esc.draw_techo()

            dr.boca_risa(10,24,3.55)
            dr.cabeza(195,159,129,10, 25, 7)
            dr.ojos()
            dr.ceja(9,27,3.8,8,27,3.8) #IZQUIERDA
            dr.ceja(11,27,3.85,12,27,3.85) #DERECHA
            dr.cuerpo()
            dr.piernaR(90)
            dr.piernaL(90)
            dr.brazoL(90,1,0,0)
            dr.brazoR(90,1,0,0)
            dr.baston()

        #Movimientos 6-0
        if self.estado == 6: #Levantar brazo derecho

            esc.draw_paredes("images/fondo1.jpg")
            esc.draw_techo()

            dr.cabeza(195,159,129,10, 25, 7)
            dr.ojos()
            dr.ceja(9,26.5,3.85,8,26.5,3.85) #IZQUIERDA
            dr.ceja(11,26.5,3.85,12,26.5,3.85) #DERECHA
            dr.boca(10,24.5,4,0,0,0,0)
            dr.cuerpo()
            dr.piernaR(90)
            dr.piernaL(90)
            dr.brazoL(90,1,0,0)
            dr.brazoR(270,1,0,0)
            dr.baston()
            
        if self.estado == 7: #Levantar brazo izquierdo

            esc.draw_paredes("images/fondo1.jpg")
            esc.draw_techo()

            dr.cabeza(195,159,129,10, 25, 7)
            dr.ojos()
            dr.ceja(9,26.5,3.85,8,26.5,3.85) #IZQUIERDA
            dr.ceja(11,26.5,3.85,12,26.5,3.85) #DERECHA
            dr.boca(10,24.5,4,0,0,0,0)
            dr.cuerpo()
            dr.piernaR(90)
            dr.piernaL(90)
            dr.brazoL(270,1,0,0)
            dr.brazoR(90,1,0,0)

        if self.estado == 8: #T-Pose

            esc.draw_paredes("images/fondo1.jpg")
            esc.draw_techo()

            dr.cabeza(195,159,129,10, 25, 7)
            dr.ojos()
            dr.ceja(9,26.5,3.85,8,26.5,3.85) #IZQUIERDA
            dr.ceja(11,26.5,3.85,12,26.5,3.85) #DERECHA
            dr.boca(10,24.5,4,0,0,0,0)
            dr.cuerpo()
            dr.piernaR(90)
            dr.piernaL(90)
            dr.brazoL(270,0,1,0)
            dr.brazoR(90,0,1,0)
            
        if self.estado == 9: #Sentado

            esc.draw_paredes("images/fondo1.jpg")
            esc.draw_techo()

            dr.cabeza(195,159,129,10, 25, 7)
            dr.ojos()
            dr.ceja(9,26.5,3.85,8,26.5,3.85) #IZQUIERDA
            dr.ceja(11,26.5,3.85,12,26.5,3.85) #DERECHA
            dr.boca(10,24.5,4,0,0,0,0)
            dr.cuerpo()
            dr.piernaR(180)
            dr.piernaL(180)
            dr.brazoL(90,1,0,0)
            dr.brazoR(90,1,0,0)
            
        if self.estado == 10: #Saltando

            esc.draw_paredes("images/fondo1.jpg")
            esc.draw_techo()

            dr.cabeza(195,159,129,10, 25, 7)
            dr.ojos()
            dr.ceja(9,26.5,3.85,8,26.5,3.85) #IZQUIERDA
            dr.ceja(11,26.5,3.85,12,26.5,3.85) #DERECHA
            dr.boca(10,24.5,4,0,0,0,0)
            dr.cuerpo()
            dr.piernaR(150)
            dr.piernaL(30)
            dr.brazoL(90,1,0,0)
            dr.brazoR(270,1,0,0)
            dr.baston()

        if self.estado == 13: #SEÑALANDO

            esc.draw_paredes("images/fondo1.jpg")
            esc.draw_techo()

            dr.cabeza(195,159,129,10, 25, 7)
            dr.ojos()
            dr.boca(10,24.5,4,0,0,0,0)
            dr.ceja(9,26.5,3.85,8,26.5,3.85) #IZQUIERDA
            dr.ceja(11,26.5,3.85,12,26.5,3.85) #DERECHA
            dr.cuerpo()
            dr.piernaR(90)
            dr.piernaL(90)
            dr.brazoL(90,1,0,0)
            dr.brazoR(180,1,0,0)
            dr.baston()

        if self.estado == 14: # CELEBRACIÖN

            esc.draw_paredes("images/fondo1.jpg")
            esc.draw_techo()

            dr.cabeza(195,159,129,10, 25, 7)
            dr.ojos()
            dr.boca(10,24.5,4,0,0,0,0)
            dr.ceja(9,26.5,3.85,8,26.5,3.85) #IZQUIERDA
            dr.ceja(11,26.5,3.85,12,26.5,3.85) #DERECHA
            dr.cuerpo()
            dr.piernaR(90)
            dr.piernaL(90)
            dr.brazoL(270,1,0,0)
            dr.brazoR(270,1,0,0)