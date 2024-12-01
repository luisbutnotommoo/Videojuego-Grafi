import pygame
import pygame_menu
import os
from Imagenes.redimensionar_imagen import ruta_actual as ruta_img

class MenuPrincipal:
    def __init__(self):
        pygame.init()
        self.jugar = True
        self.WINDOW_WIDTH = 800
        self.WINDOW_HEIGHT = 600
        self.surface = pygame.display.set_mode((self.WINDOW_WIDTH, self.WINDOW_HEIGHT))
        pygame.display.set_caption('Mi Juego')

        # Carga de imagen de fondo
        try:
            # Reemplaza 'background.jpg' con la ruta de tu imagen de fondo
            self.background_image = pygame.image.load('Imagenes/pared3.jpg')
            # Redimensiona la imagen para que coincida con el tamaño de la ventana
            self.background_image = pygame.transform.scale(self.background_image, (self.WINDOW_WIDTH, self.WINDOW_HEIGHT))
        except pygame.error:
            print("No se pudo cargar la imagen de fondo. Usando un fondo negro predeterminado.")
            self.background_image = None
        
        # Crea un tema personalizado
        self.menu_theme = pygame_menu.Theme(
            background_color=(0, 0, 0, 100),
            title_background_color=(0, 0, 0, 100),
            title_font_color=(255, 255, 255),
            widget_font_color=(255, 255, 255)
        )

        # Crea el menú principal
        self.menu = pygame_menu.Menu('Duelos De Abacos', 400, 300, theme=self.menu_theme)
        self.menu.add.button('Jugar', self.start_the_game)
        self.menu.add.button('Acerca de', self.show_about)
        self.menu.add.button('Salir', pygame_menu.events.EXIT)

    def start_the_game(self):
        print("¡Juego comenzado!")
        self.jugar = False  # Cambia esta bandera para indicar que el juego ha comenzado

    def show_about(self):
        print("Este es un juego hecho con Pygame y pygame_menu.")
        about_menu = pygame_menu.Menu('Acerca de', 400, 300, theme=pygame_menu.themes.THEME_SOLARIZED)
        about_menu.add.label('Creado con Pygame', align=pygame_menu.locals.ALIGN_CENTER)
        about_menu.add.label('Menú personalizado', align=pygame_menu.locals.ALIGN_CENTER)
        about_menu.add.button('Volver', pygame_menu.events.BACK)
        about_menu.mainloop(self.surface)

    def reset(self):
        self.jugar = True  # Reinicia la bandera para permitir volver al menú principal

    def main(self):
        clock = pygame.time.Clock()
        while True:
            if self.background_image:
                self.surface.blit(self.background_image, (0, 0))
            else:
                self.surface.fill((0, 0, 0))
            
            events = pygame.event.get()
            for event in events:
                if event.type == pygame.QUIT:
                    pygame.quit()
                    return
            
            if self.menu.is_enabled():
                self.menu.update(events)
                self.menu.draw(self.surface)
            if not self.jugar:  # Si el juego ha comenzado, salimos del bucle
                break
            
            pygame.display.update()
            clock.tick(60)

# Ejecuta el menú
if __name__ == '__main__':
    menu_principal = MenuPrincipal()  # Crear una instancia de MenuPrincipal
    menu_principal.main()  # Llamar al método main de la instancia