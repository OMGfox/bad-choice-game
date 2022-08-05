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


class GameField():
    def __init__(self, size: tuple):
        self.elements = []
        self.size = size
        self.screen = pygame.display.set_mode(self.size)

    def __draw_elements(self):
        for element in self.elements:
            element.draw()

    def draw(self):
        self.screen.fill((0, 0, 0))
        self.__draw_elements()

    def add_box(self, coord):
        self.elements.append(Box(screen=self.screen, coord=(coord[0], coord[1])))
