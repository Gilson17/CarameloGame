#!/usr/bin/python
# -*- coding: utf-8 -*-
from code import background
from code.background import Background
from code.const import VIRTUAL_WIDTH, WINDOW_HEIGHT
from code.enemy import Enemy
from code.player import Player


class EntityFactory:

     @staticmethod
     def get_entity(entity_name : str, position=(0,0)):
        match entity_name:
            case 'City1Bg':
                list_bg = []
                for i in range(7):
                    list_bg.append(Background(f'City1Bg{i}', (0,0)))
                    list_bg.append(Background(f'City1Bg{i}', (VIRTUAL_WIDTH, 0)))
                return list_bg
            case 'Walk':
                return Player('Walk',(10, WINDOW_HEIGHT + 100))
            case 'Object1':
                return Enemy('Object1', (VIRTUAL_WIDTH + 50, WINDOW_HEIGHT + 100 ))
            case 'Object2':
                return Enemy('Object2', (VIRTUAL_WIDTH + 50, WINDOW_HEIGHT + 100))




