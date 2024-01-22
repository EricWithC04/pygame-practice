import pygame, sys
from pygame.locals import *

pygame.init()

SCREEN = pygame.display.set_mode((800, 480))
pygame.display.set_caption("Mi primer juego!")

while True:
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()