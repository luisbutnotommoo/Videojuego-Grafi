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

        self.jump_height = 0.0  # Altura del salto
        self.jump_speed = 0.1    # Velocidad del salto
        self.jumping = False      # Estado de salto

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
        glEnable(GL_LIGHTING)
        glEnable(GL_LIGHT0)
        glEnable(GL_COLOR_MATERIAL)
        glEnable(GL_NORMALIZE)
        
        # Configuración de luz principal totalmente neutral
        glLightfv(GL_LIGHT0, GL_POSITION, [5.0, 10.0, 5.0, 1.0])
        glLightfv(GL_LIGHT0, GL_AMBIENT, [0.15, 0.15, 0.15, 1.0])  # Luz ambiente neutral y baja
        glLightfv(GL_LIGHT0, GL_DIFFUSE, [0.7, 0.7, 0.7, 1.0])     # Luz difusa neutral
        glLightfv(GL_LIGHT0, GL_SPECULAR, [0.4, 0.4, 0.4, 1.0])

        # Segunda luz de relleno, también neutral y suave
        glEnable(GL_LIGHT1)
        glLightfv(GL_LIGHT1, GL_POSITION, [-3.0, 5.0, -3.0, 1.0])
        glLightfv(GL_LIGHT1, GL_AMBIENT, [0.1, 0.1, 0.1, 1.0])
        glLightfv(GL_LIGHT1, GL_DIFFUSE, [0.15, 0.15, 0.15, 1.0])
        glLightfv(GL_LIGHT1, GL_SPECULAR, [0.0, 0.0, 0.0, 1.0])

        # Material para mantener colores naturales sin reflejo adicional
        glColorMaterial(GL_FRONT, GL_AMBIENT_AND_DIFFUSE)
        glMaterialfv(GL_FRONT, GL_SPECULAR, [0.2, 0.2, 0.2, 1.0])
        glMaterialf(GL_FRONT, GL_SHININESS, 20.0)

        # Fondo oscuro
        glClearColor(0.1, 0.1, 0.1, 1.0)
        self.set_perspective()


    def set_perspective(self):
        glMatrixMode(GL_PROJECTION)
        glLoadIdentity()
        gluPerspective(60, (self.display[0] / self.display[1]), 0.1, 100.0)
        glMatrixMode(GL_MODELVIEW)
        glLoadIdentity()
        glTranslatef(0.0, 0.0, -20.0)

    def configurar_luz_personaje(self, is_selected):
        if is_selected:
            # Luz neutral para el personaje seleccionado
            glEnable(GL_LIGHT2)
            glLightfv(GL_LIGHT2, GL_POSITION, [0.0, 5.0, 0.0, 1.0])
            glLightfv(GL_LIGHT2, GL_AMBIENT, [0.2, 0.2, 0.2, 1.0])  # Luz ambiente baja y neutral
            glLightfv(GL_LIGHT2, GL_DIFFUSE, [0.5, 0.5, 0.5, 1.0])  # Luz difusa neutral
            glLightfv(GL_LIGHT2, GL_SPECULAR, [0.3, 0.3, 0.3, 1.0])
            
            # Ajustar material para resaltar sin tonos amarillos
            glMaterialfv(GL_FRONT, GL_SPECULAR, [0.6, 0.6, 0.6, 1.0])
            glMaterialf(GL_FRONT, GL_SHININESS, 32.0)
        else:
            glDisable(GL_LIGHT2)
            glMaterialfv(GL_FRONT, GL_SPECULAR, [0.2, 0.2, 0.2, 1.0])
            glMaterialf(GL_FRONT, GL_SHININESS, 20.0)


    def dibujar_personaje(self, personaje, is_selected):
        glPushMatrix()
        x, y, z = personaje.posicion
        glTranslatef(x, y, z)

        # Configurar iluminación específica para el personaje
        self.configurar_luz_personaje(is_selected)
        
        if is_selected:
            # Actualizar posición de la luz del personaje seleccionado
            glLightfv(GL_LIGHT2, GL_POSITION, [x, 5.0, z, 1.0])
            
            # Aumentar brillo manteniendo el color
            glColor3f(1.0, 1.0, 1.0)
        else:
            # Color normal para personajes no seleccionados
            glColor3f(0.9, 0.9, 0.9)
            
        personaje.render()
        glPopMatrix()

    def dibujar_piso_pared(self):
        glEnable(GL_TEXTURE_2D)
        
        # Configurar material para las texturas con un filtro neutral
        glMaterialfv(GL_FRONT, GL_SPECULAR, [0.2, 0.2, 0.2, 1.0])
        glMaterialf(GL_FRONT, GL_SHININESS, 16.0)

        # Suelo con filtro de color gris
        glBindTexture(GL_TEXTURE_2D, self.floor_texture)
        glColor3f(0.6, 0.6, 0.6)  # Aplicar filtro gris a la textura del suelo
        glBegin(GL_QUADS)
        glNormal3f(0.0, 1.0, 0.0)
        glTexCoord2f(0, 0); glVertex3f(-20.0, -2.0, -20.0)
        glTexCoord2f(1, 0); glVertex3f(20.0, -2.0, -20.0)
        glTexCoord2f(1, 1); glVertex3f(20.0, -2.0, 20.0)
        glTexCoord2f(0, 1); glVertex3f(-20.0, -2.0, 20.0)
        glEnd()

        # Pared con filtro de color gris
        glBindTexture(GL_TEXTURE_2D, self.wall_texture)
        glColor3f(0.6, 0.6, 0.6)  # Aplicar filtro gris a la textura de la pared
        glBegin(GL_QUADS)
        glNormal3f(0.0, 0.0, 1.0)
        glTexCoord2f(0, 0); glVertex3f(-30.0, -2.0, -20.0)
        glTexCoord2f(1, 0); glVertex3f(30.0, -2.0, -20.0)
        glTexCoord2f(1, 1); glVertex3f(30.0, 25.0, -20.0)
        glTexCoord2f(0, 1); glVertex3f(-30.0, 25.0, -20.0)
        glEnd()

        glDisable(GL_TEXTURE_2D)


    def draw_scene(self):
        glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)

        # Dibujar escenario
        self.dibujar_piso_pared()
        self.update_jump()
        # Dibujar personajes
        for idx, character in enumerate(self.personaje):
            is_selected = idx == self.selected_character
            if is_selected:
                character.set_position(character.posicion[0], -1.0+self.jump_height, character.posicion[2])
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
                    self.selected_character = event.key - pygame.K_1
                elif event.key == pygame.K_RETURN:
                    if self.selected_character >= 0:
                        print(f"Personaje seleccionado: {self.selected_character + 1}")
                        self.personaje[self.selected_character].start_jump()  # Iniciar el salto
                        self.saltar()
                    else:
                        print("No se ha seleccionado ningún personaje.")
        return True

    def saltar(self):
        # Iniciar el salto
        self.jumping = True

    def update_jump(self):
        if self.jumping:
            # Actualizar la altura del salto
            if self.jump_height < 2.0:  # Altura máxima del salto
                self.jump_height += self.jump_speed
            else:
                self.jumping = False  # Terminar el salto al alcanzar la altura máxima
        else:
            # Bajar el personaje
            if self.jump_height > 0:
                self.jump_height -= self.jump_speed

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