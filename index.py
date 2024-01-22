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
pygame.draw.rect(SCREEN, colors["red"], (50, 40, 80, 48))
pygame.draw.line(SCREEN, colors["green"], (50, 88), (200, 88), 10)
pygame.draw.circle(SCREEN, colors["black"], (300, 88), 20, 15)

pygame.draw.ellipse(SCREEN, (80, 200, 80), (55, 80, 75, 88), 5)

points = [(100, 100), (200, 100), (150, 50)]
pygame.draw.polygon(SCREEN, colors["blue"], points, 5)

while True:
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
    pygame.display.update()