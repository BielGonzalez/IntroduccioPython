import sys
import time
from pygame.locals import *
import pygame
import random
def dibujar_suelo():
    pantalla.blit(suelo_imagen,(suelo_pos_x,500))
    pantalla.blit(suelo_imagen, (suelo_pos_x + 800,500))
pygame.init()
pantalla = pygame.display.set_mode((800,600))
clock = pygame.time.Clock()

caida = 0.25
movimiento_jugador = 0


suelo_imagen = pygame.image.load("assets/pruebasuelo.png").convert()
FONDOJUEGO = pygame.image.load("assets/fondo1.png").convert()
suelo_pos_x = 0
imagen_jugador = pygame.image.load("assets/tortuga.png").convert_alpha()
rect_jugador = imagen_jugador.get_rect(center = (400,300))
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                movimiento_jugador -= 10

    pantalla.blit(FONDOJUEGO,(0,0))

    movimiento_jugador += caida
    rect_jugador.centery += movimiento_jugador

    pantalla.blit(imagen_jugador,rect_jugador)
    suelo_pos_x -= 2
    dibujar_suelo()
    pygame.display.update()
    clock.tick(60)
