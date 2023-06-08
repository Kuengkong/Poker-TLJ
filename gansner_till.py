from tkinter import Tk, Label, Entry, Button
from pygame.locals import *
import pygame
class PokerGame(Tk):
    def __init__(self):
        super().__init__()
        self.title("Poker Game")

        # Add your UI components and logic here
        # Create a label for username
        self.username_label = Label(self, text="Username:")
        self.username_label.pack()

        # Create an entry field for username
        self.username_entry = Entry(self)
        self.username_entry.pack()

        # Create a label for selecting the number of players
        self.players_label = Label(self, text="Number of Players:")
        self.players_label.pack()

        # Create an entry field for selecting the number of players
        self.players_entry = Entry(self)
        self.players_entry.pack()

        # Create a button to start the game
        self.start_button = Button(self, text="Start Game", command=self.start_game)
        self.start_button.pack()
    def start_game(self):
        username = self.username_entry.get()
        num_players = int(self.players_entry.get())

        # Hide the initial screen
        self.username_label.pack_forget()
        self.username_entry.pack_forget()
        self.players_label.pack_forget()
        self.players_entry.pack_forget()
        self.start_button.pack_forget()

        # Create a new screen for the game
        self.create_game_screen(username, num_players)
    def create_game_screen(self, username, num_players):
        print()


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

        # Add your game screen UI components and logic here
        # For example, create a canvas to display the game view from above
        # and deal cards to players

        # Once the game is set up, call a method to start the betting round

