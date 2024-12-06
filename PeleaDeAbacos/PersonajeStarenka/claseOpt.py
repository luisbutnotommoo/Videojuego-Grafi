import pygame
from OpenGL.GLU import *
from OpenGL.GL import *
from OpenGL.GLUT import *
from pygame.locals import *
from PIL import *
from PersonajeStarenka.Acciones2S import escenario as es
from PersonajeStarenka.Acciones2S import sonido as son
from PersonajeStarenka.Acciones2S import boceto as b
from PersonajeStarenka.Acciones2S import textos as txt
from PersonajeStarenka.Acciones2S import objetosColisiones as oC
from PersonajeStarenka.Acciones2S import iluminacion as lc
from PersonajeStarenka.Acciones2S import colisiones as coli
from PersonajeStarenka.Acciones2S.iluminacionFinal import iluminacion

class PersonajeStarenka:
    def __init__(self):
        self.bandera = 0
        self.bandera1 = 0
        self.running=True
        self.bandera2 = 0
        self.instruccion = True
        self.acercaDe = False
        self.activarColi = False
        self.camara_speed = 0.1
        self.rotation_speed = 0.2
        self.mouse_sesivity = 0.1
        self.lcFin = iluminacion()
        self.valoresIniciales()
        self.inicializarCosas()
        self.ventanaInicial()
        self.texturas = [
            es.load_texture('PersonajeStarenka/Imagenes2S/descarga_resized_op.jpeg'),
            es.load_texture('PersonajeStarenka/Imagenes2S/fondo5.jpg'),
            es.load_texture('PersonajeStarenka/Imagenes2S/fondo4.jpg'),
            es.load_texture('PersonajeStarenka/Imagenes2S/fondo2.jpg'),
            es.load_texture('PersonajeStarenka/Imagenes2S/fondo3.jpg'),
            es.load_texture('PersonajeStarenka/Imagenes2S/fondo6.jpg'),
            es.load_texture('PersonajeStarenka/Imagenes2S/fondo7.jpg'),
            es.load_texture('PersonajeStarenka/Imagenes2S/fondo8.jpg')
        ]
        self.PosXPelota, self.PosYPelota, self.PosZPelota = 10, 17, 0
        self.Obj1_height = 1
        self.PosXCabeza, self.PosYCabeza, self.PosZCabeza = 0.9, 17, 0
        self.Cabeza_Height, self.Cabeza_width, self.Cabeza_depth = 7.5, 7.5, 7.5
        self.PosXCorazon, self.PosYCorazon, self.PosZCorazon = -8, 8, 0
        self.PosXTorso, self.PosYTorso, self.PosZTorso = -8, 4, 0
        self.Torso_Height, self.Torso_width, self.Torso_depth = 2, 2, 2
        self.PosXHamburguesa, self.PosYHamburguesa, self.PosZHamburguesa = 10, 17, 0
        self.PosXBola, self.PosYBola, self.PosZBola = 10, 17, 0

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
        glTranslatef(0, 0, -5)
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


    def run(self):
        self.running = True
        while self.running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    quit()
                if event.type == pygame.KEYDOWN:
                    self.handle_keydown(event)

            keys = pygame.key.get_pressed()
            self.handle_movement(keys)

            glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
            glEnable(GL_DEPTH_TEST)
            glPushMatrix()

            self.check_collisions()
            if not self.activarColi:
                if self.bandera == 0:
                    b.original()
                    es.draw_e(self.texturas[0])
                    self.handle_lighting()
                # Activar colisiones
                else:
                    self.handle_bandera()

            # Solo dibuja los objetos si activarColi es True
            if self.activarColi:
                self.bandera==-1
                if self.bandera1 == 0:
                    b.original()
                    es.draw_e(self.texturas[0])  
                    self.pelota(0, 0)  # Dibuja la pelota
                elif self.bandera1 == 1:
                    b.triste()
                    es.draw_e(self.texturas[7])
                    self.corazon(0, 0)  # Dibuja el corazón
                elif self.bandera1 == 2:
                    b.animaBrincarSplit()
                    es.draw_e(self.texturas[6])
                    self.Hamburguesa(0, 0)  # Dibuja la hamburguesa
                elif self.bandera1 == 3:
                    b.preocupado()
                    es.draw_e(self.texturas[3])
                    self.bolaDisco(0, 0)  # Dibuja la bola

                self.handle_collision_movement(keys)

            if self.instruccion:
                self.display_instructions()
            if self.acercaDe:
                txt.draw_text("Starenka Susana Ortiz Gallegos 22280683", -40, 30, -1, 25, 255, 255, 255, 0, 0, 0)

            glPopMatrix()
            pygame.display.flip()
            pygame.time.wait(10)

        self.finalizar()

    def handle_keydown(self, event):
        if event.key == pygame.K_p:
            son.sonido('PersonajeStarenka/Sonido2S/sonidoFijo.wav')
        elif event.key == pygame.K_o:
            son.stopsonido()
        elif event.key == pygame.K_ESCAPE:
            self.running=False
        elif event.key in [pygame.K_1, pygame.K_2, pygame.K_3, pygame.K_4, pygame.K_5, pygame.K_6, pygame.K_7, pygame.K_8]:
            self.bandera = int(event.key) - pygame.K_1
        elif event.key == pygame.K_n:
            self.activarColi = not self.activarColi
            
        elif event.key == pygame.K_i:
            self.instruccion = not self.instruccion
        elif event.key == pygame.K_u:
            self.acercaDe = not self.acercaDe
        elif event.key in [pygame.K_h, pygame.K_j, pygame.K_k, pygame.K_l]:
            self.bandera2 = {pygame.K_h: 1, pygame.K_j: 2, pygame.K_k: 3, pygame.K_l: 0}.get(event.key)

        # Asegúrate de que self.bandera esté dentro del rango de self.texturas
        if self.bandera < 0 or self.bandera >= len(self.texturas):
            self.bandera = 0  # O cualquier valor por defecto que desees

    def handle_movement(self, keys):
        if keys[pygame.K_s]:
            glTranslate(0, 0, 0.1)
        if keys[pygame.K_w]:
            glTranslate (0, 0, -0.1)
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

        x, y = pygame.mouse.get_rel()
        x *= self.mouse_sesivity
        y *= self.mouse_sesivity

        if x != 0:
            glRotatef(x, 0, 1, 0)
        if y != 0:
            glRotatef(y, 1, 0, 0)

        pygame.mouse.set_pos(self.display[0] // 2, self.display[1] // 2)

    def check_collisions(self):
        if coli.rombo_collision(self.PosXCabeza, self.PosYCabeza, self.PosZCabeza, self.Cabeza_width, self.Cabeza_Height, self.Cabeza_depth,
                                self.PosXPelota, self.PosYPelota, self.PosZPelota, self.Obj1_height):
            self.bandera1 = 1
            self.valoresIniciales()

        if coli.rombo_collision(self.PosXTorso, self.PosYTorso, self.PosZTorso, self.Torso_width, self.Torso_Height, self.Torso_depth,
                                self.PosXCorazon, self.PosYCorazon, self.PosZCorazon, self.Obj1_height):
            self.bandera1 = 2
            self.valoresIniciales()

        if coli.rombo_collision(self.PosXCabeza, self.PosYCabeza, self.PosZCabeza, self.Cabeza_width, self.Cabeza_Height, self.Cabeza_depth,
                                self.PosXHamburguesa, self.PosYHamburguesa, self.PosZHamburguesa, self.Obj1_height):
            self.bandera1 = 3
            self.valoresIniciales()

        if coli.rombo_collision(self.PosXCabeza, self.PosYCabeza, self.PosZCabeza, self.Cabeza_width, self.Cabeza_Height, self.Cabeza_depth,
                                self.PosXBola, self.PosYBola, self.PosZBola, self.Obj1_height):
            self.bandera1 = 0
            self.valoresIniciales()

    def handle_lighting(self):
        if self.bandera2 == 1:
            self.lcFin.iluminacionPhong()
        elif self.bandera2 == 2:
            self.lcFin.iluminacionGourad()
        elif self.bandera2 == 3:
            self.lcFin.iluminacionInterpolada()
        else:
            self.lcFin.desactivarLuz()

    def handle_bandera(self):
        actions = [
            b.original, b.asustado, b.molesto, b.preocupado, b.drawIndiferencia,
            b.sorprendido, b.felicidad, b.triste
        ]
        
        # Llama a la acción correspondiente
        actions[self.bandera]()
        
        # Verifica que self.bandera esté dentro del rango de self.texturas
        if 0 <= self.bandera < len(self.texturas):
            es.draw_e(self.texturas[self.bandera])
        else:
            print(f"Advertencia: self.bandera ({self.bandera}) está fuera de rango.")
        
        

    def handle_collision_movement(self, keys):
        
        # Maneja el movimiento de los objetos según las teclas presionadas
        if self.bandera1 == 0:  # Pelota
            if keys[pygame.K_UP]:
                self.pelota(0, 1)
            if keys[pygame.K_DOWN]:
                self.pelota(0, -1)
            if keys[pygame.K_LEFT]:
                self.pelota(-1, 0)
            if keys[pygame.K_RIGHT]:
                self.pelota(1, 0)
        elif self.bandera1 == 1:  # Corazón
            if keys[pygame.K_UP]:
                self.corazon(0, 1)
            if keys[pygame.K_DOWN]:
                self.corazon(0, -1)
            if keys[pygame.K_LEFT]:
                self.corazon(-1, 0)
            if keys[pygame.K_RIGHT]:
                self.corazon(1, 0)
        elif self.bandera1 == 2:  # Hamburguesa
            if keys[pygame.K_UP]:
                self.Hamburguesa(0, 1)
            if keys[pygame.K_DOWN]:
                self.Hamburguesa(0, -1)
            if keys[pygame.K_LEFT]:
                self.Hamburguesa(-1, 0)
            if keys[pygame.K_RIGHT]:
                self.Hamburguesa(1, 0)
        elif self.bandera1 == 3:  # Bola
            if keys[pygame.K_UP]:
                self.bolaDisco(0, 1)
            if keys[pygame.K_DOWN]:
                self.bolaDisco(0, -1)
            if keys[pygame.K_LEFT]:
                self.bolaDisco(-1, 0)
            if keys[pygame.K_RIGHT]:
                self.bolaDisco(1, 0)
    def display_instructions(self):
        instructions = [
            "1:Original  2:Escenario1  3:Escenario2  4:Escenario3 5:Escenario4",
            "6:Escenario5  7:Escenario6  8:Escenario7 s:Cam(Zo)  w:Cam(Zi)",
            "a:Cam(izq)  d:Cam(der)   r:Cam(Orginal)    q:Cam(Arriba)  e:Cam(Abajo)",
            "n:Activar colisiones h:phong j:Gouraud k:Interpolado ESC:Salir",
            "p:Sonido  o:ApagarSonido",
            "i:Instruccion(On/Of)  u:Acerca de:"
        ]
        for i, instruction in enumerate(instructions):
            txt.draw_text(instruction, -40, -10 - (i * 5), -1, 25, 255, 255, 255, 0, 0, 0)

    def finalizar(self):
        glDisable(GL_LIGHT0)
        glDisable(GL_LIGHT1)
        glDisable(GL_LIGHT2)
        glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
        pygame.display.quit()

if __name__ == "__main__":
    main = PersonajeStarenka()
    main.run()