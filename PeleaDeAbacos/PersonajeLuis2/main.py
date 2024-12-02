import math
import glfw
from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import *
import numpy as np
from PersonajeLuis2.AccionesL import personaje as perso
from PersonajeLuis2.AccionesL import escenario as escena
from PersonajeLuis2.AccionesL import sonido
import tkinter.messagebox as mbox
from PersonajeLuis2.AccionesL import mensajes
from PersonajeLuis2.AccionesL.pez import Pez
from PersonajeLuis2.AccionesL.enemigo import Enemigo


bandera_pop_up,mensaje_pop_up=False,0

# configuraciones personaje
heisenpurr = perso.Personaje()
pecesito=None
enemigo=None
angulo_personaje=0
traslacion_x=0.0
traslacion_z=0.0

# Configuraciones de la cámara
angulo_vertical = 40.95
angulo_horizontal = -5.31

radio = 11.0

mouse_sensibilidad = 0.09

posx_cursor_anterior, posy_cursor_anterior = 400, 300

objetivo_x, objetivo_y, objetivo_z = 0, 4, 0

cam_x, cam_y, cam_z = 0, 0, 0

velocidad_camara = 0.1
velocidad_zoom = 0.5

bloqueo_camara = False
cursor_activo = False

index_esc=0


def inicializar_ventana():
    if not glfw.init():
        raise Exception("No se pudo inicializar GLFW")

    window = glfw.create_window(900, 900, "Las maravillosas desventuras de Heisenpurr", None, None)
    if not window:
        glfw.terminate()
        raise Exception("No se pudo crear la ventana")
    
    glfw.make_context_current(window)
    glfw.set_input_mode(window, glfw.CURSOR, glfw.CURSOR_DISABLED)
    configurar_openGL()
    
    return window

def configurar_openGL():
    global bandera_pop_up
    glViewport(0, 0, 900, 900)
    glMatrixMode(GL_PROJECTION)
    gluPerspective(45, 1, 0.1, 100.0)
    glMatrixMode(GL_MODELVIEW)


def render_pop_up():
    global mensaje_pop_up

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

    mensajes.mostrar_imagen(mensaje_pop_up)

    glDisable(GL_BLEND)
    
    glMatrixMode(GL_PROJECTION)
    glPopMatrix()
    
    glMatrixMode(GL_MODELVIEW)
    glPopMatrix()

    glViewport(*viewport)
        

def renderizar_escena():
    global heisenpurr, pecesito,bandera_pop_up,mensaje_pop_up,enemigo
    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
    glEnable(GL_DEPTH_TEST)
    
    glLoadIdentity()
    gluLookAt(cam_x, cam_y, cam_z, objetivo_x, objetivo_y, objetivo_z, 0, 1, 0)
    
    if bandera_pop_up:
        render_pop_up()

    escena.render_escenario()
    heisenpurr.render_personaje()


    if pecesito is not None:
        pecesito.render_pez()
        if pecesito.verificar_colision(2, 3.13, 7,0.01):
            enemigo=None
        if not pecesito.render_pez():
            pecesito = None

    if enemigo is not None:
        enemigo.render_enemigo()


def movimiento_mouse(window, xpos, ypos):
    global angulo_horizontal, angulo_vertical, posx_cursor_anterior, posy_cursor_anterior
    if not bloqueo_camara:
        delta_x = xpos - posx_cursor_anterior
        delta_y = ypos - posy_cursor_anterior
        angulo_horizontal += delta_x * mouse_sensibilidad
        angulo_vertical += delta_y * mouse_sensibilidad
        angulo_vertical = max(-89.0, min(89.0, angulo_vertical))
        posx_cursor_anterior, posy_cursor_anterior = xpos, ypos

def actualizar_camara():
    global cam_x, cam_y, cam_z
    if not bloqueo_camara:
        cam_x = radio * np.cos(np.radians(angulo_vertical)) * np.sin(np.radians(angulo_horizontal))
        cam_y = (radio * np.sin(np.radians(angulo_vertical))) - 0.6
        cam_z = (radio * np.cos(np.radians(angulo_vertical)) * np.cos(np.radians(angulo_horizontal))) + 1.5

def mover_camara(dx, dy, dz):
    global objetivo_x, objetivo_y, objetivo_z, cam_x, cam_y, cam_z
    objetivo_x += dx
    objetivo_y += dy
    objetivo_z += dz
    cam_x += dx
    cam_y += dy
    cam_z += dz

def reiniciar_camara():
    global angulo_vertical, angulo_horizontal, cam_x, cam_y, cam_z,objetivo_x,objetivo_y,objetivo_z,heisenpurr
    
    angulo_vertical = 40.95
    angulo_horizontal = -5.31
    cam_x, cam_y, cam_z = 0, 0, 0   
    objetivo_x,objetivo_y,objetivo_z = 0,4,0

    heisenpurr=None
    heisenpurr=perso.Personaje()


def activar_cursor(window):
    global cursor_activo
    cursor_activo= not cursor_activo
    if cursor_activo:
        glfw.set_input_mode(window, glfw.CURSOR, glfw.CURSOR_NORMAL)
    else:
        glfw.set_input_mode(window, glfw.CURSOR, glfw.CURSOR_DISABLED)

def eventos_teclado(window, key, scancode, action, mods):
    global bloqueo_camara, index_esc,pecesito,angulo_personaje,bandera_pop_up,mensaje_pop_up,enemigo
    if key == glfw.KEY_ESCAPE and action== glfw.PRESS:
        glfw.set_window_should_close(window, True)

    if key == glfw.KEY_ENTER and action== glfw.PRESS:
        heisenpurr.reiniciar_posicion()
        reiniciar_camara()
        angulo_personaje = 0

    if key == glfw.KEY_SPACE and action== glfw.PRESS:
        heisenpurr.salto(0.8)

    if key == glfw.KEY_L:
        heisenpurr.saludo()

    if key == glfw.KEY_H:
        heisenpurr.salto_saludo(0.4)


    if key == glfw.KEY_O and action== glfw.PRESS:
        activar_cursor(window)

    if key == glfw.KEY_B and action== glfw.PRESS:
        bloqueo_camara = not bloqueo_camara

    if key == glfw.KEY_E and action== glfw.PRESS:
        index_esc+=1

        if index_esc==2:
            enemigo=Enemigo()

        if index_esc>=7:
            index_esc=0   

        sonido.stop()
        escena.set_escenario(index_esc)
        sonido.set_archivo(index_esc)
        sonido.play()
        
    if key==glfw.KEY_S and action== glfw.PRESS:
        sonido.play()

    if key==glfw.KEY_D and action== glfw.PRESS:
        sonido.stop()

    if key==glfw.KEY_A and action== glfw.PRESS:
        reiniciar_camara()

    if key == glfw.KEY_M and action== glfw.PRESS:
        mensaje_pop_up=0 
        bandera_pop_up = not bandera_pop_up
        

    if key == glfw.KEY_W and action== glfw.PRESS:
        mensaje_pop_up=1
        bandera_pop_up = not bandera_pop_up
        
        
    if key == glfw.KEY_P and action==glfw.PRESS:
        if pecesito is None:
            pecesito=Pez()
        else:
            heisenpurr.lanzamiento(pecesito)

    if key == glfw.KEY_1 and action== glfw.PRESS:
        heisenpurr.cambiar_expresion(0)
        sonido.maullido(1)

    if key == glfw.KEY_2 and action== glfw.PRESS:
        heisenpurr.cambiar_expresion(1)
        sonido.maullido(2)

    if key == glfw.KEY_3 and action== glfw.PRESS:
        heisenpurr.cambiar_expresion(2)
        sonido.maullido(3)

    if key == glfw.KEY_4 and action== glfw.PRESS:
        heisenpurr.cambiar_expresion(3)
        sonido.maullido(4)

    if key == glfw.KEY_5 and action== glfw.PRESS:
        heisenpurr.cambiar_expresion(4)
        sonido.maullido(5)

    if key == glfw.KEY_6 and action== glfw.PRESS:
        heisenpurr.cambiar_expresion(5)
        sonido.maullido(3)
    
    if key == glfw.KEY_7 and action== glfw.PRESS:
        heisenpurr.cambiar_expresion(6)
        sonido.maullido(6)

    if mods & glfw.MOD_SHIFT:
        comando_shift(key,action)
    else:
        teclas_direccion(key, action)
    

def teclas_direccion(key, action):
    global angulo_personaje
    if action == glfw.PRESS or action == glfw.REPEAT:
        if key == glfw.KEY_UP:
            direccion = mover_personaje()
            if direccion is not None:
                heisenpurr.caminar(*direccion)
            else:
                # Movimiento hacia adelante basado en el ángulo actual
                dx = 0.3 * math.sin(math.radians(angulo_personaje))
                dz = 0.3 * math.cos(math.radians(angulo_personaje))
                heisenpurr.caminar(dx, 0, dz, 0, 0, 0)
            
        elif key == glfw.KEY_RIGHT:
            # Rotación a la derecha sobre su propio eje
            heisenpurr.caminar(0, 0, 0, -45, heisenpurr.position_x, heisenpurr.position_z)
            angulo_personaje -= 45
            
        elif key == glfw.KEY_LEFT:
            # Rotación a la izquierda sobre su propio eje
            heisenpurr.caminar(0, 0, 0, 45, heisenpurr.position_x, heisenpurr.position_z)
            angulo_personaje += 45

def mover_personaje():
    global angulo_personaje
    mov = None
    signo=1
    if angulo_personaje!=0:
        signo=angulo_personaje/abs(angulo_personaje)

    if abs(angulo_personaje) == 0:
        mov = [0, 0, 0.3, 0, 0, 0]
    elif abs(angulo_personaje) == 45:
        mov = [signo*0.3, 0, 0, 0, 0, 0]
    elif abs(angulo_personaje) == 90:
        mov = [0, 0, -0.3, 0, 0, 0]
    elif abs(angulo_personaje) == 135:
        mov = [-signo*0.3, 0, 0, 0, 0, 0]
    elif abs(angulo_personaje) >= 180:
        angulo_personaje=0
        mov = [0, 0, 0.3, 0, 0, 0]


    return mov

def comando_shift(key,action):
    global radio, heisenpurr
    if action == glfw.PRESS or action == glfw.REPEAT:
        if key == glfw.KEY_UP:
            mover_camara(0, velocidad_camara, 0)
        elif key == glfw.KEY_DOWN:
            mover_camara(0, -velocidad_camara, 0)
        elif key == glfw.KEY_RIGHT:
            mover_camara(velocidad_camara, 0, 0)
        elif key == glfw.KEY_LEFT:
            mover_camara(-velocidad_camara, 0, 0)
        elif key == glfw.KEY_PAGE_UP:
            mover_camara(0, 0, -velocidad_camara)
        elif key == glfw.KEY_PAGE_DOWN:
            mover_camara(0, 0, velocidad_camara)    
        elif key == glfw.KEY_Y:
            radio = max(1.0, radio - velocidad_zoom)
        elif key == glfw.KEY_U:
            radio = min(20.0, radio + velocidad_zoom)
def main():
    window = inicializar_ventana()

    glfw.set_key_callback(window, eventos_teclado)
    glfw.set_cursor_pos_callback(window, movimiento_mouse)

    while not glfw.window_should_close(window):
        actualizar_camara()
        renderizar_escena()
        glfw.swap_buffers(window)
        glfw.poll_events()

    
    glfw.terminate()



if __name__ == "__main__":
    main()

