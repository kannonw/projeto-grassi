import pygame
from config import (SCREEN_SIZE, CAPTION, BACKGROUND_COLOR)


screen = pygame.display.set_mode(SCREEN_SIZE)
pygame.display.set_caption(CAPTION)
screen.fill(BACKGROUND_COLOR)

pygame.display.flip()


running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False


if __name__ == "__main__":
    pygame.init()