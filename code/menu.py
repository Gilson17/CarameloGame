#!/usr/bin/python
# -*- coding: utf-8 -*-
import pygame
import pygame.image
import pygame.transform
from pygame import Surface, Rect
from pygame.font import Font

from code.const import WINDOW_WIDTH, COLOR_YELLOW, MENU_OPTIONS, COLOR_WHITE, COLOR_GREEN


class Menu:
    def __init__(self, window):
        self.window = window

        image = pygame.image.load("./asset/City1.png").convert()

        window_width, window_height = self.window.get_size()
        image_width, image_height = image.get_size()

        scale = min(
            window_width / image_width,
            window_height / image_height
        )

        new_width = int(image_width * scale)
        new_height = int(image_height * scale)

        self.surf = pygame.transform.smoothscale(
            image,
            (new_width, new_height)
        )

        self.rect = self.surf.get_rect(
            center=(window_width // 2, window_height // 2)
        )

    def run(self):
        pygame.mixer.music.load('./asset/menu song.wav')
        pygame.mixer.music.play(-1)

        while True:

            self.window.blit(self.surf, self.rect)

            self.menu_text(50, "Caramel", COLOR_YELLOW, (WINDOW_WIDTH / 2, 80))
            self.menu_text(50, "Game", COLOR_YELLOW, (WINDOW_WIDTH / 2, 130))
            self.menu_text(18, "Press Space to play", COLOR_GREEN, (WINDOW_WIDTH / 2, 280))


            for i in range(len(MENU_OPTIONS)):
                self.menu_text(
                    20,
                    MENU_OPTIONS[i],
                    COLOR_WHITE,
                    (WINDOW_WIDTH / 2, 180 + 30 * i)
                )

            pygame.display.flip()

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    quit()

    def menu_text(self, text_size: int, text: str, text_color: tuple, text_center_pos: tuple):
        text_font: Font = pygame.font.SysFont(
            name="Comic Sans MS",
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
