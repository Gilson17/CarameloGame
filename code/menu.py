#!/usr/bin/python
# -*- coding: utf-8 -*-
import pygame
import pygame.image
import pygame.transform
from pygame import Surface, Rect
from pygame.font import Font

from code.const import WINDOW_WIDTH, C_YELLOW, MENU_OPTIONS, C_WHITE, C_GREEN, VIRTUAL_WIDTH, VIRTUAL_HEIGHT


class Menu:
    def __init__(self, window):
        self.window = window

        image = pygame.image.load("./asset/City1.png").convert_alpha()

        window_width, window_height = self.window.get_size()


        scale = min(
            window_width / VIRTUAL_WIDTH,
            window_height / VIRTUAL_HEIGHT
        )

        new_width = int(image.get_width() * scale)
        new_height = int(image.get_height() * scale)

        self.surf = pygame.transform.smoothscale(
            image,
            (new_width, new_height)
        )

        self.rect = self.surf.get_rect(
            center=(window_width // 2, window_height // 2)
        )

    def run(self):
        menu_option = 0
        pygame.mixer.music.load('./asset/menu song.wav')
        pygame.mixer.music.play(-1)

        #DRAW IMAGES
        while True:

            self.window.blit(self.surf, self.rect)

            self.menu_text(50, "Caramel", C_YELLOW, (WINDOW_WIDTH / 2, 80))
            self.menu_text(50, "Game", C_YELLOW, (WINDOW_WIDTH / 2, 130))
            self.menu_text(18, "Press Space to play", C_GREEN, (WINDOW_WIDTH / 2, 280))

            #CHECK ALL EVENTS
            for i in range(len(MENU_OPTIONS)):

                if i == menu_option:
                    self.menu_text(20, MENU_OPTIONS[i], C_GREEN, (WINDOW_WIDTH / 2, 180 + 30 * i))

                else:
                    self.menu_text(20, MENU_OPTIONS[i], C_WHITE, (WINDOW_WIDTH / 2, 180 + 30 * i))

            pygame.display.flip()

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    quit()
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_DOWN:
                        if menu_option < len(MENU_OPTIONS) - 1:
                            menu_option += 1
                        else:
                            menu_option = 0
                    if event.key == pygame.K_UP:
                        if menu_option > 0:
                            menu_option -= 1
                        else:
                            menu_option = len(MENU_OPTIONS) - 1
                    if event.key == pygame.K_SPACE:
                        return MENU_OPTIONS[menu_option]






    def menu_text(self, text_size: int, text: str, text_color: tuple, text_center_pos: tuple):
        text_font: Font = pygame.font.SysFont(
            name="Impact",
            size=text_size
        )

        text_surf: Surface = text_font.render(
            text,
            True,
            text_color
        ).convert_alpha()

        text_rect: Rect = text_surf.get_rect(
            center=text_center_pos
        )

        self.window.blit(text_surf, text_rect)
