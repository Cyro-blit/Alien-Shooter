import pygame
from pygame.sprite import Sprite

class Abomination(Sprite):

    def __init__(self, AlienWorld):
        super().__init__()
        self.screen = AlienWorld.screen
        self.settings = AlienWorld.my_settings

        self.image = pygame.image.load('img/VibeCheck.png')
        self.rect = self.image.get_rect()

        self.rect.x = self.rect.width
        self.rect.y = self.rect.height

        self.x = float(self.rect.x)
        self.y = float(self.rect.y)

    def update (self):
        self.x += self.settings.abomination_speed * self.settings.abomination_direction
        self.rect.x = self.x

    def check_edges(self):
        screen_rect = self.screen.get_rect()
        if self.rect.right >= screen_rect.right or self.rect.left <= 0:
            return True




