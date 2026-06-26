# C
import pygame
from pygame.examples.grid import WINDOW_WIDTH

C_YELLOW = (255, 255, 0)
C_WHITE = (255, 255, 255)
C_GREEN = (0, 255, 0)
C_ORANGE = (255, 128, 0)

# E
ENEMY_EVENT = pygame.USEREVENT

ENTITY_SCORE = {
    'City1Bg0': 0,
    'City1Bg1': 0,
    'City1Bg2': 0,
    'City1Bg3': 0,
    'City1Bg4': 0,
    'City1Bg5': 0,
    'City1Bg6': 0,
    'Walk': 0,
    'Object1': 1,
    'Object2': 1,
}

ENTITY_DAMAGE = {
    'City1Bg0': 0,
    'City1Bg1': 0,
    'City1Bg2': 0,
    'City1Bg3': 0,
    'City1Bg4': 0,
    'City1Bg5': 0,
    'City1Bg6': 0,
    'Object1': 1,
    'Object2': 1,
    'Walk': 0,

}

ENTITY_HEALTH = {
    'City1Bg0': 999,
    'City1Bg1': 999,
    'City1Bg2': 999,
    'City1Bg3': 999,
    'City1Bg4': 999,
    'City1Bg5': 999,
    'City1Bg6': 999,
    'Walk': 1,
    'Object1': 50,
    'Object2': 50,
}

ENTITY_SPEED = {
    'City1Bg0': 0,
    'City1Bg1': 3,
    'City1Bg2': 4,
    'City1Bg3': 5,
    'City1Bg4': 6,
    'City1Bg5': 7,
    'City1Bg6': 8,
    'Object1': 15,
    'Object2': 15,
}

# M
MENU_OPTIONS = ('PLAY',
                'SCORE',
                'EXIT')

# S

SPAWN_TIME = 8000
SPEED_EVENT = pygame.USEREVENT + 1

BONUS_SPEED = 0

SCORE_POS = {
    'Title': (WINDOW_WIDTH / 2, 50),
    'EnterName': (WINDOW_WIDTH / 2, 80),
    'Label': (WINDOW_WIDTH / 2, 90),
    'name': (WINDOW_WIDTH / 2, 110),
    0: (WINDOW_WIDTH / 2, 110),
    1: (WINDOW_WIDTH / 2, 130),
    2: (WINDOW_WIDTH / 2, 150),
    3: (WINDOW_WIDTH / 2, 170),
    4: (WINDOW_WIDTH / 2, 190),
    5: (WINDOW_WIDTH / 2, 210),
    6: (WINDOW_WIDTH / 2, 230),
    7: (WINDOW_WIDTH / 2, 250),
    8: (WINDOW_WIDTH / 2, 270),
    9: (WINDOW_WIDTH / 2, 290),

}
# W
WINDOW_WIDTH = 720
WINDOW_HEIGHT = 480

# v
VIRTUAL_WIDTH = 1920
VIRTUAL_HEIGHT = 1080
