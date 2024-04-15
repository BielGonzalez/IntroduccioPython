import time
from pygame.locals import *
import pygame
import random
AMPLADA = 320
ALTURA = 200
BACKGROUND_IMAGE = 'assets/fondomenu.png'
fondo = "assets/fondo.png"
WHITE = (255, 255, 255)
encendido = True
partida = False
vidas1 = 3
vidas2 = 3
wins1 = 0
wins2 = 0
corazon = 'assets/corazon.png'
bateria = 'assets/bateria.png'
win1 = "assets/win1.png"
win2 = "assets/win2.png"
personalizar = False
energia_image = pygame.image.load(bateria)
bala_imatge_o = pygame.image.load('assets/bala.png')
bala_imatge = pygame.image.load('assets/bala.png')  # pintem la superficie de color blanc
bala_imatge2 = pygame.image.load('assets/bala.png')
balagrande_imatge = pygame.image.load('assets/balagrande.png')
bales_jugador1 = []  # llista on guardem les bales del jugador 1
bales_jugador2 = []  # llista on guardem les bales del jugador 2
velocitat_bales = 3
temps_entre_bales = 500
temps_invicibilitat = 2000
temps_ultima_bala_jugador1 = 0
temps_ultima_bala_jugador2 = 0
temps_ultim_golp_jugador1 = 0
temps_ultim_golp_jugador2 = 0
temps_poder_escut = 1000  # 1 segon
temps_poder_velocitat = 3000  # 3 segons
tiempo_pausa = 0
temps_partida = 200000  # 5min
nau3 = "assets/nau.png"
nau4 = "assets/nau3.png"
seleccion = 1

pygame.init()
pygame.mixer.init()
pygame.mixer.music.load("assets/musicmenu.mp3")
pygame.mixer.music.play(-1, 5, 3000)
pygame.mixer.music.set_volume(0.05)
pantalla = pygame.display.set_mode((AMPLADA, ALTURA))
pygame.display.set_caption("Black Star")
background = pygame.image.load(BACKGROUND_IMAGE).convert()

# Control de FPS
clock = pygame.time.Clock()
fps = 60


def imprimir_pantalla_fons(image,x,y):
    background = pygame.image.load(image).convert_alpha()
    pantalla.blit(background, (x, y))


def TextPantalla(pantalla, font, tamany, text, color, posicio):
    font = pygame.font.SysFont(font, tamany)
    img = font.render(text, True, color)
    pantalla.blit(img, posicio)


def creditos():
    animacion_fin = False
    creditos = True
    pygame.mixer.music.load("assets/creditosmusic.mp3")
    pygame.mixer.music.play()
    pygame.mixer.music.set_volume(0.05)
    while creditos == True:
        if animacion_fin == False:
            for i in range(0, 60):
                time.sleep(0.02)
                pantalla.fill((0, 0, 0))
                TextPantalla(pantalla, None, 20, "Programacion: Biel G., Xavi Sancho, Arno B.", (WHITE), (10, i))
                TextPantalla(pantalla, None, 20, "Graficos: Biel G.", (WHITE), (10, i + 20))
                TextPantalla(pantalla, None, 20, "Musica: Droppin' Boppers,freesound.org", (WHITE), (10, i + 40))
                TextPantalla(pantalla, None, 20, "Efectos de sonido: pixabay.com", (WHITE), (10, i + 60))
                pygame.display.update()
            TextPantalla(pantalla, None, 18, "Pulse espacio para salir", (WHITE), (40, 180))
            animacion_fin = True
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
            if event.type == KEYDOWN:
                if event.key == K_SPACE:
                    pygame.mixer.music.stop()
                    pygame.mixer.music.load("assets/musicmenu.mp3")
                    pygame.mixer.music.play(-1, 5, 3000)
                    pygame.mixer.music.set_volume(0.05)
                    creditos = False
                    imprimir_menu()
        pygame.display.update()



def imprimir_menu():
    # Se imprime el fondo
    pantalla.blit(background, (0, 0))
    # Creamos seccion transparente y se imprime
    seccio_transparent = pygame.Surface((320, 200), pygame.SRCALPHA)
    pygame.draw.rect(seccio_transparent, (0, 0, 0, 100), (0, 35, 140, 88))
    pantalla.blit(seccio_transparent, (90, 30))
    # imprimimos el texto
    TextPantalla(pantalla, None, 24, "1- Creditos", WHITE, (100, 70))
    TextPantalla(pantalla, None, 24, "2- Jugar", WHITE, (100, 90))
    TextPantalla(pantalla, None, 24, "3- Personalizar", WHITE, (100, 110))
    TextPantalla(pantalla, None, 24, "4- Salir", WHITE, (100, 130))
    TextPantalla(pantalla, None, 16, "Wins Jugador 2", WHITE, (237, 70))
    TextPantalla(pantalla, None, 16, "Wins Jugador 1", WHITE, (0, 70))
    TextPantalla(pantalla, None, 24, str(wins2), WHITE, (267, 85))
    TextPantalla(pantalla, None, 24, str(wins1), WHITE, (30, 85))
    pygame.display.update()
#Llamamos a la funcion del menu
imprimir_menu()
while encendido:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
        if event.type == KEYDOWN:
            if event.key == K_1:
                creditos()
            if event.key == K_2:
                partida = True
            if event.key == K_3:
                personalizar = True
            if event.key == K_4:
                encendido = False

    if personalizar == True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
            if event.type == KEYDOWN:
                if event.key == K_LEFT:
                    if seleccion == 2:
                        seleccion -= 1
                        print("mondongo")
                    elif seleccion == 0:
                        seleccion += 1
                if event.key == K_RIGHT:
                    if seleccion < 0:
                        seleccion == 0
                    else:
                        seleccion -= 1
                        print("mondongaspd")
                if event.key == K_SPACE:
                    personalizar == False
                    imprimir_menu()
        if seleccion == 1:
            imprimir_pantalla_fons(fondo, 0, 0)
            imprimir_pantalla_fons(nau4,80,20)
            pygame.display.update()
        if seleccion == 0:
            imprimir_pantalla_fons(fondo, 0, 0)
            imprimir_pantalla_fons(nau3,80,20)
            pygame.display.update()
        clock.tick(fps)
    if partida == True:
        decision_astronauta1 = random.randint(1, 7)
        decision_astronauta2 = random.randint(1, 7)
        while True:
            if decision_astronauta1 == decision_astronauta2:
                decision_astronauta1 = random.randint(1,7)
                decision_astronauta2 = random.randint(1,7)
            if decision_astronauta1 != decision_astronauta2:
                break
        hitbox1 = 8
        hitbox2 = 8
        pygame.mixer_music.stop()
        pygame.mixer.music.load("assets/musicajuego.mp3")
        pygame.mixer.music.play(-1, 5, 3000)
        pygame.mixer.music.set_volume(0.35)
        disparo_sonido = pygame.mixer.Sound("assets/sonidodisparo.mp3")
        disparo_sonido.set_volume(0.15)
        explosion = pygame.mixer.Sound("assets/explosion.mp3")
        explosion.set_volume(0.25)
        sonido_victoria = pygame.mixer.Sound("assets/sonidovictoria.mp3")
        sonido_victoria.set_volume(0.15)
        current_time = pygame.time.get_ticks()
        vidas1 = 3
        austronauta1 = "assets/astronauta1.png"
        austronauta2 = "assets/astronauta2.png"
        austronauta3 = "assets/astronauta3.png"
        austronauta4 = "assets/astronauta4.png"
        austronauta5 = "assets/astronauta5.png"
        austronauta6 = "assets/astronauta6.png"
        austronauta7 = "assets/astronauta7.png"
        vidas2 = 3
        BACKGROUND_IMAGE = 'assets/fondo.png'
        pause = False
        energiajugador1 = 3
        energiajugador2 = 3
        invulnerabilitatjugador1 = False
        invulnerabilitatjugador2 = False
        boostvelocitatjugador1 = False
        boostvelocitatjugador2 = False
        bales_total_utilitzades_jugador1 = 0
        bales_total_utilitzades_jugador2 = 0
        precisio_jugador1 = 0
        precisio_jugador2 = 0
        temps_ultim_energia_jugador1 = 0
        temps_ultim_energia_jugador2 = 0
        temps_inici_partida = current_time
        tiempo_escudo = 3000
        tiempo_velocidad = 3500
        draw = False
        # Jugador 1:
        if seleccion == 1:
            image_player1 = 'assets/nau3.png'
        elif seleccion == 0:
            image_player1 = 'assets/nau.png'
        player_image = pygame.image.load(image_player1)
        player_rect = player_image.get_rect(midbottom=(AMPLADA // 2, ALTURA - 15))
        velocitat_nau = 2

        # Jugador 2:
        image_player2 = 'assets/nau2.png'
        player_image2 = pygame.image.load(image_player2)
        player_rect2 = player_image2.get_rect(midbottom=(AMPLADA // 2, ALTURA - 155))
        velocitat_nau2 = 2

        instrucciones = True
        if instrucciones == True:
            image_player2 = 'assets/nau2.png'
            player_image2 = pygame.image.load(image_player2)
            BACKGROUND_IMAGE = 'assets/fondo.png'
            background = pygame.image.load(BACKGROUND_IMAGE).convert()
            pantalla.blit(background, (0, 0))
            pantalla.blit(player_image, player_rect)
            pantalla.blit(player_image2, player_rect2)
            TextPantalla(pantalla, None, 17, "Jugador 1",
                         WHITE, (90, 170))
            TextPantalla(pantalla, None, 16, "Disparar: W",
                         WHITE, (190, 150))
            TextPantalla(pantalla, None, 16, "Moviment: A-D",
                         WHITE, (190, 140))
            TextPantalla(pantalla, None, 16, "Bostvelocitat: R",
                         WHITE, (190, 180))
            TextPantalla(pantalla, None, 16, "Escudo: E",
                         WHITE, (190, 170))
            TextPantalla(pantalla, None, 16, "Bala grande: CNTLIZQ",
                         WHITE, (190, 160))
            TextPantalla(pantalla, None, 16, "Disparar: UP",
                         WHITE, (190, 20))
            TextPantalla(pantalla, None, 16, "Moviment: LEFT-RIGTH",
                         WHITE, (190, 10))
            TextPantalla(pantalla, None, 16, "Bostvelocitat: NUM.0",
                         WHITE, (190, 50))
            TextPantalla(pantalla, None, 16, "Escudo: DOWN",
                         WHITE, (190, 40))
            TextPantalla(pantalla, None, 16, "Bala grande: CNTLIZQ",
                         WHITE, (190, 30))
            TextPantalla(pantalla, None, 17, "Jugador 2" ,
                         WHITE, (90, 10))
            pygame.display.update()
            time.sleep(4)
            pantalla.blit(background, (0, 0))
            pantalla.blit(player_image2, player_rect2)
            pygame.display.update()

        while True:
            # contador
            current_time = pygame.time.get_ticks()
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                # controlar trets de les naus
                if event.type == KEYDOWN:
                    # jugador 1
                    if event.key == K_w and current_time - temps_ultima_bala_jugador1 >= temps_entre_bales:
                        bales_jugador1.append(pygame.Rect(player_rect.centerx -4, player_rect.top, hitbox1, 10))
                        temps_ultima_bala_jugador1 = pygame.time.get_ticks()
                        disparo_sonido.play()
                    if event.key == K_e and energiajugador1 >= 1:
                        invulnerabilitatjugador1 = True
                        energiajugador1 -= 1
                        temps_ultim_energia_jugador1 = pygame.time.get_ticks()
                    if event.key == K_r and energiajugador1 >= 1:
                        boostvelocitatjugador1 = True
                        energiajugador1 -= 1
                        temps_ultim_energia_jugador1 = current_time
                    if event.key == K_f and energiajugador1 >= 2:
                        energiajugador1 -= 2
                        bala_imatge = balagrande_imatge
                        temps_ultim_energia_jugador1 = current_time
                        hitbox1 = 24
                        # jugador 2
                    if event.key == K_UP and current_time - temps_ultima_bala_jugador2 >= temps_entre_bales:
                        bales_jugador2.append(pygame.Rect(player_rect2.centerx -4, player_rect2.bottom - 10, hitbox2, 10))
                        temps_ultima_bala_jugador2 = current_time
                        disparo_sonido.play()
                    if event.key == K_KP_0 and energiajugador2 >= 1:
                        invulnerabilitatjugador2 = True
                        energiajugador2 -= 1
                        temps_ultim_energia_jugador2 = current_time
                    if event.key == K_DOWN and energiajugador2 >= 1:
                        boostvelocitatjugador2 = True
                        energiajugador2 -= 1
                        temps_ultim_energia_jugador2 = current_time
                    if event.key == K_RCTRL and energiajugador2 >= 2:
                        bala_imatge2 = balagrande_imatge
                        hitbox2 = 24
                        energiajugador2 -= 2
                        # Pause
                    if event.key == K_ESCAPE:
                        pause = True

            # Moviment del jugador 1
            keys = pygame.key.get_pressed()
            if keys[K_a]:
                player_rect.x -= velocitat_nau
            if keys[K_d]:
                player_rect.x += velocitat_nau
            # Moviment del jugador 2
            if keys[K_LEFT]:
                player_rect2.x -= velocitat_nau2
            if keys[K_RIGHT]:
                player_rect2.x += velocitat_nau2

            # Mantenir al jugador dins de la pantalla:
            player_rect.clamp_ip(pantalla.get_rect())
            player_rect2.clamp_ip(pantalla.get_rect())

            # dibuixar el fons:
            imprimir_pantalla_fons(BACKGROUND_IMAGE,0,0)

            # Actualitzar i dibuixar les bales del jugador 1:
            for bala in bales_jugador1:  # bucle que recorre totes les bales
                bala.y -= velocitat_bales + 0.5  # mou la bala
                if bala.bottom < 0 or bala.top > ALTURA:  # comprova que no ha sortit de la pantalla
                    bales_total_utilitzades_jugador1 += 1
                    bales_jugador1.remove(bala)  # si ha sortit elimina la bala
                else:
                    pantalla.blit(bala_imatge, bala)  # si no ha sortit la dibuixa
                # Detectar col·lisions jugador 2:
                if player_rect2.colliderect(bala):  # si una bala toca al jugador1 (el seu rectangle)
                    if current_time - temps_ultim_golp_jugador2 >= temps_invicibilitat and invulnerabilitatjugador2 == False:
                        vidas1 -= 1
                        precisio_jugador1 += 1
                        bales_total_utilitzades_jugador1 += 1
                        explosion.play()
                        image_player2 = 'assets/explosion.png'
                        player_image2 = pygame.image.load(image_player2)
                        BACKGROUND_IMAGE = 'assets/fondo.png'
                        background = pygame.image.load(BACKGROUND_IMAGE).convert()
                        pantalla.blit(background, (0, 0))
                        pantalla.blit(player_image, player_rect)
                        pantalla.blit(player_image2, player_rect2)
                        pygame.display.update()
                        temps_ultima_bala_jugador1 += 1000
                        temps_ultima_bala_jugador2 += 1000
                        time.sleep(1)
                        image_player2 = 'assets/nau2.png'
                        player_image2 = pygame.image.load(image_player2)
                        pantalla.blit(background, (0, 0))
                        pantalla.blit(player_image, player_rect)
                        pantalla.blit(player_image2, player_rect2)
                        pygame.display.update()
                        temps_ultim_golp_jugador2 = current_time
                    bales_jugador1.remove(bala)  # eliminem la bala
                    try:
                        for bala in bales_jugador2:
                            bales_jugador2.remove(bala)
                        bales_total_utilitzades_jugador2 += 1

                    except:
                        continue
                    # mostrem una explosió
                    # eliminem el jugador 1 (un temps)
                    # anotem punts al jugador 1

            # Actualitzar i dibuixar les bales del jugador 2:
            for bala in bales_jugador2:
                bala.y += velocitat_bales
                if bala.bottom < 0 or bala.top > ALTURA:
                    bales_total_utilitzades_jugador2 += 1
                    bales_jugador2.remove(bala)
                else:
                    pantalla.blit(bala_imatge2, bala)
                # Detectar col·lisions jugador 1:
                if player_rect.colliderect(bala):  # si una bala toca al jugador1 (el seu rectangle)
                    if current_time - temps_ultim_golp_jugador1 >= temps_invicibilitat and invulnerabilitatjugador1 == False:
                        vidas2 -= 1
                        precisio_jugador2 += 1
                        bales_total_utilitzades_jugador2 += 1
                        image_player1 = 'assets/explosion.png'
                        explosion.play()
                        player_image = pygame.image.load(image_player1)
                        BACKGROUND_IMAGE = 'assets/fondo.png'
                        background = pygame.image.load(BACKGROUND_IMAGE).convert()
                        pantalla.blit(background, (0, 0))
                        pantalla.blit(player_image, player_rect)
                        pantalla.blit(player_image2, player_rect2)
                        pygame.display.update()
                        temps_ultima_bala_jugador1 += 1000
                        temps_ultima_bala_jugador2 += 1000
                        time.sleep(1)
                        image_player1 = 'assets/nau.png'
                        player_image = pygame.image.load(image_player1)
                        pantalla.blit(background, (0, 0))
                        pantalla.blit(player_image, player_rect)
                        pantalla.blit(player_image2, player_rect2)
                        pygame.display.update()
                        temps_ultim_golp_jugador1 = current_time
                    bales_jugador2.remove(bala)  # eliminem la bala
                    try:
                        for bala in bales_jugador1:
                            bales_jugador1.remove(bala)
                        bales_total_utilitzades_jugador1 += 1
                    except:
                        continue
            if decision_astronauta1 == 1:
                imprimir_pantalla_fons(austronauta1,0,0)
            if decision_astronauta1 == 2:
                imprimir_pantalla_fons(austronauta2,0,0)
            if decision_astronauta1 == 3:
                imprimir_pantalla_fons(austronauta3,0,0)
            if decision_astronauta1 == 4:
                imprimir_pantalla_fons(austronauta4,0,0)
            if decision_astronauta1 == 5:
                imprimir_pantalla_fons(austronauta5,0,0)
            if decision_astronauta1 == 6:
                imprimir_pantalla_fons(austronauta6,0,0)
            if decision_astronauta1 == 7:
                imprimir_pantalla_fons(austronauta7,0,0)
            if decision_astronauta2 == 1:
                imprimir_pantalla_fons(austronauta1,0,180)
            if decision_astronauta2 == 2:
                imprimir_pantalla_fons(austronauta2,0,180)
            if decision_astronauta2 == 3:
                imprimir_pantalla_fons(austronauta3,0,180)
            if decision_astronauta2 == 4:
                imprimir_pantalla_fons(austronauta4,0,180)
            if decision_astronauta2 == 5:
                imprimir_pantalla_fons(austronauta5,0,180)
            if decision_astronauta2 == 6:
                imprimir_pantalla_fons(austronauta6,0,180)
            if decision_astronauta2 == 7:
                imprimir_pantalla_fons(austronauta7,0,180)
            if vidas1 >= 1:
                imprimir_pantalla_fons(corazon, 20, 0)
            if vidas1 >= 2:
                imprimir_pantalla_fons(corazon, 30, 0)
            if vidas1 >= 3:
                imprimir_pantalla_fons(corazon, 40, 0)
            if vidas2 >= 1:
                imprimir_pantalla_fons(corazon, 20, 190)
            if vidas2 >= 2:
                imprimir_pantalla_fons(corazon, 30, 190)
            if vidas2 >= 3:
                imprimir_pantalla_fons(corazon, 40, 190)

            if energiajugador1 >= 3:
                imprimir_pantalla_fons(bateria, 250, 180)
            if energiajugador1 >= 2:
                imprimir_pantalla_fons(bateria, 260 , 180)
            if energiajugador1 >= 1:
                imprimir_pantalla_fons(bateria, 270 , 180)
            if energiajugador2 >= 3:
                imprimir_pantalla_fons(bateria, 250, 10)
            if energiajugador2 >= 2:
                imprimir_pantalla_fons(bateria, 260, 10)
            if energiajugador2 >= 1:
                imprimir_pantalla_fons(bateria, 270, 10)

            if invulnerabilitatjugador1 == True and current_time - temps_ultim_energia_jugador1 >= tiempo_escudo:
                invulnerabilitatjugador1 = False
            if invulnerabilitatjugador2 == True and current_time - temps_ultim_energia_jugador2 >= tiempo_escudo:
                invulnerabilitatjugador2 = False
            if boostvelocitatjugador1 == True and current_time - temps_ultim_energia_jugador1 >= tiempo_velocidad:
                boostvelocitatjugador1 = False
                velocitat_nau = 2
            if boostvelocitatjugador2 == True and current_time - temps_ultim_energia_jugador2 >= tiempo_velocidad:
                boostvelocitatjugador2 = False
                velocitat_nau2 = 2
            if boostvelocitatjugador1 == True:
                velocitat_nau = 4
            if boostvelocitatjugador2 == True:
                velocitat_nau2 = 4

            timer = int((temps_partida - (current_time - temps_inici_partida)) / 1000)
            if timer < 10:
                TextPantalla(pantalla, None, 20, str(timer), (WHITE), (310, 5))
            elif timer < 100:
                TextPantalla(pantalla, None, 20, str(timer), (WHITE), (300, 5))
            elif timer > 99:
                TextPantalla(pantalla, None, 20, str(timer), (WHITE), (290, 5))

            if pause == True:
                tiempo_pausa = 0
                tiempo_pausa = current_time
                seccio_transparent = pygame.Surface((320, 200), pygame.SRCALPHA)
                pygame.draw.rect(seccio_transparent, (0, 0, 0, 150), (0, 0, 320, 200))
                pantalla.blit(seccio_transparent, (0, 0))
                TextPantalla(pantalla, None, 60, "PAUSE", (WHITE), (100, 90))
                pygame.display.update()
                while pause == True:
                    for event in pygame.event.get():
                        if event.type == pygame.QUIT:
                            pygame.quit()
                        if event.type == KEYDOWN:
                            if event.key == K_ESCAPE:
                                pause = False
                    current_time = pygame.time.get_ticks()
                pantalla.blit(background, (0, 0))
                pantalla.blit(player_image, player_rect)
                pantalla.blit(player_image2, player_rect2)
                temps_inici_partida = current_time - tiempo_pausa + temps_inici_partida
                pygame.display.update()

            if vidas1 == 0 or vidas2 == 0 or current_time - temps_inici_partida >= temps_partida:
                score = True
                animacio = True
                try:
                    resultado_precision1 = int((precisio_jugador1 / bales_total_utilitzades_jugador1) * 100)
                except:
                    resultado_precision1 = 0
                try:
                    resultado_precision2 = int((precisio_jugador2 / bales_total_utilitzades_jugador2) * 100)
                except:
                    resultado_precision2 = 0
                if current_time - temps_inici_partida >= temps_partida:
                            draw = True
                while score:
                    bala_imatge = bala_imatge_o
                    bala_imatge2 = bala_imatge_o
                    for event in pygame.event.get():
                        if event.type == pygame.QUIT:
                            pygame.quit()
                        if event.type == KEYDOWN:
                            if event.key == K_SPACE:
                                score = False
                    if vidas1 == 0:
                        if animacio == True:
                            image_player2 = 'assets/explosion.png'
                            player_image2 = pygame.image.load(image_player2)
                            BACKGROUND_IMAGE = 'assets/fondo.png'
                            background = pygame.image.load(BACKGROUND_IMAGE).convert()
                            pantalla.blit(background, (0, 0))
                            pantalla.blit(player_image, player_rect)
                            pantalla.blit(player_image2, player_rect2)
                            pygame.display.update()
                            time.sleep(2)
                            pantalla.blit(background, (0, 0))
                            pantalla.blit(player_image2, player_rect2)
                            pygame.display.update()
                            time.sleep(1)
                            animacio = False
                            wins2 += 1
                        imprimir_pantalla_fons(win1,0,0)
                        sonido_victoria.play()
                        TextPantalla(pantalla, None, 20, "Pulsa espacio para continuar", (255, 255, 255), (80, 130))
                        TextPantalla(pantalla, None, 17, "Precisió jugador 1  " + str(resultado_precision1) + "%",
                                     WHITE, (80, 170))
                        TextPantalla(pantalla, None, 17, "Precisió jugador 2  " + str(resultado_precision2) + "%",
                                     WHITE, (80, 185))
                    if vidas2 == 0:
                        if animacio == True:
                            image_player = 'assets/explosion.png'
                            player_image = pygame.image.load(image_player)
                            BACKGROUND_IMAGE = 'assets/fondo.png'
                            background = pygame.image.load(BACKGROUND_IMAGE).convert()
                            pantalla.blit(background, (0, 0))
                            pantalla.blit(player_image, player_rect)
                            pantalla.blit(player_image2, player_rect2)
                            pygame.display.update()
                            time.sleep(2)
                            pantalla.blit(background, (0, 0))
                            pantalla.blit(player_image, player_rect)
                            pygame.display.update()
                            time.sleep(1)
                            animacio = False
                            wins1 += 1
                        imprimir_pantalla_fons(win2,0,0)
                        sonido_victoria.play()
                        TextPantalla(pantalla, None, 20, "Pulsa espacio para continuar.", (255, 255, 255), (80, 130))
                        TextPantalla(pantalla, None, 17, "Precisió jugador 1  " + str(resultado_precision1) + "%",
                                     WHITE, (80, 170))
                        TextPantalla(pantalla, None, 17, "Precisió jugador 2  " + str(resultado_precision2) + "%",
                                     WHITE, (80, 185))

                    pygame.display.update()

                BACKGROUND_IMAGE = 'assets/fondomenu.png'
                background = pygame.image.load(BACKGROUND_IMAGE).convert()
                partida = False
                image_player1 = 'assets/nau.png'
                image_player2 = 'assets/nau2.png'
                player_image = pygame.image.load(image_player1)
                player_image2 = pygame.image.load(image_player2)
                try:
                    for bala in bales_jugador1:
                        bales_jugador1.remove(bala)
                    for bala in bales_jugador2:
                        bales_jugador2.remove(bala)
                except:
                    imprimir_menu()
                imprimir_menu()
                break

            # dibuixar els jugadors:
            pantalla.blit(player_image, player_rect)
            pantalla.blit(player_image2, player_rect2)
            pygame.display.update()
            clock.tick(fps)
