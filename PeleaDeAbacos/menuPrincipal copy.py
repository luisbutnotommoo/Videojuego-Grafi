import pygame
import pygame_menu
import os

class MenuPrincipal:
    def __init__(self):
        # Inicializa Pygame
        pygame.init()
        self.jugar=True
        # Configura la pantalla
        self.WINDOW_WIDTH = 800
        self.WINDOW_HEIGHT = 600
        self.surface = pygame.display.set_mode((self.WINDOW_WIDTH, self.WINDOW_HEIGHT))
        pygame.display.set_caption('Mi Juego')

        # Carga de imagen de fondo
        try:
            # Reemplaza 'background.jpg' con la ruta de tu imagen de fondo
            self.background_image = pygame.image.load('Imagenes/pared4.jpg')
            # Redimensiona la imagen para que coincida con el tamaño de la ventana
            self.background_image = pygame.transform.scale(self.background_image, (self.WINDOW_WIDTH, self.WINDOW_HEIGHT))
        except pygame.error:
            print("No se pudo cargar la imagen de fondo. Usando un fondo negro predeterminado.")
            self.background_image = None
            pass
        
        # Crea un tema personalizado
        self.menu_theme = pygame_menu.Theme(
            background_color=(0, 0, 0, 100),  # Transparente
            title_background_color=(0, 0, 0, 100),  # Fondo semi-transparente para el título
            title_font_color=(255, 255, 255),
            widget_font_color=(255, 255, 255)
        )

        # Crea el menú principal con el tema personalizado
        self.menu = pygame_menu.Menu('Duelo De Abacos', 400, 300, theme=self.menu_theme)
        self.menu.add.button('Nivel 1', self.start_the_game)
        self.menu.add.button('Nivel 2', self.show_about)
        self.menu.add.button('Nivel 3')
        self.menu.add.button('Volver')
        self.menu.add.button('Salir', pygame_menu.events.EXIT)

    # Funciones para las opciones del menú
    def start_the_game(self):
        print("¡Juego comenzado!")
        self.jugar=False
        # Aquí puedes agregar la lógica de inicio del juego

    def show_about(self):
        print("Este es un juego hecho con Pygame y pygame_menu.")
        
        # Opcional: Muestra un menú de información
        about_menu = pygame_menu.Menu('Acerca de', 400, 300, theme=pygame_menu.themes.THEME_SOLARIZED)
        about_menu.add.label('Creado con Pygame', align=pygame_menu.locals.ALIGN_CENTER)
        about_menu.add.label('Menú personalizado', align=pygame_menu.locals.ALIGN_CENTER)
        about_menu.add.button('Volver', pygame_menu.events.BACK)
        about_menu.mainloop(self.surface)

    # Bucle principal del juego
    def main(self):
        clock = pygame.time.Clock()
        
        while True:
            # Dibuja la imagen de fondo si existe
            if self.background_image:
                self.surface.blit(self.background_image, (0, 0))
            else:
                self.surface.fill((0, 0, 0))  # Fondo negro predeterminado
            
            # Eventos
            events = pygame.event.get()
            for event in events:
                if event.type == pygame.QUIT:
                    pygame.quit()
                    return
            
            # Actualiza y dibuja el menú
            if self.menu.is_enabled():
                self.menu.update(events)
                self.menu.draw(self.surface)
            if not self.jugar:  # Si la bandera del menú es falsa, salimos del bucle
                break
            
            pygame.display.update()
            clock.tick(60)  # Limita a 60 FPS

# Ejecuta el menú
if __name__ == '__main__':
    menu_principal = MenuPrincipal()  # Crear una instancia de MenuPrincipal
    menu_principal.main()  # Llamar al método main de la instancia