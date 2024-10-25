import pygame as game
import random
import time
import pintor as picasso

# Inicializar Pygame
game.init()

# Definir tamaño de la ventana y colores
ANCHO, ALTO = 800, 400
ventana = game.display.set_mode((ANCHO, ALTO))
game.display.set_caption("Drawing with Luis")
inicio_tiempo = time.time()

# Colores copiados de GUI
Azul_Espresso = (187,213,228)
Navy_Espresso = (18,34,66)
Amarillo_Espresso = (237,195,94)
Rosa_Espresso = (223,149,174)
Cafe_galleta1 = (170,141,114)
Cafe_galleta2 = (150,122,97)
Falso_Plateado = (234,234,234)
Verde_sage = (216,234,158)
Verde = (199,221,131)
Verde_sombra = (127,149,79)
Cafe = (100,64,39)
Cafe_sombra = (81, 37, 10)
Cafe_ilum = (140, 88, 25)
Cafe_penumbra = (56, 10, 0)
Blanco_perla = (253,250,231)
Gris = (141,141,141)
VERDE_PASTO = (34, 139, 34)

# Crear una superficie para almacenar el pasto
superficie_pasto = game.Surface((ANCHO, ALTO), game.SRCALPHA)
pasto_dibujado = False

def dibujar_pasto():
    x = 0
    superficie_pasto.fill((0, 0, 0, 0))  # Transparente
    
    while x < ANCHO:
        altura_pasto = random.randint(40, 80)
        game.draw.line(superficie_pasto, VERDE_PASTO, (x, ALTO), 
                      (x + random.randint(-5, 5), ALTO - altura_pasto), 3)
        distancia = random.randint(5, 20)
        x += distancia

def dibujar_paisaje():
    # Ejemplo con el paisaje de la tetera
    game.draw.polygon(ventana, Verde, picasso.matriz_pared_atras)
    game.draw.polygon(ventana, Verde_sombra, picasso.matriz_pared_sombra)
    game.draw.rect(ventana, Blanco_perla, (344,74,428,152))
    game.draw.polygon(ventana, Gris, picasso.convierte_coordenadas(picasso.montaña))
    game.draw.polygon(ventana, Cafe, picasso.convierte_coordenadas(picasso.mesa))
    game.draw.polygon(ventana, Cafe_sombra, picasso.convierte_coordenadas(picasso.mesa_grosor_sombra))
    game.draw.polygon(ventana, Cafe_sombra, picasso.convierte_coordenadas(picasso.mesa_pata))
    game.draw.polygon(ventana, Cafe_ilum, picasso.convierte_coordenadas(picasso.mesa_grosor_ilum))
    game.draw.polygon(ventana, Cafe_penumbra, picasso.convierte_coordenadas(picasso.mesa_pata_sombra))
    
    game.draw.polygon(ventana, Navy_Espresso, picasso.convierte_coordenadas(picasso.escala_matriz(picasso.matriz_tapa3)))
    game.draw.polygon(ventana, Navy_Espresso, picasso.convierte_coordenadas(picasso.escala_matriz(picasso.matriz_tapa4)))
    game.draw.polygon(ventana, Navy_Espresso, picasso.convierte_coordenadas(picasso.escala_matriz(picasso.matriz_tapa5)))
    game.draw.polygon(ventana, Navy_Espresso, picasso.convierte_coordenadas(picasso.escala_matriz(picasso.matriz_asa1)))
    game.draw.polygon(ventana, Navy_Espresso, picasso.convierte_coordenadas(picasso.escala_matriz(picasso.matriz_asa2)))
    game.draw.polygon(ventana, Navy_Espresso, picasso.convierte_coordenadas(picasso.escala_matriz(picasso.matriz_asa3)))
    game.draw.polygon(ventana, Navy_Espresso, picasso.convierte_coordenadas(picasso.escala_matriz(picasso.matriz_asa4)))
    
    game.draw.polygon(ventana, Azul_Espresso, picasso.convierte_coordenadas_dobles(picasso.escala_matriz_matrices(picasso.matriz_base)))
    game.draw.polygon(ventana, Azul_Espresso, picasso.convierte_coordenadas(picasso.escala_matriz(picasso.matriz_tapa1)))
    game.draw.polygon(ventana, Azul_Espresso, picasso.convierte_coordenadas(picasso.escala_matriz(picasso.matriz_tapa2)))
    game.draw.polygon(ventana, Azul_Espresso, picasso.convierte_coordenadas(picasso.escala_matriz(picasso.matriz_tapa6)))
    game.draw.polygon(ventana, Azul_Espresso, picasso.convierte_coordenadas(picasso.escala_matriz(picasso.matriz_boquilla1)))
    game.draw.polygon(ventana, Azul_Espresso, picasso.convierte_coordenadas(picasso.escala_matriz(picasso.matriz_boquilla2)))
    game.draw.polygon(ventana, Azul_Espresso, picasso.convierte_coordenadas(picasso.escala_matriz(picasso.matriz_boquilla3)))
    
    game.draw.polygon(ventana, Rosa_Espresso, picasso.convierte_coordenadas(picasso.matriz_taza))
    game.draw.lines(ventana, Rosa_Espresso, False, picasso.matriz_taza_asa, 3)
    game.draw.ellipse(ventana, Blanco_perla, (260,290,85,50))
    game.draw.ellipse(ventana, Amarillo_Espresso, (275,304,25,25))
    game.draw.ellipse(ventana, Cafe_galleta1, (285,304,25,25))
    game.draw.ellipse(ventana, Amarillo_Espresso, (285,294,25,25))
    game.draw.ellipse(ventana, Cafe_galleta1, (300,304,25,25))
    game.draw.ellipse(ventana, Amarillo_Espresso, (304,295,25,25))
    game.draw.ellipse(ventana, Cafe_galleta1, (281,304,25,25))


corriendo = True
clock = game.time.Clock()

while corriendo:
    for evento in game.event.get():
        if evento.type == game.QUIT:
            corriendo = False

    tiempo_actual = time.time() - inicio_tiempo
    
    # Antes de los 5 segundos, usar fondo verde sage
    if tiempo_actual <= 5:
        ventana.fill(Verde_sage)
        if not pasto_dibujado:
            dibujar_pasto()
            if tiempo_actual >= 5:
                pasto_dibujado = True
    else:
        # Después de 5 segundos, dibujar el paisaje de la tetera
        dibujar_paisaje()
    
    # Dibujar el pasto encima
    ventana.blit(superficie_pasto, (0, 0))
    
    game.display.flip()
    clock.tick(60)

game.quit()