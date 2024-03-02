import sys

import pygame

from simulator import Simulator


class UI:
    def __init__(self, screen, font, colors,
                 input_x, input_y,
                 input_width, input_height,
                 button_x, button_y,
                 button_width, button_height,
                 screen_width, screen_height,
                 quit_button_x, quit_button_y,
                 quit_button_width, quit_button_height):

        self.screen = screen
        self.font = font
        self.colors = colors

        self.input_box = pygame.Rect(input_x, input_y, input_width, input_height)
        self.button = pygame.Rect(button_x, button_y, button_width, button_height)
        self.quit_button = pygame.Rect(quit_button_x, quit_button_y, quit_button_width, quit_button_height)  # Define quit button

        self.input_text = ''
        self.input_active = False
        self.button_text = "Run"
        self.button_clicked = False

        self.speed = 1

        self.screen_width = screen_width
        self.screen_height = screen_height

    def handle_event(self, event):

        if event.type == pygame.MOUSEBUTTONDOWN:
            if self.input_box.collidepoint(event.pos):
                self.input_active = not self.input_active
            elif self.button.collidepoint(event.pos):
                self.button_clicked = True
            elif self.quit_button.collidepoint(event.pos):  # Check if quit button is clicked
                pygame.quit()  # Quit the game
                sys.exit()  # Ensure the game exits properly

        elif event.type == pygame.KEYDOWN:
            if self.input_active:
                if event.key == pygame.K_BACKSPACE:
                    self.input_text = self.input_text[:-1]
                else:
                    self.input_text += event.unicode
            if event.key == pygame.K_UP:
                self.speed = min(20, self.speed + 1)  # Increase speed, max limit 5
            elif event.key == pygame.K_DOWN:
                self.speed = max(1, self.speed - 1)  # Decrease speed, min limit 1

    def draw(self, hit_score, runs, screen_height):

        pygame.draw.rect(self.screen, self.colors["red"], self.quit_button)  # Draw quit button
        # Draw text for quit button
        quit_button_text = self.font.render("Quit", True, self.colors["white"])
        self.screen.blit(quit_button_text, (self.quit_button.x + 5, self.quit_button.y + 10))

        pygame.draw.rect(self.screen, self.colors["black"], self.input_box, 2)
        text_surface = self.font.render(self.input_text, True, self.colors["black"])
        self.screen.blit(text_surface, (self.input_box.x + 5, self.input_box.y + 10))

        pygame.draw.rect(self.screen, self.colors["green"], self.button)
        text_surface = self.font.render(self.button_text, True, self.colors["white"])
        self.screen.blit(text_surface, (self.button.x + 5, self.button.y + 10))

        instruction_text = self.font.render(f"Key UP to speed things up", True, self.colors["black"])
        self.screen.blit(instruction_text, (400, screen_height - 70))

        guide_text = self.font.render(f"Type a number in the box and click Run", True, self.colors["red"])
        self.screen.blit(guide_text, (400, screen_height - 110))

        speed_text = self.font.render(f"Speed: {self.speed}x", True, self.colors["black"])
        self.screen.blit(speed_text, (10, screen_height - 30))

        Simulator.draw_ui_elements(self.screen, self.font, self.colors, hit_score, runs, self.screen_width)
