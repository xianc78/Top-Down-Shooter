import pygame
import constants
pygame.init()

class Bullet:
	def __init__(self, x, y, change_x, change_y, game):
		self.image = pygame.Surface([5, 5])
		self.image.fill(constants.WHITE)
		self.rect = self.image.get_rect()
		self.rect.centerx = x
		self.rect.centery = y
		self.change_x = change_x
		self.change_y = change_y
		self.game = game
		
	def update(self):
		self.rect.x += self.change_x
		self.rect.y += self.change_y
		for wall in self.game.wall_list:
			if self.rect.colliderect(wall.rect):
				self.game.bullet_list.remove(self)
		if self.check_bounderies() == True:
			self.game.bullet_list.remove(self)
		
	def check_bounderies(self):
		return ((self.rect.left < 0) or (self.rect.right > constants.SCREEN_WIDTH)
		or (self.rect.top < 0) or (self.rect.bottom > constants.SCREEN_HEIGHT))