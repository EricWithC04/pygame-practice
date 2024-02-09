import pygame, sys, random
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
pygame.mixer.music.load("static/audio/bg-sound.wav")
pygame.mixer.music.play(-1)
pygame.mixer.music.set_volume(volume)

sfx = [
    pygame.mixer.Sound("static/audio/jump.wav"),
    pygame.mixer.Sound("static/audio/point.wav"),
    pygame.mixer.Sound("static/audio/death.wav"),
]

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
num_enemies = 999

steps = 0

def update_screen():
    global steps, right, left, bg_position, all_sprites

    x_relative = bg_position["x"] % SCREEN.get_rect().width
    SCREEN.blit(bg, (x_relative - SCREEN.get_rect().width, bg_position["y"]))

    points_font = pygame.font.Font(None, 48)
    points = points_font.render(f"Points: {new_player.points}", True, (255, 255, 255))
    points_rect = points.get_rect()
    points_rect.center = (points_rect.width // 1.5, 35)

    if x_relative < screen_d["w"]:
        SCREEN.blit(bg, (x_relative, bg_position["y"]))

    if new_player.life > 0:
        if right and new_player.rect.x >= 600:
            bg_position["x"] = bg_position["x"] - 5
        elif left and new_player.rect.x <= 50:
            bg_position["x"] = bg_position["x"] + 5
        else:
            bg_position["x"] = bg_position["x"]
    
    if steps + 1 >= 15:
        steps = 0

    all_sprites.draw(SCREEN)
    all_enemies.draw(SCREEN)

    if new_player.life == 0:
        SCREEN.blit(text, text_rect)

    SCREEN.blit(points, points_rect)

    pygame.display.flip()

all_sprites = pygame.sprite.Group()
all_enemies = pygame.sprite.Group()

new_player = Player(px, py)
all_sprites.add(new_player)

font = pygame.font.Font(None, 72)
text = font.render("GAME OVER", True, (255, 255, 255))
text_rect = text.get_rect()
text_rect.center = (
    screen_d["w"] // 2, 
    screen_d["h"] // 2
)

enemy_await = 3000
last_enemy = pygame.time.get_ticks()

while excecuted:
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE and new_player.rect.y == 155:
                new_player.jump = True
                sfx[0].play()
    
    actual_time = pygame.time.get_ticks()
    if actual_time - last_enemy > enemy_await:
        enemyAppearance = random.randrange(100)
        if enemyAppearance > 85 and num_enemies > 0:
            new_enemy = Enemy(screen_d["w"])
            all_enemies.add(new_enemy)
            num_enemies -= 1
            last_enemy = actual_time

    all_sprites.update()
    all_enemies.update()

    collision = pygame.sprite.spritecollide(new_player, all_enemies, False)
    if collision:
        for enemy in collision:
            if new_player.rect.bottom >= enemy.rect.top and new_player.rect.x > enemy.rect.x and new_player.life > 0:
                all_enemies.remove(enemy)
                new_player.points += 1
                sfx[1].play()
                new_player.jump = True
                new_player.jumpSpeed -= 1
            elif new_player.life > 0:
                new_player.life = 0
                new_player.current_frame = 0
                sfx[2].play()

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