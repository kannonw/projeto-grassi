import pygame

from enum import Enum

# Screen settings
CAPTION = "Fight Game"
SCREEN_WIDTH = 1200
SCREEN_HEIGHT = 900
SCREEN_SIZE = (SCREEN_WIDTH, SCREEN_HEIGHT)

# Colors
BLACK = pygame.Color("black")
WHITE = pygame.Color("white")
RED = pygame.Color("red")

# Frame Rate 
FPS = 60
SPRITES_PER_SECOND = 8


class PlayerDataStructure:
    def __init__(
            self, sprite_path: str, x_offset: int, y_offset: int
            ):
        self.sprite_path = sprite_path
        self.x_offset = x_offset
        self.y_offset = y_offset


class PlayerData(Enum):
    FEMALE_SLAYER = PlayerDataStructure(
        sprite_path = './assets/sprites/characters/Female Slayer Katana',
        x_offset = 48,
        y_offset = 26
    )

    DARK_KNIGHT = PlayerDataStructure(
        sprite_path = './assets/sprites/characters/Dark Knight Katana',
        x_offset = 48,
        y_offset = 12
    )
