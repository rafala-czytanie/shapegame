import pygame


class Square:
    def __init__(self, screen, color, center_x, center_y, size):
        self.screen = screen
        self.color = color
        self.center = (center_x, center_y)
        self.size = size
        self.top_left = (self.center[0] - self.size // 2, self.center[1] - self.size // 2)
        self.width = 2

    def draw(self):
        pygame.draw.rect(self.screen, self.color,
                         (self.top_left[0], self.top_left[1], self.size, self.size), self.width)
