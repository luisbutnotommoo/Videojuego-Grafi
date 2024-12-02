from OpenGL.GLU import *
from OpenGL.GL import *
from OpenGL.GLUT import *
from PersonajeEmma.actionsEV import escenario as esc
from PersonajeEmma.actionsEV import draw2 as dr

def convertColor(r, g, b, a=255):
    return (r / 255.0, g / 255.0, b / 255.0, a / 255.0)

def personaje(estado, pos_inicial_x, pos_inicial_y):
    if estado == 0:

        esc.draw_paredes("PersonajeEmma/imagenesEV/fondo1.jpg")
        esc.draw_techo()

        glPushMatrix()
        glTranslatef(-pos_inicial_x, 0, pos_inicial_y)

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
        
        glPopMatrix()

    if estado == 11: # SORPRESA

        esc.draw_paredes("PersonajeEmma/imagenesEV/estadio.jpg")
        esc.draw_techo()

        glPushMatrix()
        glTranslatef(-pos_inicial_x, 0, pos_inicial_y)

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
        
        glPopMatrix()

        #Expresiones 1-5
    if estado == 1: #Enojado

        esc.draw_paredes("PersonajeEmma/imagenesEV/callejon.jpg")
        esc.draw_techo()

        glPushMatrix()
        glTranslatef(-pos_inicial_x, 0, pos_inicial_y)
        
        dr.cabeza(255,0,0,10, 25, 7)
        dr.ojos()
        dr.ceja(9,26.5,3.85,8,27,3.85) #IZQUIERDA
        dr.ceja(11,26.5,3.85,12,27,3.85) #DERECHA
        dr.boca(10,22.5,3.5,180,0,0,1)
        dr.cuerpo()
        dr.piernaR(90)
        dr.piernaL(90)
        dr.brazoL(90,1,0,0)
        dr.brazoR(270,1,0,0)
        dr.baston()
        
        glPopMatrix()

    if estado == 2: #TRISTE

        esc.draw_paredes("PersonajeEmma/imagenesEV/Ciudad Oscura.jpeg")
        esc.draw_techo()

        glPushMatrix()
        glTranslatef(-pos_inicial_x, 0, pos_inicial_y)
        
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
        
        glPopMatrix()

    if estado == 3: #SOSPECHOSO

        esc.draw_paredes("PersonajeEmma/imagenesEV/crimen.jpg")
        esc.draw_techo()

        glPushMatrix()
        glTranslatef(-pos_inicial_x, 0, pos_inicial_y)
        
        dr.cabeza(195,159,129,10, 25, 7)
        glColor4f(*convertColor(0,0,0))
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
        
        glPopMatrix()
            
    if estado == 4: #INDIFERENTE

        esc.draw_paredes("PersonajeEmma/imagenesEV/indiferencia.jpg")
        esc.draw_techo()

        glPushMatrix()
        glTranslatef(-pos_inicial_x, 0, pos_inicial_y)
        
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
        
        glPopMatrix()

    if estado == 5: #LEVANTANDO CEJA

        esc.draw_paredes("PersonajeEmma/imagenesEV/pregunta.jpg")
        esc.draw_techo()

        glPushMatrix()
        glTranslatef(-pos_inicial_x, 0, pos_inicial_y)
        
        dr.cabeza(195,159,129,10, 25, 7)
        dr.ojos()
        dr.ceja(9,23.5,3.65,11,23.5,3.65) #BOCA
        dr.ceja(9,27.5,3.8,8,26.5,3.8) #IZQUIERDA
        dr.ceja(11,26.5,3.85,12,26.5,3.85) #DERECHA
        dr.cuerpo()
        dr.piernaR(90)
        dr.piernaL(90)
        dr.brazoL(90,1,0,0)
        dr.brazoR(270,1,0,0)
        dr.baston()
        
        glPopMatrix()


    if estado == 12: # SONRIENTE

        esc.draw_paredes("PersonajeEmma/imagenesEV/playa.jpg")
        esc.draw_techo()

        glPushMatrix()
        glTranslatef(-pos_inicial_x, 0, pos_inicial_y)
        
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
        
        glPopMatrix()

    #Movimientos 6-0
    if estado == 6: #Levantar brazo derecho

        esc.draw_paredes("PersonajeEmma/imagenesEV/fondo1.jpg")
        esc.draw_techo()

        glPushMatrix()
        glTranslatef(-pos_inicial_x, 0, pos_inicial_y)
        
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
        
        glPopMatrix()
            
    if estado == 7: #Levantar brazo izquierdo

        esc.draw_paredes("PersonajeEmma/imagenesEV/fondo1.jpg")
        esc.draw_techo()

        glPushMatrix()
        glTranslatef(-pos_inicial_x, 0, pos_inicial_y)
        
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
        
        glPopMatrix()

    if estado == 8: #T-Pose

        esc.draw_paredes("PersonajeEmma/imagenesEV/fondo1.jpg")
        esc.draw_techo()

        glPushMatrix()
        glTranslatef(-pos_inicial_x, 0, pos_inicial_y)
        
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
        
        glPopMatrix()
            
    if estado == 9: #Sentado

        esc.draw_paredes("PersonajeEmma/imagenesEV/fondo1.jpg")
        esc.draw_techo()

        glPushMatrix()
        glTranslatef(-pos_inicial_x, 0, pos_inicial_y)
        
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
        
        glPopMatrix()
            
    if estado == 10: #Saltando

        esc.draw_paredes("PersonajeEmma/imagenesEV/fondo1.jpg")
        esc.draw_techo()

        glPushMatrix()
        glTranslatef(-pos_inicial_x, 0, pos_inicial_y)
        
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
        
        glPopMatrix()

    if estado == 13: #SEÑALANDO

        esc.draw_paredes("PersonajeEmma/imagenesEV/fondo1.jpg")
        esc.draw_techo()

        glPushMatrix()
        glTranslatef(-pos_inicial_x, 0, pos_inicial_y)
        
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

        glPopMatrix()

    if estado == 14: # CELEBRACIÖN

        esc.draw_paredes("PersonajeEmma/imagenesEV/fondo1.jpg")
        esc.draw_techo()

        glPushMatrix()
        glTranslatef(-pos_inicial_x, 0, pos_inicial_y)
        
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

        glPopMatrix()
