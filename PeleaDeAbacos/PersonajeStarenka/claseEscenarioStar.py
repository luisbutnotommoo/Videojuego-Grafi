import pygame
from OpenGL.GLU import*
from OpenGL.GL import*
from OpenGL.GLUT import*
from pygame.locals import*
from PIL import*
from PersonajeStarenka.Acciones2S import escenario as es
from PersonajeStarenka.Acciones2S import sonido as son
from PersonajeStarenka.Acciones2S import boceto as b
from PersonajeStarenka.Acciones2S import textos as txt
from PersonajeStarenka.Acciones2S import objetosColisiones as oC
from PersonajeStarenka.Acciones2S import iluminacion as lc
from PersonajeStarenka.Acciones2S import colisiones as coli
from PersonajeStarenka.Acciones2S.iluminacionFinal import iluminacion



#Inicialización


class PersonajeStarenka:
    def __init__(self):
        self.bandera = 0
        self.bandera1 = 0
        self.bandera2 = 0
        self.instruccion = True
        self.acercaDe = False
        self.activarColi = False
        self.valoresIniciales()
        self.camara_speed = 0.1
        self.rotation_speed = 0.2
        self.mouse_sesivity = 0.1
        self.lcFin=iluminacion()
        self.inicializarCosas()
        self.ventanaInicial()
        self.textura1=es.load_texture('PersonajeStarenka/Imagenes2S/descarga_resized_op.jpeg')
        self.textura2=es.load_texture('PersonajeStarenka/Imagenes2S/fondo5.jpg')
        self.textura3=es.load_texture('PersonajeStarenka/Imagenes2S/fondo4.jpg')
        self.textura4=es.load_texture('PersonajeStarenka/Imagenes2S/fondo2.jpg')
        self.textura5=es.load_texture('PersonajeStarenka/Imagenes2S/fondo3.jpg')
        self.textura6=es.load_texture('PersonajeStarenka/Imagenes2S/fondo6.jpg')
        self.textura7=es.load_texture('PersonajeStarenka/Imagenes2S/fondo7.jpg')
        self.textura8=es.load_texture('PersonajeStarenka/Imagenes2S/fondo8.jpg')

    def inicializarCosas(self):
        pygame.init()
        pygame.mixer.init()
        self.display = (800, 600)
        pygame.display.set_mode(self.display, DOUBLEBUF | OPENGL)
        pygame.event.set_grab(True)  
        pygame.mouse.set_visible(False)

    def valoresIniciales(self):
        self.PosXPelota, self.PosYPelota, self.PosZPelota = 10, 17, 0
        self.Obj1_height = 1
        self.PosXCabeza, self.PosYCabeza, self.PosZCabeza = 0.9, 17, 0
        self.Cabeza_Height, self.Cabeza_width, self.Cabeza_depth = 7.5, 7.5, 7.5
        self.PosXCorazon, self.PosYCorazon, self.PosZCorazon = -8, 8, 0
        self.PosXTorso, self.PosYTorso, self.PosZTorso = -8, 4, 0
        self.Torso_Height, self.Torso_width, self.Torso_depth = 2, 2, 2
        self.PosXHamburguesa, self.PosYHamburguesa, self.PosZHamburguesa = 10, 17, 0
        self.PosXBola, self.PosYBola, self.PosZBola = 10, 17, 0

    def ventanaInicial(self):
        gluPerspective(60, (self.display[0] / self.display[1]), 0.1, 50.0)
        glTranslatef(0, 0, -5)  # Ajuste de cámara inicial para ver los objetos
        glOrtho(0, 30, 0, 30, 0, 6)

    def pelota(self,movX,movY): 
        self.PosXPelota=self.PosXPelota+movX
        self.PosYPelota=self.PosYPelota+movY
        glEnable(GL_DEPTH_TEST)
        glPushMatrix()
        glTranslatef(self.PosXPelota,self.PosYPelota,self.PosZPelota)
        lc.iluminacion()
        oC.BolaDisco('PersonajeStarenka/Imagenes2S/pelota.jpg',2,40,40)
        glDisable(GL_LIGHTING)
        glDisable(GL_LIGHT0)
        glPopMatrix()
        
    def Hamburguesa(self,movX,movY): 
        self.PosXHamburguesa=self.PosXHamburguesa+movX
        self.PosYHamburguesa=self.PosYHamburguesa+movY
        glEnable(GL_DEPTH_TEST)
        glPushMatrix()
        glTranslatef(self.PosXHamburguesa,self.PosYHamburguesa,self.PosZHamburguesa)
        oC.BolaDisco('PersonajeStarenka/Imagenes2S/hamburguesa.png',2,40,40)
        glPopMatrix()

    def bolaDisco(self,movX,movY): 
        self.PosXBola=self.PosXBola+movX
        self.PosYBola=self.PosYBola+movY
        glEnable(GL_DEPTH_TEST)
        glPushMatrix()
        glTranslatef(self.PosXBola,self.PosYBola,self.PosZBola)
        oC.BolaDisco('PersonajeStarenka/Imagenes2S/disco.jpg',2,40,40)
        glPopMatrix()

    def corazon(self,movX2, movY2):
        self.PosXCorazon=self.PosXCorazon+movX2
        self.PosYCorazon=self.PosYCorazon+movY2
        glEnable(GL_DEPTH_TEST)
        glPushMatrix()
        glTranslatef(self.PosXCorazon,self.PosYCorazon,self.PosZCorazon)
        lc.iluminacion()
        glColor3f(1,0,0)
        oC.corazon()
        glDisable(GL_LIGHTING)
        glDisable(GL_LIGHT0)
        glPopMatrix()

    def run (self):
        running=True
        while running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    quit()
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_p:  
                     son.sonido('PersonajeStarenka/Sonido2S/sonidoFijo.wav')

                    if event.key == pygame.K_o:
                        son.stopsonido()
                    
                    if event.key==pygame.K_ESCAPE:
                        running=False
                    if event.key==pygame.K_2:
                        son.stopsonido()
                        self.bandera=1
                        son.sonido('PersonajeStarenka/Sonido2S/sonido1.wav')
                    if event.key==pygame.K_1:
                        self.bandera=0
                    if event.key==pygame.K_3:
                        son.stopsonido()
                        self.bandera=2
                        son.sonido('PersonajeStarenka/Sonido2S/sonido2.wav')
                    if event.key==pygame.K_4:
                        son.stopsonido()
                        self.bandera=3
                        son.sonido('PersonajeStarenka/Sonido2S/sonido3.wav')
                    if event.key==pygame.K_5:
                        son.stopsonido()
                        self.bandera=4
                        son.sonido('PersonajeStarenka/Sonido2S/sonido4.wav')
                    if event.key==pygame.K_6:
                        son.stopsonido()
                        self.bandera=5
                        son.sonido('PersonajeStarenka/Sonido2S/sonido5.wav')
                    ##Feliz
                    if event.key==pygame.K_7:
                        son.stopsonido()
                        self.bandera=6
                        son.sonido('PersonajeStarenka/Sonido2S/sonido6.wav')
                    #Triste
                    if event.key==pygame.K_8:
                        son.stopsonido()
                        self.bandera=7
                        son.sonido('PersonajeStarenka/Sonido2S/sonido7.wav')
                    #Mover brazos
                    if event.key==pygame.K_9:
                        self.bandera=8
                    #Caminar
                    if event.key==pygame.K_0:
                        self.bandera=9
                    #Mover brazos 2
                    if event.key==pygame.K_z:
                        self.bandera=10
                    #Mover cabeza
                    if event.key==pygame.K_x:
                        self.bandera=11
                    #Saltar
                    if event.key==pygame.K_c:
                        self.bandera=12
                    #Salto split
                    if event.key==pygame.K_v:
                        self.bandera=13
                    #Caer
                    if event.key==pygame.K_b:
                        self.bandera=14
                    #Colisiones
                    if event.key==pygame.K_n :
                        self.bandera=15
                        self.activarColi=not self.activarColi
                    #Instrucciones
                    if event.key==pygame.K_i:
                        self.instruccion = not self.instruccion
                    #Acerca de
                    if event.key==pygame.K_u:
                        self.acercaDe=not self.acercaDe
                    #Iluminación Phong
                    if event.key==pygame.K_h:
                        self.bandera2=1
                    #Iluminacion Gouraud
                    if event.key==pygame.K_j:
                        self.bandera2=2
                    #Iluminacion Interpolado
                    if event.key==pygame.K_k:
                        self.bandera2=3
                    #Iluminacion desactivada
                    if event.key==pygame.K_l:
                        self.bandera2=0
                    
            
            
                keys = pygame.key.get_pressed()
                if keys[pygame.K_s]:
                    glTranslate(0, 0, 0.1)
                if keys[pygame.K_w]:
                    glTranslate(0, 0, -0.1)
                if keys[pygame.K_a]:
                    glTranslate(0.1, 0, 0)
                if keys[pygame.K_d]:
                    glTranslate(-0.1, 0, 0)
                if keys[pygame.K_q]:
                    glTranslate(0, -0.1, 0)
                if keys[pygame.K_e]:
                    glTranslate(0, 0.1, 0)
                if keys[pygame.K_r]:
                    glLoadIdentity()
                    self.ventanaInicial()

                # Movimiento y rotación con el mouse
                x, y = pygame.mouse.get_rel()
                x *= self.mouse_sesivity
                y *= self.mouse_sesivity

                if x != 0:
                    glRotatef(x, 0, 1, 0)  # Rotación en eje Y para girar la vista horizontalmente
                if y != 0:
                    glRotatef(y, 1, 0, 0)  # Rotación en eje X para girar la vista verticalmente

                pygame.mouse.set_pos(self.display[0] // 2, self.display[1] // 2)

                glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
                glEnable(GL_DEPTH_TEST)
                glPushMatrix() 
                
                if(coli.rombo_collision(self.PosXCabeza, self.PosYCabeza, self.PosZCabeza,self.Cabeza_width, self.Cabeza_Height,self.Cabeza_depth,
                    self.PosXPelota, self.PosYPelota, self.PosZPelota,self.Obj1_height)):
                    self.bandera1=1
                    self.valoresIniciales()

                if(coli.rombo_collision(self.PosXTorso, self.PosYTorso, self.PosZTorso,self.Torso_width, self.Torso_Height,self.Torso_depth,
                    self.PosXCorazon, self.PosYCorazon, self.PosZCorazon,self.Obj1_height)):
                    self.bandera1=2
                    self.valoresIniciales()

                if(coli.rombo_collision(self.PosXCabeza, self.PosYCabeza, self.PosZCabeza,self.Cabeza_width, self.Cabeza_Height,self.Cabeza_depth,
                    self.PosXHamburguesa, self.PosYHamburguesa, self.PosZHamburguesa,self.Obj1_height)):
                    self.bandera1=3
                    self.valoresIniciales()

                if(coli.rombo_collision(self.PosXCabeza, self.PosYCabeza, self.PosZCabeza,self.Cabeza_width, self.Cabeza_Height,self.Cabeza_depth,
                    self.PosXBola, self.PosYBola, self.PosZBola,self.Obj1_height)):
                    self.bandera1=0
                    self.valoresIniciales()

                if self.bandera==0:
                    b.original()
                    es.draw_e(self.textura1)   
                    if self.bandera2==1:
                        self.lcFin.iluminacionPhong()
                    elif self.bandera2==2:
                        self.lcFin.iluminacionGourad()
                    elif self.bandera2==3:
                        self.lcFin.iluminacionInterpolada()
                    else :
                        self.lcFin.desactivarLuz()
                    
                if self.bandera==1:
                    b.asustado()
                    es.draw_e(self.textura2)
                if self.bandera==2:
                    b.molesto()
                    es.draw_e(self.textura3)
                if self.bandera==3:
                    b.preocupado()
                    es.draw_e(self.textura4)
                if self.bandera==4:
                    b.drawIndiferencia()
                    es.draw_e(self.textura5)
                if self.bandera==5:
                    b.sorprendido()
                    es.draw_e(self.textura6)
                if self.bandera==6:
                    b.felicidad()
                    es.draw_e(self.textura7)
                if self.bandera==7:
                    b.triste()
                    es.draw_e(self.textura8)
                if self.bandera==8:
                    b.animaLevantar()
                    es.draw_e(self.textura1)
                if self.bandera==9:
                    b.animaCaminar()
                    es.draw_e(self.textura1)
                if self.bandera==10:
                    b.animaBrazo2()
                    es.draw_e(self.textura1)
                if self.bandera==11:
                    b.animaCabeza()
                    es.draw_e(self.textura1)
                if self.bandera==12:
                    b.animaBrincar()
                    es.draw_e(self.textura1)
                if self.bandera==13:
                    b.animaBrincarSplit()
                    es.draw_e(self.textura1)
                if self.bandera==14:
                    b.animaCaida()
                    es.draw_e(self.textura1)
                if self.bandera==15:
                    txt.draw_text("Usar flechas del teclado para mover los objetos", -40, 40, -1, 25, 255, 255, 255, 0, 0, 0)
                    if(self.bandera1==0 and self.activarColi==True):
                        b.animaCaminar()
                        es.draw_e(self.textura1)  
                        self.pelota(0,0)
                    if(self.bandera1==1):
                        b.triste()
                        es.draw_e(self.textura8)
                        self.corazon(0,0)
                    if(self.bandera1==2):
                        b.animaBrincarSplit()
                        es.draw_e(self.textura7)
                        self.Hamburguesa(0,0)
                    if(self.bandera1==3):
                        b.preocupado()
                        es.draw_e(self.textura4)
                        self.bolaDisco(0,0)
                    
                if self.activarColi:
                    if self.bandera1==0:
                        if keys[pygame.K_UP]:
                            self.pelota(0,1)
                        if keys[pygame.K_DOWN]:
                            self.pelota(0,-1)
                        if keys[pygame.K_LEFT]:
                            self.pelota(-1,0)
                        if keys[pygame.K_RIGHT]:
                            self.pelota(1,0)
                    if self.bandera1==1:
                        if keys[pygame.K_UP]:
                            self.corazon(0,1)
                        if keys[pygame.K_DOWN]:
                            self.corazon(0,-1)
                        if keys[pygame.K_LEFT]:
                            self.corazon(-1,0)
                        if keys[pygame.K_RIGHT]:
                            self.corazon(1,0)
                    if self.bandera1==2:
                        if keys[pygame.K_UP]:
                            self.Hamburguesa(0,1)
                        if keys[pygame.K_DOWN]:
                            self.Hamburguesa(0,-1)
                        if keys[pygame.K_LEFT]:
                            self.Hamburguesa(-1,0)
                        if keys[pygame.K_RIGHT]:
                            self.Hamburguesa(1,0)
                    if self.bandera1==3:
                        if keys[pygame.K_UP]:
                            self.bolaDisco(0,1)
                        if keys[pygame.K_DOWN]:
                            self.bolaDisco(0,-1)
                        if keys[pygame.K_LEFT]:
                            self.bolaDisco(-1,0)
                        if keys[pygame.K_RIGHT]:
                            self.bolaDisco(1,0)
                
                if self.instruccion:
                    txt.draw_text("1:Original  2:Escenario1  3:Escenario2  4:Escenario3 5:Escenario4 ", -40, -10, -1, 25, 255, 255, 255, 0, 0, 0)
                    txt.draw_text("6:Escenario5  7:Escenario6  8:Escenario7  9:Mov1  0:Mov2", -40, -15, -1, 25, 255, 255, 255, 0, 0, 0)
                    txt.draw_text("z:Mov3  x:Mov4  c:Mov5  v:Mov6  b:Mov7  p:Sonido  o:ApagarSonido", -40, -20, -1, 25, 255, 255, 255, 0, 0, 0)
                    txt.draw_text("n:Activar colisiones h:phong j:Gouraud k:Interpolado ESC:Salir" ,-40,40,-1,25,255,255,255,0,0,0)
                    txt.draw_text("s:Cam(Zo)  w:Cam(Zi)  a:Cam(izq)  d:Cam(der)  q:Cam(Arriba)   ", -40, -25, -1, 25, 255, 255, 255, 0, 0, 0)
                    txt.draw_text("e:Cam(Abajo)  r:Cam(Orginal)  i:Instruccion(On/Of)  u:Acerca de:", -40, -30, -1, 25, 255, 255, 255, 0, 0, 0)
                if self.acercaDe:
                    txt.draw_text("Starenka Susana Ortiz Gallegos 22280683", -40, 30, -1, 25, 255, 255, 255, 0, 0, 0)
                

                glPopMatrix() 
                
                
                pygame.display.flip()
                pygame.time.wait(10)  #
                
        self.finalizar()

    def finalizar(self):
        glDisable(GL_LIGHT0)
        glDisable(GL_LIGHT1)
        glDisable(GL_LIGHT2)
                
                # Limpiar contexto de OpenGL
        glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
        pygame.display.quit()

if __name__ == "__main__":
    main=PersonajeStarenka()
    main.run()