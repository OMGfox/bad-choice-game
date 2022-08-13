import math

import pygame


class Box():
    def __init__(self, screen: pygame.Surface, coord: tuple):
        self.coord = coord # x, y
        self.width = 100
        self.height = 100
        self.color = (255, 255, 255)
        self.border_color = (0, 0, 0)
        self.is_bad = False
        self.value = 1
        self.font = pygame.font.SysFont(None, 96)
        self.screen = screen

    def draw(self):
        color = self.color
        # if self.is_bad :
        #     color = (255, 0, 0)
        pygame.draw.rect(surface=self.screen,
                         color=color,
                         border_radius=10,
                         rect=pygame.Rect(self.coord[0],
                                          self.coord[1],
                                          self.width,
                                          self.height))
        self.__draw_border()
        self.__draw_value()

    def __draw_border(self):
        pygame.draw.rect(surface=self.screen,
                         color=self.border_color,
                         border_radius=10,
                         width=1,
                         rect=pygame.Rect(self.coord[0],
                                          self.coord[1],
                                          self.width,
                                          self.height))

    def __draw_value(self):
        if self.is_bad:
            color = (255, 0, 0)
        else:
            color = (0, 255, 0)
        value_surface = self.font.render(str(self.value), True, color)
        resized_value_surface = pygame.transform.scale(value_surface, (self.width, self.height))
        self.screen.blit(resized_value_surface, (self.coord[0], self.coord[1]))

    def set_coord(self, x, y):
        self.coord = (x, y)

    def set_size(self, width, height):
        self.width = width
        self.height = height


class ScorePanel():
    def __init__(self, screen: pygame.Surface, game_field):
        self.screen = screen
        self.game_field = game_field
        self.color = (100, 100, 100)
        self.coord = (0, 0)

    def draw(self):
        color = self.color
        pygame.draw.rect(surface=self.screen,
                         color=color,
                         rect=pygame.Rect(self.coord[0],
                                          self.coord[1],
                                          self.screen.get_width(),
                                          self.game_field.top_offset))
        self.__draw_border()

    def __draw_border(self):
        pass


class GameField():
    def __init__(self, size: tuple):
        self.elements = []
        self.size = size
        self.screen = pygame.display.set_mode(self.size)
        self.top_offset = self.size[1] // 10
        self.score_panel = ScorePanel(screen=self.screen, game_field=self)

    def __draw_elements(self):
        self.__arrange_elements()
        for element in self.elements:
            element.draw()
        self.score_panel.draw()

    def __arrange_elements(self):
        field_width = self.size[0]
        field_height = self.size[1] - self.top_offset
        amount_boxes = len(self.elements)
        rows = cols = math.sqrt(amount_boxes)
        box_width = field_width / rows
        box_height = field_height / cols
        box_x = 0
        box_y = 0 + self.top_offset
        for n, elem in enumerate(self.elements):
            if n % cols == 0 and n > 0:
                box_x = 0
                box_y += box_height
            elem.set_coord(box_x, box_y)
            elem.set_size(box_width, box_height)
            box_x += box_width

    def draw(self):
        self.screen.fill((100, 100, 100))
        self.__draw_elements()

    def add_box(self, coord=(0, 0)):
        self.elements.append(Box(screen=self.screen, coord=(coord[0], coord[1])))

    def change_screen_size(self, size):
        self.size = size
        self.screen = pygame.display.set_mode(self.size)
