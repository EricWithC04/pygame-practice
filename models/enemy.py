import pygame, random
from animations import *

class Enemy(pygame.sprite.Sprite):
    def __init__(self, width):
        super().__init__()

        self.animation_frames = enemyWalkL
        self.current_frame = 0
        self.image = self.animation_frames[self.current_frame]

        self.rect = self.image.get_rect()
        self.rect.center = (200, 240)

        self.rect.x = width
        self.rect.y = 135

        self.appearance = random.randrange(100)
    
    def update(self):
        self.current_frame = (self.current_frame + 1) % len(self.animation_frames)
        self.image = self.animation_frames[self.current_frame]
        self.rect.x -= 5