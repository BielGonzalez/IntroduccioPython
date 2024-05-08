import os
import sys
import time
from pygame.locals import *
import pygame
import random
import json


def dibujar_suelo(suelo_pos_xd):
    pantalla.blit(suelo_imagen, (suelo_pos_xd, 550))
    pantalla.blit(suelo_imagen, (suelo_pos_xd + 800, 550))


def crear_obstaculo():
    posicion_obstaculoo = random.choice(opciones_altura_obstaculos)
    pos_prueba = posicion_obstaculoo
    espacio_obstaculos = random.choice(opciones_espacio_obstaculos)
    obstaculo_abajo = imagen_obstaculos_abajo.get_rect(midtop=(1000, posicion_obstaculoo))
    obstaculo_arriba = imagen_obstaculos_arriba.get_rect(midbottom=(1000, posicion_obstaculoo - espacio_obstaculos))
    return obstaculo_abajo, obstaculo_arriba, pos_prueba


def mover_obstaculos(obstaculos):
    for obstaculo in obstaculos:
        obstaculo.centerx -= 5
    return obstaculos


def dibujar_obstaculos(obstaculos):
    for obstaculo in obstaculos:
        if obstaculo.bottom >= 600:
            pantalla.blit(imagen_obstaculos_abajo, obstaculo)
        else:
            pantalla.blit(imagen_obstaculos_arriba, obstaculo)


def colisiones_tubos(obstaculos):
    vivoo = True
    for obstaculo in obstaculos:
        if rect_jugador.colliderect(obstaculo):
            vivoo = 2
            puntuacion_actualizada('off', rect_jugador, )
    if rect_jugador.bottom >= 550:
        puntuacion_actualizada('off', rect_jugador,)
        vivoo = 2
    if rect_jugador.top <= - 10:
        puntuacion_actualizada('off', rect_jugador,)
        vivoo = 2
    return vivoo


def decidir_altura_monedas(posicion_obstaculod, coinsd):
    global posicion_moneda
    posicion_moneda = 0
    if posicion_obstaculod == 500:
        for posicion_moneda in coinsd:
            posicion_moneda = 600
    elif posicion_obstaculod == 400:
        for posicion_moneda in coinsd:
            posicion_moneda = 500
    elif posicion_obstaculod == 500:
        for posicion_moneda in coinsd:
            posicion_moneda = 400
    elif posicion_obstaculod == 400:
        for posicion_moneda in coinsd:
            posicion_moneda = 300
    return posicion_moneda


def crear_moneda(obstaculo_abajo, coinsd):
    decidir_altura_monedas(obstaculo_abajo, coinsd)
    coin1 = imagen_moneda.get_rect(center=(1000, obstaculo_abajo - 75))
    coin2 = imagen_moneda.get_rect(center=(1000, obstaculo_abajo - 7555))
    return coin1, coin2


def mover_moneda(coins_f):
    for coin_f in coins_f:
        coin_f.x -= 5
    return coins_f


def dibujar_moneda(coins_f):
    for coin_f in coins_f:
        coin1 = coin_f
        if vivo == 1:
            pantalla.blit(imagen_moneda, (coin1.x, coin1.y))


def recoger_monedas(coinsl):
    recogida1 = 0
    ww = False
    for coin in coinsl:
        if rect_jugador.colliderect(coin):
            recogida1 += 1
            ww = True
            coins.remove(coin)
    return recogida1, ww


def girar_jugador(jugador):
    nuevo_jugador = pygame.transform.rotozoom(jugador, -movimiento_jugador * 3, 1)
    return nuevo_jugador


def puntuacion_actualizada(estado_juego, rect_jugadord):
    if estado_juego == "on":
        puntuacion_surface = fuente_juego.render(str(int(puntuacion)), True, (255, 255, 255))
        puntuacion_rect = puntuacion_surface.get_rect(center=(400, 100))
        pantalla.blit(puntuacion_surface, puntuacion_rect)
    if estado_juego == "off":
        puntuacion_surface = fuente_juego.render(str(int(puntuacion)), True, (255, 255, 255))
        puntuacion_rect = puntuacion_surface.get_rect(center=(468.5, 300))
        game_over = fuente_juego.render("GAME OVER", True, (55, 148, 110))
        puntuacion_texto = fuente_juego_peque.render("PUNTUACION", True, (74, 200, 10))
        monedas_texto = fuente_juego_peque.render("MONEDAS", True, (74, 200, 10))
        monedas_texto_rect = monedas_texto.get_rect(center=(330, 250))
        monedas_c = fuente_juego.render(str(int(monedas_totales)), True, (255, 255, 255))
        monedas_c_rect = monedas_c.get_rect(center=(330, 380))
        monedas_texto2 = fuente_juego_peque.render("CONSEGUIDAS", True, (74, 200, 10))
        monedas_texto_rect2 = monedas_texto.get_rect(center=(315, 270))
        monedas_texto3 = fuente_juego_peque.render("MONEDAS", True, (74, 200, 10))
        monedas_texto_rect3 = monedas_texto3.get_rect(center=(330, 330))
        monedas_texto4 = fuente_juego_peque.render("TOTALES", True, (74, 200, 10))
        monedas_texto_rect4 = monedas_texto4.get_rect(center=(330, 350))
        monedas_conseguidas_texto = fuente_juego.render(str(int(monedas)), True, (255, 255, 255))
        monedas_conseguidas_texto_rect = monedas_conseguidas_texto.get_rect(center=(330, 300))
        mejor_puntuacion_texto = fuente_juego_peque.render("RECORD", True, (74, 200, 10))
        mejor_puntuacion_texto_rect = mejor_puntuacion_texto.get_rect(center=(468.5, 340))
        game_over_rect = game_over.get_rect(center=(400, 150))
        puntuacion_texto_rect = puntuacion_texto.get_rect(center=(470, 260))
        mejor_puntuacion_surface = fuente_juego.render(str(int(mejor_puntuacion)), True, (255, 255, 255))
        mejor_puntuacion_rect = mejor_puntuacion_surface.get_rect(center=(468.5, 380))
        pantalla.blit(FONDOJUEGO, (0, 0))
        pantalla.blit(jugador_girado, rect_jugadord)
        pantalla.blit(pruebagameover, (230, 200))
        pantalla.blit(suelo_imagen, (suelo_pos_x, 550))
        pantalla.blit(suelo_imagen, (320 - suelo_pos_x, 550))
        pantalla.blit(game_over, game_over_rect)
        pantalla.blit(mejor_puntuacion_surface, mejor_puntuacion_rect)
        pantalla.blit(mejor_puntuacion_texto, mejor_puntuacion_texto_rect)
        pantalla.blit(monedas_texto, monedas_texto_rect)
        pantalla.blit(monedas_texto2, monedas_texto_rect2)
        pantalla.blit(monedas_conseguidas_texto, monedas_conseguidas_texto_rect)
        pantalla.blit(monedas_c, monedas_c_rect)
        pantalla.blit(monedas_texto3, monedas_texto_rect3)
        pantalla.blit(monedas_texto4, monedas_texto_rect4)
        pantalla.blit(puntuacion_surface, puntuacion_rect)
        pantalla.blit(puntuacion_texto, puntuacion_texto_rect)
        pantalla.blit(play_img, play_rect)
        menu_pausa(lista_obstaculos, coins)
        pantalla.blit(reiniciar_img, reiniciar_rect)
        pantalla.blit(atras_img, atras_rect)
        pantalla.blit(exit_img, exit_rect)
        pantalla.blit(play_img, play_rect)
        return vivo


def actualizar_mejor_puntuacion(puntuaciond, mejor_puntuaciond):
    if puntuaciond > mejor_puntuaciond:
        mejor_puntuaciond = puntuacion
    return mejor_puntuaciond


def menu_pausa(lista_obstaculosl, coinsll):
    puntuacion_surface = fuente_juego.render(str(int(puntuacion)), True, (255, 255, 255))
    puntuacion_rect = puntuacion_surface.get_rect(center=(468.5, 300))
    puntuacion_texto = fuente_juego_peque.render("PUNTUACION", True, (74, 200, 10))
    monedas_texto = fuente_juego_peque.render("MONEDAS", True, (74, 200, 10))
    monedas_texto_rect = monedas_texto.get_rect(center=(330, 250))
    monedas_c = fuente_juego.render(str(int(monedas_totales)), True, (255, 255, 255))
    monedas_c_rect = monedas_c.get_rect(center=(330, 380))
    monedas_texto2 = fuente_juego_peque.render("CONSEGUIDAS", True, (74, 200, 10))
    monedas_texto_rect2 = monedas_texto.get_rect(center=(315, 270))
    monedas_texto3 = fuente_juego_peque.render("MONEDAS", True, (74, 200, 10))
    monedas_texto_rect3 = monedas_texto3.get_rect(center=(330, 330))
    monedas_texto4 = fuente_juego_peque.render("TOTALES", True, (74, 200, 10))
    monedas_texto_rect4 = monedas_texto4.get_rect(center=(330, 350))
    monedas_conseguidas_texto = fuente_juego.render(str(int(monedas)), True, (255, 255, 255))
    monedas_conseguidas_texto_rect = monedas_conseguidas_texto.get_rect(center=(330, 300))
    mejor_puntuacion_texto = fuente_juego_peque.render("RECORD", True, (74, 200, 10))
    mejor_puntuacion_texto_rect = mejor_puntuacion_texto.get_rect(center=(468.5, 340))
    puntuacion_texto_rect = puntuacion_texto.get_rect(center=(470, 260))
    mejor_puntuacion_surface = fuente_juego.render(str(int(mejor_puntuacion)), True, (255, 255, 255))
    mejor_puntuacion_rect = mejor_puntuacion_surface.get_rect(center=(468.5, 380))
    pantalla.blit(FONDOJUEGO, (0, 0))
    pantalla.blit(jugador_girado, rect_jugador)
    lista_obstaculosl = mover_obstaculos(lista_obstaculosl)
    dibujar_obstaculos(lista_obstaculosl)
    coinsll = mover_moneda(coinsll)
    dibujar_moneda(coinsll)
    pantalla.blit(seccio_transparent, (0, 0))
    pantalla.blit(pruebagameover, (230, 200))
    pantalla.blit(suelo_imagen, (suelo_pos_x, 550))
    pantalla.blit(suelo_imagen, (320 - suelo_pos_x, 550))
    pantalla.blit(mejor_puntuacion_surface, mejor_puntuacion_rect)
    pantalla.blit(mejor_puntuacion_texto, mejor_puntuacion_texto_rect)
    pantalla.blit(monedas_texto, monedas_texto_rect)
    pantalla.blit(monedas_texto2, monedas_texto_rect2)
    pantalla.blit(monedas_conseguidas_texto, monedas_conseguidas_texto_rect)
    pantalla.blit(monedas_c, monedas_c_rect)
    pantalla.blit(monedas_texto3, monedas_texto_rect3)
    pantalla.blit(monedas_texto4, monedas_texto_rect4)
    pantalla.blit(puntuacion_surface, puntuacion_rect)
    pantalla.blit(puntuacion_texto, puntuacion_texto_rect)


pygame.init()
ALTURA = 600
ANCHURA = 800
flags = pygame.DOUBLEBUF
pantalla = pygame.display.set_mode((ANCHURA, ALTURA), flags)
clock = pygame.time.Clock()
fuente_juego = pygame.font.Font('04B_19.TTF', 35)
fuente_juego_peque = pygame.font.Font('04B_19.TTF', 20)
caida = 0.20
numero = 0
recogida = False
imagen_moneda = pygame.image.load("assets/moneda.png")
monedas = 0
try:
    with open("save_data/monedas_totales.txt") as archivo_monedas:
        monedas_totales = json.load(archivo_monedas)
except:
    monedas_totales = 0
GAMEOVER = "GAME OVER"
movimiento_jugador = 0
vivo = 2
posicion_moneda = 0
posicion_obstaculo = 0
puntuacion = 0
try:
    with open("save_data/mejor_puntuacion.txt") as archivo_mejor_puntuacion:
        mejor_puntuacion = json.load(archivo_mejor_puntuacion)
except:
    mejor_puntuacion = 0
pruebagameover = pygame.image.load("assets/pruebagameover.png")
suelo_imagen = pygame.image.load("assets/prueba.png").convert()
suelo_rect = suelo_imagen.get_rect(center=(800, 0))
FONDOJUEGO = pygame.image.load("assets/fondo1.png").convert()
suelo_pos_x = 0
tienda_img = pygame.image.load("assets/empezar.png").convert()
tienda_rect = tienda_img.get_rect(center=(600, 400))
comprar_img = pygame.image.load("assets/empezar.png").convert()
comprar_rect = comprar_img.get_rect(center=(600, 400))
seleccionar_img = pygame.image.load("assets/empezar.png").convert()
seleccionar_rect = seleccionar_img.get_rect(center=(200, 400))
empezar_img = pygame.image.load("assets/empezar.png").convert()
empezar_rect = empezar_img.get_rect(center=(200, 400))
salir_img = pygame.image.load("assets/salir.png").convert()
salir_rect = salir_img.get_rect(center=(400, 400))
pausa_img = pygame.image.load("assets/pausa.png").convert()
pausa_rect = pausa_img.get_rect(center=(50, 50))
reiniciar_img = pygame.image.load("assets/reiniciar.png").convert()
reiniciar_rect = reiniciar_img.get_rect(center=(325, 500))
reiniciar_puntuaciones_img = pygame.image.load("assets/reiniciar.png").convert()
reiniciar_puntuaciones_rect = reiniciar_puntuaciones_img.get_rect(center=(100, 100))
atras_img = pygame.image.load("assets/atras.png").convert()
atras_rect = atras_img.get_rect(center=(400, 500))
exit_img = pygame.image.load("assets/exit.png").convert()
exit_rect = exit_img.get_rect(center=(475, 500))
play_img = pygame.image.load("assets/play.png").convert()
play_rect = play_img.get_rect(center=(50, 50))
imagen_jugador2 = pygame.image.load("assets/tortuga.png").convert_alpha()
imagen_jugador = pygame.image.load("assets/tortuga.png").convert_alpha()
imagen_jugador3 = pygame.image.load("assets/tortuga.png").convert_alpha()
rect_jugador = imagen_jugador.get_rect(center=(400, 300))
rect_jugador2 = imagen_jugador2.get_rect(center=(400, 300))
imagen_obstaculos_abajo = pygame.image.load("assets/troncoabajo.png").convert_alpha()
imagen_obstaculos_arriba = pygame.image.load("assets/troncoarriba.png").convert_alpha()
lista_obstaculos = []
coins = []
menu = True
tienda = False
CREAROBSTACULO = pygame.USEREVENT
CREARMONEDA = pygame.USEREVENT
pygame.time.set_timer(CREARMONEDA, 0)
pygame.time.set_timer(CREAROBSTACULO, 1500)
opciones_altura_obstaculos = [500, 400, 300, 200]
opciones_espacio_obstaculos = [150, 160]
estado = False
ALPHA = 70
NEGRE_TRANSPARENT = (0, 0, 0, ALPHA)
seccio_transparent = pygame.Surface((800, 600), pygame.SRCALPHA)
pos_empezar = empezar_rect
pos_salir = salir_rect
pos_tienda = tienda_rect
pos_reiniciar = reiniciar_rect
pos_atras = atras_rect
pos_exit = exit_rect
pos_pausa = pausa_rect
pos_play = play_rect
pos_comprar = comprar_rect
pos_seleccionar = seleccionar_rect
reinicio = "save_data/reinicio.txt"
with open(reinicio, "r") as f:
    reiniciar = json.load(f)
pos_reiniciar_puntuacion = reiniciar_puntuaciones_rect
eleccion = 0
archivo_monedas_path = "save_data/monedas_totales.txt"
archivo_mejor_puntuacion_path = "save_data/mejor_puntuacion.txt"
event = pygame.event.wait()
pygame.draw.rect(seccio_transparent, NEGRE_TRANSPARENT, (0, 0, 800, 600))
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            with open("save_data/monedas_totales.txt", "w") as archivo_monedas:
                json.dump(monedas_totales, archivo_monedas)
            with open("save_data/mejor_puntuacion.txt", "w") as archivo_mejor_puntuacion:
                json.dump(mejor_puntuacion, archivo_mejor_puntuacion)
            time.sleep(1)
            pygame.quit()
            sys.exit()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE and vivo == 1:
                movimiento_jugador = 0
                monedas_totales = monedas
                movimiento_jugador -= 6
            if event.key == pygame.K_ESCAPE and tienda:
                tienda = False
                menu = True
            if event.key == pygame.K_SPACE and vivo == 2:
                if not menu:
                    numero += 1
                    vivo = 1
                    movimiento_jugador = 0
                    puntuacion = 0
                    lista_obstaculos.clear()
                    rect_jugador.center = (300, 200)
                    monedas = 0
                    coins.clear()
            if event.key == pygame.K_SPACE and vivo == 2 and menu:
                movimiento_jugador = 0
            if event.key == pygame.K_ESCAPE and vivo == 1:
                if not estado:
                    estado = True
            if event.key == pygame.K_LEFT and tienda:
                if eleccion > 0:
                    eleccion -= 1
                    if eleccion == 0:
                        imagen_jugador2 = imagen_jugador3

                    if eleccion == 1:
                        imagen_jugador2 = imagen_moneda
            if event.key == pygame.K_RIGHT and tienda:
                if eleccion < 1:
                    eleccion += 1
                    if eleccion == 0:
                        imagen_jugador2 = imagen_jugador3
                    if eleccion == 1:
                        imagen_jugador2 = imagen_moneda
        if event.type == pygame.MOUSEBUTTONDOWN and vivo == 1:
            if pygame.mouse.get_pressed()[0]:
                movimiento_jugador = 0
                movimiento_jugador -= 6
        if event.type == CREAROBSTACULO:
            a, b, c = crear_obstaculo()
            prueba2 = a, b
            lista_obstaculos.extend(prueba2)
            coins.extend(crear_moneda(c, coins))
        if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
            if pos_seleccionar.collidepoint(event.pos) and tienda:
                imagen_jugador = imagen_jugador2
            if pos_comprar.collidepoint(event.pos) and tienda:
                if monedas_totales >= 5 and eleccion == 1:
                    monedas_totales -= 5
                    imagen_jugador = imagen_moneda
            if pos_empezar.collidepoint(event.pos) and menu:
                menu = False
                vivo = 1
            if pos_salir.collidepoint(event.pos) and menu:
                with open("save_data/monedas_totales.txt", "w") as archivo_monedas:
                    json.dump(monedas_totales, archivo_monedas)
                with open("save_data/mejor_puntuacion.txt", "w") as archivo_mejor_puntuacion:
                    json.dump(mejor_puntuacion, archivo_mejor_puntuacion)
                time.sleep(1)
                pygame.quit()
                sys.exit()
            if pos_tienda.collidepoint(event.pos) and menu:
                tienda = True
                menu = False
                vivo = 4
            if pos_reiniciar_puntuacion.collidepoint(event.pos) and menu:
                print("Asdas")
                monedas_totales = 0
                mejor_puntuacion = 0
                with open("save_data/monedas_totales.txt", "w") as archivo_monedas:
                    json.dump(monedas_totales, archivo_monedas)
                with open("save_data/mejor_puntuacion.txt", "w") as archivo_mejor_puntuacion:
                    json.dump(mejor_puntuacion, archivo_mejor_puntuacion)
            if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                if pos_reiniciar.collidepoint(event.pos) and vivo == 2:
                    estado = False
                    numero += 1
                    movimiento_jugador = 0
                    puntuacion = 0
                    lista_obstaculos.clear()
                    rect_jugador.center = (300, 200)
                    monedas = 0
                    coins.clear()
                    vivo = 1
                    pygame.display.flip()
                if pos_pausa.collidepoint(event.pos) and vivo == 1:
                    estado = True
                    pygame.time.set_timer(CREAROBSTACULO, 1500)
                if pos_atras.collidepoint(event.pos) and vivo == 2:
                    estado = False
                    puntuacion = 0
                    pygame.time.set_timer(CREAROBSTACULO, 1500)
                    vivo = 2
                    lista_obstaculos.clear()
                    coins.clear()
                    monedas = 0
                    menu = True
                    rect_jugador = imagen_jugador.get_rect(center=(400, 300))
                    pygame.display.flip()
                if pos_exit.collidepoint(event.pos) and vivo == 2:
                    with open("save_data/monedas_totales.txt", "w") as archivo_monedas:
                        json.dump(monedas_totales, archivo_monedas)
                    with open("save_data/mejor_puntuacion.txt", "w") as archivo_mejor_puntuacion:
                        json.dump(mejor_puntuacion, archivo_mejor_puntuacion)
                    time.sleep(1)
                    pygame.quit()
                    sys.exit()

    pantalla.blit(FONDOJUEGO, (0, 0))
    if tienda:
        pantalla.blit(FONDOJUEGO, (0, 0))
        jugador_girado2 = girar_jugador(imagen_jugador2)
        pantalla.blit(jugador_girado2, rect_jugador2)
        pantalla.blit(comprar_img, comprar_rect)
        pantalla.blit(seleccionar_img, seleccionar_rect)
        pygame.display.flip()
    if menu:
        lista_obstaculos.clear()
        coins.clear()
        movimiento_jugador = 0
        rect_jugador.centery += movimiento_jugador
        jugador_girado = girar_jugador(imagen_jugador)
        pantalla.blit(jugador_girado, rect_jugador)
        suelo_pos_x -= 5
        dibujar_suelo(suelo_pos_x)
        pantalla.blit(empezar_img, empezar_rect)
        pantalla.blit(salir_img, salir_rect)
        pantalla.blit(tienda_img, tienda_rect)
        pantalla.blit(reiniciar_puntuaciones_img,reiniciar_puntuaciones_rect)
        pygame.display.flip()
        clock.tick(60)
        if suelo_pos_x <= -800:
            suelo_pos_x = 0
    if vivo == 1:
        pantalla.blit(pausa_img, pausa_rect)
        movimiento_jugador += caida
        rect_jugador.centery += movimiento_jugador
        jugador_girado = girar_jugador(imagen_jugador)
        pantalla.blit(jugador_girado, rect_jugador)
        vivo = colisiones_tubos(lista_obstaculos)
        lista_obstaculos = mover_obstaculos(lista_obstaculos)
        dibujar_obstaculos(lista_obstaculos)
        coins = mover_moneda(coins)
        dibujar_moneda(coins)
        recogida = recoger_monedas(coins)
        q, w = recogida
        monedas += q
        recogida = 0
        if w:
            print(monedas_totales)
            monedas_totales += 1
            puntuacion += 1
        puntuacion_actualizada("on", rect_jugador,)
        suelo_pos_x -= 5
        dibujar_suelo(suelo_pos_x)
        vivo = colisiones_tubos(lista_obstaculos)
        if puntuacion > mejor_puntuacion:
            mejor_puntuacion = puntuacion
        if suelo_pos_x <= -800:
            suelo_pos_x = 0
        if estado:
            if suelo_pos_x <= -800:
                suelo_pos_x = 0
            dibujar_suelo(suelo_pos_x)
            lista_obstaculos = mover_obstaculos(lista_obstaculos)
            dibujar_obstaculos(lista_obstaculos)
            coins = mover_moneda(coins)
            dibujar_moneda(coins)
            menu_pausa(lista_obstaculos, coins)
            pantalla.blit(reiniciar_img, reiniciar_rect)
            pantalla.blit(atras_img, atras_rect)
            pantalla.blit(play_img, play_rect)
            pantalla.blit(exit_img, exit_rect)
            while estado:
                pygame.display.flip()
                for event in pygame.event.get():
                    if event.type == pygame.QUIT:
                        pygame.quit()
                    if event.type == pygame.KEYDOWN:
                        if event.key == pygame.K_ESCAPE and estado:
                            pygame.time.set_timer(CREAROBSTACULO, 1500)
                            estado = False
                    if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                        if pos_reiniciar.collidepoint(event.pos) and estado:
                            estado = False
                            numero += 1
                            movimiento_jugador = 0
                            puntuacion = 0
                            lista_obstaculos.clear()
                            rect_jugador.center = (300, 200)
                            monedas = 0
                            coins.clear()
                            vivo = 1
                            pygame.display.flip()
                        if pos_atras.collidepoint(event.pos) and estado:
                            estado = False
                            pygame.time.set_timer(CREAROBSTACULO, 1500)
                            puntuacion = 0
                            vivo = 2
                            lista_obstaculos.clear()
                            coins.clear()
                            monedas = 0
                            menu = True
                            rect_jugador = imagen_jugador.get_rect(center=(400, 300))
                            pygame.display.flip()
                        if pos_play.collidepoint(event.pos) and estado:
                            pygame.time.set_timer(CREAROBSTACULO, 1500)
                            estado = False
                            movimiento_jugador = 0
                        if pos_exit.collidepoint(event.pos) and estado:
                            with open("save_data/monedas_totales.txt", "w") as archivo_monedas:
                                json.dump(monedas_totales, archivo_monedas)
                            with open("save_data/mejor_puntuacion.txt", "w") as archivo_mejor_puntuacion:
                                json.dump(mejor_puntuacion, archivo_mejor_puntuacion)
                            time.sleep(1)
                            pygame.quit()
                            sys.exit()

        pygame.display.update()
        clock.tick(60)
