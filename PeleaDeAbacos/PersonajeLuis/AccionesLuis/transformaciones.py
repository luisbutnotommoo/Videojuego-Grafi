from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import *
import math

def trasladar_esfera(matriz_esfera,tupla_expresiones,mov_x,mov_y,mov_z):
    centro=matriz_esfera[0]
    centro[0]+=mov_x
    centro[1]+=mov_y
    centro[2]+=mov_z
    trasladar_rostro(tupla_expresiones,mov_x,mov_y,mov_z)

def trasladar_poliedros(tupla_poliedros,mov_x,mov_y,mov_z):
    # funciona con piramides y con prismas
    for lista_poliedro in tupla_poliedros:
        vertices=lista_poliedro[0]
        for vertice in vertices:
            vertice[0]+=mov_x
            vertice[1]+=mov_y
            vertice[2]+=mov_z

def trasladar_personaje(matriz_cabeza,tupla_prismas,tupla_piramides,tupla_expresiones,mov_x,mov_y,mov_z):
    trasladar_esfera(matriz_cabeza,tupla_expresiones,mov_x,mov_y,mov_z)
    trasladar_poliedros((tupla_prismas+tupla_piramides),mov_x,mov_y,mov_z)
    
    

def trasladar_rostro(tupla_expresiones,mov_x,mov_y,mov_z):
    for expresion in tupla_expresiones:
        for faccion in expresion:
            for vertice in faccion:
                vertice[0]+=mov_x
                vertice[1]+=mov_y
                vertice[2]+=mov_z


def trasladar_pata(pata,mov_x,mov_y,mov_z):
    for i in range(len(pata[0])):
        pata[0][i][0]+=mov_x
        pata[0][i][1]+=mov_y
        pata[0][i][2]+=mov_z


def rotar_personaje(tupla_personaje,expresiones,esfera, angulo):
    angulo_rad = (math.pi*angulo)/180


    #rotamos tronco y extremidades del personaje
    for extremidad in tupla_personaje:
        for vertice in extremidad[0]:
            x_aux=vertice[0]
            z_aux=vertice[2]
            vertice[0]=x_aux*math.cos(angulo_rad)+z_aux*math.sin(angulo_rad)
            vertice[2]=x_aux*-math.sin(angulo_rad)+z_aux*math.cos(angulo_rad)

    #rotamos las expresiones
    for expresion in expresiones:
        for faccion in expresion:
            for vertice in faccion:
                x_aux=vertice[0]
                z_aux=vertice[2]
                vertice[0]=x_aux*math.cos(angulo_rad)+z_aux*math.sin(angulo_rad)
                vertice[2]=x_aux*-math.sin(angulo_rad)+z_aux*math.cos(angulo_rad)    
    
    # cambiamos la posicion de la cabeza
    centro = esfera[0]
    x_aux=centro[0]
    z_aux=centro[2]
    centro[0]=x_aux*math.cos(angulo_rad)+z_aux*math.sin(angulo_rad)
    centro[2]=x_aux*-math.sin(angulo_rad)+z_aux*math.cos(angulo_rad)

    
