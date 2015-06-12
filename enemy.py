import pygame, random, sys
import constants
from spritesheet_functions import SpriteSheet
pygame.init()

class Enemy:
	frames = []
	def __init__(self, x, y, game):
		try:
			self.spritesheet = SpriteSheet("resources/enemy.png")
		except pygame.error:
			print "enemy.png does not exist."
			raw_input("<press enter>")
			pygame.quit()
			sys.exit()
		
		# Loading sprites from the sheet.
		image = self.spritesheet.grab_image(0, 0, 16, 16)
		image = pygame.transform.scale(image, (32, 32))
		self.frames.append(image)
		image = self.spritesheet.grab_image(16, 0, 16, 16)
		image = pygame.transform.scale(image, (32, 32))
		self.frames.append(image)
		image = self.spritesheet.grab_image(32, 0, 16, 16)
		image = pygame.transform.scale(image, (32, 32))
		self.frames.append(image)
		image = self.spritesheet.grab_image(48, 0, 16, 16)
		image = pygame.transform.scale(image, (32, 32))
		self.frames.append(image)
		
		
		self.index = 0
		self.image = self.frames[self.index]
		
		self.rect = self.image.get_rect()
		self.rect.x = x
		self.rect.y = y
		
		self.change_direction()
		'''
		direction = random.choice([[0, -5], [0, 5], [-5, 0], [5, 0]])
		self.change_x = direction[0]
		self.change_y = direction[0]
		'''
		
		self.game = game
		
		self.dead = False
		
		self.steps = 0
		self.threshold = 20
		
	def update(self):
		if not self.dead:
			self.steps += 1
			if self.steps >= self.threshold:
				self.steps = 0
				self.threshold = 20
				self.change_direction()
			self.rect.x += self.change_x
			if self.rect.left < 0:
				self.rect.left = 0
				self.steps = 0
				self.threshold = 20
				self.change_x *= -1
			elif self.rect.right > constants.SCREEN_WIDTH:
				self.rect.right = constants.SCREEN_WIDTH
				self.steps = 0
				self.threshold = 20
				self.change_x *= -1
			self.rect.y += self.change_y
			if self.rect.top < 0:
				self.rect.top = 0
				self.steps = 0
				self.threshold = 20
				self.change_y *= -1
			elif self.rect.bottom > constants.SCREEN_HEIGHT:
				self.rect.bottom = constants.SCREEN_HEIGHT
				self.steps = 0
				self.threshold = 20
				self.change_y *= -1
			for wall in self.game.wall_list:
				if self.rect.colliderect(wall.rect):
					if self.change_x > 0:
						self.rect.right = wall.rect.left
					else:
						self.rect.left = wall.rect.right
					self.change_y = random.choice([5, -5])
			
			if (self.change_x != 0) or (self.change_y != 0):
				self.index += 1
				if self.index >= 12:
					self.index = 0
				self.image = self.frames[self.index//4]
			for wall in self.game.wall_list:
				if self.rect.colliderect(wall.rect):
					if self.change_y > 0:
						self.rect.bottom = wall.rect.top
					else:
						self.rect.top = wall.rect.bottom
					self.change_x = random.choice([5, -5])
		
			for enemy in self.game.enemy_list:
				if self.rect.colliderect(enemy.rect):
					if enemy == self:
						pass
					else:
						self.change_direction()
						'''
						self.change_x *= -1
						self.change_y *= -1
						'''
			for bullet in self.game.bullet_list:
				if self.rect.colliderect(bullet.rect):
					try:
						self.game.bullet_list.remove(self)
					except ValueError:
						pass
					self.dead = True
					#self.game.enemy_list.remove(self)
		else:
			if self.image != self.frames[3]:
				self.image = self.frames[3]
			
	def change_direction(self):
		dir = random.choice(["v", "h"])
		if dir == "h":
			self.change_x = random.choice([-5, 5])
			self.change_y = 0
		else:
			self.change_x = 0
			self.change_y = random.choice([-5, 5])
		