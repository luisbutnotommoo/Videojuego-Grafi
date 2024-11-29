import pygame as py
from OpenGL.GLU import *
from OpenGL.GL import *
from OpenGL.GLUT import *
from pygame.locals import *
from PIL import *
import escenarios as es
import sonido as so
import tkinter.messagebox as messagebox 
import os
import lucesNuev as lc
from dibuja import *
from colisiones import *
import textos as txt
import firguras as obj
from firguras import *

py.init()
py.mixer.init()

display = (800,600)
py.display.set_mode(display, DOUBLEBUF | OPENGL)


gluPerspective(90, (display[0]/display[1]), 0.1, 50.0)
glTranslatef(-2,0,-2)
glOrtho(0,15,0,15,0,6)


camara_speed = 0.1
rotacion_speed = 0.2
mouse_sensivity = 0.1
py.event.set_grab(True)
py.mouse.set_visible(False)
ban = 0
directorio_script = os.path.dirname(os.path.abspath(__file__))

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

def draw(movX, movY):
    global PosXob1, PosYob1
    PosXob1=PosXob1+movX
    PosYob1=PosYob1+movY
    glEnable(GL_DEPTH_TEST)
    glColor3f(0.5,1.0,1.0)
    glPushMatrix()
    glTranslatef(PosXob1,PosYob1,PosZob1)
    #lc.iluminacion(0.0,1.0,0.0)
    obj.draw_cube()
    glDisable(GL_LIGHTING)
    glDisable(GL_LIGHT0)
    glPopMatrix()


def draw2():
    glEnable(GL_DEPTH_TEST)
    glColor3f(0.0,1.0,0.0)
    glPushMatrix()
    glTranslatef(PosObj2_X, PosObj2_Y, PosObj2_Z)
    lc.iluminacion(0.0, 0.0, 1.0)
    obj.draw_sphere(2, 40, 40)
    glDisable(GL_LIGHTING)
    glDisable(GL_LIGHT0)
    glPopMatrix()
 

ban2=0
ban3=0
ban4=0

while True:
    for event in py.event.get():
        if event.type == py.QUIT:
            py.quit()
            quit()
            #menu
        if event.type == py.KEYDOWN:
            if event.key==py.K_m:
                ban2=7
            #sonido_principal
            if event.key == py.K_p:
                so.play('C:/Users/LuisGutierrez/Documents/Lyn/blue_multiverso/machote/sonidos/guitarra.mp3')
            if event.key == py.K_q:
                so.stop()
            if event.key==py.K_ESCAPE:
                py.quit()
                quit()    
            #escenarios
            if event.key==py.K_0:
                ban=0
               
            if event.key==py.K_1:
                ban=1
                
            if event.key==py.K_2:
                ban=2
               
            if event.key==py.K_3:
                ban=3

            if event.key==py.K_4:
                ban=4
            #expresiones
            if event.key==py.K_f: #feliz
                ban2=1
                so.play('C:/Users/LuisGutierrez/Documents/Lyn/blue_multiverso/machote/sonidos/risaHombre.wav')
            if event.key==py.K_n: #asco
                ban2=2
                so.play('C:/Users/LuisGutierrez/Documents/Lyn/blue_multiverso/machote/sonidos/yuck.wav')
            if event.key==py.K_o: #asombrado
                ban2=3
                so.play('C:/Users/LuisGutierrez/Documents/Lyn/blue_multiverso/machote/sonidos/wow.wav')
            if event.key==py.K_t: #triste
                ban2=4
                so.play('C:/Users/LuisGutierrez/Documents/Lyn/blue_multiverso/machote/sonidos/llora.mp3')
            if event.key==py.K_e: #enojado
                ban2=5
                so.play('C:/Users/LuisGutierrez/Documents/Lyn/blue_multiverso/machote/sonidos/Enojado.wav')
            if event.key==py.K_r: #original
                ban2=6
                ban3=6
            #movimientos
            if event.key==py.K_RIGHT: #brazo derecho
                ban3=1
                
            if event.key==py.K_LEFT: #brazo izquierdo
                ban3=2

            if event.key==py.K_DOWN: #pierna derecha
                ban3=3
                
            if event.key==py.K_UP: #pierna izquierda
                ban3=4

            if event.key==py.K_SPACE: #cuello
                ban3=5
            if event.key==py.K_9: 
                ban4=1
            if event.key==py.K_8: 
                ban4=2
            if event.key==py.K_7: 
                ban4=3
            if event.key==py.K_TAB:
                messagebox.showinfo("Datos:", "Nombre: Lineth Hernández Torres\nNúmero de control: B22280605\nActividad: Personaje 3D\nNombre de personaje: BLUE")
         
    keys = py.key.get_pressed()
    if keys[py.K_s]:
       glTranslatef(0,0,3)
    if keys[py.K_w]:
       glTranslatef(0,0,-3)
    if keys[py.K_a]:
       glTranslatef(3,0,0)
    if keys[py.K_d]:
       glTranslatef(-3,0,0)
    if keys[py.K_x]:
       glTranslatef(0,-3,0)
    if keys[py.K_z]:
       glTranslatef(0,3,0)

    x,y =  py.mouse.get_rel()
    x *= mouse_sensivity
    y *= mouse_sensivity

    if x != 0 or y != 0:
        glRotatef(x, 0, 1, 0)
        glRotatef(y, 1, 0, 0)
    py.mouse.set_pos(display[0]//2,display[1]//2)

    if ban4 == 1:
         glClearColor(0.0, 0.0, 0.0, 1.0)
         glEnable(GL_DEPTH_TEST)
         lc.phong(0.5,0.7,0.6)
         
    if ban4 == 2:
         glClearColor(0.0, 0.0, 0.0, 1.0)
         glEnable(GL_DEPTH_TEST)
         lc.gouraud(0.8,1,0.5)
    if ban4 == 3:
         glClearColor(0.0, 0.0, 0.0, 1.0)
         glEnable(GL_DEPTH_TEST)
         lc.interpolado(0.4,0.3,0.9) 

         
    if(ban==0):
      glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
      es.draw_e5('C:/Users/LuisGutierrez/Documents/Lyn/blue_multiverso/machote/imagen/paisaje.jpg', 
            'C:/Users/LuisGutierrez/Documents/Lyn/blue_multiverso/machote/imagen/piso.jpg',
            'C:/Users/LuisGutierrez/Documents/Lyn/blue_multiverso/machote/imagen/cieloCiudad.jpg')
      glEnable(GL_DEPTH_TEST)
      glPushMatrix()
      glRotate(180,0,1,0)


      if ban4 == 1:
         glClearColor(0.0, 0.0, 0.0, 1.0)
         glEnable(GL_DEPTH_TEST)
         lc.phong(0.5,0.7,0.6)
         
      if ban4 == 2:
         glClearColor(0.0, 0.0, 0.0, 1.0)
         glEnable(GL_DEPTH_TEST)
         lc.gouraud(0.8,1,0.5)
      if ban4 == 3:
         glClearColor(0.0, 0.0, 0.0, 1.0)
         glEnable(GL_DEPTH_TEST)
         lc.interpolado(0.4,0.3,0.9)
      
      #muevo el personaje
      if keys[py.K_i]:
        draw(0,1)
      if keys[py.K_k]:
        draw(0,-1)
      if keys[py.K_l]:
        draw(-1,0)
      if keys[py.K_j]:
        draw(1,0)

      
      draw(0,0)
      if(rombo_collision(PosObj2_X, PosObj2_Y, PosObj2_Z,Obj2_width, Obj2_height,Obj2_depth,
      PosXob1, PosYob1, PosZob1,Obj1_height)):
        txt.draw_text("Colisión detectada",8,8,4,50,150,14,0,0,0,0)
      else:
        ##texto, px, py, pz, size, r g b rb gb bb
        txt.draw_text("Graficacion",8,8,4,50,150,14,0,0,0,0)  


      draw2()
      draw_cone (12,5,2,2,7,50)
      draw_mov(0,0)
      glPopMatrix()  
       

 
    if(ban==1):
      glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
      es.draw_e5('C:/Users/LuisGutierrez/Documents/Lyn/blue_multiverso/machote/imagen/esenario2.jpeg',
            'C:/Users/LuisGutierrez/Documents/Lyn/blue_multiverso/machote/imagen/piso.jpg',
            'C:/Users/LuisGutierrez/Documents/Lyn/blue_multiverso/machote/imagen/cielo.webp')
      glEnable(GL_DEPTH_TEST)
      glPushMatrix()
      glRotate(180,0,1,0)
      if ban4 == 1:
         glClearColor(0.0, 0.0, 0.0, 1.0)
         glEnable(GL_DEPTH_TEST)
         lc.phong(0.5,0.7,0.6)
         
      if ban4 == 2:
         glClearColor(0.0, 0.0, 0.0, 1.0)
         glEnable(GL_DEPTH_TEST)
         lc.gouraud(0.8,1,0.5)
      if ban4 == 3:
         glClearColor(0.0, 0.0, 0.0, 1.0)
         glEnable(GL_DEPTH_TEST)
         lc.interpolado(0.4,0.3,0.9)
      if keys[py.K_i]:
        draw_mov(0,1)
      if keys[py.K_k]:
        draw_mov(0,-1)
      if keys[py.K_l]:
        draw_mov(-1,0)
      if keys[py.K_j]:
        draw_mov(1,0)

      draw2()
      draw_cone (12,5,2,2,7,50)
      draw_mov(0,0)
      

      glPopMatrix() 
    
    if(ban==2):
      glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
      es.draw_e5('C:/Users/LuisGutierrez/Documents/Lyn/blue_multiverso/machote/imagen/biblioteca.jpeg',
            'C:/Users/LuisGutierrez/Documents/Lyn/blue_multiverso/machote/imagen/piso_cemento.jpg',
            'C:/Users/LuisGutierrez/Documents/Lyn/blue_multiverso/machote/imagen/cieloBiblioteca.jpg')
      glEnable(GL_DEPTH_TEST)
      glPushMatrix()
      glRotate(180,0,1,0)

      if ban4 == 1:
         glClearColor(0.0, 0.0, 0.0, 1.0)
         glEnable(GL_DEPTH_TEST)
         lc.phong(0.5,0.7,0.6)
         
      if ban4 == 2:
         glClearColor(0.0, 0.0, 0.0, 1.0)
         glEnable(GL_DEPTH_TEST)
         lc.gouraud(0.8,1,0.5)
      if ban4 == 3:
         glClearColor(0.0, 0.0, 0.0, 1.0)
         glEnable(GL_DEPTH_TEST)
         lc.interpolado(0.4,0.3,0.9)

      if keys[py.K_i]:
        draw_mov(0,1)
      if keys[py.K_k]:
        draw_mov(0,-1)
      if keys[py.K_l]:
        draw_mov(-1,0)
      if keys[py.K_j]:
        draw_mov(1,0)

      draw_mov(0,0)
      glPopMatrix() 

    if(ban==3):
      glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
      es.draw_e5('C:/Users/LuisGutierrez/Documents/Lyn/blue_multiverso/machote/imagen/biblioteca.jpeg',
            'C:/Users/LuisGutierrez/Documents/Lyn/blue_multiverso/machote/imagen/piso_cemento.jpg',
            'C:/Users/LuisGutierrez/Documents/Lyn/blue_multiverso/machote/imagen/cieloBiblioteca.jpg')
      glEnable(GL_DEPTH_TEST)
      glPushMatrix()
      glRotate(180,0,1,0)

      if ban4 == 1:
         glClearColor(0.0, 0.0, 0.0, 1.0)
         glEnable(GL_DEPTH_TEST)
         lc.phong(0.5,0.7,0.6)
         
      if ban4 == 2:
         glClearColor(0.0, 0.0, 0.0, 1.0)
         glEnable(GL_DEPTH_TEST)
         lc.gouraud(0.8,1,0.5)
      if ban4 == 3:
         glClearColor(0.0, 0.0, 0.0, 1.0)
         glEnable(GL_DEPTH_TEST)
         lc.interpolado(0.4,0.3,0.9)

      if keys[py.K_i]:
        draw_mov(0,1)
      if keys[py.K_k]:
        draw_mov(0,-1)
      if keys[py.K_l]:
        draw_mov(-1,0)
      if keys[py.K_j]:
        draw_mov(1,0)
      draw (0,0)
      draw2()
      draw_cone (12,5,2,2,7,50)
      draw_mov(0,0)

      glPopMatrix() 

    if(ban==4):
      glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
      es.draw_e5('C:/Users/LuisGutierrez/Documents/Lyn/blue_multiverso/machote/imagen/biblioteca.jpeg',
            'C:/Users/LuisGutierrez/Documents/Lyn/blue_multiverso/machote/imagen/piso_cemento.jpg',
            'C:/Users/LuisGutierrez/Documents/Lyn/blue_multiverso/machote/imagen/cieloBiblioteca.jpg')
      glEnable(GL_DEPTH_TEST)
      glPushMatrix()
      glRotate(180,0,1,0)

      if ban4 == 1:
         glClearColor(0.0, 0.0, 0.0, 1.0)
         glEnable(GL_DEPTH_TEST)
         lc.phong(0.5,0.7,0.6)
         
      if ban4 == 2:
         glClearColor(0.0, 0.0, 0.0, 1.0)
         glEnable(GL_DEPTH_TEST)
         lc.gouraud(0.8,1,0.5)
      if ban4 == 3:
         glClearColor(0.0, 0.0, 0.0, 1.0)
         glEnable(GL_DEPTH_TEST)
         lc.interpolado(0.4,0.3,0.9)

      if keys[py.K_i]:
        draw_mov(0,1)
      if keys[py.K_k]:
        draw_mov(0,-1)
      if keys[py.K_l]:
        draw_mov(-1,0)
      if keys[py.K_j]:
        draw_mov(1,0)

      draw (0,0)
      draw2()
      draw_cone (12,5,2,2,7,50)
      draw_mov(0,0)
      glPopMatrix() 
    
    #feliz
    if (ban2 == 1):
     glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
     if ban == 0:
        es.draw_e5('C:/Users/LuisGutierrez/Documents/Lyn/blue_multiverso/machote/imagen/cabana.jpg',
            'C:/Users/LuisGutierrez/Documents/Lyn/blue_multiverso/machote/imagen/piso_cemento.jpg',
            'C:/Users/LuisGutierrez/Documents/Lyn/blue_multiverso/machote/imagen/cieloCiudad.jpg')
     elif ban == 1:
        es.draw_e5('C:/Users/LuisGutierrez/Documents/Lyn/blue_multiverso/machote/imagen/naturalezaCabana.jpg',
            'C:/Users/LuisGutierrez/Documents/Lyn/blue_multiverso/machote/imagen/piso_cemento.jpg',
            'C:/Users/LuisGutierrez/Documents/Lyn/blue_multiverso/machote/imagen/cieloCiudad.jpg')
     elif ban == 2:
        es.draw_e5('C:/Users/LuisGutierrez/Documents/Lyn/blue_multiverso/machote/imagen/naturalezaCabana.jpg',
            'C:/Users/LuisGutierrez/Documents/Lyn/blue_multiverso/machote/imagen/piso_cemento.jpg',
            'C:/Users/LuisGutierrez/Documents/Lyn/blue_multiverso/machote/imagen/cieloCiudad.jpg')
     elif ban == 3:
        es.draw_e5('C:/Users/LuisGutierrez/Documents/Lyn/blue_multiverso/machote/imagen/naturalezaCabana2.jpg',
            'C:/Users/LuisGutierrez/Documents/Lyn/blue_multiverso/machote/imagen/piso_cemento.jpg',
            'C:/Users/LuisGutierrez/Documents/Lyn/blue_multiverso/machojjte/imagen/cieloCiudad.jpg')
     elif ban == 4:
        es.draw_e5('C:/Users/LuisGutierrez/Documents/Lyn/blue_multiverso/machote/imagen/naturalezaCabana.jpg',
            'C:/Users/LuisGutierrez/Documents/Lyn/blue_multiverso/machote/imagen/piso_cemento.jpg',
            'C:/Users/LuisGutierrez/Documents/Lyn/blue_multiverso/machote/imagen/cieloCiudad.jpg')
     if ban4 == 1:
         glClearColor(0.0, 0.0, 0.0, 1.0)
         glEnable(GL_DEPTH_TEST)
         lc.phong(0.5,0.7,0.6)
         
     if ban4 == 2:
         glClearColor(0.0, 0.0, 0.0, 1.0)
         glEnable(GL_DEPTH_TEST)
         lc.gouraud(0.8,1,0.5)
     if ban4 == 3:
         glClearColor(0.0, 0.0, 0.0, 1.0)
         glEnable(GL_DEPTH_TEST)
         lc.interpolado(0.4,0.3,0.9)
     glEnable(GL_DEPTH_TEST)
     glPushMatrix()
     glRotate(180,0,1,0)
     if keys[py.K_i]:
        draw_movhappy(0,1)
     if keys[py.K_k]:
        draw_movhappy(0,-1)
     if keys[py.K_l]:
        draw_movhappy(-1,0)
     if keys[py.K_j]:
        draw_movhappy(1,0)
     draw (0,0)
     draw2()
     draw_cone (12,5,2,2,7,50)
     draw_movhappy(0,0)
     glDisable(GL_LIGHTING)
     glDisable(GL_LIGHT0)
   
     glPopMatrix()


    #expresión_asco
    if (ban2 == 2):
     glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
     if ban == 0:
        es.draw_e5('C:/Users/LuisGutierrez/Documents/Lyn/blue_multiverso/machote/imagen/asco.jpg',
            'C:/Users/LuisGutierrez/Documents/Lyn/blue_multiverso/machote/imagen/piso_cemento.jpg',
            'C:/Users/LuisGutierrez/Documents/Lyn/blue_multiverso/machote/imagen/ascoCielo.jpg')
     elif ban == 1:
       es.draw_e5('C:/Users/LuisGutierrez/Documents/Lyn/blue_multiverso/machote/imagen/asco.jpg',
            'C:/Users/LuisGutierrez/Documents/Lyn/blue_multiverso/machote/imagen/piso_cemento.jpg',
            'C:/Users/LuisGutierrez/Documents/Lyn/blue_multiverso/machote/imagen/ascoCielo.jpg')
     elif ban == 2:
       es.draw_e5('C:/Users/LuisGutierrez/Documents/Lyn/blue_multiverso/machote/imagen/asco.jpg',
            'C:/Users/LuisGutierrez/Documents/Lyn/blue_multiverso/machote/imagen/piso_cemento.jpg',
            'C:/Users/LuisGutierrez/Documents/Lyn/blue_multiverso/machote/imagen/ascoCielo.jpg')
     elif ban == 3:
        es.draw_e5('C:/Users/LuisGutierrez/Documents/Lyn/blue_multiverso/machote/imagen/asco.jpg',
            'C:/Users/LuisGutierrez/Documents/Lyn/blue_multiverso/machote/imagen/piso_cemento.jpg',
            'C:/Users/LuisGutierrez/Documents/Lyn/blue_multiverso/machote/imagen/ascoCielo.jpg')
     elif ban == 4:
        es.draw_e5('C:/Users/LuisGutierrez/Documents/Lyn/blue_multiverso/machote/imagen/asco.jpg',
            'C:/Users/LuisGutierrez/Documents/Lyn/blue_multiverso/machote/imagen/piso_cemento.jpg',
            'C:/Users/LuisGutierrez/Documents/Lyn/blue_multiverso/machote/imagen/ascoCielo.jpg')
     
     if ban4 == 1:
         glClearColor(0.0, 0.0, 0.0, 1.0)
         glEnable(GL_DEPTH_TEST)
         lc.phong(0.5,0.7,0.6)
         
     if ban4 == 2:
         glClearColor(0.0, 0.0, 0.0, 1.0)
         glEnable(GL_DEPTH_TEST)
         lc.gouraud(0.8,1,0.5)
     if ban4 == 3:
         glClearColor(0.0, 0.0, 0.0, 1.0)
         glEnable(GL_DEPTH_TEST)
         lc.interpolado(0.4,0.3,0.9)

     glEnable(GL_DEPTH_TEST)
     glPushMatrix()
     glRotate(180,0,1,0)
     if keys[py.K_i]:
        draw_movasco(0,1)
     if keys[py.K_k]:
        draw_movasco(0,-1)
     if keys[py.K_l]:
        draw_movasco(-1,0)
     if keys[py.K_j]:
        draw_movasco(1,0)
     draw (0,0)
     draw2()
     draw_cone (12,5,2,2,7,50)
     draw_movasco(0,0)
     glDisable(GL_LIGHTING)
     glDisable(GL_LIGHT0)
   
     glPopMatrix()


 #expresión_asombro
    if (ban2 == 3):
     glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
     if ban == 0:
        es.draw_e5('C:/Users/LuisGutierrez/Documents/Lyn/blue_multiverso/machote/imagen/futurista.jpg',
            'C:/Users/LuisGutierrez/Documents/Lyn/blue_multiverso/machote/imagen/piso futurista.jpg',
            'C:/Users/LuisGutierrez/Documents/Lyn/blue_multiverso/machote/imagen/cieloFuturista.jpg')
     elif ban == 1:
        es.draw_e5('C:/Users/LuisGutierrez/Documents/Lyn/blue_multiverso/machote/imagen/futurista.jpg',
            'C:/Users/LuisGutierrez/Documents/Lyn/blue_multiverso/machote/imagen/piso futurista.jpg',
            'C:/Users/LuisGutierrez/Documents/Lyn/blue_multiverso/machote/imagen/cieloFuturista.jpg')
     elif ban == 2:
        es.draw_e5('C:/Users/LuisGutierrez/Documents/Lyn/blue_multiverso/machote/imagen/futurista.jpg',
            'C:/Users/LuisGutierrez/Documents/Lyn/blue_multiverso/machote/imagen/piso futurista.jpg',
            'C:/Users/LuisGutierrez/Documents/Lyn/blue_multiverso/machote/imagen/cieloFuturista.jpg')
     elif ban == 3:
        es.draw_e5('C:/Users/LuisGutierrez/Documents/Lyn/blue_multiverso/machote/imagen/futurista.jpg',
            'C:/Users/LuisGutierrez/Documents/Lyn/blue_multiverso/machote/imagen/piso futurista.jpg',
            'C:/Users/LuisGutierrez/Documents/Lyn/blue_multiverso/machote/imagen/cieloFuturista.jpg')
     elif ban == 4:
       es.draw_e5('C:/Users/LuisGutierrez/Documents/Lyn/blue_multiverso/machote/imagen/futurista.jpg',
            'C:/Users/LuisGutierrez/Documents/Lyn/blue_multiverso/machote/imagen/piso futurista.jpg',
            'C:/Users/LuisGutierrez/Documents/Lyn/blue_multiverso/machote/imagen/cieloFuturista.jpg')
     
     if ban4 == 1:
         glClearColor(0.0, 0.0, 0.0, 1.0)
         glEnable(GL_DEPTH_TEST)
         lc.phong(0.5,0.7,0.6)
         
     if ban4 == 2:
         glClearColor(0.0, 0.0, 0.0, 1.0)
         glEnable(GL_DEPTH_TEST)
         lc.gouraud(0.8,1,0.5)
     if ban4 == 3:
         glClearColor(0.0, 0.0, 0.0, 1.0)
         glEnable(GL_DEPTH_TEST)
         lc.interpolado(0.4,0.3,0.9)

     glEnable(GL_DEPTH_TEST)
     glPushMatrix()
     glRotate(180,0,1,0)
     if keys[py.K_i]:
        draw_movomg(0,1)
     if keys[py.K_k]:
        draw_movomg(0,-1)
     if keys[py.K_l]:
        draw_movomg(-1,0)
     if keys[py.K_j]:
        draw_movomg(1,0)
     draw (0,0)
     draw2()
     draw_cone (12,5,2,2,7,50)   
     draw_movomg(0,0)
     glDisable(GL_LIGHTING)
     glDisable(GL_LIGHT0)
   
     glPopMatrix()


    if (ban2 == 4):
     glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
     if ban == 0:
        es.draw_e5('C:/Users/LuisGutierrez/Documents/Lyn/blue_multiverso/machote/imagen/cementerio.jpg',
            'C:/Users/LuisGutierrez/Documents/Lyn/blue_multiverso/machote/imagen/cementerioLuna.jpg',
            'C:/Users/LuisGutierrez/Documents/Lyn/blue_multiverso/machote/imagen/cementerioCielo.jpg')
     elif ban == 1:
        es.draw_e5('C:/Users/LuisGutierrez/Documents/Lyn/blue_multiverso/machote/imagen/cementerio.jpg',
            'C:/Users/LuisGutierrez/Documents/Lyn/blue_multiverso/machote/imagen/cementerioLuna.jpg',
            'C:/Users/LuisGutierrez/Documents/Lyn/blue_multiverso/machote/imagen/cementerioCielo.jpg')
     elif ban == 2:
        es.draw_e5('C:/Users/LuisGutierrez/Documents/Lyn/blue_multiverso/machote/imagen/cementerio.jpg',
            'C:/Users/LuisGutierrez/Documents/Lyn/blue_multiverso/machote/imagen/cementerioLuna.jpg',
            'C:/Users/LuisGutierrez/Documents/Lyn/blue_multiverso/machote/imagen/cementerioCielo.jpg')
     elif ban == 3:
        es.draw_e5('C:/Users/LuisGutierrez/Documents/Lyn/blue_multiverso/machote/imagen/cementerio.jpg',
            'C:/Users/LuisGutierrez/Documents/Lyn/blue_multiverso/machote/imagen/cementerioLuna.jpg',
            'C:/Users/LuisGutierrez/Documents/Lyn/blue_multiverso/machote/imagen/cementerioCielo.jpg')
     elif ban == 4:
        es.draw_e5('C:/Users/LuisGutierrez/Documents/Lyn/blue_multiverso/machote/imagen/cementerio.jpg',
            'C:/Users/LuisGutierrez/Documents/Lyn/blue_multiverso/machote/imagen/cementerioLuna.jpg',
            'C:/Users/LuisGutierrez/Documents/Lyn/blue_multiverso/machote/imagen/cementerioCielo.jpg')
     
     if ban4 == 1:
         glClearColor(0.0, 0.0, 0.0, 1.0)
         glEnable(GL_DEPTH_TEST)
         lc.phong(0.5,0.7,0.6)
         
     if ban4 == 2:
         glClearColor(0.0, 0.0, 0.0, 1.0)
         glEnable(GL_DEPTH_TEST)
         lc.gouraud(0.8,1,0.5)
     if ban4 == 3:
         glClearColor(0.0, 0.0, 0.0, 1.0)
         glEnable(GL_DEPTH_TEST)
         lc.interpolado(0.4,0.3,0.9)

     glEnable(GL_DEPTH_TEST)
     glPushMatrix()
     glRotate(180,0,1,0)

     if keys[py.K_i]:
        draw_movsad(0,1)
     if keys[py.K_k]:
        draw_movsad(0,-1)
     if keys[py.K_l]:
        draw_movsad(-1,0)
     if keys[py.K_j]:
        draw_movsad(1,0)
     draw (0,0)
     draw2()
     draw_cone (12,5,2,2,7,50)  
     draw_movsad(0,0)
     glDisable(GL_LIGHTING)
     glDisable(GL_LIGHT0)
     glPopMatrix()


    #expresion de enojo
    if (ban2 == 5):
     glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
     if ban == 0:
        es.draw_e5('C:/Users/LuisGutierrez/Documents/Lyn/blue_multiverso/machote/imagen/cementerioLuna.jpg',
            'C:/Users/LuisGutierrez/Documents/Lyn/blue_multiverso/machote/imagen/cementerioCielo.jpg',
            'C:/Users/LuisGutierrez/Documents/Lyn/blue_multiverso/machote/imagen/piso.jpg')
     elif ban == 1:
        es.draw_e5('C:/Users/LuisGutierrez/Documents/Lyn/blue_multiverso/machote/imagen/cementerioLuna.jpg',
            'C:/Users/LuisGutierrez/Documents/Lyn/blue_multiverso/machote/imagen/cementerioCielo.jpg',
            'C:/Users/LuisGutierrez/Documents/Lyn/blue_multiverso/machote/imagen/piso.jpg')
     elif ban == 2:
        es.draw_e5('C:/Users/LuisGutierrez/Documents/Lyn/blue_multiverso/machote/imagen/cementerioLuna.jpg',
            'C:/Users/LuisGutierrez/Documents/Lyn/blue_multiverso/machote/imagen/cementerioCielo.jpg',
            'C:/Users/LuisGutierrez/Documents/Lyn/blue_multiverso/machote/imagen/piso.jpg')
     elif ban == 3:
       es.draw_e5('C:/Users/LuisGutierrez/Documents/Lyn/blue_multiverso/machote/imagen/cementerioLuna.jpg',
            'C:/Users/LuisGutierrez/Documents/Lyn/blue_multiverso/machote/imagen/cementerioCielo.jpg',
            'C:/Users/LuisGutierrez/Documents/Lyn/blue_multiverso/machote/imagen/piso.jpg')
     elif ban == 4:
        es.draw_e5('C:/Users/LuisGutierrez/Documents/Lyn/blue_multiverso/machote/imagen/bcementerioLuna.jpg',
            'C:/Users/LuisGutierrez/Documents/Lyn/blue_multiverso/machote/imagen/cementerioCielo.jpg',
            'C:/Users/LuisGutierrez/Documents/Lyn/blue_multiverso/machote/imagen/piso.jpg')
     if ban4 == 1:
         glClearColor(0.0, 0.0, 0.0, 1.0)
         glEnable(GL_DEPTH_TEST)
         lc.phong(0.5,0.7,0.6)
         
     if ban4 == 2:
         glClearColor(0.0, 0.0, 0.0, 1.0)
         glEnable(GL_DEPTH_TEST)
         lc.gouraud(0.8,1,0.5)
     if ban4 == 3:
         glClearColor(0.0, 0.0, 0.0, 1.0)
         glEnable(GL_DEPTH_TEST)
         lc.interpolado(0.4,0.3,0.9)

     glEnable(GL_DEPTH_TEST)
     glPushMatrix()
     glRotate(180,0,1,0)
     if keys[py.K_i]:
        draw_movEnojo(0,1)
     if keys[py.K_k]:
        draw_movEnojo(0,-1)
     if keys[py.K_l]:
        draw_movEnojo(-1,0)
     if keys[py.K_j]:
        draw_movEnojo(1,0)

     draw (0,0)
     draw2()
     draw_cone (12,5,2,2,7,50)
     draw_movEnojo(0,0)
     glDisable(GL_LIGHTING)
     glDisable(GL_LIGHT0)
     glPopMatrix()

   
 
    #original
    

    #movimientos-----------------------------------------
    #brazo derecho
    if (ban3 == 1):
     glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
     if ban == 0:
        es.draw_e5('C:/Users/LuisGutierrez/Documents/Lyn/blue_multiverso/machote/imagen/baile.jpg',
            'C:/Users/LuisGutierrez/Documents/Lyn/blue_multiverso/machote/imagen/baile2.jpg',
            'C:/Users/LuisGutierrez/Documents/Lyn/blue_multiverso/machote/imagen/pista.jpg')
     elif ban == 1:
        es.draw_e5('C:/Users/LuisGutierrez/Documents/Lyn/blue_multiverso/machote/imagen/baile.jpg',
            'C:/Users/LuisGutierrez/Documents/Lyn/blue_multiverso/machote/imagen/baile2.jpg',
            'C:/Users/LuisGutierrez/Documents/Lyn/blue_multiverso/machote/imagen/pista.jpg')
     elif ban == 2:
        es.draw_e5('C:/Users/LuisGutierrez/Documents/Lyn/blue_multiverso/machote/imagen/baile.jpg',
            'C:/Users/LuisGutierrez/Documents/Lyn/blue_multiverso/machote/imagen/baile2.jpg',
            'C:/Users/LuisGutierrez/Documents/Lyn/blue_multiverso/machote/imagen/pista.jpg')
     elif ban == 3:
       es.draw_e5('C:/Users/LuisGutierrez/Documents/Lyn/blue_multiverso/machote/imagen/baile.jpg',
            'C:/Users/LuisGutierrez/Documents/Lyn/blue_multiverso/machote/imagen/baile2.jpg',
            'C:/Users/LuisGutierrez/Documents/Lyn/blue_multiverso/machote/imagen/pista.jpg')
     elif ban == 4:
        es.draw_e5('C:/Users/LuisGutierrez/Documents/Lyn/blue_multiverso/machote/imagen/baile.jpg',
            'C:/Users/LuisGutierrez/Documents/Lyn/blue_multiverso/machote/imagen/baile2.jpg',
            'C:/Users/LuisGutierrez/Documents/Lyn/blue_multiverso/machote/imagen/pista.jpg')
     if ban4 == 1:
         glClearColor(0.0, 0.0, 0.0, 1.0)
         glEnable(GL_DEPTH_TEST)
         lc.phong(0.5,0.7,0.6)
         
     if ban4 == 2:
         glClearColor(0.0, 0.0, 0.0, 1.0)
         glEnable(GL_DEPTH_TEST)
         lc.gouraud(0.8,1,0.5)
     if ban4 == 3:
         glClearColor(0.0, 0.0, 0.0, 1.0)
         glEnable(GL_DEPTH_TEST)
         lc.interpolado(0.4,0.3,0.9)

     glEnable(GL_DEPTH_TEST)
     glPushMatrix()
     glRotate(180,0,1,0)
     if keys[py.K_i]:
        draw_mov_brazoD(0,1)
     if keys[py.K_k]:
        draw_mov_brazoD(0,-1)
     if keys[py.K_l]:
        draw_mov_brazoD(-1,0)
     if keys[py.K_j]:
        draw_mov_brazoD(1,0)
        
     draw_mov_brazoD(0,0)
     glDisable(GL_LIGHTING)
     glDisable(GL_LIGHT0)
     glPopMatrix()
     #brazo izquierdo
    if (ban3 == 2):
     glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
     if ban == 0:
        es.draw_e5('C:/Users/LuisGutierrez/Documents/Lyn/blue_multiverso/machote/imagen/baile.jpg',
            'C:/Users/LuisGutierrez/Documents/Lyn/blue_multiverso/machote/imagen/baile2.jpg',
            'C:/Users/LuisGutierrez/Documents/Lyn/blue_multiverso/machote/imagen/pista.jpg')
     elif ban == 1:
        es.draw_e5('C:/Users/LuisGutierrez/Documents/Lyn/blue_multiverso/machote/imagen/baile.jpg',
            'C:/Users/LuisGutierrez/Documents/Lyn/blue_multiverso/machote/imagen/baile2.jpg',
            'C:/Users/LuisGutierrez/Documents/Lyn/blue_multiverso/machote/imagen/pista.jpg')
     elif ban == 2:
        es.draw_e5('C:/Users/LuisGutierrez/Documents/Lyn/blue_multiverso/machote/imagen/baile.jpg',
            'C:/Users/LuisGutierrez/Documents/Lyn/blue_multiverso/machote/imagen/baile2.jpg',
            'C:/Users/LuisGutierrez/Documents/Lyn/blue_multiverso/machote/imagen/pista.jpg')
     elif ban == 3:
       es.draw_e5('C:/Users/LuisGutierrez/Documents/Lyn/blue_multiverso/machote/imagen/baile.jpg',
            'C:/Users/LuisGutierrez/Documents/Lyn/blue_multiverso/machote/imagen/baile2.jpg',
            'C:/Users/LuisGutierrez/Documents/Lyn/blue_multiverso/machote/imagen/pista.jpg')
     elif ban == 4:
        es.draw_e5('C:/Users/LuisGutierrez/Documents/Lyn/blue_multiverso/machote/imagen/baile.jpg',
            'C:/Users/LuisGutierrez/Documents/Lyn/blue_multiverso/machote/imagen/baile2.jpg',
            'C:/Users/LuisGutierrez/Documents/Lyn/blue_multiverso/machote/imagen/pista.jpg')
     if ban4 == 1:
         glClearColor(0.0, 0.0, 0.0, 1.0)
         glEnable(GL_DEPTH_TEST)
         lc.phong(0.5,0.7,0.6)
         
     if ban4 == 2:
         glClearColor(0.0, 0.0, 0.0, 1.0)
         glEnable(GL_DEPTH_TEST)
         lc.gouraud(0.8,1,0.5)
     if ban4 == 3:
         glClearColor(0.0, 0.0, 0.0, 1.0)
         glEnable(GL_DEPTH_TEST)
         lc.interpolado(0.4,0.3,0.9)

     glEnable(GL_DEPTH_TEST)
     glPushMatrix()
     glRotate(180,0,1,0)
     if keys[py.K_i]:
        draw_mov_brazoI(0,1)
     if keys[py.K_k]:
        draw_mov_brazoI(0,-1)
     if keys[py.K_l]:
        draw_mov_brazoI(-1,0)
     if keys[py.K_j]:
        draw_mov_brazoI(1,0)
        
     draw_mov_brazoI(0,0)
     glDisable(GL_LIGHTING)
     glDisable(GL_LIGHT0)
     glPopMatrix()


    if (ban3 == 3):
     glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
     if ban == 0:
        es.draw_e5('C:/Users/LuisGutierrez/Documents/Lyn/blue_multiverso/machote/imagen/baile.jpg',
            'C:/Users/LuisGutierrez/Documents/Lyn/blue_multiverso/machote/imagen/baile2.jpg',
            'C:/Users/LuisGutierrez/Documents/Lyn/blue_multiverso/machote/imagen/pista.jpg')
     elif ban == 1:
        es.draw_e5('C:/Users/LuisGutierrez/Documents/Lyn/blue_multiverso/machote/imagen/baile.jpg',
            'C:/Users/LuisGutierrez/Documents/Lyn/blue_multiverso/machote/imagen/baile2.jpg',
            'C:/Users/LuisGutierrez/Documents/Lyn/blue_multiverso/machote/imagen/pista.jpg')
     elif ban == 2:
        es.draw_e5('C:/Users/LuisGutierrez/Documents/Lyn/blue_multiverso/machote/imagen/baile.jpg',
            'C:/Users/LuisGutierrez/Documents/Lyn/blue_multiverso/machote/imagen/baile2.jpg',
            'C:/Users/LuisGutierrez/Documents/Lyn/blue_multiverso/machote/imagen/pista.jpg')
     elif ban == 3:
        es.draw_e5('C:/Users/LuisGutierrez/Documents/Lyn/blue_multiverso/machote/imagen/baile.jpg',
            'C:/Users/LuisGutierrez/Documents/Lyn/blue_multiverso/machote/imagen/baile2.jpg',
            'C:/Users/LuisGutierrez/Documents/Lyn/blue_multiverso/machote/imagen/pista.jpg')
     elif ban == 4:
        es.draw_e5('C:/Users/LuisGutierrez/Documents/Lyn/blue_multiverso/machote/imagen/baile.jpg',
            'C:/Users/LuisGutierrez/Documents/Lyn/blue_multiverso/machote/imagen/baile2.jpg',
            'C:/Users/LuisGutierrez/Documents/Lyn/blue_multiverso/machote/imagen/pista.jpg')
     
     if ban4 == 1:
         glClearColor(0.0, 0.0, 0.0, 1.0)
         glEnable(GL_DEPTH_TEST)
         lc.phong(0.5,0.7,0.6)
         
     if ban4 == 2:
         glClearColor(0.0, 0.0, 0.0, 1.0)
         glEnable(GL_DEPTH_TEST)
         lc.gouraud(0.8,1,0.5)
     if ban4 == 3:
         glClearColor(0.0, 0.0, 0.0, 1.0)
         glEnable(GL_DEPTH_TEST)
         lc.interpolado(0.4,0.3,0.9)

     glEnable(GL_DEPTH_TEST)
     glPushMatrix()
     glRotate(180,0,1,0)
     if keys[py.K_i]:
        draw_movPD(0,1)
     if keys[py.K_k]:
        draw_movPD(0,-1)
     if keys[py.K_l]:
        draw_movPD(-1,0)
     if keys[py.K_j]:
        draw_movPD(1,0)
        
     draw_movPD(0,0)
     glDisable(GL_LIGHTING)
     glDisable(GL_LIGHT0)
     glPopMatrix()
 
    if (ban3 == 4):
     glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
     if ban == 0:
        es.draw_e5('C:/Users/LuisGutierrez/Documents/Lyn/blue_multiverso/machote/imagen/naturalezaCabana2.jpg',
            'C:/Users/LuisGutierrez/Documents/Lyn/blue_multiverso/machote/imagen/piso_cemento.jpg',
            'C:/Users/LuisGutierrez/Documents/Lyn/blue_multiverso/machote/imagen/cieloCiudad.jpg')
     elif ban == 1:
        es.draw_e5('C:/Users/LuisGutierrez/Documents/Lyn/blue_multiverso/machote/imagen/naturalezaCabana2.jpg',
            'C:/Users/LuisGutierrez/Documents/Lyn/blue_multiverso/machote/imagen/piso_cemento.jpg',
            'C:/Users/LuisGutierrez/Documents/Lyn/blue_multiverso/machote/imagen/cieloCiudad.jpg')
     elif ban == 2:
        es.draw_e5('C:/Users/LuisGutierrez/Documents/Lyn/blue_multiverso/machote/imagen/naturalezaCabana2.jpg',
            'C:/Users/LuisGutierrez/Documents/Lyn/blue_multiverso/machote/imagen/piso_cemento.jpg',
            'C:/Users/LuisGutierrez/Documents/Lyn/blue_multiverso/machote/imagen/cieloCiudad.jpg')
     elif ban == 3:
        es.draw_e5('C:/Users/LuisGutierrez/Documents/Lyn/blue_multiverso/machote/imagen/naturalezaCabana2.jpg',
            'C:/Users/LuisGutierrez/Documents/Lyn/blue_multiverso/machote/imagen/piso_cemento.jpg',
            'C:/Users/LuisGutierrez/Documents/Lyn/blue_multiverso/machote/imagen/cieloCiudad.jpg')
     elif ban == 4:
        es.draw_e5('C:/Users/LuisGutierrez/Documents/Lyn/blue_multiverso/machote/imagen/naturalezaCabana2.jpg',
            'C:/Users/LuisGutierrez/Documents/Lyn/blue_multiverso/machote/imagen/piso_cemento.jpg',
            'C:/Users/LuisGutierrez/Documents/Lyn/blue_multiverso/machote/imagen/cieloCiudad.jpg')
     
     
     if ban4 == 1:
         glClearColor(0.0, 0.0, 0.0, 1.0)
         glEnable(GL_DEPTH_TEST)
         lc.phong(0.5,0.7,0.6)
         
     if ban4 == 2:
         glClearColor(0.0, 0.0, 0.0, 1.0)
         glEnable(GL_DEPTH_TEST)
         lc.gouraud(0.8,1,0.5)
     if ban4 == 3:
         glClearColor(0.0, 0.0, 0.0, 1.0)
         glEnable(GL_DEPTH_TEST)
         lc.interpolado(0.4,0.3,0.9)

     glEnable(GL_DEPTH_TEST)
     glPushMatrix()
     glRotate(180,0,1,0)
     if keys[py.K_i]:
        draw_movPI(0,1)
     if keys[py.K_k]:
        draw_movPI(0,-1)
     if keys[py.K_l]:
        draw_movPI(-1,0)
     if keys[py.K_j]:
        draw_movPI(1,0)
        
     draw_movPI(0,0)
     glDisable(GL_LIGHTING)
     glDisable(GL_LIGHT0)
     glPopMatrix()



    #cuello
    if (ban3 == 5):
     glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
     if ban == 0:
        es.draw_e5('C:/Users/LuisGutierrez/Documents/Lyn/blue_multiverso/machote/imagen/baile.jpg',
            'C:/Users/LuisGutierrez/Documents/Lyn/blue_multiverso/machote/imagen/baile2.jpg',
            'C:/Users/LuisGutierrez/Documents/Lyn/blue_multiverso/machote/imagen/ascoCielo.jpg')
     elif ban == 1:
        es.draw_e5('C:/Users/LuisGutierrez/Documents/Lyn/blue_multiverso/machote/imagen/baile.jpg',
            'C:/Users/LuisGutierrez/Documents/Lyn/blue_multiverso/machote/imagen/baile2.jpg',
            'C:/Users/LuisGutierrez/Documents/Lyn/blue_multiverso/machote/imagen/ascoCielo.jpg')
     elif ban == 2:
        es.draw_e5('C:/Users/LuisGutierrez/Documents/Lyn/blue_multiverso/machote/imagen/baile.jpg',
            'C:/Users/LuisGutierrez/Documents/Lyn/blue_multiverso/machote/imagen/baile2.jpg',
            'C:/Users/LuisGutierrez/Documents/Lyn/blue_multiverso/machote/imagen/ascoCielo.jpg')
     elif ban == 3:
        es.draw_e5('C:/Users/LuisGutierrez/Documents/Lyn/blue_multiverso/machote/imagen/baile.jpg',
            'C:/Users/LuisGutierrez/Documents/Lyn/blue_multiverso/machote/imagen/baile2.jpg',
            'C:/Users/LuisGutierrez/Documents/Lyn/blue_multiverso/machote/imagen/ascoCielo.jpg')
     elif ban == 4:
        es.draw_e5('C:/Users/LuisGutierrez/Documents/Lyn/blue_multiverso/machote/imagen/baile.jpg',
            'C:/Users/LuisGutierrez/Documents/Lyn/blue_multiverso/machote/imagen/baile2.jpg',
            'C:/Users/LuisGutierrez/Documents/Lyn/blue_multiverso/machote/imagen/ascoCielo.jpg')
     
     if ban4 == 1:
         glClearColor(0.0, 0.0, 0.0, 1.0)
         glEnable(GL_DEPTH_TEST)
         lc.phong(0.5,0.7,0.6)
         
     if ban4 == 2:
         glClearColor(0.0, 0.0, 0.0, 1.0)
         glEnable(GL_DEPTH_TEST)
         lc.gouraud(0.8,1,0.5)
     if ban4 == 3:
         glClearColor(0.0, 0.0, 0.0, 1.0)
         glEnable(GL_DEPTH_TEST)
         lc.interpolado(0.4,0.3,0.9)

     glEnable(GL_DEPTH_TEST)
     glPushMatrix()
     glRotate(180,0,1,0)
     if keys[py.K_i]:
        draw_movcuello(0,1)
     if keys[py.K_k]:
        draw_movcuello(0,-1)
     if keys[py.K_l]:
        draw_movcuello(-1,0)
     if keys[py.K_j]:
        draw_movcuello(1,0)
        
     draw_movcuello(0,0)
     glDisable(GL_LIGHTING)
     glDisable(GL_LIGHT0)
     glPopMatrix()
    

# Manejo del estado del menú o de otras interacciones fuera del bucle de transformaciones
    if(ban2 == 7):
     messagebox.showinfo("MENU", "EXPRESIONES: \n(e)->enojo\n(f)->feliz\n(t)->tristeza\n(o)->asombro\n(n)->asco\n\n\nCONTROL DE CAMARA:\n(W)->Adelante\n(S)->Atrás\n(A)->Izquierda\n(D)->Derecha\n(X)->Arriba\n(Z)->Abajo\n\n\n(0,1,2,3,4)->control de escenarios\n\n\nMOVIMIENTOS:\n(r)->original\n(I)->Arriba\n(K)->Abajo\n(J)->Izquierda\n(L)->Derecha\n(espacio)->Cuello\n('>')->Brazo derecho\n('<')->Brazo izquierdo\n(flecha hacia arriba)->pierna izquierda\n(flecha hacia abajo)->pierna derecha\n\n\nSONIDO:\n(P)->play\n(q)->stop\n\n\n(TAB)->info\n salir (ESC)")
     ban2 = 0

# Actualización de la pantalla
    py.display.flip()
    py.time.wait(100) 

