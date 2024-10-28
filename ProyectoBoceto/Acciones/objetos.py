import math
from OpenGL.GLU import*
from OpenGL.GL import*
from OpenGL.GLUT import*
from pygame.locals import*

def draw_sphere(radius,num_slices,num_segments):
    for i in range(num_slices+1):
        lat0=math.pi * (-0.5 +(i-1)/num_slices)
        z0=radius * math.sin(lat0)
        zr0=radius * math.cos(lat0)
 
        lat1=math.pi * (-0.5 + i /num_slices)
        z1=radius * math.sin(lat1)
        zr1=radius * math.cos(lat1)
 
        glBegin(GL_QUAD_STRIP)
        for j in range(num_segments+1):
            lng=2*math.pi * j / num_segments
            x=zr0 * math.cos(lng)
            y=zr0 * math.sin(lng)
 
            glNormal3f(x,y,z0)
            glVertex3f(x,y,z0)
 
            x=zr1 * math.cos(lng)
            y=zr1 * math.sin(lng)
 
            glNormal3f(x,y,z1)
            glVertex3f(x,y,z1)
 
        glEnd()


def draw_arc(radius, start_angle, end_angle, num_segments):
    glBegin(GL_LINE_STRIP)
    for i in range(num_segments + 1):
        angle = start_angle + (end_angle - start_angle) * (i / num_segments)
        x = radius * math.cos(angle)
        y = radius * math.sin(angle)
        glVertex2f(x, y)
    glEnd()


def draw_cube():
    glBegin(GL_QUADS)
 
    #cara frontal
    glVertex3f(-1.0, -1.0, 1.0)
    glVertex3f(1.0, -1.0, 1.0)
    glVertex3f(1.0, 1.0, 1.0)
    glVertex3f(-1.0, 1.0, 1.0)
 
    #cara trasera
    glVertex3f(-1.0, -1.0, -1.0)
    glVertex3f(1.0, -1.0, -1.0)
    glVertex3f(1.0, 1.0, -1.0)
    glVertex3f(-1.0, 1.0, -1.0)
 
    #caras laterales
    glVertex3f(-1.0, -1.0, 1.0)
    glVertex3f(1.0, -1.0, 1.0)
    glVertex3f(1.0, -1.0, -1.0)
    glVertex3f(-1.0, -1.0, -1.0)
 
    glVertex3f(-1.0, 1.0, 1.0)
    glVertex3f(1.0, 1.0, 1.0)
    glVertex3f(1.0, 1.0, -1.0)
    glVertex3f(-1.0, 1.0, -1.0)
 
    glVertex3f(-1.0, -1.0, 1.0)
    glVertex3f(-1.0, 1.0, 1.0)
    glVertex3f(-1.0, 1.0, -1.0)
    glVertex3f(-1.0, -1.0, -1.0)
 
    glVertex3f(1.0, -1.0, 1.0)
    glVertex3f(1.0, 1.0, 1.0)
    glVertex3f(1.0, 1.0, -1.0)
    glVertex3f(1.0, -1.0, -1.0)
 
    glEnd()

def draw_rectangle(x, y, z, width, height, depth):
    glBegin(GL_QUADS)
   
    # Cara frontal
    glVertex3f(x, y, z)
    glVertex3f(x + width, y, z)
    glVertex3f(x + width, y + height, z)
    glVertex3f(x, y + height, z)
    
    # Cara trasera
    glVertex3f(x, y, z - depth)
    glVertex3f(x + width, y, z - depth)
    glVertex3f(x + width, y + height, z - depth)
    glVertex3f(x, y + height, z - depth)
    
    # Lado izquierdo
    glVertex3f(x, y, z)
    glVertex3f(x, y, z - depth)
    glVertex3f(x, y + height, z - depth)
    glVertex3f(x, y + height, z)
    
    # Lado derecho
    glVertex3f(x + width, y, z)
    glVertex3f(x + width, y, z - depth)
    glVertex3f(x + width, y + height, z - depth)
    glVertex3f(x + width, y + height, z)
    
    # Cara superior
    glVertex3f(x, y + height, z)
    glVertex3f(x + width, y + height, z)
    glVertex3f(x + width, y + height, z - depth)
    glVertex3f(x, y + height, z - depth)
    
    # Cara inferior
    glVertex3f(x, y, z)
    glVertex3f(x + width, y, z)
    glVertex3f(x + width, y, z - depth)
    glVertex3f(x, y, z - depth)
    
    glEnd()

def draw_line():
    glBegin(GL_LINES) 
    glVertex3f(-1.0, 0.0, 0.0)  # Punto inicial de la línea
    glVertex3f(1.0, 0.0, 0.0)   # Punto final de la línea
    glEnd()

def draw_cone(base, height, num_segments):
    glBegin(GL_TRIANGLE_FAN)
    glVertex3f(0, height, 0)
    for i in range(num_segments + 1):
        angle = 2 * math.pi * i / num_segments
        x = base * math.cos(angle)
        y = 0
        z = base * math.sin(angle)
        glVertex3f(x, y, z)
    glEnd()

    #base del cono
    glBegin(GL_TRIANGLE_FAN)
    glVertex3f(0, 0, 0)
    for i in range(num_segments + 1):
        angle = 2 * math.pi * i / num_segments
        x = base * math.cos(angle)
        y = 0
        z = base * math.sin(angle)
        glVertex3f(x, y, z)
    glEnd()

