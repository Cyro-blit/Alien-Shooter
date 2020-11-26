
class Settings:

	def __init__(self):
		#Arena Settings
		self.window_width = 800
		self.window_height = 600
		self.bg_color = (0, 0, 0)


		#Ship Settings
		self.ship_speed = 5
		self.ship_life = 2


		#Bullets Settings
		self.bullet_speed = 5
		self.bullet_width = 600
		self.bullet_height = 10
		self.bullet_color = (60, 242, 187)
		self.bullet_capacity = 3


		#Kecoa Settings
		#self.kecoa_life = 2
		self.kecoa_speed = 1.0
		self.kecoa_drop_speed = 30
		self.kecoa_direction = 1 # 1 ke kanan -1 untuk ke kiri
