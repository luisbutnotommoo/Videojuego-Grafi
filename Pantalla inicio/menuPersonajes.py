import pygame
from OpenGL.GL import *
from OpenGL.GLU import *
from pygame.locals import *
from Acciones import boceto as b
from Acciones.boceto import Personaje

class SeleccionPersonaje:
    def __init__(self, display_size=(800, 600)):
        self.display = display_size
        self.init_pygame()
        self.init_opengl()

        # Estados de selección de personajes
        self.selected_character = -1
        self.personaje = [
            Personaje("original", b.original(), escala=(0.2, 0.2, 0.2)),
            Personaje("Sorprendido", b.original(), escala=(0.2, 0.2, 0.2)),
            Personaje("Asustado", b.original(), escala=(0.2, 0.2, 0.2)),
            Personaje("Molesto", b.original(), escala=(0.2, 0.2, 0.2))
        ]
        
        # Posiciones
        self.asignar_posiciones_personajes()

        # Cargar texturas
        self.floor_texture = self.load_texture("Imagenes/piso.jpg")
        self.wall_texture = self.load_texture("Imagenes/pared.jpg")

    def asignar_posiciones_personajes(self):
        posiciones = [
            (-4.5, -1.5, 0),  # Posición para personaje 1
            (-1.5, -1.5, 0),  # Posición para personaje 2
            (1.5, -1.5, 0),   # Posición para personaje 3
            (4.5, -1.5, 0)    # Posición para personaje 4
        ]
        for personaje, (x, y, z) in zip(self.personaje, posiciones):
            personaje.set_position(x, y, z)

    def init_pygame(self):
        pygame.init()
        pygame.mixer.init()
        self.screen = pygame.display.set_mode(self.display, DOUBLEBUF | OPENGL)
        pygame.event.set_grab(True)

    def init_opengl(self):
        glEnable(GL_DEPTH_TEST)
        glDisable(GL_LIGHTING)  # Desactivar iluminación
        glEnable(GL_TEXTURE_2D)  # Habilitar texturas
        glClearColor(0.1, 0.1, 0.1, 1.0)
        self.set_perspective()

    def set_perspective(self):
        glMatrixMode(GL_PROJECTION)
        glLoadIdentity()
        gluPerspective(50, (self.display[0] / self.display[1]), 0.1, 100.0)
        glMatrixMode(GL_MODELVIEW)
        glLoadIdentity()
        glTranslatef(0.0, 0.0, -20.0)

    def dibujar_personaje(self, personaje, is_selected):
        glPushMatrix()
        x, y, z = personaje.posicion
        glTranslatef(x, y, z)

        # Si el personaje está seleccionado, aumentamos un poco su escala para simular brillo
        if is_selected:
            glScalef(1.1, 1.1, 1.1)  # Aumentar un 10% su tamaño

        glColor3f(1.0, 1.0, 1.0)  # Mantener el color original

        personaje.render()
        glPopMatrix()

    def dibujar_piso_pared(self):
        glEnable(GL_TEXTURE_2D)

        # Suelo
        glBindTexture(GL_TEXTURE_2D, self.floor_texture)
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

        # Dibujar escenario sin iluminación
        self.dibujar_piso_pared()

        # Dibujar personajes sin iluminación
        for idx, character in enumerate(self.personaje):
            is_selected = idx == self.selected_character
            if is_selected:
                character.set_position(character.posicion[0], -1.0, character.posicion[2])
            else:
                character.set_position(character.posicion[0], -1.5, character.posicion[2])
            self.dibujar_personaje(character, is_selected)

        pygame.display.flip()

    def handle_input(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    return False
                elif event.key in (pygame.K_1, pygame.K_2, pygame.K_3, pygame.K_4):
                    self.selected_character = event.key - pygame.K_1  # Set selected character based on key pressed
                elif event.key == pygame.K_RETURN:  # Confirm selection
                    if self.selected_character >= 0:
                        print(f"Personaje seleccionado: {self.selected_character + 1}")
                    else:
                        print("No se ha seleccionado ningún personaje.")
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
        try:
            texture_surface = pygame.image.load(path)
        except pygame.error as e:
            print(f"Error al cargar la textura: {e}")
            return None  # Return None if texture loading fails
        texture_data = pygame.image.tostring(texture_surface, "RGB", 1)
        width, height = texture_surface.get_rect().size

        texture_id = glGenTextures(1)
        glBindTexture(GL_TEXTURE_2D, texture_id)
        glTexImage2D(GL_TEXTURE_2D, 0, GL_RGB, width, height, 0, GL_RGB, GL_UNSIGNED_BYTE, texture_data)
        glTexParameterf(GL_TEXTURE_2D, GL_TEXTURE_MIN_FILTER, GL_LINEAR)
        glTexParameterf(GL_TEXTURE_2D, GL_TEXTURE_MAG_FILTER, GL_LINEAR)
        
        # Aquí está la corrección
        glTexEnvf(GL_TEXTURE_ENV, GL_TEXTURE_ENV_MODE, GL_REPLACE)  # Cambiar a REPLACE para que las texturas se muestren con su color original
        
        return texture_id



if __name__ == "__main__":
    menu = SeleccionPersonaje()
    try:
        menu.run()
    finally:
        menu.cleanup()
