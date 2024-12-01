import pygame
import pygame_menu
import os



class MenuNivel:
    def __init__(self):
        pygame.init()  # Asegúrate de inicializar pygame
        self.jugar = True
        self.nivel = 0

        # Configura la pantalla
        self.WINDOW_WIDTH = 800
        self.WINDOW_HEIGHT = 600
        self.surface = pygame.display.set_mode((self.WINDOW_WIDTH, self.WINDOW_HEIGHT))
        pygame.display.set_caption('Mi Juego')

        # Ruta de la imagen de fondo
        ruta_imagen = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'Imagenes', 'aguaORG.jpg')
        try:
            self.background_image = pygame.image.load(ruta_imagen)
            self.background_image = pygame.transform.scale(self.background_image, (self.WINDOW_WIDTH, self.WINDOW_HEIGHT))
        except pygame.error as e:
            print(f"No se pudo cargar la imagen de fondo: {e}")
            self.background_image = None

        # Crea un tema personalizado
        self.menu_theme = pygame_menu.Theme(
            background_color=(0, 0, 0, 100),
            title_background_color=(0, 0, 0, 100),
            title_font_color=(255, 255, 255),
            widget_font_color=(255, 255, 255)
        )

        # Crea el menú de niveles
        self.menu = pygame_menu.Menu('Duelo De Abacos', 400, 300, theme=self.menu_theme)
        self.menu.add.button('Nivel 1', self.nivel1)
        self.menu.add.button('Nivel 2', self.nivel2)
        self.menu.add.button('Nivel 3', self.nivel3)
        self.menu.add.button('Volver', self.volver)
        self.menu.add.button('Salir', pygame_menu.events.EXIT)

    def reset(self):
        """Reinicia el estado del menú."""
        self.jugar = True
        self.nivel = 0

    def nivel1(self):
        print("¡Juego comenzado en Nivel 1!")
        self.nivel = 1
        self.jugar = False

    def nivel2(self):
        print("¡Juego comenzado en Nivel 2!")
        self.nivel = 2
        self.jugar = False

    def nivel3(self):
        print("¡Juego comenzado en Nivel 3!")
        self.nivel = 3
        self.jugar = False

    def volver(self):
        print("Regresando al menú principal...")
        self.jugar = False

    def main(self):
        """Bucle principal del menú."""
        clock = pygame.time.Clock()
        try:
            while self.jugar:
                # Dibuja el fondo
                if self.background_image:
                    self.surface.blit(self.background_image, (0, 0))
                else:
                    self.surface.fill((50, 50, 50))  # Fondo gris

                # Manejo de eventos
                events = pygame.event.get()
                for event in events:
                    if event.type == pygame.QUIT:
                        self.jugar = False
                        return  # Sal del menú

                # Actualiza y dibuja el menú
                if self.menu.is_enabled():
                    self.menu.update(events)
                    self.menu.draw(self.surface)

                pygame.display.update()
                clock.tick(60)  # Limita a 60 FPS
        except Exception as e:
            print(f"Error inesperado: {e}")
            pygame.quit()
            raise


# Ejecutar el menú
if __name__ == '__main__':
    menu_nivel = MenuNivel()
    menu_nivel.main()
