import pygame
from settings import Settings
from spaceship import Spaceship
import game_functions as gf

def run_game():
	pygame.init()
	ai_settings = Settings()
	screen = pygame.display.set_mode((ai_settings.screen_width, ai_settings.screen_height))
	pygame.display.set_caption('Alien Invasion')
	spaceship = Spaceship(ai_settings, screen)
	bg_color = (230, 230, 230)

	while True:
		gf.check_events(spaceship)
		spaceship.update()
		gf.update_screen(ai_settings, screen, spaceship)

run_game()