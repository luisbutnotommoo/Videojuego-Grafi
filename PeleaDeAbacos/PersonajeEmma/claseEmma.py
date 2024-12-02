import pygame
from OpenGL.GLU import *
from OpenGL.GL import *
from OpenGL.GLUT import *
from pygame.locals import *

from PersonajeEmma.actionsEV import sonido as snd
from PersonajeEmma.actionsEV import textos as txt
from PersonajeEmma.actionsEV import colisiones as coli
from PersonajeEmma.actionsEV import drawPersonaje as dr
from PersonajeEmma.actionsEV import draw2 as dr2
from PersonajeEmma.actionsEV import objetos as obj

class PersonajeEmmanuel:
    def __init__(self):
        pygame.init()
        pygame.mixer.init()
        self.display = (600, 600)
        self.screen = pygame.display.set_mode(self.display, DOUBLEBUF | OPENGL)

        # Configuración de OpenGL
        glEnable(GL_DEPTH_TEST)
        glEnable(GL_LIGHTING)
        glShadeModel(GL_SMOOTH)
        glEnable(GL_COLOR_MATERIAL)
        glColorMaterial(GL_FRONT_AND_BACK, GL_AMBIENT_AND_DIFFUSE)
        glEnable(GL_LIGHT0)
        glLightfv(GL_LIGHT0, GL_AMBIENT, [0.4, 0.4, 0.4, 1])
        glLightfv(GL_LIGHT0, GL_DIFFUSE, [0.5, 0.5, 0.5, 1])
        glLightfv(GL_LIGHT0, GL_POSITION, [1, -1, 1, 0])

        glMatrixMode(GL_PROJECTION)
        gluPerspective(45, (self.display[0] / self.display[1]), 0.1, 120.0)
        glMatrixMode(GL_MODELVIEW)
        gluLookAt(-10, 17, -50, 20, 17, 20, 0, 1, 0)
        
        # Variables de estado y posición
        self.viewMatrix = glGetFloatv(GL_MODELVIEW_MATRIX)
        glLoadIdentity()
        self.displayCenter = [self.screen.get_size()[i] // 2 for i in range(2)]
        self.mouseMove = [0, 0]
        pygame.mouse.set_pos(self.displayCenter)
        self.up_down_angle = 0.0
        self.paused = False
        self.running = True
        self.estado = 0
        self.font = pygame.font.SysFont('Arial', 20)
        self.acercade = ""
        self.colorTexto = [0, 0, 0]

        # Variables de posición del personaje y objetos
        self.pos_inicial_x = 0
        self.pos_inicial_y = 0
        self.x, self.y = 10, 7  # Posiciones del personaje
        self.radio = 1.5
        self.box_min = [self.x - self.radio, 0, self.y - self.radio]
        self.box_max = [self.x + self.radio, 6, self.y + self.radio]

        # Posiciones de los objetos
        self.posicion_esfera = [0, 3, 7]
        self.posicion_cilindro = [20, 2, 6]
        self.posicion_cubo = [10, 2, -3]
        self.posE1 = [10, 3, 16]

        self.textoColision = ""

    def run(self):
        while self.running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.running = False
                if event.type == pygame.KEYDOWN:
                    if event.key in [pygame.K_ESCAPE, pygame.K_RETURN]:
                        self.running = False
                    if event.key in [pygame.K_PAUSE, pygame.K_p]:
                        self.paused = not self.paused
                        pygame.mouse.set_pos(self.displayCenter)

                    # Manejo de teclas de acción y sonido
                    if event.key == pygame.K_i:
                        self.acercade = "\nDesarrollado por Emmanuel Vallejo"
                    elif event.key == pygame.K_n:
                        snd.sonido("PeleaDeAbacos/PersonajeEmma/soundsEV/choir.mp3")
                    elif event.key == pygame.K_m:
                        snd.stopsonido()

                    # Cambios de estado para personaje
                    estado_keys = {
                        pygame.K_o: 0, pygame.K_1: 1, pygame.K_2: 2, pygame.K_3: 3, pygame.K_4: 4,
                        pygame.K_5: 5, pygame.K_6: 6, pygame.K_7: 7, pygame.K_8: 8, pygame.K_9: 9,
                        pygame.K_0: 10, pygame.K_e: 11, pygame.K_r: 12, pygame.K_t: 13, pygame.K_y: 14
                    }

                    # Lista de teclas válidas para reproducir sonidos
                    teclas_sonido = [pygame.K_1, pygame.K_2, pygame.K_3, pygame.K_4, pygame.K_5, pygame.K_e, pygame.K_r]

                    if event.key in estado_keys:
                        self.estado = estado_keys[event.key]
                        if event.key in teclas_sonido:
                            snd.sonido(f"PeleaDeAbacos/PersonajeEmma/soundsEV/sound{self.estado}.mp3")


                # Movimiento de cámara con el ratón
                if not self.paused and event.type == pygame.MOUSEMOTION:
                    self.mouseMove = [event.pos[i] - self.displayCenter[i] for i in range(2)]
                    pygame.mouse.set_pos(self.displayCenter)

            # Lógica de actualización de cámara
            if not self.paused:
                keypress = pygame.key.get_pressed()
                glLoadIdentity()
                self.up_down_angle += self.mouseMove[1] * 0.1
                glRotatef(self.up_down_angle, 1.0, 0.0, 0.0)

                glPushMatrix()
                glLoadIdentity()
                if keypress[pygame.K_w]: glTranslatef(0, 0, 0.4)
                if keypress[pygame.K_s]: glTranslatef(0, 0, -0.5)
                if keypress[pygame.K_d]: glTranslatef(-0.5, 0, 0)
                if keypress[pygame.K_a]: glTranslatef(0.5, 0, 0)
                if keypress[pygame.K_z]: glTranslatef(0, 0.5, 0)
                if keypress[pygame.K_x]: glTranslatef(0, -0.5, 0)
                
                # Movimiento del personaje
                if keypress[pygame.K_UP]: self._mover_personaje(0, 0.5)
                if keypress[pygame.K_DOWN]: self._mover_personaje(0, -0.5)
                if keypress[pygame.K_LEFT]: self._mover_personaje(-0.5, 0)
                if keypress[pygame.K_RIGHT]: self._mover_personaje(0.5, 0)

                glRotatef(self.mouseMove[0] * 0.1, 0.0, 1.0, 0.0)
                glMultMatrixf(self.viewMatrix)
                self.viewMatrix = glGetFloatv(GL_MODELVIEW_MATRIX)
                glPopMatrix()
                glMultMatrixf(self.viewMatrix)

                # Dibujar escena
                glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
                dr.personaje(self.estado, self.pos_inicial_x, self.pos_inicial_y)

                # Dibujar objetos
                self._draw_objects()

                # Comprobación de colisiones
                self._comprobar_colisiones()
                
                # Renderizado de texto
                self._renderizar_texto()

                pygame.display.flip()
                pygame.time.wait(10)
        pygame.quit()

    def _mover_personaje(self, dx, dy):
        self.pos_inicial_x += dx
        self.x += dx
        self.box_min[0] += dx
        self.box_max[0] += dx
        self.pos_inicial_y += dy
        self.y += dy
        self.box_min[2] += dy
        self.box_max[2] += dy

    def _draw_objects(self):
        glPushMatrix()
        glTranslatef(*self.posE1)
        dr2.obj1(255, 255, 0)
        glPopMatrix()

        glPushMatrix()
        glTranslatef(*self.posicion_esfera)
        glColor4f(1, 0, 0, 1)
        obj.draw_sphere(3, 10, 20)
        glPopMatrix()

        glPushMatrix()
        glTranslatef(*self.posicion_cilindro)
        glColor4f(0, 1, 0, 1)
        obj.draw_cylinder(2, 4, 10)
        glPopMatrix()

        glPushMatrix()
        glTranslatef(*self.posicion_cubo)
        glColor4f(0, 0, 1, 1)
        obj.draw_cube()
        glPopMatrix()

    def _comprobar_colisiones(self):
        colision1 = coli.spheres(self.posicion_esfera, 3, [self.x, 3, self.y], 3)
        colision2 = coli.aabb([9.0, 1.0, -4.0], [11.0, 3.0, -2.0], self.box_min, self.box_max)
        colision3 = coli.manhattan(self.posicion_cilindro, [self.x, 1.5, self.y], 6)
        colision4 = coli.spheres(self.posE1, 3, [self.x, 3, self.y], 3)

        if colision1:
            self.colorTexto=[0,255,0]
        if colision2:
            self.colorTexto=[0,0,255]
        if colision3:
            self.colorTexto=[255,0,0]
        if colision4:
            self.colorTexto=[255,255,0]
        
        if colision1 or colision2 or colision3 or colision4:
            self.textoColision = "Colision detectada"
        else:
            self.textoColision = "Esperando colision"
            self.colorTexto = [255,255,255]
        
        txt.drawText(self.textoColision,5,30,4,30,self.colorTexto[0],self.colorTexto[1],self.colorTexto[2],0,0,0)

    def _renderizar_texto(self):
        glColor4f(1, 1, 1, 1)
        txt.render_text_2d(self.display,
                           "W,A,S,D,Z,X - Mover cámara\nFLECHAS - Mover personaje\no-Original\n1-Enojado\n2-Triste\n3-Sospechoso\n4-Indiferente\n5-Levantar ceja\nE-Sorprendido\nR-Sonriente\n6-Levantar brazo IZQ\n7-Levantar brazo DER\n8-T-Pose\n9-Sentado\n0-Saltando\nT-Señalando\nY-Celebrando\nn-Sonido ON\nm-Sonido OFF\np-Pausa\ni-Acerca de" + self.acercade,
                            10, self.display[1] - 40, self.font)  # Esquina inferior izquierda

# Ejecutar el juego

