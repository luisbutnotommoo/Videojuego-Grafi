import pygame as game
import random
import time
from threading import Thread

# coordenadas torres
torre_cuspide = [(120, 200), (200, 220), (280, 180), (200, 160), (120, 200)]
pared_izq = [(120, 520), (200, 540), (200, 220), (120, 200), (120, 520)]
pared_der = [(200, 540), (280, 500), (280, 180), (200, 220), (200, 540)]

torre_cuspide2 = [(560, 40), (640, 60), (560, 100), (480, 80), (560, 40)]
pared_izq2 = [(560, 100), (480, 80), (480, 240), (560, 260), (560, 100)]
pared_der2 = [(640, 60), (560, 100), (560, 260), (640, 220), (640, 60)]

game.init()

ANCHO, ALTO = 800, 400
ventana = game.display.set_mode((ANCHO, ALTO))
game.display.set_caption("Drawing with Luis")
inicio_tiempo = time.time()

Verde_sage = (216,234,158)
Verde = (199,221,131)
Verde_sombra = (127,149,79)
VERDE_PASTO = (34, 139, 34)
Blanco_perla=(253,250,231)

superficie_pasto1 = game.Surface((ANCHO, ALTO), game.SRCALPHA)
superficie_pasto2 = game.Surface((ANCHO, ALTO), game.SRCALPHA)
superficie_torre1 = game.Surface((ANCHO,ALTO),game.SRCALPHA)
superficie_torre2 = game.Surface((ANCHO,ALTO),game.SRCALPHA)
superficie_valle = game.Surface((ANCHO,ALTO),game.SRCALPHA)

pasto_dibujado = False
torres_dibujadas = False
valle_dibujado = False
destello_activo = False
radio_destello = 0
alpha_destello = 255

paredes = [pared_izq, pared_der, pared_izq2, pared_der2]
cuspides = [torre_cuspide, torre_cuspide2]

torre1=[torre_cuspide,pared_izq, pared_der]
torre2=[torre_cuspide2, pared_izq2, pared_der2]

# Variables globales para las posiciones
pos_y1 = 0
pos_y2 = 0
pos_x1 = 0
pos_x2 = 0
animacion_activa = True

hilo1=None
hilo2=None

def crear_destello():
    superficie_destello = game.Surface((ANCHO, ALTO), game.SRCALPHA)
    return superficie_destello

def animar_destello():
    global destello_activo, radio_destello, alpha_destello
    destello_activo = True
    radio_destello = 0
    alpha_destello = 255

def crea_hilo(hilo,metodo,argumentos):
    hilo=Thread(target=metodo,args=argumentos)
    hilo.setDaemon=True
    hilo.start()


def pintar_torres():
    superficie_torre1.fill((0, 0, 0, 0))
    for poligono in torre1:
        game.draw.polygon(superficie_torre1, (100, 100, 100), poligono)
        game.draw.polygon(superficie_torre1, (0, 0, 0), poligono, 1)    

    superficie_torre2.fill((0, 0, 0, 0))
    for poligono in torre2:
        game.draw.polygon(superficie_torre2, (89, 89, 89), poligono)  
        game.draw.polygon(superficie_torre2, (0, 0, 0), poligono, 1)    


def dibujar_pasto(hilo, superficie, lim_sup, x, ventana):
    superficie.fill((0, 0, 0, 0))  # Transparente
    while x < lim_sup:
        altura_pasto = random.randint(150, 390)
        game.draw.line(superficie, VERDE_PASTO, 
                      (x, ALTO),
                      (x + random.randint(-5, 5), ALTO - altura_pasto), 
                      2)
        x += random.randint(2, 3)


def mover_pasto():
    global pos_y1, pos_y2, pos_x1, pos_x2, animacion_activa
    
    while animacion_activa:
        time.sleep(0.08)
        
        pos_y1 += 10
        pos_y2 += 10
        pos_x1 -= 5
        pos_x2 += 5
        
        # Modifica la condición de finalización
        if pos_y1 > ALTO + 100 or pos_y2 > ALTO + 100:  # Asegura que salga por abajo
            animacion_activa = False
            # Llamar directamente a animar_destello aquí
            game.event.post(game.event.Event(game.USEREVENT + 1))  # Evento personalizado
            break



corriendo = True
clock = game.time.Clock()
superficie_destello = crear_destello()

while corriendo:
    for evento in game.event.get():
        if evento.type == game.QUIT:
            animacion_activa = False
            corriendo = False
        elif evento.type == game.USEREVENT + 1:  # Nuestro evento personalizado
            animar_destello()

    tiempo_actual = time.time() - inicio_tiempo
    
    ventana.fill(Verde_sage)
    
    if tiempo_actual <= 5:
        if not pasto_dibujado:
            crea_hilo(hilo1, dibujar_pasto, 
                     (hilo1, superficie_pasto1, ANCHO//2, 0, ventana))
            crea_hilo(hilo2, dibujar_pasto, 
                     (hilo2, superficie_pasto2, ANCHO, ANCHO//2, ventana))
            hilo_movimiento = Thread(target=mover_pasto)
            hilo_movimiento.daemon = True
            hilo_movimiento.start()
            pasto_dibujado = True
    else:
        pintar_torres()
    
    # Dibujar elementos base
    ventana.blit(superficie_valle,(0, 0))
    ventana.blit(superficie_torre1,(0, 0))
    ventana.blit(superficie_torre2,(0, 0))
    
    if pasto_dibujado:
        ventana.blit(superficie_pasto1, (pos_x1, pos_y1))
        ventana.blit(superficie_pasto2, (pos_x2, pos_y2))
    
    # Modificar el manejo del destello para hacerlo más visible
    if destello_activo:
        superficie_destello.fill((0,0,0,0))
        
        # Hacer el destello más visible
        color_destello = (255, 255, 255, alpha_destello)
        centro_destello = (ANCHO // 2, ALTO // 2)
        
        # Dibujar múltiples círculos para hacer el destello más notorio
        game.draw.circle(superficie_destello, color_destello, 
                        centro_destello, radio_destello)
        game.draw.circle(superficie_destello, (255,255,200, alpha_destello//2), 
                        centro_destello, radio_destello - 10)
        
        # Ajustar velocidad y tamaño del destello
        radio_destello += 8  # Más rápido
        alpha_destello = max(0, alpha_destello - 3)  # Más lento el desvanecimiento
        
        ventana.blit(superficie_destello, (0,0))
        
        if alpha_destello <= 0:
            destello_activo = False
            radio_destello = 0
    
    game.display.flip()
    clock.tick(60)

game.quit()