# Import everything needed
import pygame, sys
import constants, textfunctions, sounds, levels
from player import Player
from bullet import Bullet
from enemy import Enemy
from tile import *
pygame.init()

# In game text
titleText = textfunctions.titleText()
gameOverText = textfunctions.gameOverText()
pauseText = textfunctions.pauseText()

# Class that represents the game as a whole
class Game:
	bullet_list = []
	enemy_list = []
	wall_list = []
	def __init__(self, mode):
		self.score = 0
		self.lives = 3
		self.running = True
		# Set level
		self.level_list = [levels.level1, levels.level2, levels.level3]
		self.levelno = 1
		#self.level = levels.level2(self)
		self.set_level(self.level_list[self.levelno -1])
		'''
		self.enemy_list = [Enemy(48, 67, self), Enemy(32, 124, self), Enemy(67, 176, self)]
		self.wall_list = [wall(56, 74)]
		'''
		# Set game objects
		self.enemy_list = self.level.enemy_list
		self.wall_list = self.level.wall_list
		self.player = self.level.player
		self.finish = self.level.finish
		#self.player = Player(0, 0, self)
		self.mode = mode
		self.mouse = pygame.image.load("resources/cursor.png")
		pygame.mouse.set_visible(0)
		
	def update_screen(self, screen):
		if self.mode == "game":
			pygame.display.set_caption("Top Down Shooter | HP: " + str(self.player.health))
			screen.fill(constants.BLACK)
			for bullet in self.bullet_list:
				screen.blit(bullet.image, (bullet.rect.x, bullet.rect.y))
			for enemy in self.enemy_list:
				screen.blit(enemy.image, (enemy.rect.x, enemy.rect.y))
			for wall in self.wall_list:
				screen.blit(wall.image, (wall.rect.x, wall.rect.y))
			for healthpack in self.healthpack_list:
				screen.blit(healthpack.image, (healthpack.rect.x, healthpack.rect.y))
			screen.blit(self.finish.image, (self.finish.rect.x, self.finish.rect.y))
			screen.blit(self.player.image, (self.player.rect.x, self.player.rect.y))
			# Blit cursor last.
			screen.blit(self.mouse, pygame.mouse.get_pos())
		elif self.mode == "menu":
			screen.fill(constants.BLACK)
			screen.blit(titleText.text, titleText.rect)
		elif self.mode == "gameover":
			screen.fill(constants.BLACK)
			screen.blit(gameOverText.text, gameOverText.rect)
		elif self.mode == "paused":
			screen.fill(constants.BLACK)
			screen.blit(pauseText.text, pauseText.rect)
		pygame.display.update()
		
	def check_events(self, screen):
		if self.mode == "game":
			for event in pygame.event.get():
				if event.type == pygame.QUIT:
					self.terminate()
				elif event.type == pygame.KEYDOWN:
					if event.key == pygame.K_SPACE:
						self.player.shoot()
					elif event.key == pygame.K_F12:
						pygame.image.save(screen, "screenshot.png")
					elif event.key == pygame.K_ESCAPE:
						self.mode = "paused"
					# For debuging purposes
					elif event.key == pygame.K_r:
						self.mode = "gameover"
			pressed = pygame.key.get_pressed()
			self.player.change_x = 0
			self.player.change_y = 0
			if pressed[pygame.K_UP]:
				self.player.facing = "u"
				self.player.change_y = -5
			elif pressed[pygame.K_DOWN]:
				self.player.facing = "d"
				self.player.change_y = 5
			elif pressed[pygame.K_LEFT]:
				self.player.facing = "l"
				self.player.change_x = -5
			elif pressed[pygame.K_RIGHT]:
				self.player.facing = "r"
				self.player.change_x = 5
		elif self.mode == "menu":
			for event in pygame.event.get():
				if event.type == pygame.QUIT:
					self.terminate()
				elif event.type == pygame.KEYDOWN and event.key == pygame.K_RETURN:
					self.mode = "game"
		elif self.mode == "gameover":
			for event in pygame.event.get():
				if event.type == pygame.QUIT:
					self.terminate()
				elif event.type == pygame.KEYDOWN and event.key == pygame.K_RETURN:
					self.__init__("game")
		elif self.mode == "paused":
			for event in pygame.event.get():
				if event.type == pygame.QUIT:
					self.terminate()
				elif event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
					self.mode = "game"
		
	def run_logic(self):
		if self.mode == "game":
			self.player.update()
			for bullet in self.bullet_list:
				bullet.update()
			for enemy in self.enemy_list:
				enemy.update()
				
	def set_level(self, level):
		self.level = level(self)
		self.enemy_list = self.level.enemy_list
		self.wall_list = self.level.wall_list
		try:
			self.player = self.level.player
		except AttributeError:
			print "This level does not have a player."
			raw_input("<press enter>")
			self.terminate()
		try:
			self.finish = self.level.finish
		except AttributeError:
			print "This level does not have a finish."
			raw_input("<press enter>")
			self.terminate()
		self.healthpack_list = self.level.healthpack_list
		
	def terminate(self):
		pygame.quit()
		sys.exit()