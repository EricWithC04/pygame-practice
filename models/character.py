import pygame
from animations import characterIdle

class Player(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()

        self.animation_frames = characterIdle
        self.current_frame = 0
        self.image = self.animation_frames[self.current_frame]

        self.rect = self.image.get_rect()
        self.rect.center = (200, 155)

    def update(self):
        self.current_frame = (self.current_frame + 1) % len(self.animation_frames)
        self.image = self.animation_frames[self.current_frame]