from OpenGL.GL import *
from OpenGL.GLU import *
import numpy as np
import time
import copy
from PersonajeLuis2.AccionesL import colisiones

class Pez:
    def __init__(self):
        self.tiempo_inicio = None
        self.esta_en_movimiento = False
        self.toco_suelo = False
    
        self.velocidad_inicial = [0.0, 1.3, 0.6] 
        self.gravedad = -9.8
        
        # Dimensiones del área de colisión
        self.width = 0.6  
        self.height = 0.3  
        self.depth = 0.3   

        self.cuerpo_vertices = []
        segments = 30
        for i in range(segments):
            angle = 2 * np.pi * i / segments
            x = 0.3 * np.cos(angle)
            z = 0.15 * np.sin(angle)
            self.cuerpo_vertices.append((x, z, 0))

        self.tail_vertices = [
            (0.3, 0, 0),
            (0.45, 0.15, 0),
            (0.45, -0.15, 0),
        ]
        self.actualizar_posicion()

    def verificar_colision(self, otro_objeto_x, otro_objeto_y, otro_objeto_z, otro_height):
        return colisiones.rombo_collision(
            self.posicion[0], self.posicion[1], self.posicion[2],  # Posición del pez
            self.width, self.height, self.depth,                    # Dimensiones del pez
            otro_objeto_x, otro_objeto_y, otro_objeto_z,           # Posición del otro objeto
            otro_height                                            # Altura del otro objeto
        )


    def lanzar(self):
        if not self.esta_en_movimiento:
            self.tiempo_inicio = time.time()
            self.esta_en_movimiento = True
            self.actualizar_posicion()
            self.toco_suelo = False

    def actualizar_posicion(self): 
        if self.esta_en_movimiento:
            tiempo = time.time() - self.tiempo_inicio

            self.posicion[0] = self.posicion[0] + self.velocidad_inicial[0] * tiempo 
            self.posicion[1] = (self.posicion[1] + 
                              self.velocidad_inicial[1] * tiempo + 
                              0.5 * self.gravedad * tiempo * tiempo)
            self.posicion[2] = self.posicion[2] + self.velocidad_inicial[2] * tiempo 
            
            if self.posicion[1] <= 0.01:
                self.esta_en_movimiento = False
                self.toco_suelo = True
        
        else:                 
            
            from controlaClase import instanciaLuis
            self.posicion = copy.deepcopy(instanciaLuis.heisenpurr.piramides[0][0][4])

    def render_pez(self):
        if self.toco_suelo:
            return False
            
        self.actualizar_posicion()
        
        glPushMatrix()
        glTranslatef(self.posicion[0], self.posicion[1], self.posicion[2])
        
        if self.esta_en_movimiento:
            tiempo = time.time() - self.tiempo_inicio

            angulo_x = np.arctan2(self.velocidad_inicial[1] + self.gravedad * tiempo, 
                                abs(self.velocidad_inicial[2])) * 180 / np.pi

            glRotatef(90, 0, 1, 0) 
            glRotatef(angulo_x, 1, 0, 0)  

            glRotatef(tiempo * 180, 0, 0, 1)
        else:
            glRotatef(90, 0, 1, 0)
        
        # Dibujar el cuerpo
        glColor3f(0.5, 0.7, 1.0)
        glBegin(GL_TRIANGLE_FAN)
        glVertex3f(0, 0, 0)
        for vertex in self.cuerpo_vertices:
            glVertex3fv(vertex)
        glVertex3fv(self.cuerpo_vertices[0])
        glEnd()

        # Dibujar la cola
        glColor3f(0.4, 0.6, 0.9)
        glBegin(GL_TRIANGLES)
        for vertex in self.tail_vertices:
            glVertex3fv(vertex)
        glEnd()

        # Dibujar el ojo
        glColor3f(0, 0, 0)
        glPointSize(7.5)
        glBegin(GL_POINTS)
        glVertex3f(-0.1, 0.05, 0)
        glEnd()
        
        glPopMatrix()
        
        return True