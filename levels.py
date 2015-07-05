import pygame, sys
from enemy import Enemy
from tile import *
from player import Player
pygame.init()

class level():
	bullet_list = None
	enemy_list = None
	tile_list = None
	wall_list = None
	healthpack_list = None
	def __init__(self, game):
		self.game = game
		self.bullet_list = []
		self.enemy_list = []
		self.enemys = []
		self.tile_list = []
		self.wall_list = []
		self.healthpack_list = []
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
				elif tile == "p":
					self.player = Player(x, y, self.game)
				elif tile == "h":
					self.healthpack_list.append(healthpack(x, y))
				elif tile == "f":
					self.finish = finish(x, y)
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
		level.__init__(self, game)
		#self.game = game
		self.layout = [
		"   wwwww eww",
		" p h    e ww",
		"     wwwwwww",
		"www  wwwwwww",
		"ee   wwwwwww",
		"www  wwwwwww",
		"   h   h   f",
		"wwwwwwwwwwwww"
		]
		self.create_level()
		
class level2(level):
	def __init__(self, game):
		level.__init__(self, game)
		#self.game = game
		self.layout = [
		"wwwwwwwwwwwwwwwwwwww",
		"wpwww    h    e    w",
		"w e  e wwww  e e   w",
		"ww  wwwwwww h  h   w",
		" h  e   ew  e  e  fw",
		" e wwwwwwwwwwwwwwwww",
		"wwwwwwwwww"
		]
		self.create_level()
		
class level3(level):
	def __init__(self, game):
		level.__init__(self, game)
		self.layout = [
		"wwwwwwwwwwwwwwwwwwww",
		"wp e  e   w    e   w",
		"w    h    w h    e w",
		"w h   e   w e   h  w",
		"we e   e       e   f",
		"wwwwwwwwwwwwwwwwwwww"
		]
		self.create_level()