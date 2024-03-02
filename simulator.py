import math
import random
import pygame

from circle import Circle


class Simulator:
    def __init__(self, screen, square, font, colors, ui):
        self.screen = screen
        self.square = square
        self.font = font
        self.colors = colors
        self.ui = ui
        self.hit_score = 0
        self.runs = 0

    def run_simulation(self, n):
        self.hit_score = 0
        self.runs = 0
        for _ in range(n):

            x1, y1, x2, y2 = self._generate_random_points()
            center_x, center_y, radius = self._calculate_circle_properties(x1, y1, x2, y2)

            circle = Circle(self.screen, self.colors["red"], center_x, center_y, radius)
            circle.draw()
            self.shade_circle_outside(circle)

            pygame.display.flip()
            pygame.time.wait(200)  # Pause to make the circle visible

            self._clear_screen()

            if circle.is_outside(self.square):
                self.hit_score += 1

            self.runs += 1

            pygame.display.flip()
            pygame.time.wait(int(100 / self.ui.speed))  # Adjust for speed

    def _clear_screen(self):
        self.screen.fill(self.colors["white"])
        self.square.draw()
        self.ui.draw(self.hit_score, self.runs, self.ui.screen_height)

    def _generate_random_points(self):

        x1, y1 = (random.randint(self.square.top_left[0],
                                 self.square.top_left[0] + self.square.size),
                  random.randint(self.square.top_left[1],
                                 self.square.top_left[1] + self.square.size))

        x2, y2 = (random.randint(self.square.top_left[0],
                                self.square.top_left[0] + self.square.size),
                  random.randint(self.square.top_left[1],
                                 self.square.top_left[1] + self.square.size))
        return x1, y1, x2, y2

    @staticmethod
    def _calculate_circle_properties(x1, y1, x2, y2):
        center_x, center_y = (x1 + x2) // 2, (y1 + y2) // 2
        radius = math.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2) / 2
        return center_x, center_y, radius

    def shade_circle_outside(self, circle):
        for angle in range(0, 360, 1):
            rad = math.radians(angle)
            x = circle.center_x + circle.radius * math.cos(rad)
            y = circle.center_y + circle.radius * math.sin(rad)
            if x < self.square.top_left[0] or x > self.square.top_left[0] + self.square.size or y < self.square.top_left[1] or y > self.square.top_left[1] + self.square.size:
                pygame.draw.circle(self.screen, self.colors["green"], (int(x), int(y)), 3)

    @staticmethod
    def draw_ui_elements(screen, font, colors, hit_score, runs, screen_width):
        if runs > 0:
            hit_probability = hit_score / runs
            proba = font.render(f"Hit Probability: {hit_probability:.4f}", True, colors["red"])
            trials = font.render(f"Total Runs: {runs}", True, colors["black"])
            hits = font.render(f"Total Hits: {hit_score}", True, colors["black"])

        else:
            proba = font.render("Hit Probability: N/A", True, colors["red"])
            trials = font.render("Total Runs: 0", True, colors["black"])
            hits = font.render(f"Total Hits: 0", True, colors["black"])

        screen.blit(proba, (screen_width - 300, 10))
        screen.blit(trials, (screen_width - 300, 40))
        screen.blit(hits, (screen_width - 300, 70))

