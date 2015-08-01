import pygame
import constants
pygame.init()
from game import Game

game = Game("menu")

screen = pygame.display.set_mode((constants.SCREEN_WIDTH, constants.SCREEN_HEIGHT))
pygame.display.set_caption("Top Down Shooter")

clock = pygame.time.Clock()

def main():
	while True:
		#print game.mode
		game.update_screen(screen)
		game.check_events(screen)
		game.run_logic()
		clock.tick(constants.FPS)
		
if __name__ == "__main__":
	main()