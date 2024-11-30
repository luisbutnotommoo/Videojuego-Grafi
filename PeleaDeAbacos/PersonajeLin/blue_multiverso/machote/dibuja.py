from OpenGL.GLU import *
from OpenGL.GL import *
from OpenGL.GLUT import *
from pygame.locals import *
from PIL import *
import PersonajeLin.blue_multiverso.machote.objetos as ob
import PersonajeLin.blue_multiverso.machote.lucesNuev as lc

class clasePersonajeBlue:
    def __init__(self):
        
        #-----------------------------------------------------------------------
        #-----figura blue---------
        self.aux = 0
        self.PosX_objeto1 = 3 #coordenada mov 
        self.PosY_objeto1 = 6
        self.PosZ_objeto1 = 4
        self.Obj1_height = 1
        #----------------------------------------------------------------------
        ##figura colision##
        self.PosX_objeto2 = 3
        self.PosY_objeto2 = 6
        self.PosZ_objeto2 = 4
        self.Obj2_height = 1
        self.Obj2_width = 1
        self.Obj2_depth = 1
        #--------------------------------------------

        #posicion de esfera
        self.PosObj2_X = 3
        self.PosObj2_Y = 6
        self.PosObj2_Z = 4
        self.Obj2_height = 1
        self.Obj2_width = 1
        self.Obj2_depth = 1


        #cubo
        self.PosXob1 = 3  # mov en x
        self.PosYob1 = 6  # mov en y
        self.PosZob1 = 4  # mov en z
        self.Obj1_height=1

        #metodo dibuja esfera

    def draw2(self):
        glEnable(GL_DEPTH_TEST)
        glColor3f(0.0,1.0,0.0)
        glPushMatrix()
        glTranslatef(self.PosObj2_X, self.PosObj2_Y, self.PosObj2_Z)
        lc.iluminacion(0.0, 0.0, 1.0)
        ob.draw_sphere(8, 40, 40)
        glDisable(GL_LIGHTING)
        glDisable(GL_LIGHT0)
        glPopMatrix() 

    def draw_mov(self,movX,movY):
        
        self.PosX_objeto1 = self.PosX_objeto1+movX #se suma a los ejes el movimiento
        self.PosY_objeto1 = self.PosY_objeto1+movY
        glEnable(GL_DEPTH_TEST)
        glPushMatrix()
        glTranslatef(self.PosX_objeto1,self.PosY_objeto1,self.PosZ_objeto1) #trasladar a las nuevas coordenadas
        self.draw()
        glDisable(GL_LIGHTING)
        glDisable(GL_LIGHT0)
        glPopMatrix()

    def draw3(self,movX, movY):
        self.PosXob1=self.PosXob1+movX
        self.PosYob1=self.PosYob1+movY
        glEnable(GL_DEPTH_TEST)
        glPushMatrix()
        glTranslatef(self.PosXob1,self.PosYob1,self.PosZob1)
        lc.iluminacion(0.0,1.0,0.0)
        ob.draw_cube()
        glDisable(GL_LIGHTING)
        glDisable(GL_LIGHT0)
        glPopMatrix()
    #--------------------gestos con movimiento
    def draw_movEnojo(self,movX,movY):
        self.PosX_objeto1 = self.PosX_objeto1+movX #se suma a los ejes el movimiento
        self.PosY_objeto1 = self.PosY_objeto1+movY
        glEnable(GL_DEPTH_TEST)
        glPushMatrix()
        glTranslatef(self.PosX_objeto1,self.PosY_objeto1,self.PosZ_objeto1) #trasladar a las nuevas coordenadas
        self.draw_angry()
        glDisable(GL_LIGHTING)
        glDisable(GL_LIGHT0)
        glPopMatrix()

    def draw_movhappy(self,movX,movY):
        self.PosX_objeto1 = self.PosX_objeto1+movX #se suma a los ejes el movimiento
        self.PosY_objeto1 = self.PosY_objeto1+movY
        glEnable(GL_DEPTH_TEST)
        glPushMatrix()
        glTranslatef(self.PosX_objeto1,self.PosY_objeto1,self.PosZ_objeto1) #trasladar a las nuevas coordenadas
        self.draw_happy()
        glDisable(GL_LIGHTING)
        glDisable(GL_LIGHT0)
        glPopMatrix()

    def draw_movasco(self,movX,movY):
        self.PosX_objeto1 = self.PosX_objeto1+movX #se suma a los ejes el movimiento
        self.PosY_objeto1 = self.PosY_objeto1+movY
        glEnable(GL_DEPTH_TEST)
        glPushMatrix()
        glTranslatef(self.PosX_objeto1,self.PosY_objeto1,self.PosZ_objeto1) #trasladar a las nuevas coordenadas
        self.draw_asco()
        glDisable(GL_LIGHTING)
        glDisable(GL_LIGHT0)
        glPopMatrix()

    def draw_movomg(self, movX,movY):
        self.PosX_objeto1 = self.PosX_objeto1+movX #se suma a los ejes el movimiento
        self.PosY_objeto1 = self.PosY_objeto1+movY
        glEnable(GL_DEPTH_TEST)
        glPushMatrix()
        glTranslatef(self.PosX_objeto1,self.PosY_objeto1,self.PosZ_objeto1) #trasladar a las nuevas coordenadas
        self.draw_omg()
        glDisable(GL_LIGHTING)
        glDisable(GL_LIGHT0)
        glPopMatrix()
        
    def draw_movsad(self,movX,movY):
        self.PosX_objeto1 = self.PosX_objeto1+movX #se suma a los ejes el movimiento
        self.PosY_objeto1 = self.PosY_objeto1+movY
        glEnable(GL_DEPTH_TEST)
        glPushMatrix()
        glTranslatef(self.PosX_objeto1,self.PosY_objeto1,self.PosZ_objeto1) #trasladar a las nuevas coordenadas
        self.draw_sad()
        glDisable(GL_LIGHTING)
        glDisable(GL_LIGHT0)
        glPopMatrix()

    def draw_mov_brazoD(self,movX,movY):
        self.PosX_objeto1 = self.PosX_objeto1+movX #se suma a los ejes el movimiento
        self.PosY_objeto1 = self.PosY_objeto1+movY
        glEnable(GL_DEPTH_TEST)
        glPushMatrix()
        glTranslatef(self.PosX_objeto1,self.PosY_objeto1,self.PosZ_objeto1) #trasladar a las nuevas coordenadas
        self.draw_mov_brazo_D()
        glDisable(GL_LIGHTING)
        glDisable(GL_LIGHT0)
        glPopMatrix()

    def draw_mov_brazoI(self,movX,movY):
        self.PosX_objeto1 = self.PosX_objeto1+movX #se suma a los ejes el movimiento
        self.PosY_objeto1 = self.PosY_objeto1+movY
        glEnable(GL_DEPTH_TEST)
        glPushMatrix()
        glTranslatef(self.PosX_objeto1,self.PosY_objeto1,self.PosZ_objeto1) #trasladar a las nuevas coordenadas
        self.draw_mov_brazo_I()
        glDisable(GL_LIGHTING)
        glDisable(GL_LIGHT0)
        glPopMatrix()

    def draw_movcuello(self,movX,movY):
        self.PosX_objeto1 = self.PosX_objeto1+movX #se suma a los ejes el movimiento
        self.PosY_objeto1 = self.PosY_objeto1+movY
        glEnable(GL_DEPTH_TEST)
        glPushMatrix()
        glTranslatef(self.PosX_objeto1,self.PosY_objeto1,self.PosZ_objeto1) #trasladar a las nuevas coordenadas
        self.mov_cuello()
        glDisable(GL_LIGHTING)
        glDisable(GL_LIGHT0)
        glPopMatrix()

    def draw_movPD(self,movX,movY):
        self.PosX_objeto1 = self.PosX_objeto1+movX #se suma a los ejes el movimiento
        self.PosY_objeto1 = self.PosY_objeto1+movY
        glEnable(GL_DEPTH_TEST)
        glPushMatrix()
        glTranslatef(self.PosX_objeto1,self.PosY_objeto1,self.PosZ_objeto1) #trasladar a las nuevas coordenadas
        self.mov_piernaD()
        glDisable(GL_LIGHTING)
        glDisable(GL_LIGHT0)
        glPopMatrix()

    def draw_movPI(self,movX,movY):
        self.PosX_objeto1 = self.PosX_objeto1+movX #se suma a los ejes el movimiento
        self.PosY_objeto1 = self.PosY_objeto1+movY
        glEnable(GL_DEPTH_TEST)
        glPushMatrix()
        glTranslatef(self.PosX_objeto1,self.PosY_objeto1,self.PosZ_objeto1) #trasladar a las nuevas coordenadas
        self.mov_piernaI()
        glDisable(GL_LIGHTING)
        glDisable(GL_LIGHT0)
        glPopMatrix()

    def draw_mov_cuello(self):
        glEnable(GL_DEPTH_TEST)
        glColor3f(0.9, 0.8, 0.6)
        glPushMatrix()
        # Traslada las figuras a la posición deseada
        glTranslatef(-20, 0, 4)
        # Rota las figuras para que estén de pie
        glRotatef(-90, 1, 0, 0)  # Rotación de -90 grados alrededor del eje X
        glScalef(1.5, 1.5, 1.5)
        ob.mov_Cuello()
        ob.mov_Cabeza()
        
        glPopMatrix()

    def draw_mov_cara(self):
        glEnable(GL_DEPTH_TEST)
        glPushMatrix()
        # Traslada las figuras a la posición deseada
        glTranslatef(-20, 0, 4)
        # Rota las figuras para que estén de pie
        glRotatef(-90, 1, 0, 0)  # Rotación de -90 grados alrededor del eje X
        glScalef(1.5, 1.5, 1.5)
        ob.mov_draw_ojos()
        
        glPopMatrix()
    
    def draw_pies(self):
        glEnable(GL_DEPTH_TEST)
        glColor3f(0.9, 0.8, 0.6)
        glPushMatrix()
        # Traslada las figuras a la posición deseada
        glTranslatef(-20, 0, 4)
        # Rota las figuras para que estén de pie
        glRotatef(-90, 1, 0, 0)  # Rotación de -90 grados alrededor del eje X
        glScalef(1.5, 1.5, 1.5)
        ob.draw_piernaIz()
        ob.draw_piernaDe()
        
        glPopMatrix()


    def draw_Tor(self):
        glEnable(GL_DEPTH_TEST)
        glColor3f(0.0, 1.0, 0.0)
        glPushMatrix()
        # Traslada las figuras a la posición deseada
        glTranslatef(-20, 0, 4)
        # Rota las figuras para que estén de pie
        glRotatef(-90, 1, 0, 0)  # Rotación de -90 grados alrededor del eje X
        glScalef(1.5, 1.5, 1.5)
        ob.draw_Torzo()
        glPopMatrix()

    def draw_Cuello(self):
        glEnable(GL_DEPTH_TEST)
        glColor3f(0.9, 0.8, 0.6)
        glPushMatrix()
        # Traslada las figuras a la posición deseada
        glTranslatef(-20, 0, 4)
        # Rota las figuras para que estén de pie
        glRotatef(-90, 1, 0, 0)  # Rotación de -90 grados alrededor del eje X
        glScalef(1.5, 1.5, 1.5)
        ob.Cuello()
        glPopMatrix()

    def draw_Cab(self):
        glEnable(GL_DEPTH_TEST)
        glColor3f(0.9, 0.8, 0.6)
        glPushMatrix()
        # Traslada las figuras a la posición deseada
        glTranslatef(-20, 0, 4)
        # Rota las figuras para que estén de pie
        glRotatef(-90, 1, 0, 0)  # Rotación de -90 grados alrededor del eje X
        glScalef(1.5, 1.5, 1.5)
        ob.draw_Cabeza()
        glPopMatrix()


    def draw_eyes(self):
        glEnable(GL_DEPTH_TEST)
        glColor3f(0.0, 0.0, 0.0)
        glPushMatrix()
        # Traslada las figuras a la posición deseada
        glTranslatef(-20, 0, 4)
        # Rota las figuras para que estén de pie
        glRotatef(-90, 1, 0, 0)  # Rotación de -90 grados alrededor del eje X
        glScalef(1.5, 1.5, 1.5)
        ob.draw_ojos()
        glPopMatrix()


    def draw_Brazos(self):
        glEnable(GL_DEPTH_TEST)
        glColor3f(0.9, 0.8, 0.6)
        glPushMatrix()
        # Traslada las figuras a la posición deseada
        glTranslatef(-20, 0, 4)
        # Rota las figuras para que estén de pie
        glRotatef(-90, 1, 0, 0)  # Rotación de -90 grados alrededor del eje X
        glScalef(1.5, 1.5, 1.5)
        ob.draw_BrazoDe()
        ob.draw_BrazoIz()
        glPopMatrix()

    def brazo_mov_D(self):
        glEnable(GL_DEPTH_TEST)
        glColor3f(0.9, 0.8, 0.6)
        glPushMatrix()
        # Traslada las figuras a la posición deseada
        glTranslatef(-20, 0, 4)
        # Rota las figuras para que estén de pie
        glRotatef(-90, 1, 0, 0)  # Rotación de -90 grados alrededor del eje X
        glScalef(1.5, 1.5, 1.5)
        ob.brazo_Der_up()
        ob.draw_BrazoIz()
        glPopMatrix()

    def pierna_mov_D(self):
        glEnable(GL_DEPTH_TEST)
        glColor3f(0.9, 0.8, 0.6)
        glPushMatrix()
        # Traslada las figuras a la posición deseada
        glTranslatef(-20, 0, 4)
        # Rota las figuras para que estén de pie
        glRotatef(-90, 1, 0, 0)  # Rotación de -90 grados alrededor del eje X
        glScalef(1.5, 1.5, 1.5)
        ob.draw_piernaIz()
        ob.draw_piernaDemov()
        glPopMatrix()

    def pierna_mov_I(self):
        glEnable(GL_DEPTH_TEST)
        glColor3f(0.9, 0.8, 0.6)
        glPushMatrix()
        # Traslada las figuras a la posición deseada
        glTranslatef(-20, 0, 4)
        # Rota las figuras para que estén de pie
        glRotatef(-90, 1, 0, 0)  # Rotación de -90 grados alrededor del eje X
        glScalef(1.5, 1.5, 1.5)
        ob.draw_piernaDe()
        ob.draw_piernaIzmov()
        glPopMatrix()

    def brazo_mov_I(self):
        glEnable(GL_DEPTH_TEST)
        glColor3f(0.9, 0.8, 0.6)
        glPushMatrix()
        # Traslada las figuras a la posición deseada
        glTranslatef(-20, 0, 4)
        # Rota las figuras para que estén de pie
        glRotatef(-90, 1, 0, 0)  # Rotación de -90 grados alrededor del eje X
        glScalef(1.5, 1.5, 1.5)
        ob.brazo_Iz_up()
        ob.draw_BrazoDe()
        glPopMatrix()

    def enojo(self):
        glEnable(GL_DEPTH_TEST)
        glColor3f(0.0, 0.0, 0.0)
        glPushMatrix()
        # Traslada las figuras a la posición deseada
        glTranslatef(-20, 0, 4)
        # Rota las figuras para que estén de pie
        glRotatef(-90, 1, 0, 0)  # Rotación de -90 grados alrededor del eje X
        glScalef(1.5, 1.5, 1.5)
        ob.draw_enojo()
        glPopMatrix()

    def triste(self):
        glEnable(GL_DEPTH_TEST)
        glColor3f(0.0, 0.0, 0.0)
        glPushMatrix()
        # Traslada las figuras a la posición deseada
        glTranslatef(-20, 0, 4)
        # Rota las figuras para que estén de pie
        glRotatef(-90, 1, 0, 0)  # Rotación de -90 grados alrededor del eje X
        glScalef(1.5, 1.5, 1.5)
        ob.draw_triste()
        ob.lagrimas()
        glPopMatrix()

    def feliz(self):
        glEnable(GL_DEPTH_TEST)
        glColor3f(1.0, 1.0, 1.0)
        glPushMatrix()
        # Traslada las figuras a la posición deseada
        glTranslatef(-20, 0, 4)
        # Rota las figuras para que estén de pie
        glRotatef(-90, 1, 0, 0)  # Rotación de -90 grados alrededor del eje X
        glScalef(1.5, 1.5, 1.5)
        ob.draw_feliz()
        glPopMatrix()

    
    def feliz_dientes(self):
        glEnable(GL_DEPTH_TEST)
        glColor3f(0.0, 0.0, 0.0)
        glPushMatrix()
        # Traslada las figuras a la posición deseada
        glTranslatef(-20, 0, 4)
        # Rota las figuras para que estén de pie
        glRotatef(-90, 1, 0, 0)  # Rotación de -90 grados alrededor del eje X
        glScalef(1.5, 1.5, 1.5)
        ob.dientes()
        glPopMatrix()

    def dras_asombro(self):
        glEnable(GL_DEPTH_TEST)
        glColor3f(1.0, 1.0, 1.0)
        glPushMatrix()
        # Traslada las figuras a la posición deseada
        glTranslatef(-20, 0, 4)
        # Rota las figuras para que estén de pie
        glRotatef(-90, 1, 0, 0)  # Rotación de -90 grados alrededor del eje X
        glScalef(1.5, 1.5, 1.5)
        ob.asombro()
        glPopMatrix()

    def draw_asco(self):
        glEnable(GL_DEPTH_TEST)
        glColor3f(0.4, 0.8, 0.2)
        glPushMatrix()
        # Traslada las figuras a la posición deseada
        glTranslatef(-20, 0, 4)
        # Rota las figuras para que estén de pie
        glRotatef(-90, 1, 0, 0)  # Rotación de -90 grados alrededor del eje X
        glScalef(1.5, 1.5, 1.5)
        ob.draw_Cabeza()
        ob.draw_BrazoDe()
        ob.draw_BrazoIz()
        ob.draw_piernaDe()
        ob.draw_piernaIz()
        ob.Cuello()
        ob.draw_ojos_asco()
        ob.draw_enojo()
        ob.draw_Torzo()
        glPopMatrix()
        
    def draw(self):
        self.draw_pies()
        self.draw_Tor()
        self.draw_Cuello()
        self.draw_Cab()
        self.draw_eyes()
        self.draw_Brazos()

    def draw_mov_brazo_D(self):
        self.draw_pies()
        self.draw_Tor()
        self.draw_Cuello()
        self.draw_Cab()
        self.draw_eyes()
        self.brazo_mov_D()

    def draw_mov_brazo_I(self):
        self.draw_pies()
        self.draw_Tor()
        self.draw_Cuello()
        self.draw_Cab()
        self.draw_eyes()
        self.brazo_mov_I()

    def mov_piernaD(self):
        self.pierna_mov_D()
        self.draw_Tor()
        self.draw_Cuello()
        self.draw_eyes()
        self.draw_Cab()
        self.draw_Brazos()

    def mov_piernaI(self):
        self.pierna_mov_I()
        self.draw_Tor()
        self.draw_Cuello()
        self.draw_Cab()
        self.draw_eyes()
        self.draw_Brazos()

    def draw_happy(self):
        self.draw_pies()
        self.draw_Tor()
        self.draw_Cuello()
        self.draw_Cab()
        self.draw_eyes()
        self.draw_Brazos()
        self.feliz()
        self.feliz_dientes()
        

    def draw_angry(self):
        self.draw_pies()
        self.draw_Tor()
        self.draw_Cuello()
        self.draw_Cab()
        self.draw_eyes()
        self.draw_Brazos()
        self.enojo()

    def draw_sad(self):
        self.draw_pies()
        self.draw_Tor()
        self.draw_Cuello()
        self.draw_eyes()
        self.draw_Brazos()
        self.draw_Cab()
        self.triste()

    def draw_omg(self):
        self.draw_pies()
        self.draw_Tor()
        self.draw_Cuello()
        self.draw_eyes()
        self.draw_Brazos()
        self.draw_Cab()
        self.dras_asombro()

    def mov_cuello(self):
        self.draw_pies()
        self.draw_Tor()
        self.draw_Brazos()
        self.draw_Cab()
        self.draw_mov_cuello()
        self.draw_mov_cara()