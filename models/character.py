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
        self.jumpFrame = characterJump
        self.deadFrame = characterDead

        self.life = 1

        self.rect = self.image.get_rect()
        self.rect.center = (200, 240)

        self.rect.x = px
        self.rect.y = py

        self.rect.width = self.rect.width // 2
        self.rect.height = self.rect.height // 2

        self.jump = False
        self.jumpSpeed = 20
        self.jumpAcceleration = 1
        self.spaceBetweenFloor = 0

    def update(self):
        keys = pygame.key.get_pressed()
        if self.jump and self.jumpSpeed > 0:
            self.jumpSpeed -= self.jumpAcceleration
        else:
            if self.jumpSpeed < 20:
                self.jumpSpeed += self.jumpAcceleration
        if self.jumpSpeed == 0:
            self.jump = False
        if self.spaceBetweenFloor > 0 and self.jump == False:
            self.rect.y += self.jumpSpeed
            self.spaceBetweenFloor -= self.jumpSpeed
        if self.jump:
            self.image = self.jumpFrame[0]
            self.rect.y -= self.jumpSpeed
            self.spaceBetweenFloor += self.jumpSpeed
        
        if self.life == 0:
            self.rect.y = 170
            if self.current_frame + 1 < len(self.deadFrame):
                self.current_frame = (self.current_frame + 1) % len(self.deadFrame)
            self.image = self.deadFrame[self.current_frame]
        elif keys[pygame.K_d]:
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