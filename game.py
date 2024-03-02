import pygame
from simulator import Simulator
from shapes.square import Square
from ui import UI


class Game:
    def __init__(self, width, height):
        pygame.init()
        self.screen_width = width
        self.screen_height = height
        self.screen = pygame.display.set_mode((self.screen_width, self.screen_height))
        pygame.display.set_caption("Circle Simulation")
        self.clock = pygame.time.Clock()

        self.colors = {
            "white": (255, 255, 255),
            "black": (0, 0, 0),
            "red": (255, 0, 0),
            "green": (0, 255, 0)
        }

        self.font = pygame.font.Font(None, 36)

        self.square = Square(self.screen, self.colors["black"], width // 2, height // 2, 400)

        self.ui = UI(self.screen, self.font, self.colors, 100, 50, 140, 40,
                     250, 50, 80, 40, self.screen_width, self.screen_height,
                     250, 90, 80, 40)

        self.simulator = Simulator(self.screen, self.square, self.font, self.colors, self.ui)

    def run(self):
        running = True
        while running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
                else:
                    self.ui.handle_event(event)

            if self.ui.button_clicked and self.ui.input_text.isdigit():

                self.simulator.run_simulation(int(self.ui.input_text))
                self.ui.button_clicked = False

            self.screen.fill(self.colors["white"])
            self.square.draw()

            self.ui.draw(self.simulator.hit_score,
                         self.simulator.runs,
                         self.screen_height)

            pygame.display.flip()
            self.clock.tick(60)
        pygame.quit()


if __name__ == "__main__":
    game = Game(900, 700)
    game.run()
