import pygame, sys
from enemy import Enemy
from tile import *
pygame.init()

class level:
	bullet_list = []
	enemy_list = []
	enemys = []
	tile_list = []
	wall_list = []
	def create_level(self):
		x = y = 0
		for r in self.layout:
			for tile in r:
				if tile == "w":
					self.wall_list.append(wall(x, y))
				elif tile == "e":
					self.enemy_list.append(Enemy(x, y, self.game))
				elif tile == " ":
					pass
				else:
					print tile + " is not a valid character."
					raw_input("<press enter>")
					pygame.quit()
					sys.exit()
				x += 32
			x = 0
			y += 32
		
class level1(level):
	def __init__(self, game):
		self.game = game
		self.layout = [
		" wwwwwww",
		"ewwwwww ",
		"   ee   ",
		"wwwwwww "
		]
		self.create_level()