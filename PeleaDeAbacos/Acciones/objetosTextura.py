from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *
import math
from PIL import Image


'''def load_texture(file_path):
    image = Image.open(file_path).transpose(Image.FLIP_TOP_BOTTOM)
    img_data = image.convert("RGBA").tobytes()
    width, height = image.size
    textura_id = glGenTextures(1)
    glBindTexture(GL_TEXTURE_2D, textura_id)
    glTexImage2D(GL_TEXTURE_2D, 0, GL_RGBA, width, height, 0, GL_RGBA, GL_UNSIGNED_BYTE, img_data)
    glTexParameterf(GL_TEXTURE_2D, GL_TEXTURE_MIN_FILTER, GL_LINEAR)
    glTexParameterf(GL_TEXTURE_2D, GL_TEXTURE_MAG_FILTER, GL_LINEAR)
    return textura_id'''



def draw_cylinder(radius, height, num_segments, texture_id):
    glEnable(GL_TEXTURE_2D)
    glBindTexture(GL_TEXTURE_2D, texture_id)

    glBegin(GL_QUAD_STRIP)
    for i in range(num_segments + 1):
        theta = i * (2 * math.pi / num_segments)
        x = radius * math.cos(theta)
        z = radius * math.sin(theta)

        u = i / num_segments  # Coordenada U de la textura
        glTexCoord2f(u, 1.0)
        glVertex3f(x, height / 2, z)
        glTexCoord2f(u, 0.0)
        glVertex3f(x, -height / 2, z)
    glEnd()
    
    glDisable(GL_TEXTURE_2D)

def draw_cone(base, height, num_segments, texture_id):
    glEnable(GL_TEXTURE_2D)
    glBindTexture(GL_TEXTURE_2D, texture_id)

    # Superficie lateral del cono
    glBegin(GL_TRIANGLE_FAN)
    glTexCoord2f(0.5, 1.0)
    glVertex3f(0, height, 0)  # Vértice superior
    for i in range(num_segments + 1):
        angle = 2 * math.pi * i / num_segments
        x = base * math.cos(angle)
        z = base * math.sin(angle)
        u = (math.cos(angle) + 1) / 2  # Coordenadas U
        v = (math.sin(angle) + 1) / 2  # Coordenadas V
        glTexCoord2f(u, 0.0)
        glVertex3f(x, 0, z)
    glEnd()

    # Base del cono
    glBegin(GL_TRIANGLE_FAN)
    glTexCoord2f(0.5, 0.5)
    glVertex3f(0, 0, 0)  # Centro de la base
    for i in range(num_segments + 1):
        angle = 2 * math.pi * i / num_segments
        x = base * math.cos(angle)
        z = base * math.sin(angle)
        u = (math.cos(angle) + 1) / 2  # Coordenadas U
        v = (math.sin(angle) + 1) / 2  # Coordenadas V
        glTexCoord2f(u, v)
        glVertex3f(x, 0, z)
    glEnd()

    glDisable(GL_TEXTURE_2D)

def draw_sphere(radius, num_slices, num_segments, texture_id):
    glEnable(GL_TEXTURE_2D)
    glBindTexture(GL_TEXTURE_2D, texture_id)

    for i in range(num_slices + 1):
        lat0 = math.pi * (-0.5 + (i - 1) / num_slices)
        z0 = radius * math.sin(lat0)
        zr0 = radius * math.cos(lat0)
 
        lat1 = math.pi * (-0.5 + i / num_slices)
        z1 = radius * math.sin(lat1)
        zr1 = radius * math.cos(lat1)
 
        glBegin(GL_QUAD_STRIP)
        for j in range(num_segments + 1):
            lng = 2 * math.pi * j / num_segments
            x = math.cos(lng)
            y = math.sin(lng)

            u = j / num_segments  # Coordenada U de la textura
            v0 = (i - 1) / num_slices  # Coordenada V para la primera latitud
            v1 = i / num_slices  # Coordenada V para la siguiente latitud
            
            # Coordenada y vértice de la primera latitud
            glTexCoord2f(u, v0)
            glNormal3f(zr0 * x, zr0 * y, z0)
            glVertex3f(zr0 * x, zr0 * y, z0)
 
            # Coordenada y vértice de la segunda latitud
            glTexCoord2f(u, v1)
            glNormal3f(zr1 * x, zr1 * y, z1)
            glVertex3f(zr1 * x, zr1 * y, z1)
        glEnd()
    
    glDisable(GL_TEXTURE_2D)

