import pygame
import constants
pygame.init()

fontObj = pygame.font.SysFont("arial", 32)

class titleText:
	def __init__(self):
		self.text = fontObj.render("TopDown Shooter", True, constants.WHITE)
		self.rect = self.text.get_rect()
		self.rect.center = (constants.SCREEN_WIDTH/2, constants.SCREEN_HEIGHT/2)
		
class gameOverText:
	def __init__(self):
		self.text = fontObj.render("Game Over", True, constants.WHITE)
		self.rect = self.text.get_rect()
		self.rect.center = (constants.SCREEN_WIDTH/2, constants.SCREEN_HEIGHT/2)