from OpenGL.GLU import*
from OpenGL.GL import*
from OpenGL.GLUT import*
from pygame.locals import*
from PIL import*
from PersonajeStarenka.Acciones2S import objetos as obj
import math

#------Figura Original----------------
def draw_pie_izq():
    glColor3f(0.306, 0.204, 0.181)
    glPushMatrix()
    glTranslatef(0,0,0)
    obj.draw_cube()
    glPopMatrix()

def draw_pie_der():
    glColor3f(0.306, 0.204, 0.181)
    glPushMatrix()
    glTranslatef(3,0,0)
    obj.draw_cube()
    glPopMatrix()

def draw_pierna_izq():
    glColor3f(0.31, 0.396, 0.537)
    glPushMatrix()
    glTranslatef(-1,0,0)
    obj.draw_rectangle(0,1,1,2 ,5,2)
    glPopMatrix()

def draw_pierna_der():
    glColor3f(0.31, 0.396, 0.537)
    glPushMatrix()
    glTranslatef(2,0,0)
    obj.draw_rectangle(0,1,1,2 ,5,2)
    glPopMatrix()

def draw_bajoSup():
    glColor3f(0.502, 0, 0.502)
    glPushMatrix()
    glTranslatef(0,5.5,0)
    obj.draw_rectangle(-1,0,2,5 ,3,4)
    glPopMatrix()

def draw_brazoIzquierdo():
    glColor3f(0.024, 0.239, 0.482)
    glPushMatrix()
    glTranslatef(0,6,0)
    obj.draw_rectangle(-3,1,1,2 ,6,2)
    glPopMatrix()

def draw_brazoDerecho():
    glColor3f(0.024, 0.239, 0.482)
    glPushMatrix()
    glTranslatef(7,6,0)
    obj.draw_rectangle(-3,1,1,2 ,6,2)
    glPopMatrix()

def draw_torso():
    glColor3f(0.502, 0, 0.502)
    glPushMatrix()
    glTranslatef(0,6,0)
    obj.draw_rectangle(-1,0,2,5 ,7,4)
    glPopMatrix()

def draw_cabeza():
    glColor3f(1.0, 0.8784, 0.7412)
    glPushMatrix()
    glTranslatef(0.9,17,0)
    obj.draw_sphere(4,30,30)
    glPopMatrix()

def draw_pelo():
    glColor3f(0.2353, 0.1569, 0.0)
    glPushMatrix()
    glTranslatef(-1.5,19,3)
    obj.draw_rectangle(0,0,0,6,8,6)
    glPopMatrix()

def draw_ojoDer():
    glColor3f(0.2353, 0.1569, 0.0)
    glPushMatrix()
    glTranslatef(0,16.2,-4)
    obj.draw_arc(1,0,360,1)
    glPopMatrix()
    
def draw_ojoIzq():
    glColor3f(0.2353, 0.1569, 0.0)
    glPushMatrix()
    glTranslatef(3,17,-4)
    obj.draw_arc(1,0,180,1)
    glPopMatrix()

def draw_bocaNom():
    glColor3f(0.2353, 0.1569, 0.0)
    glPushMatrix()
    glTranslatef(3,15,-3)
    obj.draw_arc(1,0,60,2)
    glPopMatrix()

def caraOrg():
    draw_ojoDer()
    draw_bocaNom()
    draw_ojoIzq()

#Figura Original
def original():
    draw_pierna_der()
    draw_pie_der()
    draw_pie_izq()
    draw_pierna_izq()
    draw_bajoSup()
    draw_torso()
    draw_brazoIzquierdo()
    draw_brazoDerecho()
    draw_cabeza()
    draw_pelo()
    caraOrg()

#-----------Asustado----------------
def draw_ojoAsustadoDerecho(): 
    glColor3f(0.2353, 0.1569, 0.0)
    glPushMatrix()
    glTranslatef(3,17,-4)
    obj.draw_arc(1,0,180,10)
    glPopMatrix()

def draw_ojoAsustadoIzquierdo():
    glColor3f(0.2353, 0.1569, 0.0)
    glPushMatrix()
    glTranslatef(0,16.2,-4)
    obj.draw_arc(1,0,180,10)
    glPopMatrix()

def caraAsustado():
    draw_ojoAsustadoDerecho()
    draw_ojoAsustadoIzquierdo()
    draw_bocaEnojado()

def asustado():
    draw_pierna_der()
    draw_pie_der()
    draw_pie_izq()
    draw_pierna_izq()
    draw_bajoSup()
    draw_torso()
    draw_brazoIzquierdo()
    draw_brazoDerecho()
    movCabeza()
    draw_movPelo()
    caraAsustado()

def movCabeza():
    glColor3f(1.0, 0.8784, 0.7412)
    glPushMatrix()
    glTranslatef(0,17,0)
    glRotatef(180, 0, 1, 0) 
    obj.draw_sphere(4,30,30)
    glPopMatrix()

def draw_movPelo():
    glColor3f(0.2353, 0.1569, 0.0)
    glPushMatrix()
    glTranslatef(-2,18,2)
    glRotatef(30, 0, 0, 1) 
    obj.draw_rectangle(0,0,0,6,8,6)
    glPopMatrix()

#---------Enojado--------------------
def draw_bocaEnojado():
    glColor3f(0.2353, 0.1569, 0.0)
    glPushMatrix()
    glTranslatef(3,15,-3)
    obj.draw_line()
    glPopMatrix()

def draw_CabezaEnojada():
    glColor3f(1, 0, 0)
    glPushMatrix()
    glTranslatef(0.9,17,0) 
    obj.draw_sphere(4,30,30)
    glPopMatrix()

def brazoSeñalandoIzquierdo():
    glColor3f(0.024, 0.239, 0.482)
    glPushMatrix()
    glTranslatef(0,11,0)
    glRotatef(-60, 1, 0, 0)
    obj.draw_rectangle(-3,1,1,2 ,6,2)
    glPopMatrix()

def caraEnojada():
    draw_ojoDer()
    draw_bocaEnojado()
    draw_ojoIzq()

def molesto():
    draw_pierna_der()
    draw_pie_der()
    draw_pie_izq()
    draw_pierna_izq()
    draw_bajoSup()
    draw_torso()
    brazoSeñalandoIzquierdo()
    draw_brazoDerecho()
    draw_CabezaEnojada()
    caraEnojada()
    draw_pelo()

#---------Preocupado-------------------

def brazoArribaIzquierda():
    glColor3f(0.024, 0.239, 0.482)
    glPushMatrix()
    glTranslatef(0,10,-3)
    obj.draw_rectangle(-3,1,1,2 ,6,2)
    glPopMatrix()

def brazoArribaDerecha():
    glColor3f(0.024, 0.239, 0.482)
    glPushMatrix()
    glTranslatef(7,10,-3)
    obj.draw_rectangle(-3,1,1,2 ,6,2)
    glPopMatrix()

def draw_ojoPreocupadoDer():
    glColor3f(0.2353, 0.1569, 0.0)
    glPushMatrix()
    glTranslatef(0,16.2,-4)
    obj.draw_arc(1,0,180,1)
    glPopMatrix()

def cara_preocupada():
    draw_ojoPreocupadoDer()
    draw_ojoIzq()
    draw_bocaEnojado()

def preocupado():
    draw_pierna_der()
    draw_pie_der()
    draw_pie_izq()
    draw_pierna_izq()
    draw_bajoSup()
    draw_torso()
    brazoArribaIzquierda()
    brazoArribaDerecha()
    draw_cabeza()
    cara_preocupada()
    draw_pelo()

#------Indiferencia----------

def drawIndiferencia():
    piernaAdelanteDer()
    pieAdelanteDer()
    draw_pie_izq()
    draw_pierna_izq()
    draw_bajoSup()
    draw_torso()
    draw_brazoIzquierdo()
    draw_brazoDerecho()
    draw_cabeza()
    caraIndiferencia()
    draw_pelo()

def caraIndiferencia():
    ojoIndiferenciaIzq()
    ojoIndiferenciaDer()
    draw_bocaEnojado()

def ojoIndiferenciaIzq():
    glColor3f(0.2353, 0.1569, 0.0)  # Color personalizado
    glPushMatrix()
    glTranslatef(0,16.2,-4)
    glRotatef(360, 1, 0, 0)  # Rotar 360 grados alrededor del eje X
    obj.draw_line()
    glPopMatrix()

def ojoIndiferenciaDer():
    glColor3f(0.2353, 0.1569, 0.0)  # Color personalizado
    glPushMatrix()
    glTranslatef(3,16.2,-4)
    glRotatef(360, 1, 0, 0)  # Rotar 360 grados alrededor del eje X
    obj.draw_line()
    glPopMatrix()

def piernaAdelanteDer():
    glColor3f(0.31, 0.396, 0.537)
    glPushMatrix()
    glTranslatef(2,0,-3)
    glRotatef(15, 1, 0, 0)
    obj.draw_rectangle(0,1,1,2 ,5,2)
    glPopMatrix()

def pieAdelanteDer():
    glColor3f(0.306, 0.204, 0.181)
    glPushMatrix()
    glTranslatef(3,0,-3)
    glRotatef(15, 1, 0, 0)
    obj.draw_cube()
    glPopMatrix()

#-------Sorpendido------------------------

def ojoIzquierdoSorp():
    glColor3f(0.2353, 0.1569, 0.0)
    glPushMatrix()
    glTranslatef(3,17,-4)
    glRotatef(90,0,0,1)
    obj.draw_line()
    glPopMatrix()

def ojoDerechoSorp():
    glColor3f(0.2353, 0.1569, 0.0)
    glPushMatrix()
    glTranslatef(1,17,-4)
    glRotatef(90,0,0,1)
    obj.draw_line()
    glPopMatrix()

def bocaEnFormaDeO():
    glColor3f(0.2353, 0.1569, 0.0)
    glPushMatrix()
    glTranslatef(3,15,-3)
    obj.draw_arc(1, 180, 360, 1)
    glPopMatrix()

def caraSorprendido():
    ojoDerechoSorp()
    ojoIzquierdoSorp()
    bocaEnFormaDeO()

def sorprendido():
    draw_bajoSup()
    draw_torso()
    brazoSeñalandoIzquierdo()
    brazoSeñalandoDerecho()
    draw_cabeza()
    draw_pelo()
    caraSorprendido()
    pieAdelanteDer()
    piernaAdelanteDer()
    draw_pie_izq()
    draw_pierna_izq()

def brazoSeñalandoDerecho():
    glColor3f(0.024, 0.239, 0.482)
    glPushMatrix()
    glTranslatef(7,9,0)
    glRotatef(-60, 1, 0, 0)
    obj.draw_rectangle(-3,1,1,2 ,6,2)
    glPopMatrix()

#------Felicidad
def sonrisa():
    glPushMatrix()
    glTranslatef(1, 14, -3.7)  # Ajustar la posición en la cara del muñeco
    glRotatef(60,1,0,0)
    glColor3f(0.2353, 0.1569, 0.0)  # Color marrón oscuro para la sonrisa
    
    glBegin(GL_LINE_STRIP)
    for angle in range(-60, 61, 5):  # Aumentamos el rango para una sonrisa más ancha
        theta = math.radians(angle)
        x = 2.0 * math.cos(theta)  # Aumentamos el radio para una sonrisa más grande
        y = math.sin(theta) + 0.5 * math.sin(2 * theta)  # Añadimos una curva adicional para más expresividad
        glVertex2f(x, y)
    glEnd()
    
    glPopMatrix()


def caraFelicidad():
 ojoDerechoSorp()
 ojoIzquierdoSorp()
 sonrisa()

def felicidad():
    glPushMatrix()
    glTranslatef(0,8,0)
    pieAdelanteIzq()
    piernaAdelanteIzq()
    draw_pie_der()
    draw_pierna_der()
    draw_bajoSup()
    draw_torso()
    brazoArribaDerecha()
    brazoArribaIzquierda()
    draw_cabeza()
    caraFelicidad()
    draw_pelo()
    glPopMatrix()

    

#------Triste
def bocaTriste():
    glPushMatrix()
    glTranslatef(1.5, 12, -3.7)  # Ajustar la posición en la cara del muñeco
    glRotatef(80,0,0,1)
    glColor3f(0.2353, 0.1569, 0.0)  # Color marrón oscuro para la sonrisa
    
    glBegin(GL_LINE_STRIP)
    for angle in range(-60, 61, 5):  # Aumentamos el rango para una sonrisa más ancha
        theta = math.radians(angle)
        x = 2.0 * math.cos(theta)  # Aumentamos el radio para una sonrisa más grande
        y = math.sin(theta) + 0.5 * math.sin(2 * theta)  # Añadimos una curva adicional para más expresividad
        glVertex2f(x, y)
    glEnd()
    
    glPopMatrix()

def caraTriste():
    glPushMatrix()
    glTranslatef(0,-2,0)
    ojoDerechoSorp()
    ojoIzquierdoSorp()
    bocaTriste()
    glPopMatrix()

def triste():
    glPushMatrix()
    glRotatef(90,0,0,1)
    draw_pie_der()
    draw_pie_izq()
    draw_pierna_der()
    draw_pierna_izq()
    draw_bajoSup()
    draw_torso()
    brazoArribaDerecha()
    brazoArribaIzquierda()
    draw_cabeza()
    caraTriste()
    draw_pelo()
    glPopMatrix()
    
#------LEVANTAMIENTO DE BRAZOS

def levantarBrazos():
    draw_pierna_der()
    draw_pie_der()
    draw_pie_izq()
    draw_pierna_izq()
    draw_bajoSup()
    draw_torso()
    draw_cabeza()
    draw_pelo()
    caraOrg()
    brazoArribaDerecha()
    brazoArribaIzquierda()

#Un movimiento
def animaLevantar():
    ##Se declara una variable global
    global frame_count
    #Condicional ue verifica si la variable no existe en el espacio de nombres global.
    #En caso de que no exista, se crea una nueva variable con valor a 0. 
    if 'frame_count' not in globals():
        frame_count = 0
    
    #Cuenta los números de frames
    frame_count += 1

    #Condicional que verifica si el resto de la division de "frame_count" entre 60 es menor que 30
    #Si cumple levanta los brazos, si no vuelve a la original

    if frame_count % 60 < 30:  # Cambia cada 30 frames (aproximadamente 0.5 segundos a 60 FPS)
        levantarBrazos()
    else:
        original()

#-------CAMINAR
def pieAdelanteIzq():
    glEnable(GL_DEPTH_TEST)
    glColor3f(0.306, 0.204, 0.181)
    glPushMatrix()
    glTranslatef(0,0,-3)
    glRotatef(15, 1, 0, 0)
    obj.draw_cube()
    glPopMatrix()

def piernaAdelanteIzq():
    glEnable(GL_DEPTH_TEST)
    glColor3f(0.31, 0.396, 0.537)
    glPushMatrix()
    glTranslatef(-1,0,-3)
    glRotatef(15, 1, 0, 0)
    obj.draw_rectangle(0,1,1,2 ,5,2)
    glPopMatrix()

#Multiples movimientos
def animaCaminar():
    #Declaramos dos variables globales
    global frame_count, paso
    
    #Verificaamos que las dos variables no se encuentren dentro de globals, 
    #en caso de que no esten lo inicilizaran en 0.
    if 'frame_count' not in globals():
        frame_count = 0
    if 'paso' not in globals():
        paso = 0

    #Contador de framse
    frame_count += 1

    if frame_count % 15 == 0:  # Cambia cada 15 frames (ajusta la velocidad según lo desees)
        paso = (paso + 1) % 2  # Cambia entre 0 y 1 únicamente, repitiendo solo esos pasos

    # Dibujar el cuerpo superior
    draw_bajoSup()
    draw_torso()
    draw_brazoIzquierdo()
    draw_brazoDerecho()
    draw_cabeza()
    draw_pelo()
    caraOrg()

    # Dibujar las piernas y pies según el paso actual
    if paso == 0:
        pieAdelanteDer()
        piernaAdelanteDer()
        draw_pie_izq()
        draw_pierna_izq()

    elif paso == 1:
        pieAdelanteIzq()
        piernaAdelanteIzq()
        draw_pie_der()
        draw_pierna_der()

##Mover los dos brazos adelante y atraz
#Un movimiento
def animaBrazo2():
    global frame_count, paso
    
    if 'frame_count' not in globals():
        frame_count = 0
    if 'paso' not in globals():
        paso = 0

    frame_count += 1

    if frame_count % 15 == 0:  # Cambia cada 15 frames (ajusta la velocidad según lo desees)
        paso = (paso + 1) % 2  # Cambia entre 0 y 1 únicamente, repitiendo solo esos pasos

    # Dibujar el cuerpo superior
    draw_bajoSup()
    draw_torso()
    draw_pie_der()
    draw_pierna_der()
    draw_pie_izq()
    draw_pierna_izq()
    draw_cabeza()
    draw_pelo()
    caraOrg()

    if paso == 0:
        brazoSeñalandoDerecho()
        draw_brazoIzquierdo()

    elif paso == 1:
       brazoSeñalandoIzquierdo()
       draw_brazoDerecho()

#Mover cabeza-----------------
#Un movimiento
def cuerpoMovCabeza():
    draw_pierna_der()
    draw_pie_der()
    draw_pie_izq()
    draw_pierna_izq()
    draw_bajoSup()
    draw_torso()
    draw_brazoIzquierdo()
    draw_brazoDerecho()
    draw_movPelo()
    movCabeza()
    cara_preocupada()

def animaCabeza():
    global frame_count
    if 'frame_count' not in globals():
        frame_count = 0
    
    frame_count += 1
    if frame_count % 60 < 30:  # Cambia cada 30 frames (aproximadamente 0.5 segundos a 60 FPS)
        cuerpoMovCabeza()
    else:
        original()
        
#BRINCAR
#un movimiento
def originalBrincar():
    glPushMatrix()
    glTranslatef(0,5,0)
    original()
    glPopMatrix()

def animaBrincar():
    global frame_count
    if 'frame_count' not in globals():
        frame_count = 0
    
    frame_count += 1
    if frame_count % 60 < 30:  # Cambia cada 30 frames (aproximadamente 0.5 segundos a 60 FPS)
        originalBrincar()
    else:
        original()

#Brincar Split
#Un movimiento
def animaBrincarSplit():
    global frame_count
    if 'frame_count' not in globals():
        frame_count = 0
    
    frame_count += 1
    if frame_count % 60 < 30:  # Cambia cada 30 frames (aproximadamente 0.5 segundos a 60 FPS)
        felicidad()
    else:
        original()

#Caer
#Un movimiento
def animaCaida():
    global frame_count
    if 'frame_count' not in globals():
        frame_count = 0
    
    frame_count += 1
    if frame_count % 60 < 30:  # Cambia cada 30 frames (aproximadamente 0.5 segundos a 60 FPS)
        triste()
    else:
        original()

def felicidad2():

    draw_pierna_der()
    draw_pie_der()
    draw_pie_izq()
    draw_pierna_izq()
    draw_bajoSup()
    draw_torso()
    brazoArribaDerecha()
    brazoArribaIzquierda()
    draw_cabeza()
    caraFelicidad()
    draw_pelo()
