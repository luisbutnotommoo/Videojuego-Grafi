from OpenGL.GLU import *
from OpenGL.GL import *
from OpenGL.GLUT import *
from pygame.locals import *
from PIL import *
import objetos as ob
import lucesNuev as lc

#-----------------------------------------------------------------------
#-----figura blue---------
aux = 0
PosX_objeto1 = 3 #coordenada mov 
PosY_objeto1 = 6
PosZ_objeto1 = 4
Obj1_height = 1
#----------------------------------------------------------------------
##figura colision##
PosX_objeto2 = 3
PosY_objeto2 = 6
PosZ_objeto2 = 4
Obj2_height = 1
Obj2_width = 1
Obj2_depth = 1
#--------------------------------------------

#posicion de esfera
PosObj2_X = 3
PosObj2_Y = 6
PosObj2_Z = 4
Obj2_height = 1
Obj2_width = 1
Obj2_depth = 1


#cubo
PosXob1 = 3  # mov en x
PosYob1 = 6  # mov en y
PosZob1 = 4  # mov en z
Obj1_height=1

#metodo dibuja esfera

def draw2():
    glEnable(GL_DEPTH_TEST)
    glColor3f(0.0,1.0,0.0)
    glPushMatrix()
    glTranslatef(PosObj2_X, PosObj2_Y, PosObj2_Z)
    lc.iluminacion(0.0, 0.0, 1.0)
    ob.draw_sphere(8, 40, 40)
    glDisable(GL_LIGHTING)
    glDisable(GL_LIGHT0)
    glPopMatrix() 

def draw_mov(movX,movY):
    global PosX_objeto1,PosY_objeto1 #coordenadas globales
    PosX_objeto1 = PosX_objeto1+movX #se suma a los ejes el movimiento
    PosY_objeto1 = PosY_objeto1+movY
    glEnable(GL_DEPTH_TEST)
    glPushMatrix()
    glTranslatef(PosX_objeto1,PosY_objeto1,PosZ_objeto1) #trasladar a las nuevas coordenadas
    draw()
    glDisable(GL_LIGHTING)
    glDisable(GL_LIGHT0)
    glPopMatrix()

def draw3(movX, movY):
    global PosXob1, PosYob1
    PosXob1=PosXob1+movX
    PosYob1=PosYob1+movY
    glEnable(GL_DEPTH_TEST)
    glPushMatrix()
    glTranslatef(PosXob1,PosYob1,PosZob1)
    lc.iluminacion(0.0,1.0,0.0)
    ob.draw_cube()
    glDisable(GL_LIGHTING)
    glDisable(GL_LIGHT0)
    glPopMatrix()
#--------------------gestos con movimiento
def draw_movEnojo(movX,movY):
    global PosX_objeto1,PosY_objeto1 #coordenadas globales
    PosX_objeto1 = PosX_objeto1+movX #se suma a los ejes el movimiento
    PosY_objeto1 = PosY_objeto1+movY
    glEnable(GL_DEPTH_TEST)
    glPushMatrix()
    glTranslatef(PosX_objeto1,PosY_objeto1,PosZ_objeto1) #trasladar a las nuevas coordenadas
    draw_angry()

    glDisable(GL_LIGHTING)
    glDisable(GL_LIGHT0)
    glPopMatrix()

def draw_movhappy(movX,movY):
    global PosX_objeto1,PosY_objeto1 #coordenadas globales
    PosX_objeto1 = PosX_objeto1+movX #se suma a los ejes el movimiento
    PosY_objeto1 = PosY_objeto1+movY
    glEnable(GL_DEPTH_TEST)
    glPushMatrix()
    glTranslatef(PosX_objeto1,PosY_objeto1,PosZ_objeto1) #trasladar a las nuevas coordenadas
    draw_happy()

    glDisable(GL_LIGHTING)
    glDisable(GL_LIGHT0)
    glPopMatrix()

def draw_movasco(movX,movY):
    global PosX_objeto1,PosY_objeto1 #coordenadas globales
    PosX_objeto1 = PosX_objeto1+movX #se suma a los ejes el movimiento
    PosY_objeto1 = PosY_objeto1+movY
    glEnable(GL_DEPTH_TEST)
    glPushMatrix()
    glTranslatef(PosX_objeto1,PosY_objeto1,PosZ_objeto1) #trasladar a las nuevas coordenadas
    draw_asco()
    glDisable(GL_LIGHTING)
    glDisable(GL_LIGHT0)
    glPopMatrix()

def draw_movomg(movX,movY):
    global PosX_objeto1,PosY_objeto1 #coordenadas globales
    PosX_objeto1 = PosX_objeto1+movX #se suma a los ejes el movimiento
    PosY_objeto1 = PosY_objeto1+movY
    glEnable(GL_DEPTH_TEST)
    glPushMatrix()
    glTranslatef(PosX_objeto1,PosY_objeto1,PosZ_objeto1) #trasladar a las nuevas coordenadas
    draw_omg()
    glDisable(GL_LIGHTING)
    glDisable(GL_LIGHT0)
    glPopMatrix()
    
def draw_movsad(movX,movY):
    global PosX_objeto1,PosY_objeto1 #coordenadas globales
    PosX_objeto1 = PosX_objeto1+movX #se suma a los ejes el movimiento
    PosY_objeto1 = PosY_objeto1+movY
    glEnable(GL_DEPTH_TEST)
    glPushMatrix()
    glTranslatef(PosX_objeto1,PosY_objeto1,PosZ_objeto1) #trasladar a las nuevas coordenadas
    draw_sad()
    glDisable(GL_LIGHTING)
    glDisable(GL_LIGHT0)
    glPopMatrix()

def draw_mov_brazoD(movX,movY):
    global PosX_objeto1,PosY_objeto1 #coordenadas globales
    PosX_objeto1 = PosX_objeto1+movX #se suma a los ejes el movimiento
    PosY_objeto1 = PosY_objeto1+movY
    glEnable(GL_DEPTH_TEST)
    glPushMatrix()
    glTranslatef(PosX_objeto1,PosY_objeto1,PosZ_objeto1) #trasladar a las nuevas coordenadas
    draw_mov_brazo_D()
    glDisable(GL_LIGHTING)
    glDisable(GL_LIGHT0)
    glPopMatrix()

def draw_mov_brazoI(movX,movY):
    global PosX_objeto1,PosY_objeto1 #coordenadas globales
    PosX_objeto1 = PosX_objeto1+movX #se suma a los ejes el movimiento
    PosY_objeto1 = PosY_objeto1+movY
    glEnable(GL_DEPTH_TEST)
    glPushMatrix()
    glTranslatef(PosX_objeto1,PosY_objeto1,PosZ_objeto1) #trasladar a las nuevas coordenadas
    draw_mov_brazo_I()
    glDisable(GL_LIGHTING)
    glDisable(GL_LIGHT0)
    glPopMatrix()

def draw_movcuello(movX,movY):
    global PosX_objeto1,PosY_objeto1 #coordenadas globales
    PosX_objeto1 = PosX_objeto1+movX #se suma a los ejes el movimiento
    PosY_objeto1 = PosY_objeto1+movY
    glEnable(GL_DEPTH_TEST)
    glPushMatrix()
    glTranslatef(PosX_objeto1,PosY_objeto1,PosZ_objeto1) #trasladar a las nuevas coordenadas
    mov_cuello()
    glDisable(GL_LIGHTING)
    glDisable(GL_LIGHT0)
    glPopMatrix()

def draw_movPD(movX,movY):
    global PosX_objeto1,PosY_objeto1 #coordenadas globales
    PosX_objeto1 = PosX_objeto1+movX #se suma a los ejes el movimiento
    PosY_objeto1 = PosY_objeto1+movY
    glEnable(GL_DEPTH_TEST)
    glPushMatrix()
    glTranslatef(PosX_objeto1,PosY_objeto1,PosZ_objeto1) #trasladar a las nuevas coordenadas
    mov_piernaD()
    glDisable(GL_LIGHTING)
    glDisable(GL_LIGHT0)
    glPopMatrix()

def draw_movPI(movX,movY):
    global PosX_objeto1,PosY_objeto1 #coordenadas globales
    PosX_objeto1 = PosX_objeto1+movX #se suma a los ejes el movimiento
    PosY_objeto1 = PosY_objeto1+movY
    glEnable(GL_DEPTH_TEST)
    glPushMatrix()
    glTranslatef(PosX_objeto1,PosY_objeto1,PosZ_objeto1) #trasladar a las nuevas coordenadas
    mov_piernaI()
    glDisable(GL_LIGHTING)
    glDisable(GL_LIGHT0)
    glPopMatrix()

def draw_mov_cuello():
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

def draw_mov_cara():
    glEnable(GL_DEPTH_TEST)
    glPushMatrix()
    # Traslada las figuras a la posición deseada
    glTranslatef(-20, 0, 4)
    # Rota las figuras para que estén de pie
    glRotatef(-90, 1, 0, 0)  # Rotación de -90 grados alrededor del eje X
    glScalef(1.5, 1.5, 1.5)
    ob.mov_draw_ojos()
    
    glPopMatrix()
   
def draw_pies():
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


def draw_Tor():
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

def draw_Cuello():
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

def draw_Cab():
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


def draw_eyes():
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


def draw_Brazos():
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

def brazo_mov_D():
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

def pierna_mov_D():
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

def pierna_mov_I():
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

def brazo_mov_I():
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

def enojo():
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

def triste():
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

def feliz():
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

   
def feliz_dientes():
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

def dras_asombro():
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

def draw_asco():
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
    
def draw():
    draw_pies()
    draw_Tor()
    draw_Cuello()
    draw_Cab()
    draw_eyes()
    draw_Brazos()

def draw_mov_brazo_D():
    draw_pies()
    draw_Tor()
    draw_Cuello()
    draw_Cab()
    draw_eyes()
    brazo_mov_D()

def draw_mov_brazo_I():
    draw_pies()
    draw_Tor()
    draw_Cuello()
    draw_Cab()
    draw_eyes()
    brazo_mov_I()

def mov_piernaD():
    pierna_mov_D()
    draw_Tor()
    draw_Cuello()
    draw_eyes()
    draw_Cab()
    draw_Brazos()

def mov_piernaI():
    pierna_mov_I()
    draw_Tor()
    draw_Cuello()
    draw_Cab()
    draw_eyes()
    draw_Brazos()

def draw_happy():
    draw_pies()
    draw_Tor()
    draw_Cuello()
    draw_Cab()
    draw_eyes()
    draw_Brazos()
    feliz()
    feliz_dientes()
    

def draw_angry():
    draw_pies()
    draw_Tor()
    draw_Cuello()
    draw_Cab()
    draw_eyes()
    draw_Brazos()
    enojo()

def draw_sad():
    draw_pies()
    draw_Tor()
    draw_Cuello()
    draw_eyes()
    draw_Brazos()
    draw_Cab()
    triste()

def draw_omg():
    draw_pies()
    draw_Tor()
    draw_Cuello()
    draw_eyes()
    draw_Brazos()
    draw_Cab()
    dras_asombro()

def mov_cuello():
    draw_pies()
    draw_Tor()
    draw_Brazos()
    draw_Cab()
    draw_mov_cuello()
    draw_mov_cara()