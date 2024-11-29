
from OpenGL.GL import*
import objetos as ob


def __init__(self):
        # Atributos que antes eran globales, ahora son de la instancia
        self.PosX_objeto1 = 0
        self.PosY_objeto1 = 0
        self.PosZ_objeto1 = 0  # Si es necesario para otros métodos


#def actualizar_posicion(self, movX, movY):
#        self.posX += movX
#        self.posY += movY

def draw_mov(self, movX, movY):
        self.PosX_objeto1 += movX
        self.PosY_objeto1 += movY
        glEnable(GL_DEPTH_TEST)
        glPushMatrix()
        glTranslatef(self.PosX_objeto1, self.PosY_objeto1, self.PosZ_objeto1)
        # Iluminación, dibujo de objeto
        draw()
        glDisable(GL_LIGHTING)
        glDisable(GL_LIGHT0)
        glPopMatrix()

def draw_movEnojo(self, movX, movY):
        self.PosX_objeto1 += movX
        self.PosY_objeto1 += movY
        glEnable(GL_DEPTH_TEST)
        glPushMatrix()
        glTranslatef(self.PosX_objeto1, self.PosY_objeto1, self.PosZ_objeto1)
        # Iluminación, dibujo de objeto
        draw_angry()
        glDisable(GL_LIGHTING)
        glDisable(GL_LIGHT0)
        glPopMatrix()

def draw_movhappy(self, movX, movY):
        self.PosX_objeto1 += movX
        self.PosY_objeto1 += movY
        glEnable(GL_DEPTH_TEST)
        glPushMatrix()
        glTranslatef(self.PosX_objeto1, self.PosY_objeto1, self.PosZ_objeto1)
        # Iluminación, dibujo de objeto
        draw_happy()
        glDisable(GL_LIGHTING)
        glDisable(GL_LIGHT0)
        glPopMatrix()

def draw_movasco(self, movX, movY):
    self.PosX_objeto1 += movX
    self.PosY_objeto1 += movY
    PosX_objeto1 = PosX_objeto1+movX #se suma a los ejes el movimiento
    PosY_objeto1 = PosY_objeto1+movY
    glEnable(GL_DEPTH_TEST)
    glPushMatrix()
    glTranslatef(self.PosX_objeto1, self.PosY_objeto1, self.PosZ_objeto1) #trasladar a las nuevas coordenadas
    #iluminacion y sombras, la ilum. va antes de dibujar todo
    #ilum.iluminacion(0,1.0,0)
    #Dibujar objeto
    draw_asco()
    glDisable(GL_LIGHTING)
    glDisable(GL_LIGHT0)
    glPopMatrix()

def draw_movomg(self, movX, movY):
    self.PosX_objeto1 += movX
    self.PosY_objeto1 += movY
    PosX_objeto1 = PosX_objeto1+movX #se suma a los ejes el movimiento
    PosY_objeto1 = PosY_objeto1+movY
    glEnable(GL_DEPTH_TEST)
    glPushMatrix()
    glTranslatef(self.PosX_objeto1, self.PosY_objeto1, self.PosZ_objeto1) #trasladar a las nuevas coordenadas
    #iluminacion y sombras, la ilum. va antes de dibujar todo
    #ilum.iluminacion(0,1.0,0)
    #Dibujar objeto
    draw_omg()
    glDisable(GL_LIGHTING)
    glDisable(GL_LIGHT0)
    glPopMatrix()
    
def draw_movsad(self, movX, movY):
    self.PosX_objeto1 += movX
    self.PosY_objeto1 += movY
    PosX_objeto1 = PosX_objeto1+movX #se suma a los ejes el movimiento
    PosY_objeto1 = PosY_objeto1+movY
    glEnable(GL_DEPTH_TEST)
    glPushMatrix()
    glTranslatef(self.posX,self.posY,self.posZ) #trasladar a las nuevas coordenadas
    #iluminacion y sombras, la ilum. va antes de dibujar todo
    #ilum.iluminacion(0,1.0,0)
    #Dibujar objeto
    draw_sad()
    glDisable(GL_LIGHTING)
    glDisable(GL_LIGHT0)
    glPopMatrix()

def draw_mov_brazoD(self, movX, movY):
    self.PosX_objeto1 += movX
    self.PosY_objeto1 += movY
    PosX_objeto1 = PosX_objeto1+movX #se suma a los ejes el movimiento
    PosY_objeto1 = PosY_objeto1+movY
    glEnable(GL_DEPTH_TEST)
    glPushMatrix()
    glTranslatef(self.PosX_objeto1, self.PosY_objeto1, self.PosZ_objeto1) #trasladar a las nuevas coordenadas
    #iluminacion y sombras, la ilum. va antes de dibujar todo
    #ilum.iluminacion(0,1.0,0)
    #Dibujar objeto
    draw_mov_brazo_D()
    glDisable(GL_LIGHTING)
    glDisable(GL_LIGHT0)
    glPopMatrix()

def draw_mov_brazoI(self, movX, movY):
    self.PosX_objeto1 += movX
    self.PosY_objeto1 += movY
    PosX_objeto1 = PosX_objeto1+movX #se suma a los ejes el movimiento
    PosY_objeto1 = PosY_objeto1+movY
    glEnable(GL_DEPTH_TEST)
    glPushMatrix()
    glTranslatef(self.PosX_objeto1, self.PosY_objeto1, self.PosZ_objeto1) #trasladar a las nuevas coordenadas
    #iluminacion y sombras, la ilum. va antes de dibujar todo
    #ilum.iluminacion(0,1.0,0)
    #Dibujar objeto
    draw_mov_brazo_I()
    glDisable(GL_LIGHTING)
    glDisable(GL_LIGHT0)
    glPopMatrix()

def draw_movcuello(self, movX, movY):
    self.PosX_objeto1 += movX
    self.PosY_objeto1 += movY
    PosX_objeto1 = PosX_objeto1+movX #se suma a los ejes el movimiento
    PosY_objeto1 = PosY_objeto1+movY
    glEnable(GL_DEPTH_TEST)
    glPushMatrix()
    glTranslatef(self.PosX_objeto1, self.PosY_objeto1, self.PosZ_objeto1)#trasladar a las nuevas coordenadas
    #iluminacion y sombras, la ilum. va antes de dibujar todo
    #ilum.iluminacion(0,1.0,0)
    #Dibujar objeto
    mov_cuello()
    glDisable(GL_LIGHTING)
    glDisable(GL_LIGHT0)
    glPopMatrix()

def draw_movPD(self, movX, movY):
    self.PosX_objeto1 += movX
    self.PosY_objeto1 += movY
    PosX_objeto1 = PosX_objeto1+movX #se suma a los ejes el movimiento
    PosY_objeto1 = PosY_objeto1+movY
    glEnable(GL_DEPTH_TEST)
    glPushMatrix()
    glTranslatef(self.PosX_objeto1, self.PosY_objeto1, self.PosZ_objeto1) #trasladar a las nuevas coordenadas
    #iluminacion y sombras, la ilum. va antes de dibujar todo
    #ilum.iluminacion(0,1.0,0)
    #Dibujar objeto
    mov_piernaD()
    glDisable(GL_LIGHTING)
    glDisable(GL_LIGHT0)
    glPopMatrix()

def draw_movPI(self, movX, movY):
    self.PosX_objeto1 += movX
    self.PosY_objeto1 += movY
    PosX_objeto1 = PosX_objeto1+movX #se suma a los ejes el movimiento
    PosY_objeto1 = PosY_objeto1+movY
    glEnable(GL_DEPTH_TEST)
    glPushMatrix()
    glTranslatef(self.PosX_objeto1, self.PosY_objeto1, self.PosZ_objeto1) #trasladar a las nuevas coordenadas
    #iluminacion y sombras, la ilum. va antes de dibujar todo
    #ilum.iluminacion(0,1.0,0)
    #Dibujar objeto
    mov_piernaI()
    glDisable(GL_LIGHTING)
    glDisable(GL_LIGHT0)
    glPopMatrix()

#------------------------------------------------------------------------------------------------------------------------------------------------------


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
    glColor3f(0.0, 1.0, 0.0)
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
    glColor3f(0.0, 1.0, 0.0)
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
    glColor3f(0.0, 1.0, 0.0)
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
    glColor3f(0.0, 1.0, 0.0)
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

def mov_piernaD(self):
    self.pierna_mov_D()
    self.draw_Tor()
    self.draw_Cuello()
    self.draw_Cab()
    self.draw_eyes()
    self.draw_Brazos()

def mov_piernaI(self):
    self.pierna_mov_I()
    self.draw_Tor()
    self.draw_Cuello()
    self.draw_Cab()
    self.draw_eyes()
    self.draw_Brazos()    

def draw(self):
    self.draw_pies()
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
    self.self.draw_Tor()
    self.draw_Cuello()
    self.draw_Cab()
    self.draw_eyes()
    self.draw_Brazos()
    self.enojo()

def draw_omg(self):
    self.draw_pies()
    self.draw_Tor()
    self.draw_Cuello()
    self.draw_Cab()
    self.draw_eyes()
    self.draw_Brazos()
    self.dras_asombro()

def draw_sad(self):
    self.draw_pies()
    self.draw_Tor()
    self.draw_Cuello()
    self.draw_Cab()
    self.draw_eyes()
    self.draw_Brazos()
    self.triste()

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

def mov_cuello(self):
    self.draw_pies()
    self.draw_Tor()
    self.draw_Brazos()
    self.draw_mov_cuello()
    self.draw_mov_cara()    