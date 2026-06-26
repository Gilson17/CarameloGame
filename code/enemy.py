#!/usr/bin/python
# -*- coding: utf-8 -*-
from code.const import ENTITY_SPEED, VIRTUAL_WIDTH
from code.entity import Entity


from code import const
from code.const import ENTITY_SPEED, VIRTUAL_WIDTH
from code.entity import Entity

class Enemy(Entity):
    def __init__(self, name, position):
        super().__init__(name, position)

    def move(self):


        self.rect.centerx -= (ENTITY_SPEED[self.name] + const.BONUS_SPEED)


