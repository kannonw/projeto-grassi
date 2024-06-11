import pygame

from enum import IntEnum, auto

from config import SCREEN_WIDTH

class QuitActionType(IntEnum):
    CONTINUE = auto()
    QUIT = auto()
    RESTART = auto()
    

class Scene(pygame.sprite.Sprite):
    def __init__(self, screen: pygame.Surface) -> None:
        super(Scene, self).__init__()
        
        self.platform = pygame.Rect(*screen.get_rect().center, 0, 0).inflate(SCREEN_WIDTH, 100)
        self.platform.center = (SCREEN_WIDTH // 2, 800)