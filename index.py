import pygame, sys
from pygame.locals import *
from animations import *

pygame.init()

screen_d = {
    "w": 800,
    "h": 480
}

FPS = 18
clock = pygame.time.Clock()

SCREEN = pygame.display.set_mode((
    screen_d["w"], 
    screen_d["h"]
))

pygame.display.set_caption("Mi primer juego!")

colors = {
    "white": (255, 255, 255),
    "black": (0, 0, 0),
    "red": (255, 0, 0),
    "blue": (0, 0, 255),
    "green": (0, 255, 0),
}

bg = pygame.image.load("static/assets/background.jpg").convert()
bg_position = {
    "x": 0,
    "y": 0
}

pygame.draw.rect(SCREEN, colors["red"], (50, 40, 80, 48))
pygame.draw.line(SCREEN, colors["green"], (50, 88), (200, 88), 10)
pygame.draw.circle(SCREEN, colors["black"], (300, 88), 20, 15)

pygame.draw.ellipse(SCREEN, (80, 200, 80), (55, 80, 75, 88), 5)

points = [(100, 100), (200, 100), (150, 50)]
pygame.draw.polygon(SCREEN, colors["blue"], points, 5)

icon = pygame.image.load("static/assets/icon.png")
pygame.display.set_icon(icon)

excecuted = True

px = 50
py = 155
left = False
right = False

steps = 0

def update_screen():
    global steps, right, left, bg_position, px

    x_relative = bg_position["x"] % SCREEN.get_rect().width
    SCREEN.blit(bg, (x_relative - SCREEN.get_rect().width, bg_position["y"]))

    if x_relative < screen_d["w"]:
        SCREEN.blit(bg, (x_relative, bg_position["y"]))

    if right and px >= 600:
        bg_position["x"] = bg_position["x"] - 5
    elif left and px <= 50:
        bg_position["x"] = bg_position["x"] + 5
    else:
        bg_position["x"] = bg_position["x"]
    
    if steps + 1 >= 15:
        steps = 0

    if right:
        if steps + 1 >= 11:
            steps = 0
        SCREEN.blit(characterWalkR[steps], (px, py))
        steps += 1
    elif left:
        if steps + 1 >= 11:
            steps = 0
        SCREEN.blit(characterWalkL[steps], (px, py))
        steps += 1
    else:
        SCREEN.blit(characterIdle[steps], (px, py))
        steps += 1


while excecuted:
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
    
    keys = pygame.key.get_pressed()

    if keys[pygame.K_d]:
        right = True
        left = False
        if px < 600:
            px += 5
    elif keys[pygame.K_a]:
        right = False
        left = True
        if px > 50:
            px -= 5
    else:
        right = False
        left = False
    
    update_screen()
    
    pygame.display.update()
    clock.tick(FPS)