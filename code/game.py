#!/usr/bin/python
# -*- coding: utf-8 -*-
import pygame

from code.const import WINDOW_WIDTH, WINDOW_HEIGHT, MENU_OPTIONS
from code.level import Level
from code.menu import Menu


class Game:
    def __init__(self):
        pygame.init()

        self.window_width = WINDOW_WIDTH
        self.window_height = WINDOW_HEIGHT

        self.window = pygame.display.set_mode(
            (self.window_width, self.window_height))

        self.menu = Menu(self.window)


    def run(self, ):


        while True:
            menu = Menu(self.window)
            menu_return = menu.run()

            if menu_return == MENU_OPTIONS[0]:
                level = Level(self.window, 'level 1', menu_return)
                level_return = level.run()
            elif menu_return == MENU_OPTIONS[2]:
                pygame.quit()
                quit()
            else:
                pass


