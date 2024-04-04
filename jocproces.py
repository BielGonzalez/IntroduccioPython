import time
from pygame.locals import *
import pygame

WHITE = (255,255,255)
AMPLADA = 320
ALTURA = 200
BACKGROUND_IMAGE = '/home/alumne/PycharmProjects/pythonProject/.venv/assets/fondojuego.png'
player_image = pygame.image.load('/home/alumne/PycharmProjects/pythonProject/.venv/assets/nau.png')
player_image2 = pygame.image.load('/home/alumne/PycharmProjects/pythonProject/.venv/assets/nau2.png')
player_rect = player_image.get_rect(midbottom=(AMPLADA // 2, ALTURA - 10))
player_rect2 = player_image2.get_rect(midbottom=(AMPLADA // 2, ALTURA - 160))
velocitat_nau = 2
MUSICA_FONS = 'musicmenu.mp3'


# Bala rectangular blanca:
bala_imatge = pygame.Surface((4,10)) #definim una superficie rectangle de 4 pixels d'ample i 10 d'alçada
bala_imatge.fill(WHITE) #pintem la superficie de color blanc
bales_jugador1 = [] #llista on guardem les bales del jugador 1
bales_jugador2 = [] #llista on guardem les bales del jugador 2
velocitat_bales = 3
temps_entre_bales = 1000 #1 segon
temps_ultima_bala_jugador1 = 0 #per contar el temps que ha passat des de que ha disparat el jugador 1
temps_ultima_bala_jugador2 = 0 #per contar el temps que ha passat des de que ha disparat el jugador 2

pygame.init()
pantalla = pygame.display.set_mode((AMPLADA, ALTURA))
pygame.display.set_caption("Arcade")

# Control de FPS
clock = pygame.time.Clock()
fps = 60

def imprimir_pantalla_fons(image):
    # Imprimeixo imatge de fons:
    background = pygame.image.load(image).convert()
    pantalla.blit(background, (0, 0))


while True:
    current_time = pygame.time.get_ticks()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
        # controlar trets de les naus
        if event.type == KEYDOWN:
            # jugador 1
            if event.key == K_w and current_time - temps_ultima_bala_jugador1 >= temps_entre_bales:
                bales_jugador1.append(pygame.Rect(player_rect.centerx - 2, player_rect.top, 4, 10))
                temps_ultima_bala_jugador1 = current_time
            # jugador 2
            if event.key == K_UP and current_time - temps_ultima_bala_jugador2 >= temps_entre_bales:
                bales_jugador2.append(pygame.Rect(player_rect2.centerx - 2, player_rect2.bottom - 10, 4, 10))
                temps_ultima_bala_jugador2 = current_time

    # Moviment del jugador
    keys = pygame.key.get_pressed()
    if keys[K_a]:
        player_rect.x -= velocitat_nau
    if keys[K_d]:
        player_rect.x += velocitat_nau
    if keys[K_LEFT]:
        player_rect2.x -= velocitat_nau
    if keys[K_RIGHT]:
        player_rect2.x += velocitat_nau
    # Mantenir al jugador dins de la pantalla
    player_rect.clamp_ip(pantalla.get_rect())
    player_rect2.clamp_ip(pantalla.get_rect())
    imprimir_pantalla_fons(BACKGROUND_IMAGE)

    for bala in bales_jugador1:  # bucle que recorre totes les bales
        bala.y -= velocitat_bales  # mou la bala
        if bala.bottom < 0 or bala.top > ALTURA:  # comprova que no ha sortit de la pantalla
            bales_jugador1.remove(bala)  # si ha sortit elimina la bala
        else:
            pantalla.blit(bala_imatge, bala)  # si no ha sortit la dibuixa
        # Detectar col·lisions jugador 2:
        if player_rect2.colliderect(bala):  # si una bala toca al jugador1 (el seu rectangle)
            print("BOOM 1!")
            bales_jugador1.remove(bala)  # eliminem la bala
            # mostrem una explosió
            # eliminem el jugador 1 (un temps)
            # anotem punts al jugador 1
    for bala in bales_jugador2:
        bala.y += velocitat_bales
        if bala.bottom < 0 or bala.top > ALTURA:
            bales_jugador2.remove(bala)
        else:
            pantalla.blit(bala_imatge, bala)
        # Detectar col·lisions jugador 1:
        if player_rect.colliderect(bala):  # si una bala toca al jugador1 (el seu rectangle)
            print("BOOM 2!")
            bales_jugador2.remove(bala)  # eliminem la bala
            # mostrem una explosió
            # eliminem el jugador 1 (un temps)
            # anotem punts al jugador 1

    pantalla.blit(player_image, player_rect)
    pantalla.blit(player_image2, player_rect2)
    pygame.display.update()
    clock.tick(fps)
