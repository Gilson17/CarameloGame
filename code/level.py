#!/usr/bin/python
# -*- coding: utf-8 -*-
import pygame

from code import entityFactory, entity
from code.const import VIRTUAL_WIDTH, VIRTUAL_HEIGHT
from code.entity import Entity
from code.entityFactory import EntityFactory


class Level:
    def __init__(self, window, name, menu_option):
        self.window = window
        self.name = name
        self.menu_option = menu_option
        self.game_surface = pygame.Surface((VIRTUAL_WIDTH, VIRTUAL_HEIGHT))

        self.entity_list: list[Entity] = []
        self.entity_list.extend(EntityFactory.get_entity('City1Bg'))

        self.camera_x = 0
        self.camera_y = 0


    def run(self):
        clock = pygame.time.Clock()

        while True:
            clock.tick(60)

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    exit()


            self.game_surface.fill((0, 0, 0))

            for ent in self.entity_list:

                draw_x = ent.rect.x - self.camera_x
                draw_y = ent.rect.y - self.camera_y

                self.game_surface.blit(ent.surf, (draw_x, draw_y))
                ent.move()


            window_size = self.window.get_size()

            scaled_surface = pygame.transform.smoothscale(
                self.game_surface,
                window_size
            )

            self.window.blit(scaled_surface, (0, 0))


            pygame.display.flip()