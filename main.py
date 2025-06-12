# this allows us to use code from
# the open-source pygame library
# throughout this file
import pygame
from constants import *
from circleshape import *
from player import *

def main():
	pygame.init()
	fps_clock = pygame.time.Clock()
	dt = 0
	screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
	player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)
	print("Starting Asteroids!")
	print("Screen width: 1280")
	print("Screen height: 720")


	while True:
		for event in pygame.event.get():
    			if event.type == pygame.QUIT:
        			return
		screen.fill("black")
		player.draw(screen)
		pygame.display.flip()
		dt = (fps_clock.tick(60) / 1000)


if __name__ == "__main__":
	main()
