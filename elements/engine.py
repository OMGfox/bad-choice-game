import math
import sys
import pygame
from elements.primitives import GameField


class GameCycle():
    def __init__(self, game_field: GameField):
        self.game_field = game_field
        self.logic = GameLogic(self)
        self.level = 10
        self.run()

    def run(self):
        pygame.init()
        while True:
            self.logic.create_boxes()
            for event in pygame.event.get():
                if event.type == pygame.QUIT: sys.exit()
                if event.type == pygame.MOUSEBUTTONDOWN:
                    self.logic.box_click_down()
                if event.type == pygame.MOUSEBUTTONUP:
                    self.logic.box_click_up()
            self.game_field.draw()
            pygame.display.flip()


class GameLogic():
    def __init__(self, game_cycle):
        self.game_cycle = game_cycle
        self.game_field = game_cycle.game_field

    def create_boxes(self):
        level = self.game_cycle.level
        amount_boxes = len(self.game_field.elements)
        for i in range(int(math.pow(level, 2) - amount_boxes)):
            self.game_field.add_box()

    def box_click_down(self):
        mouse_pos = pygame.mouse.get_pos()
        for box in self.game_field.elements:
            if (box.coord[0] <= mouse_pos[0] <= box.coord[0] + box.width and
                    box.coord[1] <= mouse_pos[1] <= box.coord[1] + box.height):
                box.color = (255, 0, 0)

    def box_click_up(self):
        for box in self.game_field.elements:
            box.color = (255, 255, 255)
