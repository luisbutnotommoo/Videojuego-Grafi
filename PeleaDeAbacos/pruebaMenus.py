import pygame
import sys

class Menus:
    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode((800, 600))
        pygame.display.set_caption("Duelo de abacos")
        self.clock = pygame.time.Clock() 
        self.running = True

        try:
            self.bg_menuPrincipal = pygame.image.load("Imagenes/pared3.jpg")
            self.bg_menuPrincipal = pygame.transform.scale(self.bg_menuPrincipal, (800, 600))
            self.bg_menuNiveles = pygame.image.load("Imagenes/pared2.jpg")
            self.bg_menuNiveles = pygame.transform.scale(self.bg_menuNiveles, (800, 600))
        except pygame.error:
            print("No se pudo cargar la imagen de fondo. Usando un fondo negro predeterminado.")
            self.bg_menuPrincipal = None
            self.bg_menuNiveles = None
        
        self.esta_jugando = False
        self.estado_menu = "inicio"
        self.fondo_en_pantalla = self.bg_menuPrincipal
        self.font_titulo = pygame.font.Font(None, 45)
        self.font_opciones = pygame.font.Font(None, 36)
        self.texto_menuPrincipal = ["Jugar", "Acerca de", "Salir"]
        self.texto_niveles = ["Nivel 1", "Nivel 2", "Nivel 3", "Volver", "Salir"]
        self.selected_index = 0
        self.texto_actual = self.texto_menuPrincipal
        self.salto_actual = 60


    def handle_events(self):
        """Procesa los eventos del juego."""
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.running = False
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_DOWN:  # Flecha abajo
                    self.selected_index = (self.selected_index + 1) % len(self.texto_actual)
                elif event.key == pygame.K_UP:  # Flecha arriba
                    self.selected_index = (self.selected_index - 1) % len(self.texto_actual)
                elif event.key == pygame.K_RETURN:  # Enter (seleccionar opción)
                    print(f"Seleccionado: {self.texto_actual[self.selected_index]}")
                    # Aquí puedes agregar la lógica para lo que sucede cuando se selecciona una opción

                    if self.texto_actual == self.texto_menuPrincipal:
                        if self.texto_actual[self.selected_index] == "Jugar":
                            self.update(False)
                        elif self.texto_actual[self.selected_index] == "Salir":
                            self.running = False  # Cerrar el juego al seleccionar "Salir"
                    elif self.texto_actual == self.texto_niveles:
                        if self.texto_actual[self.selected_index] == "Volver":
                            self.update()
                        elif self.texto_actual[self.selected_index] == "Salir":
                            self.running = False  # Cerrar el juego al seleccionar "Salir"


    def update(self, estado=True):
        """Actualiza la lógica del juego."""
        # Estado true para menu principal, false para niveles
        if estado:
            self.texto_actual = self.texto_menuPrincipal
            self.salto_actual = 60
            self.fondo_en_pantalla = self.bg_menuPrincipal
        else:
            self.texto_actual = self.texto_niveles
            self.salto_actual = 40
            self.fondo_en_pantalla = self.bg_menuNiveles
        self.selected_index = 0


    def draw(self):
        """Dibuja en la pantalla."""
        self.screen.blit(self.fondo_en_pantalla, (0, 0))
            
        # SUPERFICIE TRANSPARENTE
        text_background1 = pygame.Surface((400, 300), pygame.SRCALPHA) 
        text_background1.fill((50, 50, 50, 150))
        text_background2 = pygame.Surface((400, 80), pygame.SRCALPHA) 
        text_background2.fill((50, 50, 50, 150))

        text_titulo = self.font_titulo.render("DUELO  DE  ABACOS", True, (255, 255, 255))

        # Poner texto dentro de la superficie
        text_background2.blit(text_titulo, (48, 25))
        self.texto_seleccionado(text_background1, self.texto_actual, 50, 100, self.salto_actual)
        
        # Dibujar la superficie en la pantalla principal
        self.screen.blit(text_background1, (200, 100))
        self.screen.blit(text_background2, (200, 100))  

        pygame.display.update()  # Refleja los cambios en pantalla






    def texto_seleccionado(self, surface, text_lines, x, y, salto=30):
        for i, option in enumerate(text_lines):
            if i == self.selected_index:
                text_surface = self.font_opciones.render(option, True, (0, 255, 0))  # Color de selección
            else:
                text_surface = self.font_opciones.render(option, True, (255, 255, 255))  # Blanco para otras opciones

            surface.blit(text_surface, (x, y))  # Dibujar la opción
            y += salto  # Aumentar el desplazamiento vertical para la siguiente línea

    def texto_con_salto(self, surface, text_lines, x, y, salto=30):
        for line in text_lines:
            text_surface = self.font_opciones.render(line, True, (255, 255, 255))
            surface.blit(text_surface, (x, y))  # Posicionar cada línea
            y += salto  # Aumentar la posición Y para la siguiente línea

    def run(self):
        """Bucle principal del juego."""
        while self.running:
            self.handle_events()  # Manejar eventos
            self.draw()  # Dibujar en pantalla
            self.clock.tick(30)  # Limitar a 60 FPS

        self.quit_game()  # Asegurar cierre al salir del bucle

    def quit_game(self):
        """Cierra Pygame y termina el programa."""
        pygame.quit()
        sys.exit()

if __name__ == "__main__":
    game = Menus()
    game.run() 
