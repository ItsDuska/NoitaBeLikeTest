import pygame
from Player import Player
from Cave import Cave


class Game:
    def __init__(self) -> None:
        pygame.init()
        self.winSize = (800, 800)
        self.chunkSize = (100, 100)  # y x
        self.blockSize = self.winSize[0] // self.chunkSize[0]
        self.clock = pygame.time.Clock()
        # pygame.FULLSCREEN | pygame.DOUBLEBUF | pygame.HWSURFACE
        self.näyttö = pygame.display.set_mode(self.winSize, 0, 16)
        pygame.event.set_allowed(
            pygame.QUIT | pygame.KEYDOWN | pygame.KEYUP | pygame.MOUSEBUTTONDOWN)
        self.player = Player()
        self.cave = Cave(self.chunkSize, self.blockSize)
        self.run()

    def run(self):
        #cave = Cave(80, 50, 0.5, 2)
        röpöttää = True
        while röpöttää:
            pygame.display.set_caption(str(int(self.clock.get_fps()))+" fps")
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    röpöttää = False
            self.näyttö.fill((30, 60, 45))

            self.cave.caveTiles.draw(self.näyttö)
            self.player.update()
            # print(len(self.cave.caveTiles))
            # self.cave.update()
            self.clock.tick(60)
            pygame.display.update()


if __name__ == "__main__":
    sus = Game()
