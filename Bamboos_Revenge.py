import pygame
from pygame.sprite import Group

from settings import Settings
from game_stats import GameStats
from scoreboard import Scoreboard
from button import Button
from bamboo import Bamboo
import game_functions as gf


def run_game():
    # Initialize pygame, settings, and screen object.
    pygame.init()
    ai_settings = Settings()
    screen = pygame.display.set_mode(
        (ai_settings.screen_width, ai_settings.screen_height))
    pygame.display.set_caption("Bamboo's Revenge")

    # Make the Play button.
    play_button = Button(ai_settings, screen, "Bamboo you")

    # Create an instance to store game statistics, and a scoreboard.
    stats = GameStats(ai_settings)
    sb = Scoreboard(ai_settings, screen, stats)

    # Set the background color.
    bg_color = (230, 230, 230)

    # Make a bamboo, a group of bullets, and a group of aliens.
    bamboo = Bamboo(ai_settings, screen)
    bullets = Group()
    aliens = Group()

    # Create the fleet of aliens.
    gf.create_fleet(ai_settings, screen, bamboo, aliens)

    # Start the main loop for the game.
    while True:
        gf.check_events(ai_settings, screen, stats, sb, play_button, bamboo,
                        aliens, bullets)

        if stats.game_active:
            bamboo.update()
            gf.update_bullets(ai_settings, screen, stats, sb, bamboo, aliens,
                              bullets)
            gf.update_aliens(ai_settings, screen, stats, sb, bamboo, aliens,
                             bullets)

        gf.update_screen(ai_settings, screen, stats, sb, bamboo, aliens,
                         bullets, play_button)


run_game()
