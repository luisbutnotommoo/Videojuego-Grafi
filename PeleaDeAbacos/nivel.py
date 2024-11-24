import pygame
from OpenGL.GLU import*
from OpenGL.GL import*
from OpenGL.GLUT import*
from pygame.locals import*
from PIL import*
import Acciones.objetosTextura as obj
import Acciones.escenario as esc
import Acciones.viewPortPreguntas as view
import Acciones.bancoPreguntas as bp
from Acciones.boceto import  PersonajesDeTodos
import Acciones.boceto as b
from Acciones.colisionRectangular import RectangularCollision3D
from Acciones.texto import textos as tx


class Nivel1:

    def __init__(self, display_size=(800, 600)):
        self.bandera = 0
        self.banderaJugador1 = False
        self.banderaJugador2 = False
        self.banderaColision = 0
        self.display = display_size
        self.show_message = False
        self.init_pygame()
        self.init_set_perspective()
        self.jugador_1_score = 0
        self.jugador_2_score = 0
        self.reduc1=40
        self.reduc2=40
        self.estado_emma = 0
        self.estado_luis=0
        self.personaje = [
            PersonajesDeTodos("Personaje de Emma", b.figuraEmma(self.estado_emma),rotacion=190, escala=(0.6,0.6,0.6)),
            PersonajesDeTodos("Personaje de Luis", b.figuraLuis(self.estado_luis), escala=(3.5, 3.5, 3.5))
        ]
        self.pocimaX, self.pocimaY, self.pocimaZ = -2, 5, -20
        self.esferaX, self.esferaY, self.esferaZ=-2, 5, -20
        self.sonido_seleccion = pygame.mixer.Sound("Sonidos/click.mp3")
        self.sonido_ganar = pygame.mixer.Sound("Sonidos/win.mp3")
        pygame.mixer.music.load("Sonidos/nivel1.mp3")
        pygame.mixer.music.play(loops=-1)
        self.bandera_instrucciones = True
        self.bandera_pausa = False
        self.bandera_control_instrucciones = True
        self.bandera_ganador=0
        self.puntaje_ganador = 10
        self.texturaBola=obj.load_texture("Imagenes/aguaOrg.jpg")
        self.texturaPocima=obj.load_texture("Imagenes/moradoPocimaOrg.jpg")
        self.texturaTorre=obj.load_texture("Imagenes/torreOrg.jpg")
        self.objEscenario = esc.escenario("Imagenes/pasto.jpeg", "Imagenes/castillo.jpg")
        self.objetoPregunta = bp.bancoPreguntas()
        self.objetoPregunta.elige_pregunta()
        self.fuente_instrucciones = pygame.font.SysFont(None, 30)
        self.fuente_pausa = pygame.font.SysFont(None, 40)
        self.texto_instrucciones = [
            "                               G U E R R A    D E   A B A C O S ",
            "               _____________________________________________", "",
            "                  JUGADOR 1, contesta las preguntas con A,S,D",
            "         Contesta correctamente y ataca la torre rival con W,A,S,D",
            "        JUGADOR 2, contesta las preguntas con las FLECHAS <,v,>",
            "Contesta correctamente y ataca la torre rival con las FLECHAS ^,<,v,>",
            "                     Las respuestas incorrectas no dan puntos",
            "                             ¡Se más rápido que tu adversario!",
            "               _____________________________________________", "",
            "                                - Presiona P para continuar -"
        ]
        self.opc_sel = 1
        self.txopc1 = ">"
        self.txopc2 = ""
        self.txopc3 = ""
        self.txopc4 = ""
        self.txopc5 = ""
        self.texto_pausa = [
            ""
        ]
        self.asignar_posiciones_personajes()

    def reiniciar_valores(self):
        self.pocimaX, self.pocimaY, self.pocimaZ = -2, 5, -20
        self.esferaX, self.esferaY, self.esferaZ=-2, 5, -20
    def asignar_posiciones_personajes(self):
        if self.banderaColision==1:
            self.personaje[1]= PersonajesDeTodos("Personaje de Luis", b.figuraLuis(1), escala=(3.5, 3.5, 3.5))
        if self.banderaColision==2:
            self.personaje[0]= PersonajesDeTodos("Personaje de Emma", b.figuraEmma(1), rotacion=190, escala=(0.6,0.6,0.6))
        if self.banderaColision==0:
            self.personaje[0]= PersonajesDeTodos("Personaje de Emma", b.figuraEmma(0), rotacion=190, escala=(0.6,0.6,0.6))
            self.personaje[1]= PersonajesDeTodos("Personaje de Luis", b.figuraLuis(0), escala=(3.5, 3.5, 3.5))
        posiciones = [
            (-15, -10, 0),  # Posición para personaje 1
            (18, -9, 0)    # Posición para personaje 4
        ]
        for personaje, (x, y, z) in zip(self.personaje, posiciones):
            personaje.set_position(x, y, z)
    
    def init_pygame(self):
        pygame.init()
        pygame.mixer.init()
        self.screen = pygame.display.set_mode(self.display, DOUBLEBUF | OPENGL)
        pygame.event.set_grab(True)

    def init_set_perspective(self):
        glMatrixMode(GL_PROJECTION)
        glLoadIdentity()
        gluPerspective(60, (self.display[0] / self.display[1]), 0.1, 100.0)
        glMatrixMode(GL_MODELVIEW)
        glLoadIdentity()
        glTranslatef(0.0, 0.0, -50.0)

    def pocima(self, movX, movY):
        self.pocimaX = self.pocimaX + movX
        self.pocimaY = self.pocimaY + movY
        glPushMatrix()
        glTranslatef(self.pocimaX, self.pocimaY, self.pocimaZ)
        glScalef(4, 4, 4)
        obj.draw_sphere(0.5,20,60,self.texturaPocima )
        glPopMatrix()

    def esferaMagia(self,movX,movY):
        self.esferaX = self.esferaX + movX
        self.esferaY = self.esferaY + movY
        glPushMatrix()
        glTranslatef(self.esferaX, self.esferaY, self.esferaZ)
        glScalef(4, 4, 4)
        obj.draw_sphere(0.5,20,60,self.texturaBola )
        glPopMatrix()

    def torre1(self):
        base_y = -10 + (self.reduc1 / 2)  
        glPushMatrix()
        glTranslatef(-35, base_y, -50) 
        obj.draw_cylinder(10, self.reduc1, 20, self.texturaTorre)
        glPopMatrix()

    def torre2(self):
        base_y = -10 + (self.reduc2 / 2)  
        glPushMatrix()
        glTranslatef(30, base_y, -50)  
        obj.draw_cylinder(10, self.reduc2, 20, self.texturaTorre)
        glPopMatrix()

    def draw_scene(self):
        glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
        # Dibujar escenario
        self.objEscenario.dibujar_piso_pared()
        if(self.banderaColision==0):
            self.torre1()
            self.torre2()
        if (self.banderaColision==1):
            glPushMatrix()
            glColor3f(0.984, 0.349, 0.278)
            self.torre2()
            glPopMatrix()
            glPushMatrix()
            glColor3f(0.565, 0.933, 0.565)
            self.torre1()
            glPopMatrix()
        elif (self.banderaColision==2):
            glPushMatrix()
            glColor3f(0.984, 0.349, 0.278)
            self.torre1()
            glPopMatrix()
            glPushMatrix()
            glColor3f(0.565, 0.933, 0.565)
            self.torre2()
            glPopMatrix()
                

        for personaje in self.personaje:
            personaje.render()  # Llamar al método dibujar del personaje
        
        if self.show_message:
            view.viewPort(self.display).draw_viewport(self.objetoPregunta)
        if self.bandera_control_instrucciones:
            tx.draw_text2(self.texto_instrucciones,self.fuente_instrucciones,150,50,50)
        if self.bandera_pausa:
            self.actualizar_opciones()
            tx.draw_text2(self.texto_pausa,self.fuente_pausa,150,50,50)
        if not self.bandera_control_instrucciones and not self.bandera_pausa:
            tx.draw_text2(["Presiona SPACE para mostrar la pregunta","Presiona P para pausar el juego"],self.fuente_instrucciones,0,50,500)
        if self.bandera_ganador==1:
            tx.draw_text2(["¡JUGADOR 1 ganó el juego!"],self.fuente_pausa,150,200,280)
        if self.bandera_ganador==2:
            tx.draw_text2(["¡JUGADOR 2 ganó el juego!"],self.fuente_pausa,150,200,280)

        # Detectar la colisión cuando está activada
        if self.banderaColision==1:
            self.pocima(0, 0)
            self.teclasJugador1()
            
            # Colisión de la pocima con la torre 2
            box1 = RectangularCollision3D(self.pocimaX, self.pocimaY, self.pocimaZ, 5, 5, 5)  # Tamaño de la poción
            box2 = RectangularCollision3D(20, -10, -20, 10, 50, 10)  # Tamaño de la torre 2
            box3 = RectangularCollision3D(-15, -10, -20, 10, 50, 10)  # Tamaño de la torre 1
            
            if box1.check_collision(box2):
                print("¡Colisión detectada con la Torre 2!")
                self.reduc2=self.reduc2-4
                self.reiniciar_valores()
                self.banderaColision=0
                self.asignar_posiciones_personajes()
                self.show_message=True
                
                print('Jugador1', self.jugador_1_score)
                if self.jugador_1_score == self.puntaje_ganador:
                    pygame.mixer.music.stop()
                    self.sonido_ganar.play()
                    self.bandera_ganador=1
                    self.show_message=False
            if box1.check_collision(box3):
                print("¡Colisión detectada con la Torre 1!")
                self.reduc1=self.reduc1+4
                self.reiniciar_valores()
                self.banderaColision=0
                self.asignar_posiciones_personajes()
                self.show_message=True
                
                print('Jugador1', self.jugador_1_score)
                if self.jugador_1_score == self.puntaje_ganador:
                    pygame.mixer.music.stop()
                    self.sonido_ganar.play()
                    self.bandera_ganador=1
                    self.show_message=False
                    
                
        elif self.banderaColision==2:
            
            self.esferaMagia(0, 0)
            self.teclasJugador2()
            # Colisión de la esfera magica en la torre 1
            box1 = RectangularCollision3D(self.esferaX, self.esferaY, self.esferaZ, 5, 5, 5)  # Tamaño de la poción
            box2 = RectangularCollision3D(-15, -10, -20, 10, 50, 10)  # Tamaño de la torre 2
            box3 = RectangularCollision3D(20, -10, -20, 10, 50, 10)  # Tamaño de la torre 2
            
            if box1.check_collision(box2):
                self.reduc1=self.reduc1-4
                print("¡Colisión detectada con la Torre 1!")
                self.reiniciar_valores()
                self.banderaColision=0
                self.show_message=True
                print('Jugador2:',self.jugador_2_score)
                self.asignar_posiciones_personajes()
                if self.jugador_2_score == self.puntaje_ganador:
                    pygame.mixer.music.stop()
                    self.sonido_ganar.play()
                    self.bandera_ganador=2
                    self.show_message=False
            if box1.check_collision(box3):
                self.reduc2=self.reduc2+4
                print("¡Colisión detectada con la Torre 2!")
                self.reiniciar_valores()
                self.banderaColision=0
                self.show_message=True
                print('Jugador2:',self.jugador_2_score)
                self.asignar_posiciones_personajes()
                if self.jugador_2_score == self.puntaje_ganador:
                    pygame.mixer.music.stop()
                    self.sonido_ganar.play()
                    self.bandera_ganador=2
                    self.show_message=False
                

        pygame.display.flip()

    def handle_input(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    self.bandera = 1
                    return False
                 # Configurar pausa
                if event.key == pygame.K_p:
                    if self.bandera_control_instrucciones:
                        self.bandera_instrucciones =  not self.bandera_instrucciones
                        self.bandera_control_instrucciones = not self.bandera_control_instrucciones
                    else:
                        self.bandera_pausa = not self.bandera_pausa
                    self.sonido_seleccion.play()

                # Opciones de pausa
                if self.bandera_pausa:
                    if event.key == pygame.K_UP:
                        self.opciones_pausa(-1)
                    if event.key == pygame.K_DOWN:
                        self.opciones_pausa(1)
                    if event.key == pygame.K_RETURN or event.key == pygame.K_KP_ENTER:
                        if self.opc_sel == 1:
                            self.bandera_pausa = not self.bandera_pausa
                        elif self.opc_sel == 2:
                            pygame.mixer.music.stop()
                            pygame.mixer.music.play()
                            self.jugador_1_score=0
                            self.jugador_2_score=0
                            self.bandera_instrucciones=not self.bandera_instrucciones
                            self.bandera_control_instrucciones=not self.bandera_control_instrucciones
                            self.bandera_pausa=not self.bandera_pausa
                        elif self.opc_sel == 3:
                            self.bandera_pausa = not self.bandera_pausa
                            self.bandera_instrucciones =  not self.bandera_instrucciones
                            self.bandera_control_instrucciones = not self.bandera_control_instrucciones
                        elif self.opc_sel == 4:
                            pass # VOLVER A SELECCIONAR PERSONAJES
                        elif self.opc_sel == 5:
                            return False
                    self.sonido_seleccion.play()
                
                if self.show_message:  # Si la pregunta está en pantalla
                    # Verificar si ambos jugadores ya están bloqueados
                    if self.banderaJugador1 and self.banderaJugador2:
                        return True  # No permitir más respuestas
                    
                    # Jugador 1 responde
                    if event.key in [pygame.K_a, pygame.K_s, pygame.K_d] and not self.banderaJugador1:
                        if self.respuesta(event.key, player=1):
                            self.jugador_1_score += 1  # Jugador 1 gana un punto
                            self.eventoParaGanar()
                            self.banderaColision = 1
                            self.asignar_posiciones_personajes()
                        else:
                            self.banderaJugador1 = True  # Bloquear teclas para Jugador 1
                    
                    # Jugador 2 responde
                    elif event.key in [pygame.K_DOWN, pygame.K_LEFT, pygame.K_RIGHT] and not self.banderaJugador2:
                        if self.respuesta(event.key, player=2):
                            self.jugador_2_score += 1  # Jugador 2 gana un punto
                            self.banderaColision=2
                            self.asignar_posiciones_personajes()
                            self.eventoParaGanar()
                            
                        else:
                            self.banderaJugador2 = True  # Bloquear teclas para Jugador 2
                    
                    # Verificar si ambos jugadores están bloqueados
                    if self.banderaJugador1 and self.banderaJugador2:
                        self.eventoNoAcertaron()

                if event.key == pygame.K_SPACE:  # Mostrar el mensaje al presionar la barra espaciadora
                    self.show_message = True
                if self.show_message and event.key == pygame.K_RETURN:
                    self.show_message = False  # Ocultar el mensaje al presionar Enter

        return True

    def eventoParaGanar(self):
        print("Evento: ¡Respuesta correcta!")
        self.show_message = False  # Ocultar la pregunta 
        self.banderaJugador1 = False
        self.banderaJugador2 = False
        self.objetoPregunta.elige_pregunta()
        

    def eventoNoAcertaron(self):
        print("Evento: Ambos jugadores fallaron")
        self.show_message = True  # Ocultar la pregunta
        self.objetoPregunta.elige_pregunta()
        self.banderaJugador1 = False
        self.banderaJugador2 = False

    def teclasJugador1(self):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_w]:
            self.pocima(0, 1)
        if keys[pygame.K_s]:
            self.pocima(0, -1)
        if keys[pygame.K_a]:
            self.pocima(-1, 0)
        if keys[pygame.K_d]:
            self.pocima(1, 0)
    
    def teclasJugador2(self):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_UP]:
            self.esferaMagia(0, 1)
        if keys[pygame.K_DOWN]:
            self.esferaMagia(0, -1)
        if keys[pygame.K_LEFT]:
            self.esferaMagia(-1, 0)
        if keys[pygame.K_RIGHT]:
            self.esferaMagia(1, 0)

    def respuesta(self, key, player):
        key_answer_map = {
            pygame.K_a: "a", 
            pygame.K_s: "b",
            pygame.K_d: "c",  
            pygame.K_LEFT: "a",
            pygame.K_DOWN: "b",
            pygame.K_RIGHT: "c"  # Jugador 2 presiona 'UP'
        }
        if key in key_answer_map and key_answer_map[key] == self.objetoPregunta.respuestaActual:
            return True
        return False
    
    def opciones_pausa(self,opcion):
        self.opc_sel += opcion
        if self.opc_sel > 5:
            self.opc_sel = 1
        if self.opc_sel < 1:
            self.opc_sel = 5

    def actualizar_opciones(self):
        self.txopc1 = ""
        self.txopc2 = ""
        self.txopc3 = ""
        self.txopc4 = ""
        self.txopc5 = ""

        if self.opc_sel == 1:
            self.txopc1 = ">"
        elif self.opc_sel == 2:
            self.txopc2 = ">"
        elif self.opc_sel == 3:
            self.txopc3 = ">"
        elif self.opc_sel == 4:
            self.txopc4 = ">"
        elif self.opc_sel == 5:
            self.txopc5 = ">"
        
        self.texto_pausa = [
            "P A U S A",
            "",
            self.txopc1+" Reanudar",
            self.txopc2+" Reiniciar",
            self.txopc3+" Mostrar instrucciones",
            self.txopc4+" Volver a seleccionar personajes",
            self.txopc5+" Salir"
        ]

    def run(self):
        running = True
        while running:
            running = self.handle_input()
            self.draw_scene()
            pygame.time.wait(10)
           

    def cleanup(self):
        pygame.quit()

if __name__ == "__main__":
    sP = Nivel1()
    sP.run()
