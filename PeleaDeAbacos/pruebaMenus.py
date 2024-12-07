import pygame

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
            
            self.snd_seleccion = pygame.mixer.Sound("Sonidos/click.mp3")
            pygame.mixer.music.load("Sonidos/menu_principal.mp3")
            pygame.mixer.music.play(loops=-1)
        except pygame.error:
            print("No se pudo cargar la imagen de fondo. Usando un fondo negro predeterminado.")
            self.bg_menuPrincipal = None
            self.bg_menuNiveles = None
        
        self.estado_general = "sin seleccionar"

        self.fondo_en_pantalla = self.bg_menuPrincipal
        self.font_titulo = pygame.font.Font(None, 45)
        self.font_opciones = pygame.font.Font(None, 36)
        self.font_acerca_de = pygame.font.Font(None, 25)
        self.texto_menuPrincipal = ["Jugar", "Acerca de", "Salir"]
        self.texto_niveles = ["Nivel 1", "Nivel 2", "Nivel 3", "Volver", "Salir"]
        self.texto_acerca_de = ["Nombre del software: Duelo de abacos","",
                                "Versión del Juego: 1.0","",
                                "Equipo de Desarrollo:",
                                "- Hernández Torres Lineth",
                                "- Ortiz Gallegos Starenka Susana",
                                "- Vallejo Ramírez Emmanuel",
                                "- Rivera Cruz Luis Antonio","",
                                "Herramientas Utilizadas: Python, Pygame, OpenGL, PIL, GLFW.","",
                                "Agradecimientos: Agradecemos públicamente a Beyonce."]
        self.selected_index = 0
        self.texto_actual = self.texto_menuPrincipal
        self.salto_actual = 60
        self.bandera_acerca_de = False


    def handle_events(self):
        """Procesa los eventos del juego."""
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.running = False
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_DOWN and not self.bandera_acerca_de:
                    self.selected_index = (self.selected_index + 1) % len(self.texto_actual)
                    self.snd_seleccion.play()
                elif event.key == pygame.K_UP and not self.bandera_acerca_de:
                    self.selected_index = (self.selected_index - 1) % len(self.texto_actual)
                    self.snd_seleccion.play()
                elif event.key == pygame.K_RETURN:
                    self.snd_seleccion.play()
                    if self.texto_actual == self.texto_menuPrincipal and not self.bandera_acerca_de:
                        if self.texto_actual[self.selected_index] == "Jugar":
                            self.update(False)
                        elif self.texto_actual[self.selected_index] == "Acerca de":
                            self.bandera_acerca_de = True
                            self.selected_index = 0
                        elif self.texto_actual[self.selected_index] == "Salir":
                            self.estado_general = "salir"
                            pygame.mixer.music.stop()
                            self.running = False
                    elif self.texto_actual == self.texto_niveles and not self.bandera_acerca_de:
                        if self.texto_actual[self.selected_index] == "Nivel 1":
                            self.estado_general = "personaje1"
                            pygame.mixer.music.stop()
                            self.running = False
                        if self.texto_actual[self.selected_index] == "Nivel 2":
                            self.estado_general = "personaje2"
                            pygame.mixer.music.stop()
                            self.running = False
                        if self.texto_actual[self.selected_index] == "Nivel 3":
                            self.estado_general = "personaje3"
                            pygame.mixer.music.stop()
                            self.running = False
                        if self.texto_actual[self.selected_index] == "Volver":
                            self.update()
                        elif self.texto_actual[self.selected_index] == "Salir":
                            self.estado_general = "salir"
                            pygame.mixer.music.stop()
                            self.running = False
                    elif self.bandera_acerca_de:
                        self.bandera_acerca_de = False


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
        if self.bandera_acerca_de: 
            # Cuando la bandera esté activa, pintara el mensaje 'Acerca de'   
            text_background1 = pygame.Surface((600, 350), pygame.SRCALPHA) 
            text_background1.fill((50, 50, 50, 150))
            self.texto_con_salto(text_background1, self.texto_acerca_de, self.font_acerca_de, 10, 10, 20)
            self.texto_seleccionado(text_background1, ["Volver"], 255, 300)
            self.screen.blit(text_background1, (100, 100))
        else:
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




    def texto_con_salto(self, surface, text_lines, font, x, y, salto=30):
        for line in text_lines:
            text_surface = font.render(line, True, (255, 255, 255))
            surface.blit(text_surface, (x, y))  # Posicionar cada línea
            y += salto  # Aumentar la posición Y para la siguiente línea



    def texto_seleccionado(self, surface, text_lines, x, y, salto=30):
        for i, option in enumerate(text_lines):
            if i == self.selected_index:
                text_surface = self.font_opciones.render(option, True, (0, 255, 0))  # Color de selección
            else:
                text_surface = self.font_opciones.render(option, True, (255, 255, 255))

            surface.blit(text_surface, (x, y)) 
            y += salto 


    def run(self):
        """Bucle principal del juego."""
        while self.running:
            self.handle_events()
            self.draw() 
            self.clock.tick(60) 
        
        #self.quit_game()
        return self.estado_general  # Retornar el valor deseado (ej. "game over", "exit", etc.)

    def quit_game(self):
        pygame.quit()

if __name__ == "__main__":
    game = Menus()
    game.run() 
