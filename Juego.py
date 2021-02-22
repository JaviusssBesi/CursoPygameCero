import pygame, sys
from pygame.locals import *

pygame.init()

PANTALLA = pygame.display.set_mode((500, 400))
pygame.display.set_caption('Mi primer juego :D')

BLANCO = (255, 255, 255)
NEGRO = (0, 0, 0)
ROJO = (255, 0, 0)
AZUL = (0, 0, 255)
VERDE = (0, 255, 0)

HC74225 = (199, 66, 37)
H61CD35 = (97, 205, 53)

PANTALLA.fill(BLANCO)

rectangulo1 = pygame.draw.rect(PANTALLA, ROJO, (100, 50, 100, 50))
print(rectangulo1)

pygame.draw.line(PANTALLA, VERDE, (100, 104), (199, 104), 10)

pygame.draw.circle(PANTALLA, NEGRO, (122, 252), 20, 0)

pygame.draw.ellipse(PANTALLA, H61CD35, (275, 200, 40, 80))

puntos = [(100, 300), (100, 100), (150, 100), (150, 300), (300, 200)]
pygame.draw.polygon(PANTALLA, AZUL, puntos, 8)


#Bucle del juego
while True:
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()

    pygame.display.update()