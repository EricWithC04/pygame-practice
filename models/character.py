import pygame
from animations import *

class Player(pygame.sprite.Sprite):
    def __init__(self, px, py):
        super().__init__()

        self.animation_frames = characterIdle
        self.current_frame = 0
        self.image = self.animation_frames[self.current_frame]
        self.walkR = characterWalkR
        self.walkL = characterWalkL

        self.rect = self.image.get_rect()
        self.rect.center = (200, 240)

        self.rect.x = px
        self.rect.y = py

    def update(self):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_d]:
            if self.rect.x <= 600:
                self.rect.x += 5
            self.current_frame = (self.current_frame + 1) % len(self.walkR)
            self.image = self.walkR[self.current_frame]
        elif keys[pygame.K_a]:
            if self.rect.x >= 50:
                self.rect.x -= 5
            self.current_frame = (self.current_frame + 1) % len(self.walkL)
            self.image = self.walkL[self.current_frame]
        else:
            self.current_frame = (self.current_frame + 1) % len(self.animation_frames)
            self.image = self.animation_frames[self.current_frame]