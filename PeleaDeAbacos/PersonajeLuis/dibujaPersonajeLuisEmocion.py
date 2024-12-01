from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import *


import PersonajeLuis.AccionesLuis.transformaciones as transf
import PersonajeLuis.AccionesLuis.escultor as pigmalion
import PersonajeLuis.AccionesLuis.coordenadas as coords

import time
import threading
import copy 

#hacemos deepcopy de las coordenadas para poder manipularlas sin alterar las coordenadas originales 

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
    def __init__(self, emocion):
        global brazo,cabeza,cola,cuerpo,oreja,pata,brazo2,oreja2,pata2,feliz,triste,enojado,enamorado,disgustado,aterrado,sorprendido
        self.cabeza=cabeza
        # aunque las patas son prismas, los separe para trabajar mejor con el metodo caminar
        self.patas=[pata,pata2]
        self.prismas=[cuerpo,cola]
        self.piramides=[brazo,brazo2,oreja,oreja2]
        self.expresiones=[feliz,enamorado,enojado,triste,disgustado,aterrado,sorprendido]
        self.emocion=emocion
        self.hilo=None
        self.hilo_aux=None
        self.hilo_aux2=None
        self.caminando = False
        self.position_x = 0
        self.position_z = 0

    def reiniciar_posicion(self):
        # regresamos a 0,0,0
        self.position_x = 0
        self.position_z = 0
        self.caminando = False
        # matamos los hilos de ejecucion, si es que estan activos
        if self.hilo_aux:
            self.hilo_aux = None
        if self.hilo_aux2:
            self.hilo_aux2 = None
        if self.hilo:
            self.hilo = None
        reiniciar_coords()


    def render_personaje(self, emocion):
        self.emocion=emocion
        global negro,blanco,marron,azul,plata
        pigmalion.render_esfera(self.cabeza[0],self.cabeza[1],blanco,self.expresiones[self.emocion])
        pigmalion.render_prismas(self.patas+self.prismas,[marron,marron,marron,blanco])
        pigmalion.render_piramides(self.piramides,[blanco,blanco,negro,blanco])
        
    #def cambiar_expresion(self,emocion):
       # self.emocion=emocion

    def caminar(self,mov_x, mov_y,mov_z,angulo,traslacion_x,traslacion_z):
        if not self.caminando:
            self.caminando = True
            #asignamos metodo y parametros a 2 hilos, cada uno controla una pierna distinta
            # al ser 2 hilos el angulo se duplicara, por eso en main se manda + o - 45 grados
            self.hilo_aux = threading.Thread(target=self.mover_pierna, args=(mov_x, mov_y,mov_z,angulo,traslacion_x,traslacion_z,True))
            self.hilo_aux2 = threading.Thread(target=self.mover_pierna, args=(mov_x, mov_y,mov_z,angulo,traslacion_x,traslacion_z,False))
            self.hilo_aux.daemon = True
            self.hilo_aux2.daemon = True
            self.hilo_aux.start()
            # le damos un poco de retraso al segundo hilo
            time.sleep(0.15)
            self.hilo_aux2.start()


    def mover_pierna(self, mov_x, mov_y, mov_z, angulo, bandera):
        if angulo%360 != 0:
            # obtener la posicion del centro del personaje
            centro_x = self.position_x
            centro_z = self.position_z
            
            # Trasladamos al origen
            transf.trasladar_personaje(self.cabeza, self.prismas+self.patas, 
                                     self.piramides, self.expresiones, 
                                     -centro_x, 0, -centro_z)
            
            # Rotamos al personaje
            transf.rotar_personaje(self.piramides+self.prismas+self.patas,
                                 self.expresiones, self.cabeza, angulo)
            
            # Trasladamos a donde estaba
            transf.trasladar_personaje(self.cabeza, self.prismas+self.patas,
                                     self.piramides, self.expresiones,
                                     centro_x, 0, centro_z)
            
            #matamos los hilos
            if bandera:
                self.hilo_aux = None
            else:
                self.hilo_aux2 = None
                self.caminando = False
        else:
            # Si no hay angulo para rotar solo camina
            if bandera:
                pata_aux = self.patas[0]
            else:
                pata_aux = self.patas[1]

            for i in range(3):
                #trasladamos lentamente
                transf.trasladar_pata(pata_aux, mov_x/3, mov_y/3, mov_z/3)
                time.sleep(0.15)
                transf.trasladar_personaje(self.cabeza, self.prismas,
                                         self.piramides, self.expresiones,
                                         mov_x/3, mov_y/3, mov_z/3)
                # Actualizar la posición del personaje
                self.position_x += mov_x/3
                self.position_z += mov_z/3
                time.sleep(0.15)
                transf.trasladar_pata(pata_aux, mov_x/3, mov_y/3, mov_z/3)
        
            if bandera:
                self.hilo_aux = None
            else:
                self.hilo_aux2 = None
                self.caminando = False

    def lanzamiento(self, objeto):
        #asignamos el metodo al hilo de lanzamiento
        if self.hilo is None:
            self.hilo = threading.Thread(target=self.lanzar, args=(objeto,))
            self.hilo.daemon = True
            self.hilo.start()

    def lanzar(self, objeto):
        def mover_brazo(self, valor):
            #subimos el apice del brazo 1 unidad 
            for i in range(10):
                self.piramides[0][0][4][1] += valor * 0.1
                time.sleep(0.03)

        from PersonajeLuis.AccionesLuis.pez import Pez
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
        # asignamos un hilo al metodo saltar
        self.hilo = threading.Thread(target=self.saltar, args=(mov_y,))
        self.hilo.daemon = True
        self.hilo.start()

    def saltar(self,mov_y):
        #trasladamos el personaje hacia arriba
        transf.trasladar_personaje(self.cabeza, self.prismas+self.patas,self.piramides, self.expresiones,0, mov_y, 0)
        time.sleep(0.09)
        #regresamos el personaje a su posicion
        transf.trasladar_personaje(self.cabeza, self.prismas+self.patas,self.piramides, self.expresiones,0, -mov_y, 0)
        #matamos el hilo
        self.hilo=None

    def saludo(self):
        self.hilo_aux = threading.Thread(target=self.saludar, args=())
        self.hilo_aux.daemon = True
        self.hilo_aux.start()
    
    def saludar(self):
        #subimos el brazo 2 unidades
        self.piramides[0][0][4][1] +=2.0
        
        #movemos a la izquierda 0.5 unidades
        for i in range(5):
                self.piramides[0][0][4][0] -=0.1
                time.sleep(0.09)
        
        #regresamos las 0.5 unidades a la derecha
        for i in range(5):
                self.piramides[0][0][4][0] +=0.1
                time.sleep(0.09)
        #bajamos el brazo las 2 unidades
        self.piramides[0][0][4][1] -=2.0
        self.hilo_aux=None
        
    def salto_saludo(self,mov_y):
        #hacemos un salto, un saludo y cambiamos a la cara de enamorado
        self.salto(mov_y)
        self.saludo()
        self.emocion=3