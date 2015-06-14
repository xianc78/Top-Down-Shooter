import pygame, sys
import constants, textfunctions, sounds, levels
from player import Player
from bullet import Bullet
from enemy import Enemy
from tile import *
pygame.init()

titleText = textfunctions.titleText()
gameOverText = textfunctions.gameOverText()

# Exactly what it says.
class Game:
	bullet_list = []
	enemy_list = []
	wall_list = []
	def __init__(self):
		self.score = 0
		self.lives = 3
		self.running = True
		self.level_list = [levels.level1]
		self.levelno = 1
		self.level = self.level_list[self.levelno - 1](self)
		'''
		self.enemy_list = [Enemy(48, 67, self), Enemy(32, 124, self), Enemy(67, 176, self)]
		self.wall_list = [wall(56, 74)]
		'''
		self.enemy_list = self.level.enemy_list
		self.wall_list = self.level.wall_list
		self.player = Player(0, 0, self)
		self.mode = "menu"
		self.mouse = pygame.image.load("resources/cursor.png")
		pygame.mouse.set_visible(0)
		
	def update_screen(self, screen):
		if self.mode == "game":
			screen.fill(constants.BLACK)
			for bullet in self.bullet_list:
				screen.blit(bullet.image, (bullet.rect.x, bullet.rect.y))
			for enemy in self.enemy_list:
				screen.blit(enemy.image, (enemy.rect.x, enemy.rect.y))
			for wall in self.wall_list:
				screen.blit(wall.image, (wall.rect.x, wall.rect.y))
			screen.blit(self.player.image, (self.player.rect.x, self.player.rect.y))
			# Blit cursor last.
			screen.blit(self.mouse, pygame.mouse.get_pos())
		elif self.mode == "menu":
			screen.blit(titleText.text, titleText.rect)
		elif self.mode == "gameover":
			screen.fill(constants.BLACK)
			screen.blit(gameOverText.text, gameOverText.rect)
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
					'''
					# For debuging purposes
					elif event.key == pygame.K_r:
						self.mode = "gameover"
					'''
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
		elif (self.mode == "menu") or (self.mode == "gameover"):
			for event in pygame.event.get():
				if event.type == pygame.QUIT:
					self.terminate()
				elif event.type == pygame.KEYDOWN and event.key == pygame.K_RETURN:
					self.mode = "game"
		
	def run_logic(self):
		if self.mode == "game":
			self.player.update()
			for bullet in self.bullet_list:
				bullet.update()
			for enemy in self.enemy_list:
				enemy.update()
		
	def terminate(self):
		pygame.quit()
		sys.exit()