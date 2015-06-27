import pygame
import constants
pygame.init()

class tile:
	def __init__(self, x, y):
		pass
		
class wall:
	def __init__(self, x, y):
		self.image = pygame.Surface([32, 32])
		self.image.fill(constants.WHITE)
		self.rect = self.image.get_rect()
		self.rect.x = x
		self.rect.y = y
		
class finish:
	def __init__(self, x, y):
		self.image = pygame.Surface([32, 32])
		self.image.fill(constants.RED)
		self.rect = self.image.get_rect()
		self.rect.x = x
		self.rect.y = y