import pygame
from OpenGL.GLU import *
from OpenGL.GL import *
from OpenGL.GLUT import *
from pygame.locals import *
from PIL import *

from actionsEV import sonido as snd
from actionsEV import textos as txt
from actionsEV import colisiones as coli
from actionsEV import drawPersonaje as dr
from actionsEV import draw2 as dr2
from actionsEV import objetos as obj

pygame.init()
pygame.mixer.init()
display = (600, 600)
scree = pygame.display.set_mode(display, DOUBLEBUF | OPENGL)

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
gluPerspective(45, (display[0]/display[1]), 0.1, 120.0)
glMatrixMode(GL_MODELVIEW)
gluLookAt(-10, 17, -50, 20, 17, 20, 0, 1, 0)
viewMatrix = glGetFloatv(GL_MODELVIEW_MATRIX)
glLoadIdentity()

displayCenter = [scree.get_size()[i] // 2 for i in range(2)]
mouseMove = [0, 0]
pygame.mouse.set_pos(displayCenter)

up_down_angle = 0.0
paused = False
run = True
estado = 0
font = pygame.font.SysFont('Arial', 20)
acercade = ""

pos_inicial_x = 0
pos_inicial_y = 0
# variables de movimiento del personaje
x = 10
y = 7
# AABB
radio = 1.5 
box_min = [x - radio, 0, y - radio]
box_max = [x + radio, 6, y + radio]
#Posiciones objetos
posicion_esfera=[0,3,7]
posicion_cilindro=[20,2,6]
posicion_cubo=[10,2,-3]
posE1 = [10, 3, 16]

colorTexto = [0,0,0]

while run:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE or event.key == pygame.K_RETURN:
                run = False
            if event.key == pygame.K_PAUSE or event.key == pygame.K_p:
                paused = not paused
                pygame.mouse.set_pos(displayCenter)

            if event.key == pygame.K_i:
                acercade = "\nDesarrollado por Emmanuel Vallejo"
            if event.key == pygame.K_n:
                snd.sonido("PersonajeEmma/sounds/choir.mp3")
            if event.key == pygame.K_m:
                snd.stopsonido()

            if event.key == pygame.K_o:
                estado = 0
            if event.key == pygame.K_1:
                estado = 1
                snd.sonido("PersonajeEmma/soundsEV/sound1.mp3")
            if event.key == pygame.K_2:
                estado = 2
                snd.sonido("PersonajeEmma/soundsEV/sound2.mp3")
            if event.key == pygame.K_3:
                estado = 3
                snd.sonido("PersonajeEmma/soundsEV/sound3.mp3")
            if event.key == pygame.K_4:
                estado = 4
                snd.sonido("PersonajeEmma/soundsEV/sound4.mp3")
            if event.key == pygame.K_5:
                estado = 5
                snd.sonido("PersonajeEmma/soundsEV/sound5.mp3")
            if event.key == pygame.K_6:
                estado = 6
            if event.key == pygame.K_7:
                estado = 7
            if event.key == pygame.K_8:
                estado = 8
            if event.key == pygame.K_9:
                estado = 9
            if event.key == pygame.K_0:
                estado = 10
            if event.key == pygame.K_e:
                estado = 11
                snd.sonido("PersonajeEmma/soundsEV/sound11.mp3")
            if event.key == pygame.K_r:
                estado = 12
                snd.sonido("PersonajeEmma/soundsEV/sound12.mp3")
            if event.key == pygame.K_t:
                estado = 13
            if event.key == pygame.K_y:
                estado = 14

        if not paused: 
            if event.type == pygame.MOUSEMOTION:
                mouseMove = [event.pos[i] - displayCenter[i] for i in range(2)]
            pygame.mouse.set_pos(displayCenter)    

    if not paused:
        keypress = pygame.key.get_pressed()
        glLoadIdentity()
        up_down_angle += mouseMove[1]*0.1
        glRotatef(up_down_angle, 1.0, 0.0, 0.0)

        glPushMatrix()
        glLoadIdentity()

        if keypress[pygame.K_w]:
            glTranslatef(0,0,0.4)
        if keypress[pygame.K_s]:
            glTranslatef(0,0,-0.5)
        if keypress[pygame.K_d]:
            glTranslatef(-0.5,0,0)
        if keypress[pygame.K_a]:
            glTranslatef(0.5,0,0)
        if keypress[pygame.K_z]:
            glTranslatef(0,0.5,0)
        if keypress[pygame.K_x]:
            glTranslatef(0,-0.5,0)

        if keypress[pygame.K_UP]:
            pos_inicial_y += 0.5
            y += 0.5
            box_min[2] += 0.5  
            box_max[2] += 0.5 
        if keypress[pygame.K_DOWN]:
            pos_inicial_y -= 0.5
            y -= 0.5
            box_min[2] -= 0.5  
            box_max[2] -= 0.5 
        if keypress[pygame.K_LEFT]:
            pos_inicial_x -= 0.5
            x += 0.5
            box_min[0] -= 0.5 
            box_max[0] -= 0.5  
        if keypress[pygame.K_RIGHT]:
            pos_inicial_x += 0.5
            x -= 0.5
            box_min[0] += 0.5  
            box_max[0] += 0.5

        glRotatef(mouseMove[0]*0.1, 0.0, 1.0, 0.0)

        glMultMatrixf(viewMatrix)
        viewMatrix = glGetFloatv(GL_MODELVIEW_MATRIX)

        glPopMatrix()
        glMultMatrixf(viewMatrix)

        #glLightfv(GL_LIGHT0, GL_POSITION, [1, -1, 1, 0])

        glClear(GL_COLOR_BUFFER_BIT|GL_DEPTH_BUFFER_BIT)
        dr.personaje(estado,pos_inicial_x,pos_inicial_y)
        
        glPushMatrix()
        glTranslatef(posE1[0], posE1[1], posE1[2])
        dr2.obj1(255,255,0)
        glPopMatrix()

        glPushMatrix()
        glTranslatef(*posicion_esfera)
        glColor4f(1,0,0,1)
        obj.draw_sphere(3,10,20)
        glPopMatrix()

        glPushMatrix()
        glTranslatef(*posicion_cilindro)
        glColor4f(0,1,0,1)
        obj.draw_cylinder(2,4,10)
        glPopMatrix()
        
        glPushMatrix()
        glTranslatef(*posicion_cubo)
        glColor4f(0,0,1,1)
        obj.draw_cube()
        glPopMatrix()
        
        glColor4f(1,1,1,1)

        colision1 = coli.spheres(posicion_esfera,3,[x,3,y],3)
        colision2 = coli.aabb([9.0, 1.0, -4.0],[11.0, 3.0, -2.0], box_min, box_max)
        colision3 = coli.manhattan(posicion_cilindro,[x,1.5,y],6)
        colision4 = coli.spheres(posE1,2,[x,3,y],3)

        if colision1:
            colorTexto=[255,0,0]
        if colision2:
            colorTexto=[0,0,255]
        if colision3:
            colorTexto=[0,255,0]
        if colision4:
            colorTexto=[255,255,0]

        if colision1 or colision2 or colision3 or colision4:
            txt.drawText("Colision detectada",5,30,4,30,colorTexto[0],colorTexto[1],colorTexto[2],0,0,0)
        else:
            txt.drawText("Esperando colision",5,30,4,30,255,255,255,0,0,0)
        
        txt.render_text_2d(display,
                           "W,A,S,D,Z,X - Mover cámara\nFLECHAS - Mover personaje\no-Original\n1-Enojado\n2-Triste\n3-Sospechoso\n4-Indiferente\n5-Levantar ceja\nE-Sorprendido\nR-Sonriente\n6-Levantar brazo IZQ\n7-Levantar brazo DER\n8-T-Pose\n9-Sentado\n0-Saltando\nT-Señalando\nY-Celebrando\nn-Sonido ON\nm-Sonido OFF\np-Pausa\ni-Acerca de" + acercade,
                            10, display[1] - 40, font)  # Esquina inferior izquierda

        pygame.display.flip()
        pygame.time.wait(10)

pygame.quit()