import pygame
from config import (FPS, SCREEN_SIZE, CAPTION, WHITE)

from src.scenes.scene import QuitActionType
from src.scenes.scene_manager import SceneManager
from src.game_entities.player import Player, Keyboard, Direction


def main_loop(
        game_controller : SceneManager, screen: pygame.Surface, game_entities: pygame.sprite.Group, clock: pygame.time.Clock
        ):
    
    action: QuitActionType = QuitActionType.CONTINUE
    while action == QuitActionType.CONTINUE:
        screen.fill(WHITE)
        # pygame.display.update()
        action = game_controller.update()
        clock.tick(FPS)

    return action


def main():
    import platform
    import subprocess
    import sys

    pygame.init()

    # Screen settings
    screen = pygame.display.set_mode(SCREEN_SIZE)
    pygame.display.set_caption(CAPTION)
    
    # Make sure the game will display correctly on high DPI monitors on Windows.
    if platform.system() == "Windows":
        from ctypes import windll

        try:
            windll.user32.SetProcessDPIAware()
        except AttributeError:
            pass

    # Instacing players
    game_entities = pygame.sprite.Group()
    
    player_1 = Player(screen, (160, 180), Direction.LEFT, Keyboard.ARROW)
    player_2 = Player(screen, (600, 180), Direction.RIGHT, Keyboard.WASD)
    
    game_entities.add(player_1)
    game_entities.add(player_2)

    scene = SceneManager(screen, game_entities)

    quit_game: QuitActionType = main_loop(scene, screen, game_entities, pygame.time.Clock())

    pygame.quit()

    if quit_game == QuitActionType.RESTART:
        subprocess.Popen([sys.executable, "run.py"]).wait()
    else:
        sys.exit()


if __name__ == "__main__":
    main()
