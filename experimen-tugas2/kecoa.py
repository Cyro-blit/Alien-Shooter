import pygame
from pygame.sprite import Sprite

class Kecoa(Sprite):

	def __init__(self, AlienWorld):
		super().__init__()
		self.screen = AlienWorld.screen

		self.image = pygame.image.load('img/kecoa.png')
		self.rect = self.image.get_rect()

		#posisi sementara
		self.rect.x = self.rect.width
		self.rect.y = self.rect.height

		#variable untuk simpan x sebagai data float
		self.x = float(self.rect.x)