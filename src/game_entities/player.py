from config import (SCREEN_WIDTH, SCREEN_HEIGHT, FPS, WHITE, SPRITES_PER_SECOND)
import os

import pygame
from pygame.locals import (
    RLEACCEL,
    K_UP,
    K_DOWN,
    K_LEFT,
    K_RIGHT,
    K_ESCAPE,
    KEYDOWN,
    QUIT,
    K_w,
    K_a,
    K_s,
    K_d,
)

from aenum import Enum, skip
from enum import IntEnum, auto

class Keyboard(Enum):
    @skip
    class ARROW(Enum):
        UP = K_UP
        LEFT = K_LEFT
        RIGHT = K_RIGHT

    @skip
    class WASD(Enum):
        UP = K_w
        LEFT = K_a
        RIGHT = K_d


class Animation(IntEnum):
    IDLE = 0
    # ATTACK = auto()

class Direction(IntEnum):
    RIGHT = 0 
    LEFT = 1


class Player(pygame.sprite.Sprite):
    def __init__(
            self, screen: pygame.Surface, position: tuple, direction: Direction, keyboard, height = 300, sprites_per_frame = SPRITES_PER_SECOND
            ):
        super(Player, self).__init__()
        
        sprite_path = "./assets/sprites/characters/Female Slayer Katana"

        self.screen = screen
        self.keyboard = keyboard
        self.current_animation = Animation.IDLE

        self.sprites = self.load_sprites(sprite_path)
        self.sprites_per_frame = sprites_per_frame
        self.current_sprite = 0
        self.height = height

        self.on_ground = False
        self.is_animating = False
        # self.previous_direction = direction
        self.direction = direction

        self.image = self.sprites[self.current_animation][self.current_sprite]
        self.rect = self.image.get_rect()
        self.rect.center = position

        if self.direction == Direction.LEFT:
            self.flip()

        self.gravity_force = 3


    def load_sprites(self, sprite_path: str) -> list:
        loaded_sprites = []

        # Load the sprites and make them transparent
        for type_ in Animation:
            # Get path from specifided animation (idle, attack, ...)
            path = os.path.join(sprite_path, type_.name.lower())
            spritesheet = []

            for sprite in os.listdir(path):
                image_surface = pygame.image.load(os.path.join(path, sprite)).convert_alpha()
                image_surface.set_colorkey(WHITE, RLEACCEL)
                # image_surface = pygame.transform.scale(
                #     image_surface, (image_surface.get_width() * (image_surface.get_height() / new_height), image_surface.get_height() * 1 + (self.height / SCREEN_HEIGHT))
                #     )
                spritesheet.append(image_surface)

            loaded_sprites.append(spritesheet)

        return loaded_sprites
    

    def update(self) -> None:
        if not self.is_animating:
            self.animate()

        self.move()


    def animate(self) -> None:
        self.is_animating = True
        self.current_sprite += self.sprites_per_frame / FPS

        if self.current_sprite > len(self.sprites[self.current_animation]) - 1:
            self.current_sprite = 0
        
        self.image = self.sprites[self.current_animation][int(self.current_sprite)]

        if self.direction == Direction.LEFT:
            self.flip()

        self.is_animating = False
        

    def move(self) -> None:
        key = pygame.key.get_pressed()

        if not self.on_ground:
            self.rect.y += self.gravity_force
        elif key[self.keyboard.UP.value]:
            self.rect.y -= 100
        
        if key[self.keyboard.RIGHT.value]:
            self.rect.x += 5
            self.direction = Direction.RIGHT
                
        if key[self.keyboard.LEFT.value]:
            self.rect.x -= 5
            self.direction = Direction.LEFT


    def flip(self):
        self.image = pygame.transform.flip(self.image, True, False)
        self.screen.blit(self.image, self.rect)


    def collide(self, sprite_group: pygame.sprite.Group, platform_rect):
        if pygame.Rect.colliderect(self.rect, platform_rect):
            self.on_ground = True
        else:
            self.on_ground = False

        if pygame.sprite.spritecollide(self, sprite_group, False):
            print('Colliding')
            # self.speedx = -self.speedx
            # self.speedy = -self.speedy
        