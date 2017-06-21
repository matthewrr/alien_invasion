import sys
import pygame

def check_keydown_events(event, spaceship):
	if event.key == pygame.K_RIGHT:
		spaceship.moving_right = True
	elif event.key == pygame.K_LEFT:
		spaceship.moving_left = True

def check_keyup_events(event, spaceship):
	if event.key == pygame.K_RIGHT:
		spaceship.moving_right = False
	elif event.key == pygame.K_LEFT:
		spaceship.moving_left = False

def check_events(spaceship):
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			sys.exit()
		elif event.type == pygame.KEYDOWN:
			check_keydown_events(event, spaceship)
		elif event.type == pygame.KEYUP:
			check_keyup_events(event, spaceship)

def update_screen(ai_settings, screen, spaceship):
	screen.fill(ai_settings.bg_color)
	spaceship.blitme()
	pygame.display.flip()