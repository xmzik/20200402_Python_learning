import sys
import pygame
from settings import *
from ship import *
import game_functions as gf


def run_game():
    # Initialize game and create a screen object.

    pygame.init()
    #creating Settings object
    ai_settings = Settings()
    screen = pygame.display.set_mode((ai_settings.screen_width, ai_settings.screen_height))
    pygame.display.set_caption("Alien Invasion")
    # creating Ship object
    ship = Ship(screen)


    # Start the main loop for the game.

    while True:
        # Watch for keyboard and mouse events.
        gf.check_events(ship)
        ship.update()
        gf.update_screen(ai_settings, screen, ship)




run_game()
