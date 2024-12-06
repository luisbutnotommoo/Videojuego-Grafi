import math
import glfw
import pygame
from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import *
import numpy as np
from PersonajeLuis2.AccionesL import personaje as perso

from PersonajeLuis2.AccionesL import sonido

from PersonajeLuis2.AccionesL import mensajes

from PersonajeLuis2.AccionesL.escenario3 import Escenario
from PersonajeLuis2.AccionesL.pez import Pez

class PersonajeLuis:
    def __init__(self):
        self.bandera_pop_up, self.mensaje_pop_up = True,2

        # configuraciones personaje
        self.heisenpurr = perso.Personaje()
        self.pecesito=None
        self.enemigo=None
        self.angulo_personaje=0
        self.traslacion_x=0.0
        self.traslacion_z=0.0

        # Configuraciones de la cámara
        self.angulo_vertical = 40.95
        self.angulo_horizontal = -5.31

        self.radio = 11.0

        self.mouse_sensibilidad = 0.09

        self.posx_cursor_anterior, self.posy_cursor_anterior = 400, 300

        self.objetivo_x, self.objetivo_y, self.objetivo_z = 0, 4, 0

        self.cam_x, self.cam_y, self.cam_z = 0, 0, 0

        self.velocidad_camara = 0.1
        self.velocidad_zoom = 0.5

        self.bloqueo_camara = False
        self.cursor_activo = False

        self.index_esc=0

        pygame.init()
        pygame.mixer.init()
        

    def inicializar_ventana(self):
        if not glfw.init():
            raise Exception("No se pudo inicializar GLFW")

        window = glfw.create_window(900, 900, "Las maravillosas desventuras de Heisenpurr", None, None)
        if not window:
            glfw.terminate()
            raise Exception("No se pudo crear la ventana")
        
        glfw.make_context_current(window)
        glfw.set_input_mode(window, glfw.CURSOR, glfw.CURSOR_DISABLED)
        self.configurar_openGL()
        
        self.esc = Escenario()
        
        return window

    def configurar_openGL(self):
        glViewport(0, 0, 900, 900)
        glMatrixMode(GL_PROJECTION)
        gluPerspective(45, 1, 0.1, 100.0)
        glMatrixMode(GL_MODELVIEW)


    def render_pop_up(self):
        #global mensaje_pop_up

        viewport = glGetIntegerv(GL_VIEWPORT)

        window_width, window_height = 900, 900  
        popup_width, popup_height = 600, 600 
        x = (window_width - popup_width) // 2
        y = (window_height - popup_height) // 2
        
        glViewport(x, y, popup_width, popup_height)
        glMatrixMode(GL_PROJECTION)
        glPushMatrix()
        glLoadIdentity()
        glOrtho(0, popup_width, 0, popup_height, -1, 1)
        
        glMatrixMode(GL_MODELVIEW)
        glPushMatrix()
        glLoadIdentity()

        glEnable(GL_BLEND)
        glBlendFunc(GL_SRC_ALPHA, GL_ONE_MINUS_SRC_ALPHA)

        mensajes.mostrar_imagen(self.mensaje_pop_up)

        glDisable(GL_BLEND)
        
        glMatrixMode(GL_PROJECTION)
        glPopMatrix()
        
        glMatrixMode(GL_MODELVIEW)
        glPopMatrix()

        glViewport(*viewport)
            

    def renderizar_escena(self):
        glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
        glEnable(GL_DEPTH_TEST)
        
        glLoadIdentity()
        gluLookAt(self.cam_x, self.cam_y, self.cam_z, self.objetivo_x, self.objetivo_y, self.objetivo_z, 0, 1, 0)
        
        if self.bandera_pop_up:
            self.render_pop_up()

        #escena.render_escenario()
        self.esc.render_escenario()
        self.heisenpurr.render_personaje()

        if self.pecesito is not None:
            self.pecesito.render_pez()
            if self.pecesito.verificar_colision(2, 3.13, 7,0.01):
                self.enemigo=None
            if not self.pecesito.render_pez():
                self.pecesito = None



    def movimiento_mouse(self, window, xpos, ypos):
        if not self.bloqueo_camara:
            delta_x = xpos - self.posx_cursor_anterior
            delta_y = ypos - self.posy_cursor_anterior
            self.angulo_horizontal += delta_x * self.mouse_sensibilidad
            self.angulo_vertical += delta_y * self.mouse_sensibilidad
            self.angulo_vertical = max(-89.0, min(89.0, self.angulo_vertical))
            self.posx_cursor_anterior, self.posy_cursor_anterior = xpos, ypos

    def actualizar_camara(self):
        if not self.bloqueo_camara:
            self.cam_x = self.radio * np.cos(np.radians(self.angulo_vertical)) * np.sin(np.radians(self.angulo_horizontal))
            self.cam_y = (self.radio * np.sin(np.radians(self.angulo_vertical))) - 0.6
            self.cam_z = (self.radio * np.cos(np.radians(self.angulo_vertical)) * np.cos(np.radians(self.angulo_horizontal))) + 1.5

    def mover_camara(self, dx, dy, dz):
        self.objetivo_x += dx
        self.objetivo_y += dy
        self.objetivo_z += dz
        self.cam_x += dx
        self.cam_y += dy
        self.cam_z += dz

    def reiniciar_camara(self):
        
        self.angulo_vertical = 40.95
        self.angulo_horizontal = -5.31
        self.cam_x, self.cam_y, self.cam_z = 0, 0, 0   
        self.objetivo_x, self.objetivo_y, self.objetivo_z = 0,4,0

        self.heisenpurr=None
        self.heisenpurr=perso.Personaje()


    def activar_cursor(self, window):
        self.cursor_activo = not self.cursor_activo
        if self.cursor_activo:
            glfw.set_input_mode(window, glfw.CURSOR, glfw.CURSOR_NORMAL)
        else:
            glfw.set_input_mode(window, glfw.CURSOR, glfw.CURSOR_DISABLED)

    def eventos_teclado(self, window, key, scancode, action, mods):
        if key == glfw.KEY_ESCAPE and action== glfw.PRESS:
            glfw.set_window_should_close(window, True)

        if key == glfw.KEY_ENTER and action== glfw.PRESS:
            self.heisenpurr.reiniciar_posicion()
            self.reiniciar_camara()
            self.angulo_personaje = 0

        if key == glfw.KEY_SPACE and action== glfw.PRESS:
            self.heisenpurr.salto(0.8)

        if key == glfw.KEY_L:
            self.heisenpurr.saludo()

        if key == glfw.KEY_H:
            self.heisenpurr.salto_saludo(0.4)


        if key == glfw.KEY_O and action== glfw.PRESS:
            self.activar_cursor(window)

        if key == glfw.KEY_B and action== glfw.PRESS:
            self.bloqueo_camara = not self.bloqueo_camara

        if key == glfw.KEY_E and action== glfw.PRESS:
            self.index_esc+=1

            if self.index_esc>4:
                self.index_esc=0   

            sonido.stop()
            self.esc.set_escenario(self.index_esc)
            sonido.set_archivo(self.index_esc)
            sonido.play()
            
        if key==glfw.KEY_S and action== glfw.PRESS:
            sonido.play()

        if key==glfw.KEY_D and action== glfw.PRESS:
            sonido.stop()

        if key==glfw.KEY_A and action== glfw.PRESS:
            self.reiniciar_camara()

        if key == glfw.KEY_M and action== glfw.PRESS:
            self.mensaje_pop_up=0 #Pulsa Esc para quitar el demo de heisenpurr e ir al nivel o pulsa M para quitar este pop up
            self.bandera_pop_up = not self.bandera_pop_up
            

        if key == glfw.KEY_W and action== glfw.PRESS:
            self.mensaje_pop_up=1 
            self.bandera_pop_up = not self.bandera_pop_up

        if key == glfw.KEY_F and action== glfw.PRESS:
            self.mensaje_pop_up=3#Instrucciones heisenpurr
            sonido.stop()
            sonido.play()
             
            
            
        if key == glfw.KEY_P and action==glfw.PRESS:
            if self.pecesito is None:
                self.pecesito=Pez()
            else:
                self.heisenpurr.lanzamiento(self.pecesito)

        if key == glfw.KEY_1 and action== glfw.PRESS:
            self.heisenpurr.cambiar_expresion(0)
            sonido.maullido(1)

        if key == glfw.KEY_2 and action== glfw.PRESS:
            self.heisenpurr.cambiar_expresion(1)
            sonido.maullido(2)

        if key == glfw.KEY_3 and action== glfw.PRESS:
            self.heisenpurr.cambiar_expresion(2)
            sonido.maullido(3)

        if key == glfw.KEY_4 and action== glfw.PRESS:
            self.heisenpurr.cambiar_expresion(3)
            sonido.maullido(4)

        if key == glfw.KEY_5 and action== glfw.PRESS:
            self.heisenpurr.cambiar_expresion(4)
            sonido.maullido(5)

        if key == glfw.KEY_6 and action== glfw.PRESS:
            self.heisenpurr.cambiar_expresion(5)
            sonido.maullido(3)
        
        if key == glfw.KEY_7 and action== glfw.PRESS:
            self.heisenpurr.cambiar_expresion(6)
            sonido.maullido(6)

        if mods & glfw.MOD_SHIFT:
            self.comando_shift(key,action)
        else:
            self.teclas_direccion(key, action)
        

    def teclas_direccion(self, key, action):
        if action == glfw.PRESS or action == glfw.REPEAT:
            if key == glfw.KEY_UP:
                direccion = self.mover_personaje()
                if direccion is not None:
                    self.heisenpurr.caminar(*direccion)
                else:
                    # Movimiento hacia adelante basado en el ángulo actual
                    dx = 0.3 * math.sin(math.radians(self.angulo_personaje))
                    dz = 0.3 * math.cos(math.radians(self.angulo_personaje))
                    self.heisenpurr.caminar(dx, 0, dz, 0, 0, 0)
                
            elif key == glfw.KEY_RIGHT:
                # Rotación a la derecha sobre su propio eje
                self.heisenpurr.caminar(0, 0, 0, -45, self.heisenpurr.position_x, self.heisenpurr.position_z)
                self.angulo_personaje -= 45
                
            elif key == glfw.KEY_LEFT:
                # Rotación a la izquierda sobre su propio eje
                self.heisenpurr.caminar(0, 0, 0, 45, self.heisenpurr.position_x, self.heisenpurr.position_z)
                self.angulo_personaje += 45

    def mover_personaje(self):
        mov = None
        signo=1
        if self.angulo_personaje!=0:
            signo=self.angulo_personaje/abs(self.angulo_personaje)

        if abs(self.angulo_personaje) == 0:
            mov = [0, 0, 0.3, 0, 0, 0]
        elif abs(self.angulo_personaje) == 45:
            mov = [signo*0.3, 0, 0, 0, 0, 0]
        elif abs(self.angulo_personaje) == 90:
            mov = [0, 0, -0.3, 0, 0, 0]
        elif abs(self.angulo_personaje) == 135:
            mov = [-signo*0.3, 0, 0, 0, 0, 0]
        elif abs(self.angulo_personaje) >= 180:
            self.angulo_personaje=0
            mov = [0, 0, 0.3, 0, 0, 0]
        return mov

    def comando_shift(self, key,action):
        if action == glfw.PRESS or action == glfw.REPEAT:
            if key == glfw.KEY_UP:
                self.mover_camara(0, self.velocidad_camara, 0)
            elif key == glfw.KEY_DOWN:
                self.mover_camara(0, -self.velocidad_camara, 0)
            elif key == glfw.KEY_RIGHT:
                self.mover_camara(self.velocidad_camara, 0, 0)
            elif key == glfw.KEY_LEFT:
                self.mover_camara(-self.velocidad_camara, 0, 0)
            elif key == glfw.KEY_PAGE_UP:
                self.mover_camara(0, 0, -self.velocidad_camara)
            elif key == glfw.KEY_PAGE_DOWN:
                self.mover_camara(0, 0, self.velocidad_camara)    
            elif key == glfw.KEY_Y:
                self.radio = max(1.0, self.radio - self.velocidad_zoom)
            elif key == glfw.KEY_U:
                self.radio = min(20.0, self.radio + self.velocidad_zoom)

    def run(self):
        window = self.inicializar_ventana()

        glfw.set_key_callback(window, self.eventos_teclado)
        glfw.set_cursor_pos_callback(window, self.movimiento_mouse)

        while not glfw.window_should_close(window):
            self.actualizar_camara()
            self.renderizar_escena()
            glfw.swap_buffers(window)
            glfw.poll_events()

        
        glfw.terminate()

if __name__ == "__main__":
    juego = PersonajeLuis()  # Crear instancia de la clase
    juego.run()             # Llamar al método main de la instancia
