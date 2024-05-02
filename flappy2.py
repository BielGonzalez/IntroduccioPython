import sys
import time
from pygame.locals import *
import pygame
import random
def dibujar_suelo():
    pantalla.blit(suelo_imagen,(suelo_pos_x,550))
    pantalla.blit(suelo_imagen, (suelo_pos_x + 800,550))


def crear_obstaculo():
    posicion_obstaculo = random.choice(opciones_altura_obstaculos)
    espacio_obstaculos = random.choice(opciones_espacio_obstaculos)
    obstaculo_abajo = imagen_obstaculos_abajo.get_rect(midtop = (1000,posicion_obstaculo))
    obstaculo_arriba = imagen_obstaculos_arriba.get_rect(midbottom =(1000, posicion_obstaculo - espacio_obstaculos))
    return obstaculo_abajo, obstaculo_arriba, posicion_obstaculo
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
            vivo = False
            puntuacion_actualizada('off')
    if rect_jugador.bottom >= 550:
        puntuacion_actualizada('off')
        vivo = False
    if rect_jugador.top <= - 10:
        puntuacion_actualizada('off')
        vivo = False
    return vivo
def decidir_altura_mondeas(posicion_obstaculo):
    global posicion_moneda
    posicion_moneda = 0
    if posicion_obstaculo == 500:
        posicion_moneda = 600
    elif posicion_obstaculo == 400:
        posicion_moneda = 500
    elif posicion_obstaculo == 300:
        posicion_moneda = 400
    elif posicion_obstaculo == 200:
        posicion_moneda = 300
    return posicion_moneda
def crear_moneda():
    decidir_altura_mondeas(posicion_obstaculo)
    coin1 = imagen_moneda.get_rect(center = (1000,posicion_moneda))
    coin2 = imagen_moneda.get_rect(center =(1000, posicion_moneda))
    return coin1,coin2
def mover_moneda(coins_f):
    for coin_f in coins_f:
        coin_f.x -= 5
    return coins_f
def dibujar_moneda(coins_f):
    for coin_f in coins_f:
        coin1 = coin_f
        if vivo:
            pantalla.blit(imagen_moneda,(coin1.x ,coin1.y))
def girar_jugador(jugador):
    nuevo_jugador = pygame.transform.rotozoom(jugador,-movimiento_jugador*3 , 1)
    return nuevo_jugador
def puntuacion_actualizada(estado_juego):
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

def actualizar_mejor_puntuacion(puntuacion,mejor_puntuacion):
        if puntuacion > mejor_puntuacion:
            mejor_puntuacion = puntuacion
        return mejor_puntuacion
pygame.init()
pantalla = pygame.display.set_mode((800,600))
clock = pygame.time.Clock()
fuente_juego = pygame.font.Font('04B_19.TTF',35)
fuente_juego_peque = pygame.font.Font('04B_19.TTF',20)
caida = 0.20
numero = 0
imagen_moneda = pygame.image.load("assets/moneda.png")
monedas = 0
monedas_totales = 0
GAMEOVER ="GAME OVER"
movimiento_jugador = 0
vivo = True
posicion_obstaculo = 0
puntuacion = 0
mejor_puntuacion = 0
pruebagameover = pygame.image.load("assets/pruebagameover.png")
suelo_imagen = pygame.image.load("assets/prueba.png").convert()
suelo_rect = suelo_imagen.get_rect(center = (800,0))
FONDOJUEGO = pygame.image.load("assets/fondo1.png").convert()
suelo_pos_x = 0
imagen_jugador = pygame.image.load("assets/tortuga.png").convert_alpha()
rect_jugador = imagen_jugador.get_rect(center = (400,300))
imagen_obstaculos_abajo = pygame.image.load("assets/troncoabajo.png").convert_alpha()
imagen_obstaculos_arriba = pygame.image.load("assets/troncoarriba.png").convert_alpha()
lista_obstaculos = []
coins = []
CREAROBSTACULO = pygame.USEREVENT
CREARMONEDA = pygame.USEREVENT
pygame.time.set_timer(CREARMONEDA,1500)
pygame.time.set_timer(CREAROBSTACULO,1500)
opciones_altura_obstaculos = [500,400,300,200]
opciones_espacio_obstaculos = [150,200,175]
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE and vivo:
                movimiento_jugador = 0
                movimiento_jugador -= 6
            if event.key == pygame.K_SPACE and vivo == False:
                numero += 1
                vivo = True
                movimiento_jugador = 0
                puntuacion = 0
                lista_obstaculos.clear()
                rect_jugador.center = (300,200)
                monedas = 0

        if event.type == pygame.MOUSEBUTTONDOWN and vivo:
            if (pygame.mouse.get_pressed()[0]):
                movimiento_jugador = 0
                movimiento_jugador -= 6
        if event.type == CREARMONEDA:
            coins.extend(crear_moneda())
        if event.type == CREAROBSTACULO:
            lista_obstaculos.extend(crear_obstaculo())
    pantalla.blit(FONDOJUEGO,(0,0))

    if vivo:
        print(mejor_puntuacion)
        movimiento_jugador += caida
        rect_jugador.centery += movimiento_jugador

        jugador_girado = girar_jugador(imagen_jugador)
        pantalla.blit(jugador_girado,rect_jugador)
        vivo = colisiones_tubos(lista_obstaculos)
        lista_obstaculos = mover_obstaculos(lista_obstaculos)
        dibujar_obstaculos(lista_obstaculos)

        coins = mover_moneda(coins)
        dibujar_moneda(coins)
        puntuacion += 0.007
        monedas += 0.02
        monedas_totales += 0.02
        puntuacion_actualizada("on")
        suelo_pos_x -= 5
        dibujar_suelo()
        vivo = colisiones_tubos(lista_obstaculos)
        if puntuacion > mejor_puntuacion:
            mejor_puntuacion = puntuacion
        if suelo_pos_x <= -800:
            suelo_pos_x = 0
        pygame.display.update()
        clock.tick(60)
