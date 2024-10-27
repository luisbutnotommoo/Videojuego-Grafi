import pygame
from OpenGL.GL import *
from OpenGL.GLU import *
from pygame.locals import *
import math

class SeleccionPersonaje:
    def __init__(self, display_size=(800, 600)):
        self.display = display_size
        self.init_pygame()
        self.init_opengl()

        # Estados de selección de personajes
        self.selected_character = -1
        self.personaje = [{'x': -7.5, 'y': -1.5, 'z': 0}, 
                           {'x': -2.5, 'y': -1.5, 'z': 0}, 
                           {'x': 2.5, 'y': -1.5, 'z': 0},
                           {'x': 7.5, 'y': -1.5, 'z': 0}]  # Coordenadas de cada personaje
        self.plataformaInvisible_glow = 0.0
        self.glow_increasing = True

        # Cargar texturas
        self.floor_texture = self.load_texture("Imagenes/piso.jpg")
        self.wall_texture = self.load_texture("Imagenes/pared.jpg")

    
    def init_pygame(self):
        pygame.init()
        pygame.mixer.init()
        self.screen = pygame.display.set_mode(self.display, DOUBLEBUF | OPENGL)
        pygame.event.set_grab(True)
        
    def init_opengl(self):
        glEnable(GL_DEPTH_TEST)
        glEnable(GL_LIGHTING)
        glEnable(GL_LIGHT0)
        glClearColor(0.1, 0.1, 0.1, 1.0)
        self.set_perspective()

    ##Pantalla, camara de inicio
    def set_perspective(self):
        glMatrixMode(GL_PROJECTION)
        glLoadIdentity()
        gluPerspective(50, (self.display[0] / self.display[1]), 0.1, 100.0)
        glMatrixMode(GL_MODELVIEW)
        glLoadIdentity()
        glTranslatef(0.0, 0.0, -20.0)


    def dibujar_personaje(self, posicion, is_selected):
        glPushMatrix()
        glTranslatef(posicion['x'], posicion['y'], posicion['z'])
        glColor3f(1.0, 1.0, 1.0)
        if is_selected:
            glMaterialfv(GL_FRONT, GL_EMISSION, [0.4, 0.4, 1.0, 1.0])  # Brillo azul
        else:
            glMaterialfv(GL_FRONT, GL_EMISSION, [0.0, 0.0, 0.0, 1.0])  # Sin brillo
        
        # Dibujar el personaje 
        glBegin(GL_QUADS)
        size = 1.0
        for x, y, z in [(-size, -size, size), (size, -size, size), (size, size, size), (-size, size, size)]:  # Frente
            glVertex3f(x, y, z)
        glEnd()
        glPopMatrix()


    def dibujar_piso_pared(self):
        glEnable(GL_TEXTURE_2D)
        glBindTexture(GL_TEXTURE_2D, self.floor_texture)
        
        # Suelo
        glBegin(GL_QUADS)
        glTexCoord2f(0, 0); glVertex3f(-20.0, -2.0, -20.0)
        glTexCoord2f(1, 0); glVertex3f(20.0, -2.0, -20.0)
        glTexCoord2f(1, 1); glVertex3f(20.0, -2.0, 20.0)
        glTexCoord2f(0, 1); glVertex3f(-20.0, -2.0, 20.0)
        glEnd()
        
        # Pared
        glBindTexture(GL_TEXTURE_2D, self.wall_texture)
        glBegin(GL_QUADS)
        glTexCoord2f(0, 0); glVertex3f(-30.0, -2.0, -20.0)
        glTexCoord2f(1, 0); glVertex3f(30.0, -2.0, -20.0)
        glTexCoord2f(1, 1); glVertex3f(30.0, 25.0, -20.0)
        glTexCoord2f(0, 1); glVertex3f(-30.0, 25.0, -20.0)
        glEnd()

        glDisable(GL_TEXTURE_2D)

    def draw_scene(self):
        glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
        self.dibujar_piso_pared()
        
        for idx, character in enumerate(self.personaje):
            is_selected = idx == self.selected_character
            if is_selected:
                character['y'] = -1.0  # Aumento
            else:
                character['y'] = -1.5  # posición original
            self.dibujar_personaje(character, is_selected)


        
        pygame.display.flip()

    def handle_input(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    return False
                elif event.key == pygame.K_1:
                    self.selected_character = 0
                elif event.key == pygame.K_2:
                    self.selected_character = 1
                elif event.key == pygame.K_3:
                    self.selected_character = 2
                elif event.key == pygame.K_4:
                    self.selected_character = 3
                elif event.key == pygame.K_RETURN:  # Aceptar el personaje seleccionado
                    print(f"Personaje seleccionado: {self.selected_character + 1}")
        return True

    def run(self):
        running = True
        while running:
            running = self.handle_input()
            self.draw_scene()
            pygame.time.wait(10)

    def cleanup(self):
        pygame.quit()

    def load_texture(self, path):
        texture_surface = pygame.image.load(path)
        texture_data = pygame.image.tostring(texture_surface, "RGB", 1)
        width, height = texture_surface.get_rect().size

        texture_id = glGenTextures(1)
        glBindTexture(GL_TEXTURE_2D, texture_id)
        glTexImage2D(GL_TEXTURE_2D, 0, GL_RGB, width, height, 0, GL_RGB, GL_UNSIGNED_BYTE, texture_data)
        glTexParameterf(GL_TEXTURE_2D, GL_TEXTURE_MIN_FILTER, GL_LINEAR)
        glTexParameterf(GL_TEXTURE_2D, GL_TEXTURE_MAG_FILTER, GL_LINEAR)
        return texture_id

if __name__ == "__main__":
    menu = SeleccionPersonaje()
    try:
        menu.run()
    finally:
        menu.cleanup()