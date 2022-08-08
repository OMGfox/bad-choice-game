import math

import pygame


class Box():
    def __init__(self, screen: pygame.Surface, coord: tuple):
        self.coord = coord # x, y
        self.width = 100
        self.height = 100
        self.color = (255, 255, 255)
        self.screen = screen

    def draw(self):
        pygame.draw.rect(surface=self.screen,
                         color=self.color,
                         rect=pygame.Rect(self.coord[0],
                                          self.coord[1],
                                          self.width,
                                          self.height))

    def set_coord(self, x, y):
        self.coord = (x, y)

    def set_size(self, width, height):
        self.width = width
        self.height = height


class GameField():
    def __init__(self, size: tuple):
        self.elements = []
        self.size = size
        self.screen = pygame.display.set_mode(self.size)

    def __draw_elements(self):
        self.__arrange_elements()
        for element in self.elements:
            element.draw()

    def __arrange_elements(self):
        field_width = self.size[0]
        field_height = self.size[1]
        amount_boxes = len(self.elements)
        rows = cols = math.sqrt(amount_boxes)
        box_width = field_width / rows
        box_height = field_height / cols
        box_x = 0
        box_y = 0
        for n, elem in enumerate(self.elements):
            if n % cols == 0 and n > 0:
                box_x = 0
                box_y += box_height
            elem.set_coord(box_x, box_y)
            elem.set_size(box_width, box_height)
            box_x += box_width

    def draw(self):
        self.screen.fill((0, 0, 0))
        self.__draw_elements()

    def add_box(self, coord=(0, 0)):
        self.elements.append(Box(screen=self.screen, coord=(coord[0], coord[1])))

    def change_screen_size(self, size):
        self.size = size
        self.screen = pygame.display.set_mode(self.size)
