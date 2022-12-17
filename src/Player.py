from AnimationHandler import Sprites
import pygame


class Player:
    def __init__(self,) -> None:
        self.sijainti = ["assets", "Pelaaja", "idle", "Idle1-sheet.png"]
        # C: \Users\Olli\Documents\KoodiJutut\PythonKämät\NoitaBeLikeTest\assets\Pelaaja\idle\Idle1-sheet.png
        self.moves = [3, 1]
        self.kuvat = Sprites(self.sijainti, self.moves, pygame.math.Vector2(
            400, 400), 16, 16, 3, 700)

    def update(self):
        self.kuvat.update(pygame.math.Vector2(
            400, 400), 0, True)
