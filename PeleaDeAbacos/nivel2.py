import pygame
from OpenGL.GLU import*
from OpenGL.GL import*
from OpenGL.GLUT import*
from pygame.locals import*
from PIL import*
import Acciones.objetosTextura as obj
import Acciones.escenario as esc
import Acciones.viewPortPreguntas as view
import Acciones.bancoPreguntas2 as bp
from Acciones.boceto2 import  PersonajesDeTodos
import Acciones.boceto2 as b
from Acciones.colisionRectangular import RectangularCollision3D
from Acciones.texto import textos as tx
from Imagenes.controla_img import *
from Sonidos.controla_mp3 import MP3


class Nivel2:

    def __init__(self, display_size=(800, 600), personajesJugables=[]):
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
        self.personaje = personajesJugables

        self.banderaMenu=True
        self.banderaMenuPrincipal=True
        self.banderaMenuNivel=True
        self.banderaSiguienteNivel = True

        self.pocimaX, self.pocimaY, self.pocimaZ = -2, 5, -20
        self.esferaX, self.esferaY, self.esferaZ=-2, 5, -20

        self.mp3=MP3()
        self.sonido_seleccion = 'click.mp3'
        self.sonido_ganar = 'win.mp3'
        self.mp3.reproducir_sonido_fondo('nivel1.mp3')

        self.bandera_instrucciones = True
        self.bandera_pausa = False
        self.bandera_control_instrucciones = True
        self.bandera_ganador=0
        self.puntaje_ganador = 10
        self.texturaBola=cargar_textura("aguaOrg.jpg")
        self.texturaPocima=cargar_textura("moradoPocimaOrg.jpg")
        self.texturaTorre=cargar_textura("torreOrg.jpg")
        self.objEscenario = esc.escenario(cargar_imagen("piso3.jpg"),cargar_imagen( "castillo2.jpg"))
        self.iteraPregunta=0
        self.objetoBanco = bp.BancoPreguntas(5,2)
        self.cuestionario=self.objetoBanco.generar_banco_preguntas()
        self.preguntaActual=self.cuestionario[self.iteraPregunta]
        self.fuente_instrucciones = pygame.font.SysFont(None, 30)
        self.fuente_pausa = pygame.font.SysFont(None, 40)
        self.texto_instrucciones = [
            "                               D U E L O    D E   A B A C O S ",
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
        self.txopc6 = ""
        self.txopc7 = ""
        self.texto_pausa = [
            ""
        ]
        self.texto_sig_nivel = [""]

    def actualizarRender(self):
        for personaje in self.personaje:
            glPushMatrix()
            personaje["objeto"].render()
            glPopMatrix()

    def reiniciar_valores(self):
        self.pocimaX, self.pocimaY, self.pocimaZ = -2, 5, -20
        self.esferaX, self.esferaY, self.esferaZ=-2, 5, -20

    def actualizar_estado_emocional(self, nombre_personaje, emocion):
        # Actualiza la emoción de un personaje
        for personaje in self.personaje:
            if personaje["nombre"] == nombre_personaje:
                personaje["objeto"].set_emotion(emocion)  # Actualizar emoción del personaje
                print(f"{nombre_personaje} tiene ahora la emoción {emocion}")

    
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
            glPushMatrix()
            personaje["objeto"].render()
            glPopMatrix()  # Llamar al método dibujar del personaje
        
        if self.show_message:
            view.viewPort(self.display).draw_viewport2(f"Pregunta {self.iteraPregunta}:"+self.preguntaActual['texto'])
        if self.bandera_control_instrucciones:
            tx.draw_text2(self.texto_instrucciones,self.fuente_instrucciones,150,50,50)
        if self.bandera_pausa:
            self.actualizar_opciones()
            tx.draw_text2(self.texto_pausa,self.fuente_pausa,150,50,50)
        if not self.bandera_control_instrucciones and not self.bandera_pausa:
            tx.draw_text2(["Presiona SPACE para mostrar la pregunta","Presiona P para pausar el juego"],self.fuente_instrucciones,0,20,500)
            tx.draw_text2([f"Puntuación jugador 1= {self.jugador_1_score}"],self.fuente_instrucciones,0,50,20)
            tx.draw_text2([f"Puntuación jugador 2= {self.jugador_2_score}"],self.fuente_instrucciones,0,500,20)
        if self.bandera_ganador==1:
            self.actualizar_opciones_sig_nivel(1)
            tx.draw_text2(self.texto_sig_nivel,self.fuente_pausa,150,270,170)
        if self.bandera_ganador==2:
            self.actualizar_opciones_sig_nivel(2)
            tx.draw_text2(self.texto_sig_nivel,self.fuente_pausa,150,270,170)
        
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
                self.actualizar_estado_emocional(self.personaje[0]["nombre"], 0)
                self.actualizar_estado_emocional(self.personaje[1]["nombre"], 0)
                self.actualizarRender()
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
                self.actualizar_estado_emocional(self.personaje[1]["nombre"], 0)
                self.actualizar_estado_emocional(self.personaje[0]["nombre"], 0)
                self.actualizarRender()
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
                self.actualizar_estado_emocional(self.personaje[1]["nombre"], 0)
                self.actualizar_estado_emocional(self.personaje[0]["nombre"], 0)
                self.actualizarRender()
                self.show_message=True
                print('Jugador2:',self.jugador_2_score)
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
                self.actualizar_estado_emocional(self.personaje[1]["nombre"], 0)
                self.actualizar_estado_emocional(self.personaje[0]["nombre"], 0)
                self.actualizarRender()
                self.show_message=True
                print('Jugador2:',self.jugador_2_score)
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
                            self.banderaMenu=False
                            return False
                        elif self.opc_sel == 5:
                            self.banderaMenuNivel=False
                            return False
                        elif self.opc_sel == 6:
                            self.banderaMenuPrincipal=False
                            return False
                        elif self.opc_sel == 7:
                            pygame.quit()  # Cierra Pygame
                            sys.exit()
                            return False
                    self.sonido_seleccion.play()
                    # Opciones de siguiente nivel
                if self.bandera_ganador != 0:
                    if event.key == pygame.K_UP:
                        self.opciones_sig_nivel(-1)
                    if event.key == pygame.K_DOWN:
                        self.opciones_sig_nivel(1)
                    if event.key == pygame.K_RETURN or event.key == pygame.K_KP_ENTER:
                        if self.opc_sel == 1:
                            self.banderaSiguienteNivel=False
                            return False
                        elif self.opc_sel == 2:
                            pygame.mixer.music.stop()
                            pygame.mixer.music.play()
                            self.jugador_1_score=0
                            self.jugador_2_score=0
                            self.bandera_instrucciones=not self.bandera_instrucciones
                            self.bandera_control_instrucciones=not self.bandera_control_instrucciones
                            self.bandera_ganador=0
                        elif self.opc_sel == 3:
                            self.banderaMenuPrincipal=False
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
                            self.actualizar_estado_emocional(self.personaje[0]["nombre"],1 )
                            self.actualizar_estado_emocional(self.personaje[1]["nombre"], 2)
                            self.actualizarRender()

                           
                        else:
                            self.banderaJugador1 = True  # Bloquear teclas para Jugador 1
                    
                    # Jugador 2 responde
                    elif event.key in [pygame.K_DOWN, pygame.K_LEFT, pygame.K_RIGHT] and not self.banderaJugador2:
                        if self.respuesta(event.key, player=2):
                            self.jugador_2_score += 1  # Jugador 2 gana un punto
                            self.banderaColision=2
                            self.actualizar_estado_emocional(self.personaje[0]["nombre"], 2)
                            self.actualizar_estado_emocional(self.personaje[1]["nombre"], 1)
                            self.actualizarRender()
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
        self.iteraPregunta+=1
        

    def eventoNoAcertaron(self):
        print("Evento: Ambos jugadores fallaron")
        self.show_message = True  # Ocultar la pregunta
        self.iteraPregunta+=1
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
        if key in key_answer_map and key_answer_map[key] == self.preguntaActual['respuesta_correcta']:
            return True
        return False
    
    def opciones_pausa(self,opcion):
        self.opc_sel += opcion
        if self.opc_sel > 7:
            self.opc_sel = 1
        if self.opc_sel < 1:
            self.opc_sel = 7

    def actualizar_opciones(self):
        self.txopc1 = ""
        self.txopc2 = ""
        self.txopc3 = ""
        self.txopc4 = ""
        self.txopc5 = ""
        self.txopc6 = ""
        self.txopc7 = ""

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
        elif self.opc_sel == 6:
            self.txopc6 = ">"
        elif self.opc_sel == 7:
            self.txopc7 = ">"
        
        
        self.texto_pausa = [
            "P A U S A",
            "",
            self.txopc1+" Reanudar",
            self.txopc2+" Reiniciar",
            self.txopc3+" Mostrar instrucciones",
            self.txopc4+" Volver a seleccionar personajes",
            self.txopc5+" Volver a seleccionar un nivel",
            self.txopc6+" Volver al menu principal",
            self.txopc7+" Salir"
        ]
    def opciones_sig_nivel(self,opcion):
        self.opc_sel += opcion
        if self.opc_sel > 3:
            self.opc_sel = 1
        if self.opc_sel < 1:
            self.opc_sel = 3
    def actualizar_opciones_sig_nivel(self,ganador):
        self.txopc1 = ""
        self.txopc2 = ""
        self.txopc3 = ""

        if self.opc_sel == 1:
            self.txopc1 = ">"
        elif self.opc_sel == 2:
            self.txopc2 = ">"
        elif self.opc_sel == 3:
            self.txopc3 = ">"
        
        self.texto_sig_nivel = [
            f"Jugador {ganador} ganó",
            "",
            self.txopc1+" Siguiente nivel",
            self.txopc2+" Reiniciar nivel",
            self.txopc3+" Volver al Menú",
        ]
    def run(self):
        running = True
        while running:
            running = self.handle_input()
            if not self.banderaMenu:  # Si la bandera del menú es falsa, salimos del bucle
                self.cleanup()
                break
            if not self.banderaMenuNivel:
                self.cleanup()
                break
            if not self.banderaMenuPrincipal:
                self.cleanup()
                break
            if not self.banderaSiguienteNivel:
                self.cleanup()
                break
            self.draw_scene()
            pygame.time.wait(10)
           

    def cleanup(self):
        try:
        # Limpiar texturas
            if hasattr(self, 'floor_texture'):
                glDeleteTextures([self.floor_texture, self.wall_texture])
            
                # Deshabilitar luces
                glDisable(GL_LIGHT0)
                glDisable(GL_LIGHT1)
                glDisable(GL_LIGHT2)
                
                # Limpiar contexto de OpenGL
                glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
               
                pygame.mixer.music.stop()
                pygame.mixer.music.unload()
                pygame.mixer.quit()
                # Reiniciar estado de Pygame
                pygame.display.quit()
                pygame.display.init()
        except Exception as e:
            print(f"Error en cleanup: {e}")


if __name__ == "__main__":
    sP = Nivel2()
    sP.run()
