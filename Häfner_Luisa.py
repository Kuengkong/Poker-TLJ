from tkinter import *
import pygame
from pygame.locals import *

# Create the main game window
WINDOW_WIDTH, WINDOW_HEIGHT = 800, 600
screen = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))

if __name__ == "__main__":
    pygame.init()
    # Initialize game variables and objects

    running = True
    while running:
        screen.fill((255, 0, 0))
        for event in pygame.event.get():
            if event.type == QUIT:
                running = False
        # Handle game logic and drawing here
        # Set up the font
        font = pygame.font.Font(None, 36)  # You can specify the font and size here

        # Set up the text and create a text surface
        text = "POKER"  # Your label text
        label = font.render(text, True, (255, 255, 255))  # Render the text surface

        # Set the position of the label
        label_rect = label.get_rect()
        label_rect.center = (WINDOW_WIDTH // 2, WINDOW_HEIGHT // 2)  # Center the label in the window

        # Blit the label onto the window surface
        screen.blit(label, label_rect)

        # Update the display
        pygame.display.flip()

        pygame.display.update()
    pygame.quit()

# Add widgets and functionality to the window
# Add a label for the title

