import pygame

class Background(pygame.sprite.Sprite):
    def __init__(self, image_path, position=(0, 0)):
        super().__init__()

        self.image = pygame.image.load(image_path)
        self.rect = self.image.get_rect()
        self.rect.topleft = position
