import pygame
from os import path


class Sprites(pygame.sprite.Sprite):
    def __init__(self, path: list[str], animations: list[int], position: pygame.math.Vector2, height: int, width: int, scale: int, cooldown: int, isAnimating: bool) -> None:
        super().__init__()
        self.position: pygame.math.Vector2 = position
        self.animationList: list[list[pygame.Surface]] = []
        self.stepCounter: int = 0
        self.frame: int = 0
        self.height: int = height
        self.width: int = width
        self.scale: int = scale
        self.coolDown: int = cooldown
        self.näyttö = pygame.display.get_surface()
        self.isAnimating: bool = isAnimating
        self.lastUpdate: int = 0
        # Kaikki objektin animaatiot esim idel, walking, attack ja muut
        self.animations: list[int] = animations
        self.sheet: pygame.Surface = pygame.image.load(
            path.join(*path))
        if self.isAnimating:
            self.makeAnimationList()

    def get_image(self, frame: int):
        image = pygame.Surface((self.width, self.height)).convert_alpha()
        image.blit(self.sheet, (0, 0),
                   ((frame*self.width), 0, self.width, self.height))
        image = pygame.transform.scale(
            image, (self.width*self.scale, self.height*self.scale))
        image.set_colorkey((0, 0, 0))
        return image

    def makeAnimationList(self):
        for animation in self.animations:
            temp = []
            for _ in range(animation):
                temp.append(self.get_image(self.stepCounter))
                self.stepCounter += 1
            self.animationList.append(temp)

    def update(self, position: pygame.math.Vector2, action: int, isAnimating: bool):
        self.position = position
        currentTime: int = pygame.time.get_ticks()
        if currentTime - self.lastUpdate >= self.coolDown and isAnimating:
            self.frame += 1
            self.lastUpdate = currentTime
            if self.frame >= len(self.animationList):
                self.frame = 0
        self.näyttö.blit(self.animationList[action][self.frame], self.position)
