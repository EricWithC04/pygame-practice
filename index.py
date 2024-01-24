import pygame, sys
from pygame.locals import *
from animations import *
from models.character import Player
from models.enemy import Enemy
# from models.background import Background

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

# background = Background("static/assets/background.jpg", (0, 0))
bg = pygame.image.load("static/assets/background.jpg").convert()

volume = 0.5
pygame.mixer.music.load("static/audio/bg-sound.mp3")
pygame.mixer.music.play(-1)
pygame.mixer.music.set_volume(volume)

v_icons = [
    pygame.image.load("static/assets/icons/volumen-1.png"),
    pygame.image.load("static/assets/icons/volumen-2.png"),
    pygame.image.load("static/assets/icons/volumen-3.png"),
    pygame.image.load("static/assets/icons/mute.png")
]

v_icons = [pygame.transform.scale(img, (img.get_width() // 5, img.get_height() // 5)) for img in v_icons]

bg_position = {
    "x": 0,
    "y": 0
}

icon = pygame.image.load("static/assets/icon.png")
pygame.display.set_icon(icon)

excecuted = True

px = 50
py = 155
left = False
right = False

steps = 0

def update_screen():
    global steps, right, left, bg_position, all_sprites

    x_relative = bg_position["x"] % SCREEN.get_rect().width
    SCREEN.blit(bg, (x_relative - SCREEN.get_rect().width, bg_position["y"]))

    if x_relative < screen_d["w"]:
        SCREEN.blit(bg, (x_relative, bg_position["y"]))

    if right and new_player.rect.x >= 600:
        bg_position["x"] = bg_position["x"] - 5
    elif left and new_player.rect.x <= 50:
        bg_position["x"] = bg_position["x"] + 5
    else:
        bg_position["x"] = bg_position["x"]
    
    if steps + 1 >= 15:
        steps = 0
    
    all_sprites.draw(SCREEN)
    pygame.display.flip()

all_sprites = pygame.sprite.Group()

new_player = Player(px, py)
all_sprites.add(new_player)

new_enemy = Enemy()
all_sprites.add(new_enemy)

while excecuted:
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
    
    all_sprites.update()
    keys = pygame.key.get_pressed()

    if keys[pygame.K_d]:
        right = True
        left = False
    elif keys[pygame.K_a]:
        right = False
        left = True
    else:
        right = False
        left = False
    
    def vol_icon():
        global volume
        if volume <= 0:
            SCREEN.blit(v_icons[3], (650, 30))
        elif volume > 0.7:
            SCREEN.blit(v_icons[0], (650, 30))
        elif volume > 0.4:
            SCREEN.blit(v_icons[1], (650, 30))
        elif volume > 0:
            SCREEN.blit(v_icons[2], (650, 30))

    update_screen()

    if keys[pygame.K_8] and volume > 0:
        volume -= 0.02
        pygame.mixer.music.set_volume(volume)
        vol_icon()
    elif keys[pygame.K_9] and volume < 1.0:
        volume += 0.02
        pygame.mixer.music.set_volume(volume)
        vol_icon()
    elif keys[pygame.K_8] or keys[pygame.K_9]:
        vol_icon()
    
    pygame.display.update()
    clock.tick(FPS)