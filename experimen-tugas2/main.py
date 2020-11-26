import pygame
import sys

from settings import Settings
from ship import Ship
from bullet import Bullet
from kecoa import Kecoa

class AlienWorld:

	def __init__(self):
		pygame.init()
		self.my_settings = Settings()

		self.error = False
		self.screen = pygame.display.set_mode([self.my_settings.window_width, self.my_settings.window_height])
		#self.screen = pygame.display.set_mode([0,0], pygame.FULLSCREEN)
		self.title = pygame.display.set_caption("Game ALIEN")
		self.bg_color = self.my_settings.bg_color

		self.my_ship = Ship(self)
		self.bullets = pygame.sprite.Group() #container for bullet
		self.kecoa_army = pygame.sprite.Group()


		self.create_kecoa_army()

	def run_game(self):
		while not self.error:
			self.check_events() #refactoring
			self.my_ship.update() #piloting ship
			self.bullets.update()
			self.remove_bullet()
			self.update_frame() #refactoring

	def check_events(self):
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				#sys.exit()
				self.error = True
			elif event.type == pygame.KEYDOWN:
				self.check_keydown_event(event) #refactoring

			elif event.type == pygame.KEYUP:
				self.check_keyup_event(event) #refactoring
				


	def check_keydown_event(self, event):
		if event.key == pygame.K_w: #forward
			self.my_ship.moving_up = True
		elif event.key == pygame.K_s: #backward
			self.my_ship.moving_down = True
		elif event.key == pygame.K_d: #right
			self.my_ship.moving_right = True
		elif event.key == pygame.K_a: #left
			self.my_ship.moving_left = True
		elif event.key == pygame.K_q: #quit
			self.error = True
		elif event.key == pygame.K_SPACE: #fire!
			self.fire_bullet()
		elif event.key == pygame.K_f  and pygame.key.get_mods() & pygame.KMOD_RCTRL:
			self.screen = pygame.display.set_mode([0,0], pygame.FULLSCREEN)
		elif event.key == pygame.K_f  and pygame.key.get_mods() & pygame.KMOD_SHIFT:
			self.screen = pygame.display.set_mode([self.my_settings.window_width, self.my_settings.window_height])

	def check_keyup_event(self, event):
		if event.key == pygame.K_w:
			self.my_ship.moving_up = False
		elif event.key == pygame.K_s:
			self.my_ship.moving_down = False
		elif event.key == pygame.K_d:
			self.my_ship.moving_right = False
		elif event.key == pygame.K_a:
			self.my_ship.moving_left = False

	def fire_bullet(self):
		if len(self.bullets) < self.my_settings.bullet_capacity: 
			new_bullet = Bullet(self)
			self.bullets.add(new_bullet)

	def remove_bullet(self):
		for bullet in self.bullets.copy():
			if bullet.rect.bottom <= 0:
				self.bullets.remove(bullet)
		#print(len(self.bullets))

	def create_kecoa(self, each_kecoa, every_row):
		kecoa = Kecoa(self)
		kecoa_width, kecoa_height = kecoa.rect.size
		kecoa.x = kecoa_width + (2 * kecoa_width * each_kecoa)
		kecoa.rect.x = kecoa.x
		kecoa.rect.y = kecoa_height + (2 * kecoa_height * every_row)
		self.kecoa_army.add(kecoa)

	def create_kecoa_army(self):
		kecoa = Kecoa(self)
		kecoa_width, kecoa_height = kecoa.rect.size
		available_space_for_kecoa = self.my_settings.window_width - (2*kecoa_width)
		number_of_kecoa = available_space_for_kecoa // (2*kecoa_width)

		ship_p1_height = self.my_ship.rect.height
		available_space_for_row = self.my_settings.window_height - (3*kecoa_height) - ship_p1_height
		number_of_row = available_space_for_row //  (2*kecoa_height)

		for every_row in range(number_of_row):
			for each_kecoa in range(number_of_kecoa+1):
				self.create_kecoa(each_kecoa, every_row)


	def update_frame(self):
		self.screen.fill(self.bg_color)
		self.my_ship.blit_ship()

		for bullet in self.bullets.sprites():
			bullet.draw()

		self.kecoa_army.draw(self.screen)

		pygame.display.flip()


Game_ALIEN = AlienWorld()
Game_ALIEN.run_game()