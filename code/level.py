#!/usr/bin/python
# -*- coding: utf-8 -*-
import sys
import random
import pygame
from pygame import Surface
from pygame.font import Font

from code import const
from code.const import VIRTUAL_WIDTH, VIRTUAL_HEIGHT, C_WHITE, WINDOW_HEIGHT, C_GREEN, ENEMY_EVENT, SPAWN_TIME, \
    C_ORANGE, SPEED_EVENT
from code.entity import Entity
from code.entityFactory import EntityFactory
from code.entityMediator import EntityMediator
from code.player import Player


class Level:
    def __init__(self, window, name, menu_option):
        self.window = window
        self.name = name
        self.menu_option = menu_option
        self.game_surface = pygame.Surface((VIRTUAL_WIDTH, VIRTUAL_HEIGHT))

        self.entity_list: list[Entity] = []
        self.entity_list.extend(EntityFactory.get_entity('City1Bg'))
        self.entity_list.append(EntityFactory.get_entity('Walk'))

        self.current_spawn_time = SPAWN_TIME
        pygame.time.set_timer(ENEMY_EVENT, self.current_spawn_time)
        pygame.time.set_timer(SPEED_EVENT, 2000)

        self.timeout = 120000
        const.BONUS_SPEED = 0

        self.camera_x = 0
        self.camera_y = 0

    def run(self):
        clock = pygame.time.Clock()
        pygame.mixer_music.load('./asset/background song.mp3')
        pygame.mixer_music.play(-1)
        pygame.mixer_music.set_volume(0.3)

        while True:
            dt = clock.tick(60)
            self.timeout -= dt

            if self.timeout <= 0:
                self.timeout = 0
                for ent in self.entity_list:
                    if isinstance(ent, Player):
                        self.last_score = ent.score
                        break
                return "WIN", self.last_score

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()

                if event.type == ENEMY_EVENT:
                    choice = random.choice(('Object1', 'Object2'))
                    self.entity_list.append(EntityFactory.get_entity(choice))
                    self.current_spawn_time = max(1500, self.current_spawn_time - 400)
                    pygame.time.set_timer(ENEMY_EVENT, self.current_spawn_time)

                if event.type == SPEED_EVENT:
                    const.BONUS_SPEED += 1

            self.game_surface.fill((0, 0, 0))

            for ent in self.entity_list:
                draw_x = ent.rect.x - self.camera_x
                draw_y = ent.rect.y - self.camera_y
                self.game_surface.blit(ent.surf, (draw_x, draw_y))
                ent.move()

            window_size = self.window.get_size()
            scaled_surface = pygame.transform.smoothscale(self.game_surface, window_size)
            self.window.blit(scaled_surface, (0, 0))

            self.level_text(20, f'{self.name} - Timeout: {self.timeout / 1000 :.1f}s', C_WHITE,
                            (WINDOW_HEIGHT - 120, 5))
            self.level_text(20, f'fps:{clock.get_fps():.0f}', C_WHITE, (10, 5))

            for ent in self.entity_list:
                if isinstance(ent, Player):
                    self.level_text(20, f'score: {ent.score}', C_ORANGE, (window_size[0] - 120, 5))
                    break

            EntityMediator.verify_interation(entity_list=self.entity_list)
            EntityMediator.verify_health(entity_list=self.entity_list)

            player_alive = False
            for ent in self.entity_list:
                if isinstance(ent, Player):
                    player_alive = True
                    self.last_score = ent.score
                    break

            if not player_alive:
                return "LOSS", self.last_score

            pygame.display.flip()

    def level_text(self, text_size: int, text: str, text_color: tuple, text_pos: tuple):
        text_font: Font = pygame.font.SysFont(name="Impact", size=text_size)
        text_surf: Surface = text_font.render(text, True, text_color).convert_alpha()
        text_rect = text_surf.get_rect(left=text_pos[0], top=text_pos[1])
        self.window.blit(source=text_surf, dest=text_rect)
