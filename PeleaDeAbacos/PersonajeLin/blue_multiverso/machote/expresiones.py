import pygame
from pygame.locals import *
from OpenGL.GL import *
from OpenGL.GLU import *
import math


def draw_boca():
    glBegin(GL_POLYGON)
    glColor3f(0.0, 1.0, 1.0)  # Color cyan
    for point in boca1:
        glVertex3f(point[0], point[1], point[2])
    glEnd()

def draw_bocaenojada():
    glBegin(GL_POLYGON)
    glColor3f(0.0, 1.0, 1.0)  # Color cyan
    for point in bocaenojada:
        glVertex3f(point[0], point[1], point[2])
    glEnd()    


def draw_ojo():
    glBegin(GL_POLYGON)
    glColor3f(0.0, 1.0, 1.0)  # Color cyan
    for point in ojo1:
        glVertex3f(point[0], point[1], point[2])
    glEnd()


def draw_ojo2():
    glBegin(GL_POLYGON)
    glColor3f(0.0, 1.0, 1.0)  # Color cyan
    for point in ojo2:
        glVertex3f(point[0], point[1], point[2])
    glEnd() 

def draw_ceja():
    glBegin(GL_POLYGON)
    glColor3f(0.0, 1.0, 1.0)  # Color cyan
    for point in ceja:
        glVertex3f(point[0], point[1], point[2])
    glEnd() 

def draw_ceja2():
    glBegin(GL_POLYGON)
    glColor3f(0.0, 1.0, 1.0)  # Color cyan
    for point in ceja2:
        glVertex3f(point[0], point[1], point[2])
    glEnd()      

def draw_cejatriste():
    glBegin(GL_POLYGON)
    glColor3f(0.0, 1.0, 1.0)  # Color cyan
    for point in cejatriste:
        glVertex3f(point[0], point[1], point[2])
    glEnd() 

def draw_cejatriste2():
    glBegin(GL_POLYGON)
    glColor3f(0.0, 1.0, 1.0)  # Color cyan
    for point in cejatriste2:
        glVertex3f(point[0], point[1], point[2])
    glEnd()     

def draw_bocatriste():
    glBegin(GL_POLYGON)
    glColor3f(0.0, 1.0, 1.0)  # Color cyan
    for point in bocatriste:
        glVertex3f(point[0], point[1], point[2])
    glEnd()     


def draw_cejagui1():
    glBegin(GL_POLYGON)
    glColor3f(0.0, 1.0, 1.0)  # Color cyan
    for point in cejagui:
        glVertex3f(point[0], point[1], point[2])
    glEnd()    

def draw_ojogui1():
    glBegin(GL_POLYGON)
    glColor3f(0.0, 1.0, 1.0)  # Color cyan
    for point in ojogui:
        glVertex3f(point[0], point[1], point[2])
    glEnd()      

def draw_bocafeliz():
    glBegin(GL_POLYGON)
    glColor3f(0.0, 1.0, 1.0)  # Color cyan
    for point in bocaFeliz:
        glVertex3f(point[0], point[1], point[2])
    glEnd()     


def draw_ojofeliz1():
    glBegin(GL_POLYGON)
    glColor3f(0.0, 1.0, 1.0)  # Color cyan
    for point in ojoFeliz:
        glVertex3f(point[0], point[1], point[2])
    glEnd()    

def draw_ojofeliz2():
    glBegin(GL_POLYGON)
    glColor3f(0.0, 1.0, 1.0)  # Color cyan
    for point in ojoFeliz2:
        glVertex3f(point[0], point[1], point[2])
    glEnd()   

def draw_bocaseria1():
    glBegin(GL_POLYGON)
    glColor3f(0.0, 1.0, 1.0)  # Color cyan
    for point in bocaseria:
        glVertex3f(point[0], point[1], point[2])
    glEnd()   

def draw_cejagui2():
    glBegin(GL_POLYGON)
    glColor3f(0.0, 1.0, 1.0)  # Color cyan
    for point in cejagui2:
        glVertex3f(point[0], point[1], point[2])
    glEnd()  

def draw_ojotache():
    glBegin(GL_POLYGON)
    glColor3f(0.0, 1.0, 1.0)  # Color cyan
    for point in ojotache1:
        glVertex3f(point[0], point[1], point[2])
    glEnd()   

def draw_ojotache2():
    glBegin(GL_POLYGON)
    glColor3f(0.0, 1.0, 1.0)  # Color cyan
    for point in ojotache2:
        glVertex3f(point[0], point[1], point[2])
    glEnd()   

def draw_ojotache3():
    glBegin(GL_POLYGON)
    glColor3f(0.0, 1.0, 1.0)  # Color cyan
    for point in ojotache11:
        glVertex3f(point[0], point[1], point[2])
    glEnd()  

def draw_ojotache4():
    glBegin(GL_POLYGON)
    glColor3f(0.0, 1.0, 1.0)  # Color cyan
    for point in ojotache22:
        glVertex3f(point[0], point[1], point[2])
    glEnd()                   
            


boca1 =[
    (9, 10, 11.3),
    (9.5, 9.5, 11.3),
    (10.5, 9.5, 11.3),
    (11, 10, 11.3)
]

bocaenojada =[
    (9.2, 9.8, 11.3),
    (9.2, 9.4, 11.3),
    (10.8, 9.4, 11.3),
    (10.8, 9.8, 11.3)
]

ojo1 =[
    (9.4, 10.8, 11.3),
    (9.52, 10.71, 11.3),
    (9.6, 10.6, 11.3),
    (9.52, 10.48, 11.3),
    (9.4, 10.4, 11.3),
    (9.29, 10.48, 11.3),
    (9.2, 10.6, 11.3),
    (9.29, 10.72, 11.3)
]

ojo2 =[
    (10.6, 10.8, 11.3),
    (10.48, 10.71, 11.3),
    (10.4, 10.6, 11.3),
    (10.48, 10.48, 11.3),
    (10.6, 10.4, 11.3),
    (10.71, 10.48, 11.3),
    (10.8, 10.6, 11.3),
    (10.71, 10.72, 11.3)
]

ojotache1 =[
    (10.54, 10.6, 11.3),
    (10.5, 10.56, 11.3),
    (10.66, 10.4, 11.3),
    (10.7, 10.44, 11.3)
]

ojotache2 =[
    (10.5, 10.44, 11.3),
    (10.54, 10.4, 11.3),
    (10.7, 10.56, 11.3),
    (10.66, 10.6, 11.3)
]

ojotache11 =[
    (9.46, 10.6, 11.3),
    (9.5, 10.56, 11.3),
    (9.34, 10.4, 11.3),
    (9.3, 10.44, 11.3)
]

ojotache22 =[
    (9.5, 10.44, 11.3),
    (9.46, 10.4, 11.3),
    (9.3, 10.56, 11.3),
    (9.34, 10.6, 11.3)
]

cejagui =[
    (9.2988, 10.8404, 11.3),
    (9.4995, 10.8447, 11.3),
    (9.5, 10.9, 11.3),
    (9.3, 10.9, 11.3)
]

cejagui2 =[
    (10.7012, 10.8404, 11.3),
    (10.5005, 10.8447, 11.3),
    (10.5, 10.9, 11.3),
    (10.7, 10.9, 11.3)
]

ojogui =[
    (10.6, 10.8, 11.3),
    (10.5577, 10.7608, 11.3),
    (10.5195, 10.7247, 11.3),
    (10.5524, 10.7003, 11.3),
    (10.5970, 10.7428, 11.3),
    (10.6384, 10.7417, 11.3),
    (10.6798, 10.7025, 11.3),
    (10.7297, 10.7014, 11.3),
    (10.7148, 10.7269, 11.3),
    (10.6638, 10.7714, 11.3)
]

ceja =[
    (9.3591, 10.9025, 11.3),
    (9.4174, 10.9424, 11.3),
    (9.5386, 10.7645, 11.3),
    (9.6, 10.8, 11.3)
]

ceja2 =[
    (10.6409, 10.9025, 11.3),
    (10.5826, 10.9424, 11.3),
    (10.4614, 10.7645, 11.3),
    (10.4, 10.8, 11.3)
]

cejatriste =[
    (9.2963, 10.8573, 11.3),
    (9.3680, 10.8266, 11.3),
    (9.5362, 10.9202, 11.3),
    (9.5362, 10.9202, 11.3)
]

cejatriste2 =[
    (10.7037, 10.8573, 11.3),
    (10.6320, 10.8266, 11.3),
    (10.4638, 10.9202, 11.3),
    (10.4638, 10.9202, 11.3)
]

bocatriste =[
    (9.2, 9.4, 11.3),
    (9.2753, 9.5262, 11.3),
    (9.3705, 9.6584, 11.3),
    (9.5027, 9.7774, 11.3),
    (9.6508, 9.8012, 11.3),
    (10.3492, 9.8012, 11.3),
    (10.4973, 9.7774, 11.3),
    (10.6295, 9.6584, 11.3),
    (10.7247, 9.5262, 11.3),
    (10.8, 9.4, 11.3),
    (10.6, 9.4, 11.3),
    (10.4, 9.6, 11.3),
    (9.6, 9.6, 11.3),
    (9.4, 9.4, 11.3)
]

ojoFeliz =[
    (9.4, 10.8, 11.3),
    (9.4988, 10.7605, 11.3),
    (9.6, 10.7, 11.3),
    (9.651, 10.6467, 11.3),
    (9.7, 10.6, 11.3),
    (9.1, 10.6, 11.3),
    (9.1497, 10.6493, 11.3),
    (9.2, 10.7, 11.3),
    (9.3006, 10.7605, 11.3)
]

ojoFeliz2 =[
    (10.6, 10.8, 11.3),
    (10.4988, 10.7605, 11.3),
    (10.4, 10.7, 11.3),
    (10.651, 10.6467, 11.3),
    (10.7, 10.6, 11.3),
    (10.9, 10.6, 11.3),
    (10.8503, 10.6493, 11.3),
    (10.8, 10.7, 11.3),
    (10.6994, 10.7605, 11.3)
]

bocaFeliz =[
    (10, 9.4, 11.3),
    (9.2, 9.8, 11.3),
    (9.5, 9.8, 11.3),
    (10, 9.6, 11.3),
    (10.5, 9.8, 11.3),
    (10.8, 9.8, 11.3)
]

bocaseria =[
    (9.2, 9.4, 11.3),
    (10.8, 9.4, 11.3),
    (10.8, 9.5, 11.3),
    (9.2, 9.5, 11.3)
]

bocaFelizNa =[
    (10, 9.8, 11.3),
    (9.2, 9.4, 11.3),
    (9.6, 9.4, 11.3),
    (10, 9.6, 11.3),
    (10.4, 9.4, 11.3),
    (10.8, 9.4, 11.3)
]

boca =[
    (9, 9.7, 11.3),
    (9.12, 9.52, 11.3),
    (9.29, 9.41, 11.3),
    (9.6, 9.4, 11.3),
    (10, 9.4, 11.3),
    (10.4, 9.4, 11.3),
    (10.71, 9.41, 11.3),
    (10.88, 9.52, 11.3),
    (11, 9.7, 10.6, 11.3),
    (10.8, 9.7, 11.3),
    (10.6, 9.7, 11.3),
    (10.3, 9.7, 11.3),
    (10, 9.7, 11.3),
    (9.7, 9.7, 11.3),
    (9.3, 9.7, 11.3)
]