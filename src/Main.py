import pygame
import noise
from Player import Player

from Cave import Cave
# loladfadwad
# daffefaF


class Game:
    def __init__(self) -> None:
        pygame.init()
        self.winSize = (800, 800)
        self.chunkSize = (100, 300)
        self.clock = pygame.time.Clock()
        # pygame.FULLSCREEN | pygame.DOUBLEBUF | pygame.HWSURFACE
        self.näyttö = pygame.display.set_mode(self.winSize, 0, 16)
        pygame.event.set_allowed(
            pygame.QUIT | pygame.KEYDOWN | pygame.KEYUP | pygame.MOUSEBUTTONDOWN)
        self.player = Player()
        self.run()

    def run(self):
        #cave = Cave(80, 50, 0.5, 2)
        röpöttää = True
        while röpöttää:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    röpöttää = False
            self.näyttö.fill((0, 60, 0))
            self.player.update()

            self.clock.tick(60)
            pygame.display.update()


if __name__ == "__main__":
    sus = Game()
