import numpy as np
import pygame as pg
from random import randint
from perlin_noise import PerlinNoise
from Block import Block


class Cave:
    def __init__(self, chunkSize, blockSize) -> None:
        self.caveTiles = pg.sprite.Group()
        self.chunkSize = chunkSize
        self.noise = PerlinNoise(7, randint(1, 100_000))
        # f loat sus = (noise([x/chunkSize[0], y/self.chunkSize[1]]))
        self.luoCave(blockSize)

    def luoCave(self, blockSize):
        self.cave = np.empty(
            shape=(self.chunkSize[0], self.chunkSize[1]), dtype=object)
        for y in range(self.chunkSize[0]):
            for x in range(self.chunkSize[1]):
                value = self.noise([x/self.chunkSize[0], y/self.chunkSize[1]])
                isPassable, blockType = self.checkValue(value)
                block = Block(
                    isPassable, pg.math.Vector2(x*blockSize*10, y*blockSize*10), blockType, 16, 16,)
                self.caveTiles.add(block)
                self.cave[y][x] = block

    def update(self):
        self.caveTiles.update()

    def checkValue(self, value):
        if value < 0:
            return False, "kivi1.png"
        return True, "ruoho1.png"
