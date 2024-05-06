import sys
import time
from pygame.locals import *
import pygame
import random
def dibujar_suelo(suelo_pos_x):
    pantalla.blit(suelo_imagen,(suelo_pos_x,550))
    pantalla.blit(suelo_imagen, (suelo_pos_x + 800,550))
def crear_obstaculo():
    posicion_obstaculo = random.choice(opciones_altura_obstaculos)
    pos_prueba = posicion_obstaculo
    espacio_obstaculos = random.choice(opciones_espacio_obstaculos)
    obstaculo_abajo = imagen_obstaculos_abajo.get_rect(midtop = (1000,posicion_obstaculo))
    obstaculo_arriba = imagen_obstaculos_arriba.get_rect(midbottom =(1000, posicion_obstaculo - espacio_obstaculos))
    return obstaculo_abajo, obstaculo_arriba, pos_prueba
def mover_obstaculos(obstaculos):
    for obstaculo in obstaculos:
        obstaculo.centerx -= 5
    return obstaculos
def dibujar_obstaculos(obstaculos):
    for obstaculo in obstaculos:
        if obstaculo.bottom >= 600:
            pantalla.blit(imagen_obstaculos_abajo,obstaculo)
        else:
            pantalla.blit(imagen_obstaculos_arriba,obstaculo)
def colisiones_tubos(obstaculos):
    vivo = True
    for obstaculo in obstaculos:
        if rect_jugador.colliderect(obstaculo):
            vivo = 2
            puntuacion_actualizada('off',rect_jugador,vivo)
    if rect_jugador.bottom >= 550:
        puntuacion_actualizada('off',rect_jugador,vivo)
        vivo = 2
    if rect_jugador.top <= - 10:
        puntuacion_actualizada('off',rect_jugador,vivo)
        vivo = 2
    return vivo
def decidir_altura_monedas(posicion_obstaculo, coins):
    global posicion_moneda
    posicion_moneda = 0
    if posicion_obstaculo == 500:
        for posicion_moneda in coins:
            posicion_moneda = 600
    elif posicion_obstaculo == 400:
        for posicion_moneda in coins:
            posicion_moneda = 500
    elif posicion_obstaculo == 500:
        for posicion_moneda in coins:
            posicion_moneda = 400
    elif posicion_obstaculo == 400:
        for posicion_moneda in coins:
            posicion_moneda = 300
    return posicion_moneda
def crear_moneda(obstaculo_abajo,coins):
    decidir_altura_monedas(obstaculo_abajo,coins)
    coin1 = imagen_moneda.get_rect(center = (1000,obstaculo_abajo-75))
    coin2 = imagen_moneda.get_rect(center =(1000,obstaculo_abajo-7555))
    return coin1,coin2
def mover_moneda(coins_f):
    for coin_f in coins_f:
        coin_f.x -= 5
    return coins_f
def dibujar_moneda(coins_f):
    for coin_f in coins_f:
        coin1 = coin_f
        if vivo == 1:
            pantalla.blit(imagen_moneda,(coin1.x ,coin1.y))
def recoger_monedas(coins):
    recogida = 0
    w = False
    for coin in coins:
        if rect_jugador.colliderect(coin):
            recogida += 1
            w = True
            coins.remove(coin)
    return recogida, w
def girar_jugador(jugador):
    nuevo_jugador = pygame.transform.rotozoom(jugador,-movimiento_jugador*3 , 1)
    return nuevo_jugador
def puntuacion_actualizada(estado_juego,rect_jugador,vivo,):
    if estado_juego == "on":
        puntuacion_surface = fuente_juego.render(str(int(puntuacion)),True,(255,255,255))
        puntuacion_rect = puntuacion_surface.get_rect(center = (400,100))
        pantalla.blit(puntuacion_surface,puntuacion_rect)
    if estado_juego == "off":
        puntuacion_surface = fuente_juego.render(str(int(puntuacion)), True, (255, 255, 255))
        puntuacion_rect = puntuacion_surface.get_rect(center=(468.5,300))
        game_over = fuente_juego.render("GAME OVER", True, (55, 148, 110))
        puntuacion_texto = fuente_juego_peque.render("PUNTUACION", True, (74, 200, 10))
        monedas_texto = fuente_juego_peque.render("MONEDAS", True, (74, 200, 10))
        monedas_texto_rect = monedas_texto.get_rect(center = (330, 250))
        monedas_c = fuente_juego.render(str(int(monedas_totales)), True, (255, 255, 255))
        monedas_c_rect = monedas_c.get_rect(center=(330, 380))
        monedas_texto2 = fuente_juego_peque.render("CONSEGUIDAS", True, (74, 200, 10))
        monedas_texto_rect2 = monedas_texto.get_rect(center = (315, 270))
        monedas_texto3 = fuente_juego_peque.render("MONEDAS", True, (74, 200, 10))
        monedas_texto_rect3 = monedas_texto3.get_rect(center = (330, 330))
        monedas_texto4 = fuente_juego_peque.render("TOTALES", True, (74, 200, 10))
        monedas_texto_rect4 = monedas_texto4.get_rect(center = (330, 350))
        monedas_conseguidas_texto = fuente_juego.render(str(int(monedas)), True, (255,255,255))
        monedas_conseguidas_texto_rect = monedas_conseguidas_texto.get_rect(center = (330, 300))
        mejor_puntuacion_texto = fuente_juego_peque.render("RECORD",True,(74, 200, 10))
        mejor_puntuacion_texto_rect = mejor_puntuacion_texto.get_rect(center = (468.5,340))
        game_over_rect = game_over.get_rect(center=(400, 150))
        puntuacion_texto_rect = puntuacion_texto.get_rect(center=(470, 260))
        mejor_puntuacion_surface = fuente_juego.render(str(int(mejor_puntuacion)),True,(255,255,255))
        mejor_puntuacion_rect = mejor_puntuacion_surface.get_rect(center = (468.5,380))
        pantalla.blit(FONDOJUEGO,(0,0))
        pantalla.blit(jugador_girado,rect_jugador)
        pantalla.blit(pruebagameover, (230, 200))
        pantalla.blit(suelo_imagen,(suelo_pos_x,550))
        pantalla.blit(suelo_imagen,(320-suelo_pos_x,550))
        pantalla.blit(game_over, game_over_rect)
        pantalla.blit(mejor_puntuacion_surface,mejor_puntuacion_rect)
        pantalla.blit(mejor_puntuacion_texto,mejor_puntuacion_texto_rect)
        pantalla.blit(monedas_texto,monedas_texto_rect)
        pantalla.blit(monedas_texto2,monedas_texto_rect2)
        pantalla.blit(monedas_conseguidas_texto,monedas_conseguidas_texto_rect)
        pantalla.blit(monedas_c,monedas_c_rect)
        pantalla.blit(monedas_texto3,monedas_texto_rect3)
        pantalla.blit(monedas_texto4,monedas_texto_rect4)
        pantalla.blit(puntuacion_surface, puntuacion_rect)
        pantalla.blit(puntuacion_texto, puntuacion_texto_rect)
        pantalla.blit(play_img, play_rect)
        menu_pausa(lista_obstaculos, coins)
        pantalla.blit(reiniciar_img, reiniciar_rect)
        pantalla.blit(atras_img, atras_rect)
        pantalla.blit(exit_img, exit_rect)
        pantalla.blit(play_img, play_rect)
        return vivo
def actualizar_mejor_puntuacion(puntuacion,mejor_puntuacion):
        if puntuacion > mejor_puntuacion:
            mejor_puntuacion = puntuacion
        return mejor_puntuacion
def menu_pausa(lista_obstaculos,coins):
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
    lista_obstaculos = mover_obstaculos(lista_obstaculos)
    dibujar_obstaculos(lista_obstaculos)
    coins = mover_moneda(coins)
    dibujar_moneda(coins)
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
pantalla = pygame.display.set_mode((800,600))
clock = pygame.time.Clock()
fuente_juego = pygame.font.Font('04B_19.TTF',35)
fuente_juego_peque = pygame.font.Font('04B_19.TTF',20)
caida = 0.20
numero = 0
recogida = False
imagen_moneda = pygame.image.load("assets/moneda.png")
monedas = 0
monedas_totales = 0
GAMEOVER ="GAME OVER"
movimiento_jugador = 0
vivo = 2
posicion_moneda = 0
posicion_obstaculo = 0
puntuacion = 0
mejor_puntuacion = 0
pruebagameover = pygame.image.load("assets/pruebagameover.png")
suelo_imagen = pygame.image.load("assets/prueba.png").convert()
suelo_rect = suelo_imagen.get_rect(center = (800,0))
FONDOJUEGO = pygame.image.load("assets/fondo1.png").convert()
suelo_pos_x = 0

tienda_img = pygame.image.load("assets/empezar.png").convert()
tienda_rect = tienda_img.get_rect(center=(600,400))
empezar_img = pygame.image.load("assets/empezar.png").convert()
empezar_rect = empezar_img.get_rect(center=(200,400))
salir_img = pygame.image.load("assets/salir.png").convert()
salir_rect = salir_img.get_rect(center=(400,400))
empezar_rect2 = empezar_img.get_rect(center=(20000,40000))
salir_rect2 = salir_img.get_rect(center=(40000,40000))
pausa_img = pygame.image.load("assets/pausa.png").convert()
pausa_rect = pausa_img.get_rect(center=(50,50))
reiniciar_img = pygame.image.load("assets/reiniciar.png").convert()
reiniciar_rect = reiniciar_img.get_rect(center=(325,500))
atras_img = pygame.image.load("assets/atras.png").convert()
atras_rect = atras_img.get_rect(center=(400,500))
exit_img = pygame.image.load("assets/exit.png").convert()
exit_rect = exit_img.get_rect(center=(475,500))
play_img = pygame.image.load("assets/play.png").convert()
play_rect = play_img.get_rect(center=(50,50))
imagen_jugador2 = pygame.image.load("assets/tortuga.png").convert_alpha()
imagen_jugador = pygame.image.load("assets/tortuga.png").convert_alpha()
rect_jugador = imagen_jugador.get_rect(center = (400,300))
imagen_obstaculos_abajo = pygame.image.load("assets/troncoabajo.png").convert_alpha()
imagen_obstaculos_arriba = pygame.image.load("assets/troncoarriba.png").convert_alpha()
lista_obstaculos = []
coins = []
menu = True
tienda = False
CREAROBSTACULO = pygame.USEREVENT
CREARMONEDA = pygame.USEREVENT
pygame.time.set_timer(CREARMONEDA,0)
pygame.time.set_timer(CREAROBSTACULO,1500)
opciones_altura_obstaculos = [500,400,300,200]
opciones_espacio_obstaculos = [150,160]
estado = False
ALPHA = 70
NEGRE_TRANSPARENT = (0,0,0,ALPHA)
seccio_transparent = pygame.Surface((800,600),pygame.SRCALPHA)
pos_reiniciar = reiniciar_rect
pos_atras = atras_rect
pos_exit = exit_rect
pos_play = play_rect
eleccion = 0
event = pygame.event.wait()
pygame.draw.rect(seccio_transparent,NEGRE_TRANSPARENT,(0,0,800,600))
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE and vivo == 1:
                movimiento_jugador = 0
                monedas_totales = monedas
                movimiento_jugador -= 6
            if event.key == pygame.K_SPACE and vivo == 2 and menu == False:
                numero += 1
                vivo = 1
                movimiento_jugador = 0
                puntuacion = 0
                lista_obstaculos.clear()
                rect_jugador.center = (300,200)
                monedas = 0
                coins.clear()
            if event.key == pygame.K_SPACE and vivo == 2 and menu == True:
                movimiento_jugador = 0
            if event.key == pygame.K_ESCAPE and vivo == 1 and estado == False:
                estado = True
            if event.key == pygame.K_LEFT:
                if eleccion < 0:
                    eleccion -= 1
                if eleccion == 0:
                    imagen_jugador = imagen_jugador2
                if eleccion == 1:
                    imagen_jugador = imagen_moneda
            if event.key == pygame.K_RIGHT:
                if eleccion > 1:
                    eleccion += 1
                if eleccion == 0:
                    imagen_jugador = imagen_jugador2
                if eleccion == 1:
                    imagen_jugador = imagen_moneda
                pygame.display.flip()
        if event.type == pygame.MOUSEBUTTONDOWN and vivo == 1:
            if (pygame.mouse.get_pressed()[0]):
                movimiento_jugador = 0
                movimiento_jugador -= 6
        if event.type == CREAROBSTACULO:
            a, b, c = crear_obstaculo()
            prueba2 = a,b
            lista_obstaculos.extend(prueba2)
            coins.extend(crear_moneda(c, coins))
        if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
            if pos_empezar.collidepoint(event.pos):
                menu = False
                vivo = 1
            if pos_salir.collidepoint(event.pos):
                pygame.quit()
                sys.exit()
            if pos_tienda.collidepoint(event.pos) and menu:
                tienda = True
                menu = False
                vivo = 4
            if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                pos_salir = salir_rect
                pos_empezar = empezar_rect
                if pos_reiniciar.collidepoint(event.pos) and vivo == 2 :
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
                    pygame.quit()
                    sys.exit()

    pantalla.blit(FONDOJUEGO,(0,0))
    if tienda:
        keys = pygame.key.get_pressed()
        pantalla.blit(FONDOJUEGO,(0,0))
        jugador_girado = girar_jugador(imagen_jugador)
        pantalla.blit(jugador_girado, rect_jugador)
        for event in pygame.event.get():
            if event.type == KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    tienda =False
                    menu = True
        pygame.display.flip()
    if menu:
        lista_obstaculos.clear()
        coins.clear()
        pos_empezar = empezar_rect
        pos_salir = salir_rect
        pos_pausa = pausa_rect
        pos_tienda = tienda_rect
        movimiento_jugador = 0
        rect_jugador.centery += movimiento_jugador
        jugador_girado = girar_jugador(imagen_jugador)
        pantalla.blit(jugador_girado,rect_jugador)
        suelo_pos_x -= 5
        dibujar_suelo(suelo_pos_x)
        pantalla.blit(empezar_img,empezar_rect)
        pantalla.blit(salir_img,salir_rect)
        pantalla.blit(tienda_img,tienda_rect)

        pygame.display.flip()
        clock.tick(60)
        if suelo_pos_x <= -800:
            suelo_pos_x = 0
    if vivo == 1:
        pos_salir = salir_rect2
        pos_empezar = empezar_rect2
        pantalla.blit(pausa_img, pausa_rect)
        movimiento_jugador += caida
        rect_jugador.centery += movimiento_jugador
        jugador_girado = girar_jugador(imagen_jugador)
        pantalla.blit(jugador_girado,rect_jugador)
        vivo = colisiones_tubos(lista_obstaculos)
        lista_obstaculos = mover_obstaculos(lista_obstaculos)
        dibujar_obstaculos(lista_obstaculos)
        coins = mover_moneda(coins)
        dibujar_moneda(coins)
        recogida = recoger_monedas(coins)
        q,w = recogida
        monedas += q
        recogida = 0
        if w:
            monedas_totales += 1
            puntuacion += 1
        puntuacion_actualizada("on",rect_jugador,vivo)
        suelo_pos_x -= 5
        dibujar_suelo(suelo_pos_x)
        vivo = colisiones_tubos(lista_obstaculos)

        if puntuacion > mejor_puntuacion:
            mejor_puntuacion = puntuacion
        if suelo_pos_x <= -800:
            suelo_pos_x = 0
        if estado == True:
            if suelo_pos_x <= -800:
                suelo_pos_x = 0
            dibujar_suelo(suelo_pos_x)
            lista_obstaculos = mover_obstaculos(lista_obstaculos)
            dibujar_obstaculos(lista_obstaculos)
            coins = mover_moneda(coins)
            dibujar_moneda(coins)
            menu_pausa(lista_obstaculos,coins)
            pantalla.blit(reiniciar_img, reiniciar_rect)
            pantalla.blit(atras_img, atras_rect)
            pantalla.blit(play_img, play_rect)
            pantalla.blit(exit_img, exit_rect)
            while estado == True:
                pos_reiniciar = reiniciar_rect
                pos_atras = atras_rect
                pos_exit = exit_rect
                pos_pausa = pausa_rect
                pos_play = play_rect
                pygame.display.flip()
                for event in pygame.event.get():
                    if event.type == pygame.QUIT:
                        pygame.quit()
                    if event.type == pygame.KEYDOWN:
                        if event.key == pygame.K_ESCAPE:
                            pygame.time.set_timer(CREAROBSTACULO, 1500)
                            estado = False
                    if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                        if pos_reiniciar.collidepoint(event.pos) and estado == True:
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
                        if pos_atras.collidepoint(event.pos) and estado == True:
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
                        if pos_play.collidepoint(event.pos) and estado == True:
                            pygame.time.set_timer(CREAROBSTACULO, 1500)
                            estado = False
                            movimiento_jugador = 0
                        if pos_exit.collidepoint(event.pos) and estado == True:
                            pygame.quit()
                            sys.exit()

        pygame.display.update()
        clock.tick(60)
