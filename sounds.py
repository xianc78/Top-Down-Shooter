import pygame, sys
pygame.init()

try:
	laserSound = pygame.mixer.Sound("resources/laser.wav")
except pygame.error:
	print "laser.wav doesn't exist."
	raw_input("<press enter>")
	pygame.quit()
	sys.exit()