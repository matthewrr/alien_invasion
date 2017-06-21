import pygame
from pygame.sprite import Group
from settings import Settings
from spaceship import Spaceship
import game_functions as gf

def run_game():
	pygame.init()
	ai_settings = Settings()
	screen = pygame.display.set_mode((ai_settings.screen_width, ai_settings.screen_height))
	pygame.display.set_caption('Alien Invasion')
	spaceship = Spaceship(ai_settings, screen)
	bullets = Group()
	bg_color = (230, 230, 230)

	while True:
		gf.check_events(ai_settings, screen, spaceship, bullets)
		spaceship.update()
		bullets.update()
		gf.update_screen(ai_settings, screen, spaceship, bullets)

run_game()