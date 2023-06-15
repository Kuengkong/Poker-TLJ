import sys
import pygame
from pygame.locals import *

# Create the main game window
WINDOW_WIDTH, WINDOW_HEIGHT = 800, 600
screen = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))

if __name__ == "__main__":
    pygame.init()

    clock = pygame.time.Clock()

    # Initialize game variables and objects
    font = pygame.font.Font(None, 36)  # You can specify the font and size here
    # Set up the text and create a text surface
    text = "POKER"  # Your label text
    label = font.render(text, True, (255, 255, 255))  # Render the text surface
    # Set the position of the label
    label_rect = label.get_rect()
    label_rect.center = (WINDOW_WIDTH // 2, WINDOW_HEIGHT // 2)  # Center the label in the window

    # Define the button dimensions and position
    button_width, button_height = 200, 50
    button_x, button_y = WINDOW_WIDTH // 2 - button_width // 2, WINDOW_HEIGHT // 2 + 100

    # Create a rectangle for the button
    button_rect = pygame.Rect(button_x, button_y, button_width, button_height)

    running = True
    while running:
        screen.fill((255, 0, 0))

        # Blit the label onto the window surface
        screen.blit(label, label_rect)

        # Draw the button rectangle
        pygame.draw.rect(screen, (0, 255, 0), button_rect)

        # Add button text
        button_font = pygame.font.Font(None, 24)
        button_text = button_font.render("Start Game", True, (0, 0, 0))
        text_rect = button_text.get_rect(center= "Start")