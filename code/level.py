#!/usr/bin/python
# -*- coding: utf-8 -*-
import random

import pygame
from pygame import Surface
from pygame.font import Font

from code import entityFactory, entity
from code.const import VIRTUAL_WIDTH, VIRTUAL_HEIGHT, COLOR_WHITE, WINDOW_HEIGHT, COLOR_GREEN, ENEMY_EVENT, SPAWN_TIME
from code.entity import Entity
from code.entityFactory import EntityFactory
from code.entityMediator import EntityMediator


class Level:
    def __init__(self, window, name, menu_option):
        self.window = window
        self.name = name
        self.menu_option = menu_option
        self.game_surface = pygame.Surface((VIRTUAL_WIDTH, VIRTUAL_HEIGHT))

        self.entity_list: list[Entity] = []
        self.entity_list.extend(EntityFactory.get_entity('City1Bg'))
        self.entity_list.append(EntityFactory.get_entity('Walk'))
        pygame.time.set_timer(ENEMY_EVENT,SPAWN_TIME)

        self.camera_x = 0
        self.camera_y = 0

    def run(self):
        clock = pygame.time.Clock()
        pygame.mixer_music.load('./asset/background song.mp3')
        pygame.mixer_music.play(-1)

        while True:
            clock.tick(60)

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    exit()

                if event.type == ENEMY_EVENT:
                    choice = random.choice(('Object1', 'Object2'))
                    self.entity_list.append(EntityFactory.get_entity(choice))

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

            self.level_text(20, f'fps:{clock.get_fps():.0f}', COLOR_WHITE, (10, 5))
            self.level_text(15, f'entity: {len(self.entity_list)}', COLOR_WHITE, (10, WINDOW_HEIGHT - 20))

            pygame.display.flip()

            EntityMediator.verify_interation(entity_list=self.entity_list)
            EntityMediator.verify_health(entity_list=self.entity_list)

    def level_text(self, text_size: int, text: str, text_color: tuple, text_pos: tuple):
        text_font: Font = pygame.font.SysFont(name="Impact", size=text_size)
        text_surf: Surface = text_font.render(text, True, text_color).convert_alpha()
        text_rect = text_surf.get_rect(left=text_pos[0], top=text_pos[1])
        self.window.blit(source=text_surf, dest=text_rect)
