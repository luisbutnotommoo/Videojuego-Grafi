import math
from OpenGL.GLU import*
from OpenGL.GL import*
from OpenGL.GLUT import*
from pygame.locals import*
from PIL import Image
from PersonajeStarenka.Acciones2S import objetos as obj


def load_texture(FileName):
    im = Image.open(FileName)
    ix, iy = im.size
    image = im.tobytes("raw", "RGBA", 0, -1)
    
    texture_id = glGenTextures(1)
    glBindTexture(GL_TEXTURE_2D, texture_id)
    glPixelStorei(GL_UNPACK_ALIGNMENT, 1)

    glTexImage2D(GL_TEXTURE_2D, 0, GL_RGBA, ix, iy, 0, GL_RGBA, GL_UNSIGNED_BYTE, image)
   
    glTexParameterf(GL_TEXTURE_2D, GL_TEXTURE_WRAP_S, GL_REPEAT)
    glTexParameterf(GL_TEXTURE_2D, GL_TEXTURE_WRAP_T, GL_REPEAT)
    glTexParameterf(GL_TEXTURE_2D, GL_TEXTURE_MAG_FILTER, GL_LINEAR)
    glTexParameterf(GL_TEXTURE_2D, GL_TEXTURE_MIN_FILTER, GL_LINEAR)

    return texture_id

def BolaDisco(fileImage, radius, num_slices, num_segments):
    texture_id = load_texture(fileImage)
    glEnable(GL_TEXTURE_2D)
    glBindTexture(GL_TEXTURE_2D, texture_id)
    
    for i in range(num_slices):
        lat0 = math.pi * (-0.5 + float(i) / num_slices)
        z0 = math.sin(lat0)
        zr0 = math.cos(lat0)

        lat1 = math.pi * (-0.5 + float(i+1) / num_slices)
        z1 = math.sin(lat1)
        zr1 = math.cos(lat1)

        glBegin(GL_QUAD_STRIP)
        for j in range(num_segments + 1):
            lng = 2 * math.pi * float(j) / num_segments
            x = math.cos(lng)
            y = math.sin(lng)

            s = float(j) / num_segments
            t1 = float(i) / num_slices
            t2 = float(i+1) / num_slices

            glTexCoord2f(s, t1)
            glNormal3f(x * zr0, y * zr0, z0)
            glVertex3f(x * zr0 * radius, y * zr0 * radius, z0 * radius)

            glTexCoord2f(s, t2)
            glNormal3f(x * zr1, y * zr1, z1)
            glVertex3f(x * zr1 * radius, y * zr1 * radius, z1 * radius)

        glEnd()
    
    glDisable(GL_TEXTURE_2D)

def corazon():
    glPushMatrix()
    
    # 2 esferas
    glPushMatrix()
    glTranslatef(-0.5, 0, 0)
    glRotatef(45, 0, 0, 1)
    glScalef(1, 1.3, 0.8)
    obj.draw_sphere(0.5, 20, 20)
    glPopMatrix()

    glPushMatrix()
    glTranslatef(0.5, 0, 0)
    glRotatef(-45, 0, 0, 1)
    glScalef(1, 1.3, 0.8)
    obj.draw_sphere(0.5, 20, 20)
    glPopMatrix()

    # Pico
    glPushMatrix()
    glTranslatef(0, -0.5, 0)
    glRotatef(-45, 0, 0, 1)
    glScalef(1, 1.5, 0.8)
    obj.draw_cone(0.5, 1, 20)
    glPopMatrix()

    glPopMatrix()