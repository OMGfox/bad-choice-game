import math
import random
import sys
import pygame
from elements.primitives import GameField


class GameCycle():
    def __init__(self, game_field: GameField):
        self.game_field = game_field
        self.logic = GameLogic(self)
        self.level = 1
        self.difficulty = 2  # 4 - easy, 3 - normal, 2 - hard
        self.score = 0
        self.selected_box = None
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
            if (box.coord[0] < mouse_pos[0] < box.coord[0] + box.width and
                    box.coord[1] < mouse_pos[1] < box.coord[1] + box.height):
                box.color = (0, 100, 100)
                self.game_cycle.selected_box = box

    def box_click_up(self):
        for box in self.game_field.elements:
            box.color = (255, 255, 255)

        selected_box = self.game_cycle.selected_box
        if selected_box is None:
            return

        # check if mouse position in clicked box while click up.
        mouse_pos = pygame.mouse.get_pos()
        if (selected_box.coord[0] < mouse_pos[0] < selected_box.coord[0] + selected_box.width and
                selected_box.coord[1] < mouse_pos[1] < selected_box.coord[1] + selected_box.height):
            self.add_score()
            if not self.is_game_over():
                self.next_level()
            else:
                self.new_game()

    def bad_box_arrangement(self):
        amount_boxes = len(self.game_field.elements)
        if amount_boxes < 2:
            return
        for i in range(amount_boxes // self.game_cycle.difficulty):
            random_box_number = random.randrange(0, amount_boxes - 1)
            is_bad = self.game_field.elements[random_box_number].is_bad
            while is_bad:
                random_box_number = random.randrange(0, amount_boxes - 1)
                is_bad = self.game_field.elements[random_box_number].is_bad
            self.game_field.elements[random_box_number].is_bad = True

    def box_value_arrangement(self):
        for box in self.game_field.elements:
            if box.is_bad:
                box.value = self.game_cycle.level * self.game_cycle.difficulty * -1
            else:
                box.value = self.game_cycle.level * self.game_cycle.difficulty

    def reset_boxes(self):
        for box in self.game_field.elements:
            box.is_bad = False

    def next_level(self):
        self.game_cycle.level += 1
        self.reset_boxes()
        self.create_boxes()
        self.bad_box_arrangement()
        self.box_value_arrangement()

    def new_game(self):
        self.game_cycle.level = 1
        self.reset_boxes()
        self.game_cycle.score = 0
        self.game_field.elements.clear()
        self.create_boxes()

    def add_score(self):
        self.game_cycle.score += self.game_cycle.selected_box.value

    def is_game_over(self) -> bool:
        print(self.game_cycle.score)
        if self.game_cycle.score < 0:
            return True
        else:
            return False
