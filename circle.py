import math
import pygame

from square import Square


class Circle:
    def __init__(self, screen, color, center_x, center_y, radius):
        self.screen = screen
        self.color = color
        self.center_x = center_x
        self.center_y = center_y
        self.radius = radius
        self.width = 2

    def draw(self):
        pygame.draw.circle(self.screen, self.color, (self.center_x, self.center_y), self.radius, self.width)

    def is_outside(self, square: Square, degree_step: int = 5):

        for angle in range(0, 360, degree_step):
            rad = math.radians(angle)
            x = self.center_x + self.radius * math.cos(rad)
            y = self.center_y + self.radius * math.sin(rad)

            if x < square.top_left[0] or \
               x > square.top_left[0] + square.size or \
               y < square.top_left[1] or \
               y > square.top_left[1] + square.size:
                return True

        return False

