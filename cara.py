import pygame, sys
from pygame.locals import *

AMPLE = 800
ALT = 600
TAMANY = (AMPLE,ALT)
NEGRE = (0,0,0)
VERMELL = (255,0,0,0)
BLANC = (255,255,255)
VERDE = (0,255,0)
VERDE2 = (40,114,51)
VERDE3 = (0,143,57)
VERDE4 = (29,25,16)
GRANATE = (83,4,7)
pygame.init()
pantalla = pygame.display.set_mode(TAMANY)
pygame.display.set_caption('Cercle')
while True: # main game loop
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()

    pantalla.fill(VERDE)
    pygame.draw.circle(pantalla, BLANC, (200,200),100)
    pygame.draw.circle(pantalla, BLANC, (600, 200), 100)
    pygame.draw.circle(pantalla, VERMELL, (200, 200), 40,20)
    pygame.draw.circle(pantalla, VERMELL, (600, 200), 40,20)
    pygame.draw.circle(pantalla, NEGRE, (200, 200), 25)
    pygame.draw.circle(pantalla, NEGRE, (600, 200), 25)
    pygame.draw.circle(pantalla, NEGRE, (200, 200), 130,20)
    pygame.draw.circle(pantalla, NEGRE, (600, 200), 130,20)
    pygame.draw.line(pantalla, NEGRE,(330,200),(470,200),20)
    pygame.draw.line(pantalla, VERMELL, (700,350),(750,500),9)
    pygame.draw.line(pantalla, VERMELL, (690, 400), (750, 380), 9)
    pygame.draw.line(pantalla, VERMELL, (700, 460), (780, 440), 9)
    pygame.draw.ellipse(pantalla, VERDE2,(275,350,250,200))
    pygame.draw.ellipse(pantalla, GRANATE, (310, 440, 180, 100))
    pygame.draw.ellipse(pantalla, VERDE3, (275, 350, 250, 200),10)

    pygame.display.update()
