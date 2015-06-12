import pygame
import constants, sounds
from spritesheet_functions import SpriteSheet
from bullet import Bullet

class Player:
	# Create walking frames
	frames_u = []
	frames_d = []
	frames_l = []
	frames_r = []
	# Speed
	change_x = 0
	change_y = 0
	# Health
	health = 100
	
	def __init__(self, x, y, game):
		self.game = game
		self.bullet_list = self.game.bullet_list
		try:
			self.spritesheet = SpriteSheet("resources/player.png")
		except pygame.error:
			print "player.png does not exist."
			raw_input("<press enter>")
			pygame.quit()
			sys.exit()
		
		# Loading sprites from sheet.
		# Down facing images
		image = self.spritesheet.grab_image(16, 0, 16, 16)
		image = pygame.transform.scale(image, (32, 32))
		self.frames_d.append(image)
		image = self.spritesheet.grab_image(32, 0, 16, 16)
		image = pygame.transform.scale(image, (32, 32))
		self.frames_d.append(image)
		# Up facing images
		image = self.spritesheet.grab_image(64, 0, 16, 16)
		image = pygame.transform.scale(image, (32, 32))
		self.frames_u.append(image)
		image = self.spritesheet.grab_image(80, 0, 16, 16)
		image = pygame.transform.scale(image, (32, 32))
		self.frames_u.append(image)
		# Left facing images
		image = self.spritesheet.grab_image(112, 0, 16, 16)
		image = pygame.transform.scale(image, (32, 32))
		image = pygame.transform.flip(image, True, False)
		self.frames_l.append(image)
		image = self.spritesheet.grab_image(128, 0, 16, 16)
		image = pygame.transform.scale(image, (32, 32))
		image = pygame.transform.flip(image, True, False)
		self.frames_l.append(image)
		# Right facing images
		image = self.spritesheet.grab_image(112, 0, 16, 16)
		image = pygame.transform.scale(image, (32, 32))
		self.frames_r.append(image)
		image = self.spritesheet.grab_image(128, 0, 16, 16)
		image = pygame.transform.scale(image, (32, 32))
		self.frames_r.append(image)
		
		self.index = 0
		self.image = self.frames_d[self.index]
		self.rect = self.image.get_rect()
		self.rect.x = x
		self.rect.y = y
		self.facing = "d"
		
	def update(self):
		# Animate the image
		if (self.change_x != 0) or (self.change_y != 0):
			self.index += 1
			if self.index >= 12:
				self.index = 0
			if self.facing == "u":
				self.image = self.frames_u[self.index//6]
			elif self.facing == "d":
				self.image = self.frames_d[self.index//6]
			elif self.facing == "l":
				self.image = self.frames_l[self.index//6]
			elif self.facing == "r":
				self.image = self.frames_r[self.index//6]
				
		# Move the object		
		self.rect.x += self.change_x
		for wall in self.game.wall_list:
			if self.rect.colliderect(wall.rect):
				if self.change_x > 0:
					self.rect.right = wall.rect.left
				else:
					self.rect.left = wall.rect.right
		self.rect.y += self.change_y
		
		# Check collisions
		for enemy in self.game.enemy_list:
			if self.rect.colliderect(enemy.rect):
				if enemy.dead:
					pass
				else:
					self.health -= 10
		for wall in self.game.wall_list:
			if self.rect.colliderect(wall.rect):
				if self.change_y > 0:
					self.rect.bottom = wall.rect.top
				else:
					self.rect.top = wall.rect.bottom
		if self.rect.left < 0:
			self.rect.left = 0
		elif self.rect.right > constants.SCREEN_WIDTH:
			self.rect.right = constants.SCREEN_WIDTH
		elif self.rect.top < 0:
			self.rect.top = 0
		elif self.rect.bottom > constants.SCREEN_HEIGHT:
			self.rect.bottom = constants.SCREEN_HEIGHT
		
	def shoot(self):
		sounds.laserSound.play()
		if self.facing == "u":
			self.bullet_list.append(Bullet(self.rect.centerx, self.rect.centery, 0, -10, self.game))
		elif self.facing == "d":
			self.bullet_list.append(Bullet(self.rect.centerx, self.rect.centery, 0, 10, self.game))
		elif self.facing == "l":
			self.bullet_list.append(Bullet(self.rect.centerx, self.rect.centery, -10, 0, self.game))
		elif self.facing == "r":
			self.bullet_list.append(Bullet(self.rect.centerx, self.rect.centery, 10, 0, self.game))