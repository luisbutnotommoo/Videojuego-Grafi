from OpenGL.GLU import *
from OpenGL.GL import *
from OpenGL.GLUT import *
from pygame.locals import *
from PIL import Image
from PersonajeLuis2.AccionesL import recursos

class Escenario:
    
    """
    def __init__(self):
        self.escenario = recursos.ambiente[0]
        self.tex_pared = None
        self.tex_suelo = None
    """

    """
    def init_textures(self):
        self.tex_pared = self.load_texture(self.escenario[0])
        self.tex_suelo = self.load_texture(self.escenario[1])
    """

    def __init__(self):
        self.escenario=recursos.ambiente[0]
        self.tex_pared = self.load_texture(self.escenario[0])
        self.tex_suelo = self.load_texture(self.escenario[1])

    def set_escenario(self, index):
        self.escenario = recursos.ambiente[index]
        self.tex_pared = self.load_texture(self.escenario[0])
        self.tex_suelo = self.load_texture(self.escenario[1])

    def load_texture(self, filename):
        im = Image.open(filename)
        #ix, iy = im.size
        #image = im.tobytes("raw", "RGBX", 0, -1)
        print(f"Tamaño de la imagen: {im.size}")  # Verifica el tamaño de la imagen
        ix, iy, image = im.size[0], im.size[1], im.tobytes("raw", "RGBX", 0, -1)
        texture_id = glGenTextures(1)
        glBindTexture(GL_TEXTURE_2D, texture_id)
        glPixelStorei(GL_UNPACK_ALIGNMENT, 1)
        glTexImage2D(GL_TEXTURE_2D, 0, GL_RGB, ix, iy, 0, GL_RGBA, GL_UNSIGNED_BYTE, image)
        glTexParameterf(GL_TEXTURE_2D, GL_TEXTURE_WRAP_S, GL_REPEAT)
        glTexParameterf(GL_TEXTURE_2D, GL_TEXTURE_WRAP_T, GL_REPEAT)
        glTexParameterf(GL_TEXTURE_2D, GL_TEXTURE_MAG_FILTER, GL_LINEAR)
        glTexParameterf(GL_TEXTURE_2D, GL_TEXTURE_MIN_FILTER, GL_LINEAR)
        return texture_id

    def render_escenario(self):
        # Dibujar suelo
        glEnable(GL_TEXTURE_2D)
        glBindTexture(GL_TEXTURE_2D, self.tex_suelo)
        glBegin(GL_QUADS)
        glColor(1, 1, 1)
        glTexCoord2f(0, 0)
        glVertex3f(-20, 0, 20)
        glTexCoord2f(1, 0)
        glVertex3f(40, 0, 20)
        glTexCoord2f(1, 1)
        glVertex3f(40, 0, -40)
        glTexCoord2f(0, 1)
        glVertex3f(-20, 0, -40)
        glEnd()
        glDisable(GL_TEXTURE_2D)

        # Paredes
        glEnable(GL_TEXTURE_2D)
        glBindTexture(GL_TEXTURE_2D, self.tex_pared)
        # Pared 1
        glBegin(GL_QUADS)
        glColor(1, 1, 1)
        glTexCoord2f(0, 0)
        glVertex3f(-20, 0, 20)
        glTexCoord2f(1, 0)
        glVertex3f(40, 0, 20)
        glTexCoord2f(1, 1)
        glVertex3f(40, 40, 20)
        glTexCoord2f(0, 1)
        glVertex3f(-20, 40, 20)
        glEnd()
        # Pared 2
        glBegin(GL_QUADS)
        glColor(1, 1, 1)
        glTexCoord2f(0, 0)
        glVertex3f(20, 0, 20)
        glTexCoord2f(1, 0)
        glVertex3f(20, 0, -40)
        glTexCoord2f(1, 1)
        glVertex3f(20, 40, -40)
        glTexCoord2f(0, 1)
        glVertex3f(20, 40, 20)
        glEnd()
        # Pared 3
        glBegin(GL_QUADS)
        glColor(1, 1, 1)
        glTexCoord2f(0, 0)
        glVertex3f(20, 0, -20)
        glTexCoord2f(1, 0)
        glVertex3f(-20, 0, -40)
        glTexCoord2f(1, 1)
        glVertex3f(-20, 40, -40)
        glTexCoord2f(0, 1)
        glVertex3f(20, 40, -20)
        glEnd()
        # Pared 4
        glBegin(GL_QUADS)
        glColor(1, 1, 1)
        glTexCoord2f(0, 0)
        glVertex3f(-20, 0, -40)
        glTexCoord2f(1, 0)
        glVertex3f(-20, 0, 20)
        glTexCoord2f(1, 1)
        glVertex3f(-20, 40, 20)
        glTexCoord2f(0, 1)
        glVertex3f(-20, 40, -40)
        glEnd()

        glDisable(GL_TEXTURE_2D)
