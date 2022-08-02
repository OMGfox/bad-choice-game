import pygame


class Box():
    def __init__(self, screen: pygame.Surface, coord: tuple):
        self.coord = coord # x, y

    def draw(self):
        pass


class GameField():
    def __init__(self, size: tuple):
        self.elements = []
        self.size = 100, 100
        self.screen = pygame.display.set_mode(self.size)

    def __draw_elements(self):
        for element in self.elements:
            element.draw()

    def draw(self):
        self.__draw_elements()
        self.screen.fill((0, 0, 0))

    def add_box(self, coord):
        self.elements.append(Box(screen=self.screen, coord=(coord[0], coord[1])))
