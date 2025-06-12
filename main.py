# this allows us to use code from
# the open-source pygame library
# throughout this file
import pygame
from constants import *
from circleshape import *
from player import *
from asteroid import *
from asteroidfield import *
from shot import *

def main():
	pygame.init()
	fps_clock = pygame.time.Clock()
	dt = 0
	screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

	asteroids = pygame.sprite.Group()
	updatable = pygame.sprite.Group()
	drawable = pygame.sprite.Group()
	shots = pygame.sprite.Group()

	Shot.containers = (shots, updatable, drawable)
	Player.containers = (updatable, drawable)
	Asteroid.containers = (asteroids, updatable, drawable)
	AsteroidField.containers = (updatable)

	player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)
	asteroid_field = AsteroidField()

	print("Starting Asteroids!")
	print("Screen width: 1280")
	print("Screen height: 720")


	while True:
		for event in pygame.event.get():
    			if event.type == pygame.QUIT:
        			return
		screen.fill("black")
		updatable.update(dt)
		for asteroid in asteroids:
			if asteroid.collision(player):
				print("Game Over!")
				pygame.QUIT
			for shot in shots:
				if asteroid.collision(shot):
					shot.kill()
					asteroid.split()
		for thing in drawable:
			thing.draw(screen)
		pygame.display.flip()
		dt = (fps_clock.tick(60) / 1000)


if __name__ == "__main__":
	main()
