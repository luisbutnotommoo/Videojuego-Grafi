from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import *


from PersonajeLuis2.AccionesL import transformaciones as transf
from PersonajeLuis2.AccionesL import escultor as pigmalion
from PersonajeLuis2.AccionesL import coordenadas as coords

import time
import threading
import copy 


cuerpo=copy.deepcopy(coords.cuerpo)
cabeza=copy.deepcopy(coords.cabeza)
cola=copy.deepcopy(coords.cola)
brazo=copy.deepcopy(coords.brazo)
oreja=copy.deepcopy(coords.oreja)
pata=copy.deepcopy(coords.pata)
brazo2=copy.deepcopy(coords.brazo2)
oreja2=copy.deepcopy(coords.oreja2)
pata2=copy.deepcopy(coords.pata2)

feliz=copy.deepcopy(coords.feliz)
triste=copy.deepcopy(coords.triste)
enojado=copy.deepcopy(coords.enojado)
enamorado=copy.deepcopy(coords.enamorado)
disgustado=copy.deepcopy(coords.disgustado)
aterrado=copy.deepcopy(coords.aterrado)
sorprendido=copy.deepcopy(coords.sorprendido)

negro= (0.01,0.01,0.01)
blanco=(1,1,1)
gris=(0.5,0.5,0.5)
marron=(0.7, 0.5, 0.3)
marron_oscuro = (0.49, 0.35, 0.21)
plata=(0.9, 0.9, 0.8)
azul=(0.5, 0.8, 1)

def reiniciar_coords():
    global brazo,cabeza,cola,cuerpo,oreja,pata,brazo2,oreja2,pata2,feliz,triste,enojado,enamorado,disgustado,aterrado,sorprendido
    cuerpo = copy.deepcopy(coords.cuerpo)
    cabeza = copy.deepcopy(coords.cabeza)
    cola = copy.deepcopy(coords.cola)
    brazo = copy.deepcopy(coords.brazo)
    oreja = copy.deepcopy(coords.oreja)
    pata = copy.deepcopy(coords.pata)
    brazo2 = copy.deepcopy(coords.brazo2)
    oreja2 = copy.deepcopy(coords.oreja2)
    pata2 = copy.deepcopy(coords.pata2)
    feliz = copy.deepcopy(coords.feliz)
    triste = copy.deepcopy(coords.triste)
    enojado = copy.deepcopy(coords.enojado)
    enamorado = copy.deepcopy(coords.enamorado)
    disgustado=copy.deepcopy(coords.disgustado)
    aterrado=copy.deepcopy(coords.aterrado)
    sorprendido=copy.deepcopy(coords.sorprendido)

class Personaje():
    def __init__(self):
        global brazo,cabeza,cola,cuerpo,oreja,pata,brazo2,oreja2,pata2,feliz,triste,enojado,enamorado,disgustado,aterrado,sorprendido
        self.cabeza=cabeza
        self.patas=[pata,pata2]
        self.prismas=[cuerpo,cola]
        self.piramides=[brazo,brazo2,oreja,oreja2]
        self.expresiones=[feliz,triste,enojado,enamorado,disgustado,aterrado,sorprendido]
        self.emocion=0
        self.hilo=None
        self.hilo_aux=None
        self.hilo_aux2=None
        self.caminando = False
        self.position_x = 0
        self.position_z = 0

    def reiniciar_posicion(self):
        self.position_x = 0
        self.position_z = 0
        self.caminando = False
        if self.hilo_aux:
            self.hilo_aux = None
        if self.hilo_aux2:
            self.hilo_aux2 = None
        if self.hilo:
            self.hilo = None
        reiniciar_coords()


    def render_personaje(self):
        global negro,blanco,marron,azul,plata
        pigmalion.render_esfera(self.cabeza[0],self.cabeza[1],blanco,self.expresiones[self.emocion])
        pigmalion.render_prismas(self.patas+self.prismas,[marron,marron,marron,blanco])
        pigmalion.render_piramides(self.piramides,[blanco,blanco,negro,blanco])
        
    def cambiar_expresion(self,emocion):
        self.emocion=emocion

    def caminar(self,mov_x, mov_y,mov_z,angulo,traslacion_x,traslacion_z):
        if not self.caminando:
            self.caminando = True
            self.hilo_aux = threading.Thread(target=self.mover_pierna, args=(mov_x, mov_y,mov_z,angulo,traslacion_x,traslacion_z,True))
            self.hilo_aux2 = threading.Thread(target=self.mover_pierna, args=(mov_x, mov_y,mov_z,angulo,traslacion_x,traslacion_z,False))
            self.hilo_aux.daemon = True
            self.hilo_aux2.daemon = True
            self.hilo_aux.start()
            time.sleep(0.15)
            self.hilo_aux2.start()


    def mover_pierna(self, mov_x, mov_y, mov_z, angulo, traslacion_x, traslacion_z, bandera):
        if angulo%360 != 0:
            # Obtener el centro actual del personaje
            centro_x = self.position_x
            centro_z = self.position_z
            
            # 1. Trasladar al origen
            transf.trasladar_personaje(self.cabeza, self.prismas+self.patas, 
                                     self.piramides, self.expresiones, 
                                     -centro_x, 0, -centro_z)
            
            # 2. Rotar
            transf.rotar_personaje(self.piramides+self.prismas+self.patas,
                                 self.expresiones, self.cabeza, angulo)
            
            # 3. Regresar a la posición
            transf.trasladar_personaje(self.cabeza, self.prismas+self.patas,
                                     self.piramides, self.expresiones,
                                     centro_x, 0, centro_z)
            
            if bandera:
                self.hilo_aux = None
            else:
                self.hilo_aux2 = None
                self.caminando = False
        else:
            # El código existente para el movimiento lineal
            if bandera:
                pata_aux = self.patas[0]
            else:
                pata_aux = self.patas[1]

            for i in range(3):
                transf.trasladar_pata(pata_aux, 0, mov_x/3, mov_y/3, mov_z/3)
                time.sleep(0.15)
                transf.trasladar_personaje(self.cabeza, self.prismas,
                                         self.piramides, self.expresiones,
                                         mov_x/3, mov_y/3, mov_z/3)
                # Actualizar la posición del personaje
                self.position_x += mov_x/3
                self.position_z += mov_z/3
                time.sleep(0.15)
                transf.trasladar_pata(pata_aux, 4, mov_x/3, mov_y/3, mov_z/3)
        
            if bandera:
                self.hilo_aux = None
            else:
                self.hilo_aux2 = None
                self.caminando = False

    def lanzamiento(self, objeto):
        if self.hilo is None:
            self.hilo = threading.Thread(target=self.lanzar, args=(objeto,))
            self.hilo.daemon = True
            self.hilo.start()

    def lanzar(self, objeto):
        def mover_brazo(self, valor):
            for i in range(10):
                self.piramides[0][0][4][1] += valor * 0.1
                time.sleep(0.03)

        from PersonajeLuis2.AccionesL.pez import Pez
        if isinstance(objeto, Pez):
            try:
                mover_brazo(self, 1)
                time.sleep(0.08)
                objeto.lanzar()  # Lanzar el pez
                time.sleep(0.08)
                mover_brazo(self, -1)
            finally:
                self.hilo = None

    def salto(self,mov_y):
        self.hilo = threading.Thread(target=self.saltar, args=(mov_y,))
        self.hilo.daemon = True
        self.hilo.start()

    def saltar(self,mov_y):
        transf.trasladar_personaje(self.cabeza, self.prismas+self.patas,self.piramides, self.expresiones,0, mov_y, 0)
        time.sleep(0.09)
        transf.trasladar_personaje(self.cabeza, self.prismas+self.patas,self.piramides, self.expresiones,0, -mov_y, 0)
        self.hilo=None

    def saludo(self):
        self.hilo_aux = threading.Thread(target=self.saludar, args=())
        self.hilo_aux.daemon = True
        self.hilo_aux.start()
    
    def saludar(self):
        self.piramides[0][0][4][1] +=2.0
        
        for i in range(5):
                self.piramides[0][0][4][0] -=0.1
                time.sleep(0.09)
        
        for i in range(5):
                self.piramides[0][0][4][0] +=0.1
                time.sleep(0.09)
        
        self.piramides[0][0][4][1] -=2.0
        self.hilo_aux=None
        
    def salto_saludo(self,mov_y):
        self.salto(mov_y)
        self.saludo()
        self.emocion=3