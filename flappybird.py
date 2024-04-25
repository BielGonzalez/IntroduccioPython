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
    return obstaculo_abajo, obstaculo_arriba
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
    for obstaculo in obstaculos:
        if rect_jugador.colliderect(obstaculo):
            print("funciona papa ")
        if rect_jugador.top <= 20 or rect_jugador.bottom >= 520:
            print("funciona mama")
def girar_jugador(jugador):
    nuevo_jugador = pygame.transform.rotozoom(jugador,-movimiento_jugador*3 , 1)
    return nuevo_jugador
def puntuacion_actualizada():
    puntuacion_surface = fuente_juego.render('Score',True,(255,255,255))
    puntuacion_rect = puntuacion_surface.get_rect(center = (400,100))
pygame.init()
pantalla = pygame.display.set_mode((800,600))
clock = pygame.time.Clock()
fuente_juego = pygame.font.Font(None,40)
caida = 0.20
movimiento_jugador = 0
puntuacion = 0
mejor_puntuacion = 0
suelo_imagen = pygame.image.load("assets/prueba.jpg").convert()
FONDOJUEGO = pygame.image.load("assets/fondo1.png").convert()
suelo_pos_x = 0
imagen_jugador = pygame.image.load("assets/tortuga.png").convert_alpha()
rect_jugador = imagen_jugador.get_rect(center = (400,300))
imagen_obstaculos_abajo = pygame.image.load("assets/troncoabajo.png").convert_alpha()
imagen_obstaculos_arriba = pygame.image.load("assets/troncoarriba.png").convert_alpha()
lista_obstaculos = []
CREAROBSTACULO = pygame.USEREVENT
pygame.time.set_timer(CREAROBSTACULO,1500)
opciones_altura_obstaculos = [500,400,300,200]
opciones_espacio_obstaculos = [150,200,175]
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                movimiento_jugador = 0
                movimiento_jugador -= 6
        if event.type == pygame.MOUSEBUTTONDOWN:
            if (pygame.mouse.get_pressed()[0]):
                movimiento_jugador = 0
                movimiento_jugador -= 6
        if event.type == CREAROBSTACULO:
            lista_obstaculos.extend(crear_obstaculo())
    pantalla.blit(FONDOJUEGO,(0,0))

    movimiento_jugador += caida
    rect_jugador.centery += movimiento_jugador

    jugador_girado = girar_jugador(imagen_jugador)
    pantalla.blit(jugador_girado,rect_jugador)
    lista_obstaculos = mover_obstaculos(lista_obstaculos)
    dibujar_obstaculos(lista_obstaculos)

    suelo_pos_x -= 5
    dibujar_suelo()
    colisiones_tubos(lista_obstaculos)
    if suelo_pos_x <= -800:
        suelo_pos_x = 0
    pygame.display.update()
    clock.tick(60)
