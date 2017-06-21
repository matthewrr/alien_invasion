import sys
import pygame
from bullet import Bullet

def check_keydown_events(event, ai_settings, screen, spaceship, bullets):
	if event.key == pygame.K_RIGHT:
		spaceship.moving_right = True
	elif event.key == pygame.K_LEFT:
		spaceship.moving_left = True
	elif event.key == pygame.K_SPACE:
		new_bullet = Bullet(ai_settings, screen, spaceship)
		bullets.add(new_bullet)


def check_keyup_events(event, spaceship):
	if event.key == pygame.K_RIGHT:
		spaceship.moving_right = False
	elif event.key == pygame.K_LEFT:
		spaceship.moving_left = False

def check_events(ai_settings, screen, spaceship, bullets):
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			sys.exit()
		elif event.type == pygame.KEYDOWN:
			check_keydown_events(event, ai_settings, screen, spaceship, bullets)
		elif event.type == pygame.KEYUP:
			check_keyup_events(event, spaceship)

def update_screen(ai_settings, screen, spaceship, bullets):
	screen.fill(ai_settings.bg_color)
	for bullet in bullets.sprites():
		bullet.draw_bullet()
	spaceship.blitme()
	pygame.display.flip()