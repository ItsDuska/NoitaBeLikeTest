import pygame
import os


class Block(pygame.sprite.Sprite):
    def __init__(self, isPassable, pos, blocktype, height, width, group, blockSize) -> None:
        super().__init__(group)
        self.näyttö = pygame.display.get_surface()
        self.image: pygame.Surface = pygame.image.load(
            os.path.join("assets", "blocks", blocktype))
        # self.image = pygame.transform.scale(
        # self.image, (width*10, height*10))
        self.näyttö.blit(self.image, (width//blockSize, height//blockSize))
        self.position = pos
        self.isPassable: bool = isPassable
        self.rect = self.image.get_rect(topleft=pos)
