import pygame
from pygame.locals import *

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
        pygame.display.update()
    pygame.quit()
