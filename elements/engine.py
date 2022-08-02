import sys
import pygame
from elements.primitives import GameField


class GameCycle():
    def __init__(self, game_field: GameField):
        self.game_field = game_field
        self.is_running = False
        self.run()

    def run(self):
        pygame.init()

        while 1:
            for event in pygame.event.get():
                if event.type == pygame.QUIT: sys.exit()
            self.game_field.draw()
            pygame.display.flip()


if __name__ == '__main__':
    size = (100, 100)
    gf = GameField(size=size)
    GameCycle(game_field=gf).run()