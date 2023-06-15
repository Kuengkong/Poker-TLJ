import sys
from tkinter import *
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

    running = True
    while running:
        screen.fill((255, 0, 0))


        # Blit the label onto the window surface
        screen.blit(label, label_rect)


        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
        clock.tick(60)
        pygame.display.update()
    start_img = pygame.image.load('start_btn.png').convert_alpha()
    exit_ing = pygame.image.load('exit_btn.png').convert_alpha()
    class Button():
        def _init_(self, x, y, image):
            self.image = image
            self.rect = self.image.get_rect()
            self.rect


    # Set up the window
    pygame.init()
    width, height = 800, 600
    screen = pygame.display.set_mode((width, height))
    pygame.display.set_caption("Username Selection")
    # Define colors
    BLACK = (0, 0, 0)
    WHITE = (255, 255, 255)
    GREEN = (0, 255, 0)


    # Define input box dimensions
    input_box_width, input_box_height = 400, 50

    # Create a rectangle for the input box
    input_box_rect = pygame.Rect(
        width // 2 - input_box_width // 2,
        height // 2 - input_box_height // 2 - 50,
        input_box_width,
        input_box_height,
    )

    # Create a rectangle for the submit button
    button_rect = pygame.Rect(
        width // 2 - input_box_width // 2,
        height // 2 - input_box_height // 2 + 50,
        input_box_width,
        input_box_height,
    )

    # Run the username selection loop
    username = ""
    username_selected = False
    username_font = pygame.font.Font(None, 36)
    input_active = False

    while not username_selected:
        # Handle events
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()

            elif event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                # Check if the input box or button was clicked
                if input_box_rect.collidepoint(event.pos):
                    input_active = True
                else:
                    input_active = False
                if button_rect.collidepoint(event.pos):
                    if username.strip() != "":
                        username_selected = True
            elif event.type == pygame.KEYDOWN:
                if input_active:
                    if event.key == pygame.K_BACKSPACE:
                        username = username[:-1]
                    else:
                        username += event.unicode

        # Clear the screen
        screen.fill(WHITE)

        # Draw the input box
        pygame.draw.rect(screen, BLACK, input_box_rect, 2)
        input_text = username_font.render(username, True, BLACK)
        screen.blit(input_text, (input_box_rect.x + 5, input_box_rect.y + 5))

        # Draw the submit button
        pygame.draw.rect(screen, GREEN, button_rect)
        pygame.draw.rect(screen, BLACK, button_rect, 2)
        submit_text = username_font.render("Submit", True, BLACK)
        submit_text_rect = submit_text.get_rect(center=button_rect.center)
        screen.blit(submit_text, submit_text_rect)

        # Update the display
        pygame.display.flip()



