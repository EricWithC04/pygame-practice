import pygame, sys
from pygame.locals import *

pygame.init()

SCREEN = pygame.display.set_mode((800, 480))
pygame.display.set_caption("Mi primer juego!")

colors = {
    "white": (255, 255, 255),
    "black": (0, 0, 0),
    "red": (255, 0, 0),
    "blue": (0, 0, 255),
    "green": (0, 255, 0),
}

SCREEN.fill(colors["white"])
pygame.draw.rect(SCREEN, colors["red"], (50, 40, 160, 48))

while True:
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
    pygame.display.update()