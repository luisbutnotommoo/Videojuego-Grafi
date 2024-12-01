import pygame
import pygame_menu

# Inicializa Pygame
pygame.init()

# Configura la pantalla
surface = pygame.display.set_mode((600, 400))

# Funciones para las opciones del menú
def start_the_game():
    print("¡Juego comenzado!")

def show_about():
    print("Este es un juego hecho con Pygame y pygame_menu.")

# Crea el menú principal
menu = pygame_menu.Menu('Bienvenido', 400, 300, theme=pygame_menu.themes.THEME_BLUE)
menu.add.button('Jugar', start_the_game)
menu.add.button('Acerca de', show_about)
menu.add.button('Salir', pygame_menu.events.EXIT)

# Ejecuta el menú
menu.mainloop(surface)

# Finaliza Pygame al cerrar el menú
pygame.quit()