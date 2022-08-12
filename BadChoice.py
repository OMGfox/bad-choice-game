#!/usr/bin/env python3
from elements.engine import GameCycle
from elements.primitives import GameField


class BadChoice():
    def __init__(self, field_size: tuple):
        self.field = GameField(field_size)
        self.game_cycle = GameCycle(self.field)

    def start(self):
        self.game_cycle.run()


if __name__ == '__main__':
    field_size = (600, 600)
    BadChoice(field_size).start()
