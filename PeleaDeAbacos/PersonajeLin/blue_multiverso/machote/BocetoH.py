from OpenGL.GLU import *
from OpenGL.GL import *
from OpenGL.GLUT import *
from pygame.locals import *
from PIL import *

#---------------------------------------------------
def draw_piernaDer():
    glBegin(GL_QUADS)
    # Front Face
    glColor3f(0.0, 0.5, 0.0)  # Verde oscuro
    glVertex3f(0.5, -1.5, 0.0)  # 1
    glVertex3f(0.5, -2.5, 0.0)  # 2
    glVertex3f(1.5, -2.5, 0.0)  # 3
    glVertex3f(1.5, -1.5, 0.0)  # 4
    
    # Back Face
    glColor3f(0.0, 0.5, 0.0)  # Verde oscuro
    glVertex3f(0.5, -1.5, 2.0)  # 5
    glVertex3f(0.5, -2.5, 2.0)  # 6
    glVertex3f(1.5, -2.5, 2.0)  # 7
    glVertex3f(1.5, -1.5, 2.0)  # 8
    
    # Side Faces
    # Side 1
    glColor3f(0.0, 0.5, 0.0)  # Verde oscuro
    glVertex3f(0.5, -1.5, 0.0)  # 1
    glVertex3f(0.5, -1.5, 2.0)  # 5
    glVertex3f(0.5, -2.5, 2.0)  # 6
    glVertex3f(0.5, -2.5, 0.0)  # 2
    
    # Side 2
    glColor3f(0.0, 0.5, 0.0)  # Verde oscuro
    glVertex3f(1.5, -1.5, 0.0)  # 4
    glVertex3f(1.5, -1.5, 2.0)  # 8
    glVertex3f(1.5, -2.5, 2.0)  # 7
    glVertex3f(1.5, -2.5, 0.0)  # 3

    #cara inferior
    glColor3f(0.0, 0.5, 0.0)  # Verde oscuro
    glVertex3f(0.5, -1.5, 0.0)  # 1
    glVertex3f(1.5, -1.5, 0.0)  # 4
    glVertex3f(1.5, -1.5, 2.0)  # 8
    glVertex3f(0.5, -1.5, 2.0)  # 5

    #cara posterior
    glColor3f(0.0, 0.5, 0.0)  # Verde oscuro
    glVertex3f(0.5, -2.5, 0.0)  # 2
    glVertex3f(1.5, -2.5, 0.0)  # 3
    glVertex3f(1.5, -2.5, 2.0)  # 7
    glVertex3f(0.5, -2.5, 2.0)  # 6
    
    glEnd()

def draw_piernaIzq():
    glBegin(GL_QUADS)
    # Front Face
    glColor3f(0.0, 0.5, 0.0)  # Verde oscuro
    glVertex3f(-1.5,-1.5,0.0)  # 1
    glVertex3f(-1.5,-2.5,0.0)  # 2
    glVertex3f(-0.5,-2.5,0.0)  # 3
    glVertex3f(-0.5,-1.5,0.0)  # 4
    
    # Back Face
    glColor3f(0.0, 0.5, 0.0)  # Verde oscuro
    glVertex3f(-1.5, -1.5, 2.0)  # 5
    glVertex3f(-1.5,-2.5,2.0)  # 6
    glVertex3f(-0.5,-2.5,2.0)  # 7
    glVertex3f(-0.5, -1.5, 2.0)  # 8
    
    # Side Faces
    # Side 1
    glColor3f(0.0, 0.5, 0.0)  # Verde oscuro
    glVertex3f(-1.5,-1.5,0.0)  # 1
    glVertex3f(-1.5, -1.5, 2.0)  # 5
    glVertex3f(-1.5,-2.5,2.0)  # 6
    glVertex3f(-1.5,-2.5,0.0)  # 2
    
    # Side 2
    glColor3f(0.0, 0.5, 0.0)  # Verde oscuro
    glVertex3f(-0.5,-1.5,0.0)  # 4
    glVertex3f(-0.5, -1.5, 2.0)  # 8
    glVertex3f(-0.5,-2.5,2.0)  # 7
    glVertex3f(-0.5,-2.5,0.0)  # 3

    #cara inferior
    glColor3f(0.0, 0.5, 0.0)  # Verde oscuro
    glVertex3f(-1.5,-1.5,0.0)  # 1
    glVertex3f(-0.5,-1.5,0.0)  # 4
    glVertex3f(-0.5, -1.5, 2.0)  # 8
    glVertex3f(-1.5, -1.5, 2.0)  # 5

    #cara posterior
    glColor3f(0.0, 0.5, 0.0)  # Verde oscuro
    glVertex3f(-1.5,-2.5,0.0)  # 2
    glVertex3f(-0.5,-2.5,0.0)  # 3
    glVertex3f(-0.5,-2.5,2.0)  # 7
    glVertex3f(-1.5,-2.5,2.0)  # 6

    glEnd()
#------------------------------------------------------
def draw_torso():
    glBegin(GL_QUADS)
    # Front Face
    
    glColor3f(0.0, 0.2, 0.5)  # Azul marino
    glVertex3f(-1.5, -1, 2)   # 1
    glVertex3f(-1.5, -3, 2)   # 2
    glVertex3f(1.5, -3, 2)    # 3
    glVertex3f(1.5, -1, 2)    # 4
    
    # Back Face
    glColor3f(0.0, 0.2, 0.5)  # Azul marino
    glVertex3f(-1.5, -1, 6)   # 5
    glVertex3f(-1.5, -3, 6)   # 6
    glVertex3f(1.5, -3, 6)    # 7
    glVertex3f(1.5, -1, 6)    # 8
    
    # Side Faces
    # Side 1
    glColor3f(0.0, 0.2, 0.5)  # Azul marino
    glVertex3f(-1.5, -1, 2)   # 1
    glVertex3f(-1.5, -1, 6)   # 5
    glVertex3f(-1.5, -3, 6)   # 6
    glVertex3f(-1.5, -3, 2)   # 2
    
    # Side 2
    glColor3f(0.0, 0.2, 0.5)  # Azul marino
    glVertex3f(1.5, -1, 2)    # 4
    glVertex3f(1.5, -1, 6)    # 8
    glVertex3f(1.5, -3, 6)    # 7
    glVertex3f(1.5, -3, 2)    # 3

    # Bottom Face
    glColor3f(0.0, 0.2, 0.5)  # Azul marino
    glVertex3f(-1.5, -3, 2)   # 2
    glVertex3f(1.5, -3, 2)    # 3
    glVertex3f(1.5, -3, 6)    # 7
    glVertex3f(-1.5, -3, 6)   # 6

    glEnd()
#---------------------------------------------------------------
def draw_cabeza():
    glBegin(GL_QUADS)
    # Front Face
    glColor3f(0.0, 0.5, 0.0)  # Verde oscuro
    glVertex3f(-1, -1, 6)   # 1
    glVertex3f(-1, -3, 6)   # 2
    glVertex3f(1, -3, 6)    # 3
    glVertex3f(1, -1, 6)    # 4
    
    # Back Face
    glColor3f(0.0, 0.5, 0.0)  # Verde oscuro
    glVertex3f(-1, -1, 8)   # 5
    glVertex3f(-1, -3, 8)   # 6
    glVertex3f(1, -3, 8)    # 7
    glVertex3f(1, -1, 8)    # 8
    
    # Side Faces
    # Side 1
    glColor3f(0.0, 0.5, 0.0)  # Verde oscuro
    glVertex3f(-1, -1, 6)   # 1
    glVertex3f(-1, -1, 8)   # 5
    glVertex3f(-1, -3, 8)   # 6
    glVertex3f(-1, -3, 6)   # 2
    
    # Side 2
    glColor3f(0.0, 0.5, 0.0)  # Verde oscuro
    glVertex3f(1, -1, 6)    # 4
    glVertex3f(1, -1, 8)    # 8
    glVertex3f(1, -3, 8)    # 7
    glVertex3f(1, -3, 6)    # 3

    # Bottom Face
    glColor3f(0.0, 0.5, 0.0)  # Verde oscuro
    glVertex3f(-1, -3, 6)   # 2
    glVertex3f(1, -3, 6)    # 3
    glVertex3f(1, -3, 8)    # 7
    glVertex3f(-1, -3, 8)   # 6

    glEnd()
#-------------------------------------------
def draw_oreja_izquierda():
    glBegin(GL_QUADS)
    # Front Face
    glColor3f(0.0, 0.5, 0.0)  # Verde oscuro
    glVertex3f(-1, -1.8, 8)    # 1
    glVertex3f(-1, -2.5, 8)    # 2
    glVertex3f(-0.3, -2.5, 8)  # 3
    glVertex3f(-0.3, -1.8, 8)  # 4
    
    # Back Face
    glColor3f(0.0, 0.5, 0.0)  # Verde oscuro
    glVertex3f(-1, -1.8, 8.3)    # 5
    glVertex3f(-1, -2.5, 8.3)    # 6
    glVertex3f(-0.3, -2.5, 8.3)  # 7
    glVertex3f(-0.3, -1.8, 8.3)  # 8
    
    # Side Faces
    # Side 1
    glColor3f(0.0, 0.5, 0.0)  # Verde oscuro
    glVertex3f(-1, -1.8, 8)    # 1
    glVertex3f(-1, -1.8, 8.3)    # 5
    glVertex3f(-1, -2.5, 8.3)    # 6
    glVertex3f(-1, -2.5, 8)    # 2
    
    # Side 2
    glColor3f(0.0, 0.5, 0.0)  # Verde oscuro
    glVertex3f(-0.3, -1.8, 8)    # 4
    glVertex3f(-0.3, -1.8, 8.3)    # 8
    glVertex3f(-0.3, -2.5, 8.3)    # 7
    glVertex3f(-0.3, -2.5, 8)    # 3

    # Bottom Face
    glColor3f(0.0, 0.5, 0.0)  # Verde oscuro
    glVertex3f(-1, -2.5, 8)    # 2
    glVertex3f(-0.3, -2.5, 8)    # 3
    glVertex3f(-0.3, -2.5, 8.3)    # 7
    glVertex3f(-1, -2.5, 8.3)    # 6

    glEnd()

def draw_oreja_derecha():
    glBegin(GL_QUADS)
    # Front Face
    glColor3f(0.0, 0.5, 0.0)  # Verde oscuro
    glVertex3f(0.3, -1.8, 8)    # 1
    glVertex3f(0.3, -2.5, 8)    # 2
    glVertex3f(1, -2.5, 8)    # 3
    glVertex3f(1, -1.8, 8)    # 4
    
    # Back Face
    glColor3f(0.0, 0.5, 0.0)  # Verde oscuro
    glVertex3f(0.3, -1.8, 8.3)    # 5
    glVertex3f(0.3, -2.5, 8.3)    # 6
    glVertex3f(1, -2.5, 8.3)    # 7
    glVertex3f(1, -1.8, 8.3)    # 8
    
    # Side Faces
    # Side 1
    glColor3f(0.0, 0.5, 0.0)  # Verde oscuro
    glVertex3f(0.3, -1.8, 8)    # 1
    glVertex3f(0.3, -1.8, 8.3)    # 5
    glVertex3f(0.3, -2.5, 8.3)    # 6
    glVertex3f(0.3, -2.5, 8)    # 2
    
    # Side 2
    glColor3f(0.0, 0.5, 0.0)  # Verde oscuro
    glVertex3f(1, -1.8, 8)    # 4
    glVertex3f(1, -1.8, 8.3)    # 8
    glVertex3f(1, -2.5, 8.3)    # 7
    glVertex3f(1, -2.5, 8)    # 3

    # Bottom Face
    glColor3f(0.0, 0.5, 0.0)  # Verde oscuro
    glVertex3f(0.3, -2.5, 8)    # 2
    glVertex3f(1, -2.5, 8)    # 3
    glVertex3f(1, -2.5, 8.3)    # 7
    glVertex3f(0.3, -2.5, 8.3)    # 6

    glEnd()

#-------------------------------------------
def draw_BrazoDer():
    glBegin(GL_QUADS)
 # Front Face
    glColor3f(0.0, 0.5, 0.0)  # Verde oscuro
    glVertex3f(-2.7,-1.5,4.0)  # 1
    glVertex3f(-2.7,-2.5,4.0)  # 2
    glVertex3f(-1.5,-2.5,5.0)  # 3
    glVertex3f(-1.5,-1.5,5.0)  # 4
    
    # Back Face
    glColor3f(0.0, 0.5, 0.0)  # Verde oscuro
    glVertex3f(-2.7,-1.5,5.0)  # 5
    glVertex3f(-2.7,-2.5,5.0)  # 6
    glVertex3f(-1.5,-2.5,6.0)  # 7
    glVertex3f(-1.5,-1.5,6.0)  # 8
    
    # Side Faces
    # Side 1
    glColor3f(0.0, 0.5, 0.0)  # Verde oscuro
    glVertex3f(-2.7,-1.5,4.0)  # 1
    glVertex3f(-2.7,-1.5,5.0)  # 5
    glVertex3f(-2.7,-2.5,5.0)  # 6
    glVertex3f(-2.7,-2.5,4.0)  # 2
    
    # Side 2
    glColor3f(0.0, 0.5, 0.0)  # Verde oscuro
    glVertex3f(-1.5,-1.5,5.0)  # 4
    glVertex3f(-1.5,-1.5,6.0)  # 8
    glVertex3f(-1.5,-2.5,6.0) # 7
    glVertex3f(-1.5,-2.5,5.0)  # 3

    #cara inferior
    glColor3f(0.0, 0.5, 0.0)  # Verde oscuro
    glVertex3f(-2.7,-1.5,4.0)  # 1
    glVertex3f(-1.5,-1.5,5.0)  # 4
    glVertex3f(-1.5,-1.5,6.0)  # 8
    glVertex3f(-2.7,-1.5,5.0)  # 5

    #cara posterior
    glColor3f(0.0, 0.5, 0.0)  # Verde oscuro
    glVertex3f(-2.7,-2.5,4.0)  # 2
    glVertex3f(-1.5,-2.5,5.0)  # 3
    glVertex3f(-1.5,-2.5,6.0)  # 7
    glVertex3f(-2.7,-2.5,5.0)  # 6


    glEnd()

def draw_BrazoIzq():
    glBegin(GL_QUADS)
 # Front Face
    glColor3f(0.0, 0.5, 0.0)  # Verde oscuro
    glVertex3f(2.7,-1.5,4.0)  # 1
    glVertex3f(2.7,-2.5,4.0)  # 2
    glVertex3f(1.5,-2.5,5.0)  # 3
    glVertex3f(1.5,-1.5,5.0)  # 4
    
    # Back Face
    glColor3f(0.0, 0.5, 0.0)  # Verde oscuro
    glVertex3f(2.7,-1.5,5.0)  # 5
    glVertex3f(2.7,-2.5,5.0)  # 6
    glVertex3f(1.5,-2.5,6.0)  # 7
    glVertex3f(1.5,-1.5,6.0)  # 8
    
    # Side Faces
    # Side 1
    glColor3f(0.0, 0.5, 0.0)  # Verde oscuro
    glVertex3f(2.7,-1.5,4.0)  # 1
    glVertex3f(2.7,-1.5,5.0)  # 5
    glVertex3f(2.7,-2.5,5.0)  # 6
    glVertex3f(2.7,-2.5,4.0)  # 2
    
    # Side 2
    glColor3f(0.0, 0.5, 0.0)  # Verde oscuro
    glVertex3f(1.5,-1.5,5.0)  # 4
    glVertex3f(1.5,-1.5,6.0)  # 8
    glVertex3f(1.5,-2.5,6.0) # 7
    glVertex3f(1.5,-2.5,5.0)  # 3

    #cara inferior
    glColor3f(0.0, 0.5, 0.0)  # Verde oscuro
    glVertex3f(2.7,-1.5,4.0)  # 1
    glVertex3f(1.5,-1.5,5.0)  # 4
    glVertex3f(1.5,-1.5,6.0)  # 8
    glVertex3f(2.7,-1.5,5.0)  # 5

    #cara posterior
    glColor3f(0.0, 0.5, 0.0)  # Verde oscuro
    glVertex3f(2.7,-2.5,4.0)  # 2
    glVertex3f(1.5,-2.5,5.0)  # 3
    glVertex3f(1.5,-2.5,6.0)  # 7
    glVertex3f(2.7,-2.5,5.0)  # 6

    glEnd()

#--------------------------------------------
def draw_escudo():
    glBegin(GL_QUADS)
    # Front Face
    glColor3f(0.0, 0.5, 0.5)  # Color del escudo (azul verdoso)
    glVertex3f(-1, -3, 3)   # 1
    glVertex3f(-5, -3, 3)   # 2
    glVertex3f(-3, -1, 3)   # 3
    glVertex3f(-3, -3, 1)   # 4
    
    # Back Face
    glColor3f(0.0, 0.5, 0.5)  # Color del escudo (azul verdoso)
    glVertex3f(-1, -3, 5)   # 5
    glVertex3f(-5, -3, 5)   # 6
    glVertex3f(-3, -1, 5)   # 7
    glVertex3f(-3, -3, 7)   # 8
    
    # Side Faces
    # Side 1
    glColor3f(0.0, 0.5, 0.5)  # Color del escudo (azul verdoso)
    glVertex3f(-1, -3, 3)   # 1
    glVertex3f(-1, -3, 5)   # 5
    glVertex3f(-3, -1, 5)   # 7
    glVertex3f(-3, -1, 3)   # 3
    
    # Side 2
    glColor3f(0.0, 0.5, 0.5)  # Color del escudo (azul verdoso)
    glVertex3f(-5, -3, 3)   # 2
    glVertex3f(-5, -3, 5)   # 6
    glVertex3f(-3, -1, 5)   # 7
    glVertex3f(-3, -1, 3)   # 3
    
    # Bottom Face
    glColor3f(0.0, 0.5, 0.5)  # Color del escudo (azul verdoso)
    glVertex3f(-1, -3, 3)   # 1
    glVertex3f(-5, -3, 3)   # 2
    glVertex3f(-5, -3, 5)   # 6
    glVertex3f(-1, -3, 5)   # 5
    
    glEnd()

#--------------------------------------------
def draw_ojos():
    glBegin(GL_QUADS)

    glVertex3f(-0.2,-3,7)#1
    glVertex3f(-0.6,-3,7)#4
    glVertex3f(-0.6,-3,7.5)#5
    glVertex3f(-0.2,-3,7.5)#8
    
    glVertex3f(0.6,-3,7)#1
    glVertex3f(0.2,-3,7)#4
    glVertex3f(0.2,-3,7.5)#5
    glVertex3f(0.6,-3,7.5)#8

    glEnd()

#----------------------------------------------
def draw_enojo():
    glBegin(GL_QUADS)

    glColor3f(0.8, 0.0, 0.0) #rojo
    glVertex3f(-0.2,-3,7)#1
    glVertex3f(-0.6,-3,7)#4
    glVertex3f(-0.6,-3,7.5)#5
    glVertex3f(-0.2,-3,7.5)#8

    glColor3f(0.8, 0.0, 0.0) #rojo
    glVertex3f(0.6,-3,7)#1
    glVertex3f(0.2,-3,7)#4
    glVertex3f(0.2,-3,7.5)#5
    glVertex3f(0.6,-3,7.5)#8

    #cejas:
    glColor3f(0.8, 0.0, 0.0) #rojo

    glVertex3f(-0.7,-3,8)#1
    glVertex3f(-0.7,-3,8.1)#4
    glVertex3f(-0.1,-3,7.7)#5
    glVertex3f(-0.1,-3,7.6)#8

    glColor3f(0.8, 0.0, 0.0) #rojo

    glVertex3f(0.7,-3,8)#1
    glVertex3f(0.7,-3,8.1)#4
    glVertex3f(0.1,-3,7.7)#5
    glVertex3f(0.1,-3,7.6)#8

    glEnd()
#-----------------------------------------------
def draw_espada():
    glBegin(GL_QUADS)
    # Front Face
    glColor3f(0.8, 0.8, 0.8)  # Color gris claro
    glVertex3f(2.7, -2.6, 4.0)   # 1
    glVertex3f(2.7, -4.0, 4.0)   # 2
    glVertex3f(2.2, -4.0, 4.0)   # 3
    glVertex3f(2.2, -2.6, 4.0)   # 4
    
    # Back Face
    glColor3f(0.8, 0.8, 0.8)  # Color gris claro
    glVertex3f(2.7, -2.6, 4.3)   # 5
    glVertex3f(2.7, -4.0, 4.3)   # 6
    glVertex3f(2.2, -4.0, 4.3)   # 7
    glVertex3f(2.2, -2.6, 4.3)   # 8
    
    # Side Faces
    # Side 1
    glColor3f(0.8, 0.8, 0.8)  # Color gris claro
    glVertex3f(2.7, -2.6, 4.0)   # 1
    glVertex3f(2.7, -2.6, 4.3)   # 5
    glVertex3f(2.7, -4.0, 4.3)   # 6
    glVertex3f(2.7, -4.0, 4.0)   # 2
    
    # Side 2
    glColor3f(0.8, 0.8, 0.8)  # Color gris claro
    glVertex3f(2.2, -2.6, 4.0)   # 4
    glVertex3f(2.2, -2.6, 4.3)   # 8
    glVertex3f(2.2, -4.0, 4.3)   # 7
    glVertex3f(2.2, -4.0, 4.0)   # 3

    # Bottom Face
    glColor3f(0.8, 0.8, 0.8)  # Color gris claro
    glVertex3f(2.7, -4.0, 4.0)   # 2
    glVertex3f(2.2, -4.0, 4.0)   # 3
    glVertex3f(2.2, -4.0, 4.3)   # 7
    glVertex3f(2.7, -4.0, 4.3)   # 6

    glEnd()

#--------------------------------------
def draw_feliz():
    glBegin(GL_QUADS)

    glVertex3f(-0.4,-3,6.2)#1
    glVertex3f(0.4,-3,6.2)#4
    glVertex3f(0.6,-3,6.5)#5
    glVertex3f(-0.6,-3,6.5)#8
    glEnd()

def draw_asombro():
    glBegin(GL_QUADS)

    glVertex3f(-0.2,-3,6.2)#1
    glVertex3f(0.2,-3,6.2)#4
    glVertex3f(0.2,-3,6.5)#5
    glVertex3f(-0.2,-3,6.5)#8

    #cejas:
    glVertex3f(-0.7,-3,7.6)#1
    glVertex3f(-0.7,-3,7.7)#4
    glVertex3f(-0.1,-3,8.3)#5
    glVertex3f(-0.1,-3,8.2)#8

    glVertex3f(0.7,-3,7.6)#1
    glVertex3f(0.7,-3,7.7)#4
    glVertex3f(0.1,-3,8.3)#5
    glVertex3f(0.1,-3,8.2)#8

    glEnd()

def draw_guiño():
    glBegin(GL_QUADS)

    glVertex3f(-0.2,-3,7)#1
    glVertex3f(-0.6,-3,7)#4
    glVertex3f(-0.6,-3,7.10)#5
    glVertex3f(-0.2,-3,7.10)#8

    glVertex3f(-0.2,-3,7.1)#1
    glVertex3f(-0.6,-3,7.5)#4
    glVertex3f(-0.6,-3,7.4)#5
    glVertex3f(-0.2,-3,7)#8
    
    glVertex3f(0.6,-3,7)#1
    glVertex3f(0.2,-3,7)#4
    glVertex3f(0.2,-3,7.5)#5
    glVertex3f(0.6,-3,7.5)#8

    glVertex3f(-0.4,-3,6.2)#1
    glVertex3f(0.4,-3,6.2)#4
    glVertex3f(0.6,-3,6.5)#5
    glVertex3f(-0.6,-3,6.5)#8

    glEnd()

def draw_triste():
    glBegin(GL_QUADS)

    glVertex3f(-0.4,-3,6.5)#1
    glVertex3f(0.4,-3,6.5)#4
    glVertex3f(0.6,-3,6.3)#5
    glVertex3f(-0.6,-3,6.3)#8

    #cejas:
    glVertex3f(-0.7,-3,7.6)#1
    glVertex3f(-0.7,-3,7.7)#4
    glVertex3f(-0.1,-3,8.1)#5
    glVertex3f(-0.1,-3,8.0)#8

    glVertex3f(0.7,-3,7.6)#1
    glVertex3f(0.7,-3,7.7)#4
    glVertex3f(0.1,-3,8.1)#5
    glVertex3f(0.1,-3,8.0)#8

    #lagrima
    """
    glVertex3f(-0.2,-3,7)#1
    glVertex3f(-0.6,-3,7)#4
    glVertex3f(-0.6,-3,7.5)#5
    glVertex3f(-0.2,-3,7.5)#8
    """

    glColor3f(0.0, 0.0, 1.0) #azul
    glVertex3f(-0.45,-3,6.65)#1
    glVertex3f(-0.6,-3,6.65)#4
    glVertex3f(-0.6,-3,6.9)#5
    glVertex3f(-0.45,-3,6.9)#8

    glEnd()

#------------MOVIMIENTOS--------------------

def mover_piernaIzq():
    glBegin(GL_QUADS)
    # Base
    glColor3f(0.0, 0.5, 0.0)  # Verde oscuro

    glVertex3f(-1.5,-2.5,1)  # 1
    glVertex3f(-1.5,-3.5,1)  # 2
    glVertex3f(-0.5,-3.5,1)  # 3
    glVertex3f(-0.5,-2.5,1)  # 4
    
    # Parte alta
    glColor3f(0.0, 0.5, 0.0)  # Verde oscuro

    glVertex3f(-1.5, -1.5, 2.0)  # 5
    glVertex3f(-1.5,-2.5,2.0)  # 6
    glVertex3f(-0.5,-2.5,2.0)  # 7
    glVertex3f(-0.5, -1.5, 2.0)  # 8
    

    # Side Faces
    # Side 1
    glColor3f(0.0, 0.5, 0.0)  # Verde oscuro

    glVertex3f(-1.5,-2.5,1.0)  # 1
    glVertex3f(-1.5, -1.5, 2.0)  # 5
    glVertex3f(-1.5,-2.5,2.0)  # 6
    glVertex3f(-1.5,-3.5,1.0)  # 2
    
    # Side 2
    glColor3f(0.0, 0.5, 0.0)  # Verde oscuro

    glVertex3f(-0.5,-2.5,1.0)  # 4
    glVertex3f(-0.5, -1.5, 2.0)  # 8
    glVertex3f(-0.5,-2.5,2.0)  # 7
    glVertex3f(-0.5,-3.5,1.0)  # 3

    #cara inferior
    glColor3f(0.0, 0.5, 0.0)  # Verde oscuro

    glVertex3f(-1.5,-2.5,1.0)  # 1
    glVertex3f(-0.5,-2.5,1.0)  # 4
    glVertex3f(-0.5, -1.5, 2.0)  # 8
    glVertex3f(-1.5, -1.5, 2.0)  # 5

    #cara posterior
    glColor3f(0.0, 0.5, 0.0)  # Verde oscuro

    glVertex3f(-1.5,-3.5,1.0)  # 2
    glVertex3f(-0.5,-3.5,1.0)  # 3
    glVertex3f(-0.5,-2.5,2.0)  # 7
    glVertex3f(-1.5,-2.5,2.0)  # 6

    glEnd()

def mover_piernaDer():
    glBegin(GL_QUADS)
    # Front Face
    glColor3f(0.0, 0.5, 0.0)  # Verde oscuro
    glVertex3f(0.5, -2.5, 1.0)  # 1
    glVertex3f(0.5, -3.5, 1.0)  # 2
    glVertex3f(1.5, -3.5, 1.0)  # 3
    glVertex3f(1.5, -2.5, 1.0)  # 4
    
    # Back Face
    glColor3f(0.0, 0.5, 0.0)  # Verde oscuro
    glVertex3f(0.5, -1.5, 2.0)  # 5
    glVertex3f(0.5, -2.5, 2.0)  # 6
    glVertex3f(1.5, -2.5, 2.0)  # 7
    glVertex3f(1.5, -1.5, 2.0)  # 8
    
    # Side Faces
    # Side 1
    glColor3f(0.0, 0.5, 0.0)  # Verde oscuro
    glVertex3f(0.5, -2.5, 1.0)  # 1
    glVertex3f(0.5, -1.5, 2.0)  # 5
    glVertex3f(0.5, -2.5, 2.0)  # 6
    glVertex3f(0.5, -3.5, 1.0)  # 2
    
    # Side 2
    glColor3f(0.0, 0.5, 0.0)  # Verde oscuro
    glVertex3f(1.5, -2.5, 1.0)  # 4
    glVertex3f(1.5, -1.5, 2.0)  # 8
    glVertex3f(1.5, -2.5, 2.0)  # 7
    glVertex3f(1.5, -3.5, 1.0)  # 3

    #cara inferior
    glColor3f(0.0, 0.5, 0.0)  # Verde oscuro
    glVertex3f(0.5, -2.5, 1.0)  # 1
    glVertex3f(1.5, -2.5, 1.0)  # 4
    glVertex3f(1.5, -1.5, 2.0)  # 8
    glVertex3f(0.5, -1.5, 2.0)  # 5

    #cara posterior
    glColor3f(0.0, 0.5, 0.0)  # Verde oscuro
    glVertex3f(0.5, -3.5, 1.0)  # 2
    glVertex3f(1.5, -3.5, 1.0)  # 3
    glVertex3f(1.5, -2.5, 2.0)  # 7
    glVertex3f(0.5, -2.5, 2.0)  # 6
    
    glEnd()