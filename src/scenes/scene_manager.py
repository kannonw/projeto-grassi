import pygame

from src.scenes.scene import Scene, QuitActionType
from src.scenes.fight_scene import FightScene

from config import RED

class SceneManager:
    def __init__(self, screen: pygame.Surface, game_entities: pygame.sprite.Group):
        self.screen = screen
        self.active_scene: Scene = FightScene(self.screen)
        self.game_entities = game_entities


    def update(self) -> QuitActionType:
        for event in pygame.event.get():
            if event.type == pygame.QUIT or event.type == pygame.K_ESCAPE:
                return QuitActionType.QUIT

        self.collision()
        self.game_entities.update()
        self.game_entities.draw(self.screen)

        pygame.draw.rect(self.screen, RED, self.active_scene.platform)
        pygame.draw.rect(self.screen, (255, 192, 203), self.game_entities.sprites()[0].hitbox, 2)
        pygame.draw.rect(self.screen, (255, 192, 203), self.game_entities.sprites()[1].hitbox, 2)

        pygame.draw.rect(self.screen, RED, self.game_entities.sprites()[0].rect, 2)
        pygame.draw.rect(self.screen, RED, self.game_entities.sprites()[1].rect, 2)

        pygame.display.flip()

        return QuitActionType.CONTINUE
    

    def collision(self):
        for entity in self.game_entities:
            self.game_entities.remove(entity)
            entity.collide(self.game_entities, self.active_scene.platform)
            self.game_entities.add(entity)

