import pygame as py
from OpenGL.GLU import *
from OpenGL.GL import *
from OpenGL.GLUT import *
from pygame.locals import *
from PIL import *
import PersonajeLin.blue_multiverso.machote.escenarios as es
import PersonajeLin.blue_multiverso.machote.sonido as so
import tkinter.messagebox as messagebox 
import os
import PersonajeLin.blue_multiverso.machote.lucesNuev as lc
from PersonajeLin.blue_multiverso.machote.dibuja import *
from PersonajeLin.blue_multiverso.machote.colisiones import *
import PersonajeLin.blue_multiverso.machote.textos as txt
import PersonajeLin.blue_multiverso.machote.firguras as obj
from PersonajeLin.blue_multiverso.machote.firguras import *


class PersonajeLin:
   def __init__(self):
    py.init()
    py.mixer.init()
    self.running = True

    self.display = (800, 600)
    py.display.set_mode(self.display, DOUBLEBUF | OPENGL)

    gluPerspective(90, (self.display[0]/self.display[1]), 0.1, 50.0)
    glTranslatef(-1, -1, -5)
    glOrtho(0, 15, 0, 15, 0, 6)
    self.font_instrucciones = pygame.font.SysFont('Imprint MT Shadow', 25)
    self.camara_speed = 0.1
    self.rotacion_speed = 0.2
    self.mouse_sensivity = 0.1
    py.event.set_grab(True)
    py.mouse.set_visible(False)
    self.ban = 0
    self.directorio_script = os.path.dirname(os.path.abspath(__file__))

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
    self.Obj1_height = 1

    self.ban2=0
    self.ban3=0
    self.ban4=0

   def draw(self,movX, movY):
      self.PosXob1=self.PosXob1+movX
      self.PosYob1=self.PosYob1+movY
      glEnable(GL_DEPTH_TEST)
      glColor3f(0.5,1.0,1.0)
      glPushMatrix()
      glTranslatef(self.PosXob1,self.PosYob1,self.PosZob1)
      #lc.iluminacion(0.0,1.0,0.0)
      obj.draw_cube()
      glDisable(GL_LIGHTING)
      glDisable(GL_LIGHT0)
      glPopMatrix()


   def draw2(self):
      glEnable(GL_DEPTH_TEST)
      glColor3f(0.0,1.0,0.0)
      glPushMatrix()
      glTranslatef(self.PosObj2_X, self.PosObj2_Y, self.PosObj2_Z)
      lc.iluminacion(0.0, 0.0, 1.0)
      obj.draw_sphere(2, 40, 40)
      glDisable(GL_LIGHTING)
      glDisable(GL_LIGHT0)
      glPopMatrix()
   

   def dibuja_textos(self):
        glColor4f(2, 2, 2, 1)
        self.render_text_2d(self.display,"Teclas |M| - Acciones del Personaje\n|Esc| - Salir",10,40,self.font_instrucciones)
        

   def render_text_2d(self, display, text, x, y, font, line_height=18):
        lines = text.split('\n')  # Dividir el texto en líneas donde haya saltos de línea (\n)
        
        for i, line in enumerate(lines):
            text_surface = font.render(line, True, (0, 0, 0), None)  # Fondo transparente
            text_data = pygame.image.tostring(text_surface, "RGBA", True)
            text_width, text_height = text_surface.get_size()
            glEnable(GL_TEXTURE_2D)
            texture_id = glGenTextures(1)
            glBindTexture(GL_TEXTURE_2D, texture_id)
            glTexImage2D(GL_TEXTURE_2D, 0, GL_RGBA, text_width, text_height, 0, GL_RGBA, GL_UNSIGNED_BYTE, text_data)
            glTexParameterf(GL_TEXTURE_2D, GL_TEXTURE_MIN_FILTER, GL_LINEAR)
            glTexParameterf(GL_TEXTURE_2D, GL_TEXTURE_MAG_FILTER, GL_LINEAR)
            glEnable(GL_BLEND)
            glBlendFunc(GL_SRC_ALPHA, GL_ONE_MINUS_SRC_ALPHA)
            glMatrixMode(GL_PROJECTION)
            glPushMatrix()
            glLoadIdentity()
            glOrtho(0, display[0], 0, display[1], -1, 1)
            glMatrixMode(GL_MODELVIEW)
            glPushMatrix()
            glLoadIdentity()
            glBindTexture(GL_TEXTURE_2D, texture_id)
            glBegin(GL_QUADS)
            glTexCoord2f(0, 0); glVertex2f(x, y - i * line_height)  
            glTexCoord2f(1, 0); glVertex2f(x + text_width, y - i * line_height)
            glTexCoord2f(1, 1); glVertex2f(x + text_width, y + text_height - i * line_height)
            glTexCoord2f(0, 1); glVertex2f(x, y + text_height - i * line_height)
            glEnd()
            
          #  glDeleteTextures(int(texture_id))
            glPopMatrix()
            glMatrixMode(GL_PROJECTION)
            glPopMatrix()
            glMatrixMode(GL_MODELVIEW)
            glDisable(GL_BLEND)
            glDisable(GL_TEXTURE_2D)
   def run(self):
      while self.running :
         
         for event in py.event.get():
            if event.type == py.QUIT:
                  self.running = False
                  #menu
            if event.type == py.KEYDOWN:
                  if event.key==py.K_m:
                     self.ban2=7
                  #sonido_principal
                  if event.key == py.K_p:
                     so.play('PersonajeLin/blue_multiverso/machote/sonidos/guitarra.mp3')
                  if event.key == py.K_q:
                     so.stop()
                  if event.key==py.K_ESCAPE:
                     self.running = False
                  #escenarios
                  if event.key==py.K_0:
                     self.ban=0
                     
                  if event.key==py.K_1:
                     self.ban=1
                     
                  if event.key==py.K_2:
                     self.ban=2
                     
                  if event.key==py.K_3:
                     self.ban=3

                  if event.key==py.K_4:
                     self.ban=4
                  #expresiones
                  if event.key==py.K_f: #feliz
                     self.ban2=1
                     so.play('PersonajeLin/blue_multiverso/machote/sonidos/risaHombre.wav')
                  if event.key==py.K_n: #asco
                     self.ban2=2
                     so.play('PersonajeLin/blue_multiverso/machote/sonidos/yuck.wav')
                  if event.key==py.K_o: #asombrado
                     self.ban2=3
                     so.play('PersonajeLin/blue_multiverso/machote/sonidos/wow.wav')
                  if event.key==py.K_t: #triste
                     self.ban2=4
                     so.play('PersonajeLin/blue_multiverso/machote/sonidos/llora.mp3')
                  if event.key==py.K_e: #enojado
                     self.ban2=5
                     so.play('PersonajeLin/blue_multiverso/machote/sonidos/Enojado.wav')
                  if event.key==py.K_r: #original
                     self.ban2=6
                     self.ban3=6
                  #movimientos
                  if event.key==py.K_RIGHT: #brazo derecho
                     self.ban3=1
                     
                  if event.key==py.K_LEFT: #brazo izquierdo
                     self.ban3=2

                  if event.key==py.K_DOWN: #pierna derecha
                     self.ban3=3
                     
                  if event.key==py.K_UP: #pierna izquierda
                     self.ban3=4

                  if event.key==py.K_SPACE: #cuello
                     self.ban3=5
                  if event.key==py.K_9: 
                     self.ban4=1
                  if event.key==py.K_8: 
                     self.ban4=2
                  if event.key==py.K_7: 
                     self.ban4=3
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
         x *= self.mouse_sensivity
         y *= self.mouse_sensivity

         if x != 0 or y != 0:
            glRotatef(x, 0, 1, 0)
            glRotatef(y, 1, 0, 0)
         py.mouse.set_pos(self.display[0]//2,self.display[1]//2)

         if self.ban4 == 1:
               glClearColor(0.0, 0.0, 0.0, 1.0)
               glEnable(GL_DEPTH_TEST)
               lc.phong(0.5,0.7,0.6)
               
         if self.ban4 == 2:
               glClearColor(0.0, 0.0, 0.0, 1.0)
               glEnable(GL_DEPTH_TEST)
               lc.gouraud(0.8,1,0.5)
         if self.ban4 == 3:
               glClearColor(0.0, 0.0, 0.0, 1.0)
               glEnable(GL_DEPTH_TEST)
               lc.interpolado(0.4,0.3,0.9) 

               
         if(self.ban==0):
               glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
               es.draw_e5('PersonajeLin/blue_multiverso/machote/imagen/paisaje.jpg', 
                     'PersonajeLin/blue_multiverso/machote/imagen/piso.jpg',
                     'PersonajeLin/blue_multiverso/machote/imagen/cieloCiudad.jpg')
               glEnable(GL_DEPTH_TEST)
               glPushMatrix()
               glRotate(180,0,1,0)


               if self.ban4 == 1:
                  glClearColor(0.0, 0.0, 0.0, 1.0)
                  glEnable(GL_DEPTH_TEST)
                  lc.phong(0.5,0.7,0.6)
                  
               if self.ban4 == 2:
                  glClearColor(0.0, 0.0, 0.0, 1.0)
                  glEnable(GL_DEPTH_TEST)
                  lc.gouraud(0.8,1,0.5)
               if self.ban4 == 3:
                  glClearColor(0.0, 0.0, 0.0, 1.0)
                  glEnable(GL_DEPTH_TEST)
                  lc.interpolado(0.4,0.3,0.9)
               
               #muevo el personaje
               if keys[py.K_i]:
                  self.draw(0,1)
               if keys[py.K_k]:
                  self.draw(0,-1)
               if keys[py.K_l]:
                  self.draw(-1,0)
               if keys[py.K_j]:
                  self.draw(1,0)

               
               self.draw(0,0)
               if(rombo_collision(self.PosObj2_X, self.PosObj2_Y, self.PosObj2_Z,self.Obj2_width, self.Obj2_height,self.Obj2_depth,
               self.PosXob1, self.PosYob1, self.PosZob1,self.Obj1_height)):
                  txt.draw_text("Colisión detectada",8,8,4,50,150,14,0,0,0,0)
               else:
               ##texto, px, py, pz, size, r g b rb gb bb
                  txt.draw_text("Graficacion",8,8,4,50,150,14,0,0,0,0)  


               draw2()
               draw_cone (12,5,2,2,7,50)
               draw_mov(0,0)
               glPopMatrix()  
            

      
         if(self.ban==1):
                  glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
                  es.draw_e5('PersonajeLin/blue_multiverso/machote/imagen/biblioteca.jpg',
                        'PersonajeLin/blue_multiverso/machote/imagen/piso_cemento.jpg',
                        'PersonajeLin/blue_multiverso/machote/imagen/cieloBiblioteca.jpg')
                  glEnable(GL_DEPTH_TEST)
                  glPushMatrix()
                  glRotate(180,0,1,0)
                  if self.ban4 == 1:
                     glClearColor(0.0, 0.0, 0.0, 1.0)
                     glEnable(GL_DEPTH_TEST)
                     lc.phong(0.5,0.7,0.6)
                     
                  if self.ban4 == 2:
                     glClearColor(0.0, 0.0, 0.0, 1.0)
                     glEnable(GL_DEPTH_TEST)
                     lc.gouraud(0.8,1,0.5)
                  if self.ban4 == 3:
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
         
         if(self.ban==2):
               glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
               es.draw_e5('PersonajeLin/blue_multiverso/machote/imagen/biblioteca.jpg',
                     'PersonajeLin/blue_multiverso/machote/imagen/piso_cemento.jpg',
                     'PersonajeLin/blue_multiverso/machote/imagen/cieloBiblioteca.jpg')
               glEnable(GL_DEPTH_TEST)
               glPushMatrix()
               glRotate(180,0,1,0)

               if self.ban4 == 1:
                  glClearColor(0.0, 0.0, 0.0, 1.0)
                  glEnable(GL_DEPTH_TEST)
                  lc.phong(0.5,0.7,0.6)
                  
               if self.ban4 == 2:
                  glClearColor(0.0, 0.0, 0.0, 1.0)
                  glEnable(GL_DEPTH_TEST)
                  lc.gouraud(0.8,1,0.5)
               if self.ban4 == 3:
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

         if(self.ban==3):
               glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
               es.draw_e5('PersonajeLin/blue_multiverso/machote/imagen/biblioteca.jpg',
                     'PersonajeLin/blue_multiverso/machote/imagen/piso_cemento.jpg',
                     'PersonajeLin/blue_multiverso/machote/imagen/cieloBiblioteca.jpg')
               glEnable(GL_DEPTH_TEST)
               glPushMatrix()
               glRotate(180,0,1,0)

               if self.ban4 == 1:
                  glClearColor(0.0, 0.0, 0.0, 1.0)
                  glEnable(GL_DEPTH_TEST)
                  lc.phong(0.5,0.7,0.6)
                  
               if self.ban4 == 2:
                  glClearColor(0.0, 0.0, 0.0, 1.0)
                  glEnable(GL_DEPTH_TEST)
                  lc.gouraud(0.8,1,0.5)
               if self.ban4 == 3:
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

         if(self.ban==4):
                  glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
                  es.draw_e5('PersonajeLin/blue_multiverso/machote/imagen/biblioteca.jpg',
                        'PersonajeLin/blue_multiverso/machote/imagen/piso_cemento.jpg',
                        'PersonajeLin/blue_multiverso/machote/imagen/cieloBiblioteca.jpg')
                  glEnable(GL_DEPTH_TEST)
                  glPushMatrix()
                  glRotate(180,0,1,0)

                  if self.ban4 == 1:
                     glClearColor(0.0, 0.0, 0.0, 1.0)
                     glEnable(GL_DEPTH_TEST)
                     lc.phong(0.5,0.7,0.6)
                     
                  if self.ban4 == 2:
                     glClearColor(0.0, 0.0, 0.0, 1.0)
                     glEnable(GL_DEPTH_TEST)
                     lc.gouraud(0.8,1,0.5)
                  if self.ban4 == 3:
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

                  self.draw (0,0)
                  self.draw2()
                  draw_cone (12,5,2,2,7,50)
                  draw_mov(0,0)
                  glPopMatrix() 
            
         #feliz
         if (self.ban2 == 1):
            glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
            if self.ban == 0:
               es.draw_e5('PersonajeLin/blue_multiverso/machote/imagen/cabana.jpg',
                     'PersonajeLin/blue_multiverso/machote/imagen/piso_cemento.jpg',
                     'PersonajeLin/blue_multiverso/machote/imagen/cieloCiudad.jpg')
            elif self.ban == 1:
               es.draw_e5('PersonajeLin/blue_multiverso/machote/imagen/naturalezaCabana.jpg',
                     'PersonajeLin/blue_multiverso/machote/imagen/piso_cemento.jpg',
                     'PersonajeLin/blue_multiverso/machote/imagen/cieloCiudad.jpg')
            elif self.ban == 2:
               es.draw_e5('PersonajeLin/blue_multiverso/machote/imagen/naturalezaCabana.jpg',
                     'PersonajeLin/blue_multiverso/machote/imagen/piso_cemento.jpg',
                     'PersonajeLin/blue_multiverso/machote/imagen/cieloCiudad.jpg')
            elif self.ban == 3:
               es.draw_e5('PersonajeLin/blue_multiverso/machote/imagen/naturalezaCabana2.jpg',
                     'PersonajeLin/blue_multiverso/machote/imagen/piso_cemento.jpg',
                     'PersonajeLin/blue_multiverso/machote/imagen/cieloCiudad.jpg')
            elif self.ban == 4:
               es.draw_e5('PersonajeLin/blue_multiverso/machote/imagen/naturalezaCabana.jpg',
                     'PersonajeLin/blue_multiverso/machote/imagen/piso_cemento.jpg',
                     'PersonajeLin/blue_multiverso/machote/imagen/cieloCiudad.jpg')
            if self.ban4 == 1:
                  glClearColor(0.0, 0.0, 0.0, 1.0)
                  glEnable(GL_DEPTH_TEST)
                  lc.phong(0.5,0.7,0.6)
                  
            if self.ban4 == 2:
                  glClearColor(0.0, 0.0, 0.0, 1.0)
                  glEnable(GL_DEPTH_TEST)
                  lc.gouraud(0.8,1,0.5)
            if self.ban4 == 3:
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
            self.draw (0,0)
            self.draw2()
            draw_cone (12,5,2,2,7,50)
            draw_movhappy(0,0)
            glDisable(GL_LIGHTING)
            glDisable(GL_LIGHT0)
            
            glPopMatrix()


         #expresión_asco
         if (self.ban2 == 2):
            glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
            if self.ban == 0:
               es.draw_e5('PersonajeLin/blue_multiverso/machote/imagen/asco.jpg',
                     'PersonajeLin/blue_multiverso/machote/imagen/piso_cemento.jpg',
                     'PersonajeLin/blue_multiverso/machote/imagen/ascoCielo.jpg')
            elif self.ban == 1:
               es.draw_e5('PersonajeLin/blue_multiverso/machote/imagen/asco.jpg',
                     'PersonajeLin/blue_multiverso/machote/imagen/piso_cemento.jpg',
                     'PersonajeLin/blue_multiverso/machote/imagen/ascoCielo.jpg')
            elif self.ban == 2:
               es.draw_e5('PersonajeLin/blue_multiverso/machote/imagen/asco.jpg',
                     'PersonajeLin/blue_multiverso/machote/imagen/piso_cemento.jpg',
                     'PersonajeLin/blue_multiverso/machote/imagen/ascoCielo.jpg')
            elif self.ban == 3:
               es.draw_e5('PersonajeLin/blue_multiverso/machote/imagen/asco.jpg',
                     'PersonajeLin/blue_multiverso/machote/imagen/piso_cemento.jpg',
                     'PersonajeLin/blue_multiverso/machote/imagen/ascoCielo.jpg')
            elif self.ban == 4:
               es.draw_e5('PersonajeLin/blue_multiverso/machote/imagen/asco.jpg',
                     'PersonajeLin/blue_multiverso/machote/imagen/piso_cemento.jpg',
                     'PersonajeLin/blue_multiverso/machote/imagen/ascoCielo.jpg')
            
            if self.ban4 == 1:
                  glClearColor(0.0, 0.0, 0.0, 1.0)
                  glEnable(GL_DEPTH_TEST)
                  lc.phong(0.5,0.7,0.6)
                  
            if self.ban4 == 2:
                  glClearColor(0.0, 0.0, 0.0, 1.0)
                  glEnable(GL_DEPTH_TEST)
                  lc.gouraud(0.8,1,0.5)
            if self.ban4 == 3:
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
            self.draw (0,0)
            self.draw2()
            draw_cone (12,5,2,2,7,50)
            draw_movasco(0,0)
            glDisable(GL_LIGHTING)
            glDisable(GL_LIGHT0)
            
            glPopMatrix()


      #expresión_asombro
         if (self.ban2 == 3):
            glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
            if self.ban == 0:
               es.draw_e5('PersonajeLin/blue_multiverso/machote/imagen/futurista.jpg',
                     'PersonajeLin/blue_multiverso/machote/imagen/piso futurista.jpg',
                     'PersonajeLin/blue_multiverso/machote/imagen/cieloFuturista.jpg')
            elif self.ban == 1:
               es.draw_e5('PersonajeLin/blue_multiverso/machote/imagen/futurista.jpg',
                     'PersonajeLin/blue_multiverso/machote/imagen/piso futurista.jpg',
                     'PersonajeLin/blue_multiverso/machote/imagen/cieloFuturista.jpg')
            elif self.ban == 2:
               es.draw_e5('PersonajeLin/blue_multiverso/machote/imagen/futurista.jpg',
                     'PersonajeLin/blue_multiverso/machote/imagen/piso futurista.jpg',
                     'PersonajeLin/blue_multiverso/machote/imagen/cieloFuturista.jpg')
            elif self.ban == 3:
               es.draw_e5('PersonajeLin/blue_multiverso/machote/imagen/futurista.jpg',
                     'PersonajeLin/blue_multiverso/machote/imagen/piso futurista.jpg',
                     'PersonajeLin/blue_multiverso/machote/imagen/cieloFuturista.jpg')
            elif self.ban == 4:
               es.draw_e5('PersonajeLin/blue_multiverso/machote/imagen/futurista.jpg',
                     'PersonajeLin/blue_multiverso/machote/imagen/piso futurista.jpg',
                     'PersonajeLin/blue_multiverso/machote/imagen/cieloFuturista.jpg')
            
            if self.ban4 == 1:
                  glClearColor(0.0, 0.0, 0.0, 1.0)
                  glEnable(GL_DEPTH_TEST)
                  lc.phong(0.5,0.7,0.6)
                  
            if self.ban4 == 2:
                  glClearColor(0.0, 0.0, 0.0, 1.0)
                  glEnable(GL_DEPTH_TEST)
                  lc.gouraud(0.8,1,0.5)
            if self.ban4 == 3:
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
            self.draw (0,0)
            self.draw2()
            draw_cone (12,5,2,2,7,50)   
            draw_movomg(0,0)
            glDisable(GL_LIGHTING)
            glDisable(GL_LIGHT0)
            
            glPopMatrix()


         if (self.ban2 == 4):
            glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
            if self.ban == 0:
               es.draw_e5('PersonajeLin/blue_multiverso/machote/imagen/cementerio.jpg',
                     'PersonajeLin/blue_multiverso/machote/imagen/cementerioLuna.jpg',
                     'PersonajeLin/blue_multiverso/machote/imagen/cementerioCielo.jpg')
            elif self.ban == 1:
               es.draw_e5('PersonajeLin/blue_multiverso/machote/imagen/cementerio.jpg',
                     'PersonajeLin/blue_multiverso/machote/imagen/cementerioLuna.jpg',
                     'PersonajeLin/blue_multiverso/machote/imagen/cementerioCielo.jpg')
            elif self.ban == 2:
               es.draw_e5('PersonajeLin/blue_multiverso/machote/imagen/cementerio.jpg',
                     'PersonajeLin/blue_multiverso/machote/imagen/cementerioLuna.jpg',
                     'PersonajeLin/blue_multiverso/machote/imagen/cementerioCielo.jpg')
            elif self.ban == 3:
               es.draw_e5('PersonajeLin/blue_multiverso/machote/imagen/cementerio.jpg',
                     'PersonajeLin/blue_multiverso/machote/imagen/cementerioLuna.jpg',
                     'PersonajeLin/blue_multiverso/machote/imagen/cementerioCielo.jpg')
            elif self.ban == 4:
               es.draw_e5('PersonajeLin/blue_multiverso/machote/imagen/cementerio.jpg',
                     'PersonajeLin/blue_multiverso/machote/imagen/cementerioLuna.jpg',
                     'PersonajeLin/blue_multiverso/machote/imagen/cementerioCielo.jpg')
         
            if self.ban4 == 1:
                  glClearColor(0.0, 0.0, 0.0, 1.0)
                  glEnable(GL_DEPTH_TEST)
                  lc.phong(0.5,0.7,0.6)
                  
            if self.ban4 == 2:
                  glClearColor(0.0, 0.0, 0.0, 1.0)
                  glEnable(GL_DEPTH_TEST)
                  lc.gouraud(0.8,1,0.5)
            if self.ban4 == 3:
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
            self.draw (0,0)
            self.draw2()
            draw_cone (12,5,2,2,7,50)  
            draw_movsad(0,0)
            glDisable(GL_LIGHTING)
            glDisable(GL_LIGHT0)
            glPopMatrix()


         #expresion de enojo
         if (self.ban2 == 5):
            glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
            if self.ban == 0:
               es.draw_e5('PersonajeLin/blue_multiverso/machote/imagen/cementerioLuna.jpg',
                     'PersonajeLin/blue_multiverso/machote/imagen/cementerioCielo.jpg',
                     'PersonajeLin/blue_multiverso/machote/imagen/piso.jpg')
            elif self.ban == 1:
               es.draw_e5('PersonajeLin/blue_multiverso/machote/imagen/cementerioLuna.jpg',
                     'PersonajeLin/blue_multiverso/machote/imagen/cementerioCielo.jpg',
                     'PersonajeLin/blue_multiverso/machote/imagen/piso.jpg')
            elif self.ban == 2:
               es.draw_e5('PersonajeLin/blue_multiverso/machote/imagen/cementerioLuna.jpg',
                     'PersonajeLin/blue_multiverso/machote/imagen/cementerioCielo.jpg',
                     'PersonajeLin/blue_multiverso/machote/imagen/piso.jpg')
            elif self.ban == 3:
               es.draw_e5('PersonajeLin/blue_multiverso/machote/imagen/cementerioLuna.jpg',
                     'PersonajeLin/blue_multiverso/machote/imagen/cementerioCielo.jpg',
                     'PersonajeLin/blue_multiverso/machote/imagen/piso.jpg')
            elif self.ban == 4:
               es.draw_e5('PersonajeLin/blue_multiverso/machote/imagen/cementerioLuna.jpg',
                     'PersonajeLin/blue_multiverso/machote/imagen/cementerioCielo.jpg',
                     'PersonajeLin/blue_multiverso/machote/imagen/piso.jpg')
            if self.ban4 == 1:
                  glClearColor(0.0, 0.0, 0.0, 1.0)
                  glEnable(GL_DEPTH_TEST)
                  lc.phong(0.5,0.7,0.6)
                  
            if self.ban4 == 2:
                  glClearColor(0.0, 0.0, 0.0, 1.0)
                  glEnable(GL_DEPTH_TEST)
                  lc.gouraud(0.8,1,0.5)
            if self.ban4 == 3:
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

            self.draw (0,0)
            self.draw2()
            draw_cone (12,5,2,2,7,50)
            draw_movEnojo(0,0)
            glDisable(GL_LIGHTING)
            glDisable(GL_LIGHT0)
            glPopMatrix()

         
      
         #original
         

         #movimientos-----------------------------------------
         #brazo derecho
         if (self.ban3 == 1):
            glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
            if self.ban == 0:
               es.draw_e5('PersonajeLin/blue_multiverso/machote/imagen/baile.jpg',
                     'PersonajeLin/blue_multiverso/machote/imagen/baile2.jpg',
                     'PersonajeLin/blue_multiverso/machote/imagen/pista.jpg')
            elif self.ban == 1:
               es.draw_e5('PersonajeLin/blue_multiverso/machote/imagen/baile.jpg',
                     'PersonajeLin/blue_multiverso/machote/imagen/baile2.jpg',
                     'PersonajeLin/blue_multiverso/machote/imagen/pista.jpg')
            elif self.ban == 2:
               es.draw_e5('PersonajeLin/blue_multiverso/machote/imagen/baile.jpg',
                     'PersonajeLin/blue_multiverso/machote/imagen/baile2.jpg',
                     'PersonajeLin/blue_multiverso/machote/imagen/pista.jpg')
            elif self.ban == 3:
               es.draw_e5('PersonajeLin/blue_multiverso/machote/imagen/baile.jpg',
                     'PersonajeLin/blue_multiverso/machote/imagen/baile2.jpg',
                     'PersonajeLin/blue_multiverso/machote/imagen/pista.jpg')
            elif self.ban == 4:
               es.draw_e5('PersonajeLin/blue_multiverso/machote/imagen/baile.jpg',
                     'PersonajeLin/blue_multiverso/machote/imagen/baile2.jpg',
                     'PersonajeLin/blue_multiverso/machote/imagen/pista.jpg')
            if self.ban4 == 1:
                  glClearColor(0.0, 0.0, 0.0, 1.0)
                  glEnable(GL_DEPTH_TEST)
                  lc.phong(0.5,0.7,0.6)
                  
            if self.ban4 == 2:
                  glClearColor(0.0, 0.0, 0.0, 1.0)
                  glEnable(GL_DEPTH_TEST)
                  lc.gouraud(0.8,1,0.5)
            if self.ban4 == 3:
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
         if (self.ban3 == 2):
            glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
            if self.ban == 0:
               es.draw_e5('PersonajeLin/blue_multiverso/machote/imagen/baile.jpg',
                     'PersonajeLin/blue_multiverso/machote/imagen/baile2.jpg',
                     'PersonajeLin/blue_multiverso/machote/imagen/pista.jpg')
            elif self.ban == 1:
               es.draw_e5('PersonajeLin/blue_multiverso/machote/imagen/baile.jpg',
                     'PersonajeLin/blue_multiverso/machote/imagen/baile2.jpg',
                     'PersonajeLin/blue_multiverso/machote/imagen/pista.jpg')
            elif self.ban == 2:
               es.draw_e5('PersonajeLin/blue_multiverso/machote/imagen/baile.jpg',
                     'PersonajeLin/blue_multiverso/machote/imagen/baile2.jpg',
                     'PersonajeLin/blue_multiverso/machote/imagen/pista.jpg')
            elif self.ban == 3:
               es.draw_e5('PersonajeLin/blue_multiverso/machote/imagen/baile.jpg',
                     'PersonajeLin/blue_multiverso/machote/imagen/baile2.jpg',
                     'PersonajeLin/blue_multiverso/machote/imagen/pista.jpg')
            elif self.ban == 4:
               es.draw_e5('PersonajeLin/blue_multiverso/machote/imagen/baile.jpg',
                     'PersonajeLin/blue_multiverso/machote/imagen/baile2.jpg',
                     'PersonajeLin/blue_multiverso/machote/imagen/pista.jpg')
            if self.ban4 == 1:
                  glClearColor(0.0, 0.0, 0.0, 1.0)
                  glEnable(GL_DEPTH_TEST)
                  lc.phong(0.5,0.7,0.6)
                  
            if self.ban4 == 2:
                  glClearColor(0.0, 0.0, 0.0, 1.0)
                  glEnable(GL_DEPTH_TEST)
                  lc.gouraud(0.8,1,0.5)
            if self.ban4 == 3:
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


         if (self.ban3 == 3):
            glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
            if self.ban == 0:
               es.draw_e5('PersonajeLin/blue_multiverso/machote/imagen/baile.jpg',
                     'PersonajeLin/blue_multiverso/machote/imagen/baile2.jpg',
                     'PersonajeLin/blue_multiverso/machote/imagen/pista.jpg')
            elif self.ban == 1:
               es.draw_e5('PersonajeLin/blue_multiverso/machote/imagen/baile.jpg',
                     'PersonajeLin/blue_multiverso/machote/imagen/baile2.jpg',
                     'PersonajeLin/blue_multiverso/machote/imagen/pista.jpg')
            elif self.ban == 2:
               es.draw_e5('PersonajeLin/blue_multiverso/machote/imagen/baile.jpg',
                     'PersonajeLin/blue_multiverso/machote/imagen/baile2.jpg',
                     'PersonajeLin/blue_multiverso/machote/imagen/pista.jpg')
            elif self.ban == 3:
               es.draw_e5('PersonajeLin/blue_multiverso/machote/imagen/baile.jpg',
                     'PersonajeLin/blue_multiverso/machote/imagen/baile2.jpg',
                     'PersonajeLin/blue_multiverso/machote/imagen/pista.jpg')
            elif self.ban == 4:
               es.draw_e5('PersonajeLin/blue_multiverso/machote/imagen/baile.jpg',
                     'PersonajeLin/blue_multiverso/machote/imagen/baile2.jpg',
                     'PersonajeLin/blue_multiverso/machote/imagen/pista.jpg')
            
            if self.ban4 == 1:
                  glClearColor(0.0, 0.0, 0.0, 1.0)
                  glEnable(GL_DEPTH_TEST)
                  lc.phong(0.5,0.7,0.6)
                  
            if self.ban4 == 2:
                  glClearColor(0.0, 0.0, 0.0, 1.0)
                  glEnable(GL_DEPTH_TEST)
                  lc.gouraud(0.8,1,0.5)
            if self.ban4 == 3:
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
      
         if (self.ban3 == 4):
            glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
            if self.ban == 0:
               es.draw_e5('PersonajeLin/blue_multiverso/machote/imagen/naturalezaCabana2.jpg',
                     'PersonajeLin/blue_multiverso/machote/imagen/piso_cemento.jpg',
                     'PersonajeLin/blue_multiverso/machote/imagen/cieloCiudad.jpg')
            elif self.ban == 1:
               es.draw_e5('PersonajeLin/blue_multiverso/machote/imagen/naturalezaCabana2.jpg',
                     'PersonajeLin/blue_multiverso/machote/imagen/piso_cemento.jpg',
                     'PersonajeLin/blue_multiverso/machote/imagen/cieloCiudad.jpg')
            elif self.ban == 2:
               es.draw_e5('PersonajeLin/blue_multiverso/machote/imagen/naturalezaCabana2.jpg',
                     'PersonajeLin/blue_multiverso/machote/imagen/piso_cemento.jpg',
                     'PersonajeLin/blue_multiverso/machote/imagen/cieloCiudad.jpg')
            elif self.ban == 3:
               es.draw_e5('PersonajeLin/blue_multiverso/machote/imagen/naturalezaCabana2.jpg',
                     'PersonajeLin/blue_multiverso/machote/imagen/piso_cemento.jpg',
                     'PersonajeLin/blue_multiverso/machote/imagen/cieloCiudad.jpg')
            elif self.ban == 4:
               es.draw_e5('PersonajeLin/blue_multiverso/machote/imagen/naturalezaCabana2.jpg',
                     'PersonajeLin/blue_multiverso/machote/imagen/piso_cemento.jpg',
                     'PersonajeLin/blue_multiverso/machote/imagen/cieloCiudad.jpg')
            
            
            if self.ban4 == 1:
                  glClearColor(0.0, 0.0, 0.0, 1.0)
                  glEnable(GL_DEPTH_TEST)
                  lc.phong(0.5,0.7,0.6)
                  
            if self.ban4 == 2:
                  glClearColor(0.0, 0.0, 0.0, 1.0)
                  glEnable(GL_DEPTH_TEST)
                  lc.gouraud(0.8,1,0.5)
            if self.ban4 == 3:
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
         if (self.ban3 == 5):
            glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
            if self.ban == 0:
               es.draw_e5('PersonajeLin/blue_multiverso/machote/imagen/baile.jpg',
                     'PersonajeLin/blue_multiverso/machote/imagen/baile2.jpg',
                     'PersonajeLin/blue_multiverso/machote/imagen/ascoCielo.jpg')
            elif self.ban == 1:
               es.draw_e5('PersonajeLin/blue_multiverso/machote/imagen/baile.jpg',
                     'PersonajeLin/blue_multiverso/machote/imagen/baile2.jpg',
                     'PersonajeLin/blue_multiverso/machote/imagen/ascoCielo.jpg')
            elif self.ban == 2:
               es.draw_e5('PersonajeLin/blue_multiverso/machote/imagen/baile.jpg',
                     'PersonajeLin/blue_multiverso/machote/imagen/baile2.jpg',
                     'PersonajeLin/blue_multiverso/machote/imagen/ascoCielo.jpg')
            elif self.ban == 3:
               es.draw_e5('PersonajeLin/blue_multiverso/machote/imagen/baile.jpg',
                     'PersonajeLin/blue_multiverso/machote/imagen/baile2.jpg',
                     'PersonajeLin/blue_multiverso/machote/imagen/ascoCielo.jpg')
            elif self.ban == 4:
               es.draw_e5('PersonajeLin/blue_multiverso/machote/imagen/baile.jpg',
                     'PersonajeLin/blue_multiverso/machote/imagen/baile2.jpg',
                     'PersonajeLin/blue_multiverso/machote/imagen/ascoCielo.jpg')
            
            if self.ban4 == 1:
                  glClearColor(0.0, 0.0, 0.0, 1.0)
                  glEnable(GL_DEPTH_TEST)
                  lc.phong(0.5,0.7,0.6)
                  
            if self.ban4 == 2:
                  glClearColor(0.0, 0.0, 0.0, 1.0)
                  glEnable(GL_DEPTH_TEST)
                  lc.gouraud(0.8,1,0.5)
            if self.ban4 == 3:
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
         if(self.ban2 == 7):
            messagebox.showinfo("MENU", "EXPRESIONES: \n(e)->enojo\n(f)->feliz\n(t)->tristeza\n(o)->asombro\n(n)->asco\n\n\nCONTROL DE CAMARA:\n(W)->Adelante\n(S)->Atrás\n(A)->Izquierda\n(D)->Derecha\n(X)->Arriba\n(Z)->Abajo\n\n\n(0,1,2,3,4)->control de escenarios\n\n\nMOVIMIENTOS:\n(r)->original\n(I)->Arriba\n(K)->Abajo\n(J)->Izquierda\n(L)->Derecha\n(espacio)->Cuello\n('>')->Brazo derecho\n('<')->Brazo izquierdo\n(flecha hacia arriba)->pierna izquierda\n(flecha hacia abajo)->pierna derecha\n\n\nSONIDO:\n(P)->play\n(q)->stop\n\n\n(TAB)->info\n salir (ESC)")
            self.ban2 = 0
         self.dibuja_textos()
      # Actualización de la pantalla
         py.display.flip()
         py.time.wait(100) 

      pygame.display.quit() 

