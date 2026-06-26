import sys

import pygame
from code.Score import Score
from code.const import WINDOW_WIDTH, WINDOW_HEIGHT, MENU_OPTIONS
from code.level import Level
from code.menu import Menu


class Game:
    def __init__(self):
        pygame.init()
        self.window_width = WINDOW_WIDTH
        self.window_height = WINDOW_HEIGHT
        self.window = pygame.display.set_mode((self.window_width, self.window_height))
        self.menu = Menu(self.window)

    def run(self):
        score = Score(self.window)

        while True:
            menu = Menu(self.window)
            menu_return = menu.run()

            if menu_return == MENU_OPTIONS[0]:
                level = Level(self.window, 'level 1', menu_return)
                level_return = level.run()

                if isinstance(level_return, tuple):
                    status, player_score = level_return

                    score.show_score(current_game_data=(status, player_score))

            elif menu_return == MENU_OPTIONS[1]:
                score.show_score()

            elif menu_return == MENU_OPTIONS[2]:
                pygame.quit()
                sys.exit()
