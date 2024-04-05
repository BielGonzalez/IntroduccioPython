import time
import pygame
AMPLADA = 320
ALTURA = 200
BACKGROUND_IMAGE = 'fondo.png'

pygame.init()
pantalla = pygame.display.set_mode((AMPLADA, ALTURA))
pygame.display.set_caption("Arcade")

def imprimir_pantalla_fons(image):
    # Imprimeixo imatge de fons:
    background = pygame.image.load(image).convert()
    pantalla.blit(background, (0, 0))
def animacio_inici():
    imprimir_pantalla_fons(BACKGROUND_IMAGE)
    pygame.display.update()
    # time.sleep(3)
    # FONT I TEXT de tamany 64
    font = pygame.font.SysFont(None, 52)
    for i in range(120):
        time.sleep(0.01)
        imprimir_pantalla_fons(BACKGROUND_IMAGE)
        img = font.render("Dark Star", True, (i+90, i+i, i))
        pantalla.blit(img, (60, 200-i))
        pantalla.blit(img, (60, 200-i+1))
        pygame.display.update()
    time.sleep(3)


def imprimir_menu():
    imprimir_pantalla_fons(BACKGROUND_IMAGE)
    # CREAR LA SUPERFÍCIE TRANSPARENT I EL RECTANGLE SOBRE ELLA:
    seccio_transparent = pygame.Surface((240, 120), pygame.SRCALPHA)
    pygame.draw.rect(seccio_transparent, (0, 0, 0, 100), (0, 0, 240, 120))
    # DIBUIXAR LA SUPERFÍCIE TRANSPARENT A LA FINESTRA
    pantalla.blit(seccio_transparent, (40, 40))
    # FONT I TEXT de tamany 64
    font = pygame.font.SysFont(None, 36)
    img = font.render("1.- Crèdits", True, (255, 255, 255))
    img2 = font.render("2.- Jugar", True, (255, 255, 255))
    img3 = font.render("3.- Sortir", True, (255, 255, 255))
    # dibuixem el text
    pantalla.blit(img, (70, 50))
    pantalla.blit(img2, (70, 90))
    pantalla.blit(img3, (70, 130))
    pygame.display.update()




def musica_fons(musica):
    ambient_music = pygame.mixer.Sound(musica)
    music_chanel = pygame.mixer.Channel(0)
    ambient_music.play()

musica_fons('musicmenu.mp3')
animacio_inici()
imprimir_menu()
decisio = input("")
if decisio == "1":
    pantalla.blit(pygame.image.load("fondo.png").convert(), (0, 0))
    pygame.display.update()
    imprimir_pantalla_fons(BACKGROUND_IMAGE)
    pygame.display.update()
    # time.sleep(3)
    # FONT I TEXT de tamany 64
    font = pygame.font.SysFont(None, 52)
    for i in range(120):
        time.sleep(0.01)
        imprimir_pantalla_fons(BACKGROUND_IMAGE)
        img = font.render("Creat", True, (i + 90, i + i, i))
        pantalla.blit(img, (60, 200 - i))
        pantalla.blit(img, (60, 200 - i + 1))
        pygame.display.update()
    time.sleep(3)
while True:
    pygame.display.update()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
