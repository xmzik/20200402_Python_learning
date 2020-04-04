import sys

import pygame

from settings import Settings


def run_game():
    # Initialize game and create a screen object.

    pygame.init()
    screen = pygame.display.set_mode((1200, 800))
    pygame.display.set_caption("Alien Invasion")
    bg_color = (230, 230, 230)

    # Start the main loop for the game.

    while True:
        # Watch for keyboard and mouse events.
        for event in pygame.event.get():

            if event.type == pygame.QUIT:
                sys.exit()

        # Make the most recently drawn screen visible.
        screen.fill(bg_color)
        pygame.display.flip()


run_game()
