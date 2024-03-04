import random

scores = {"computer": 0, "player": 0}

class Board:
    """
    Represents the game board.
    """

    def __init__(self, size, num_ships, name, type):
        """
        Initialize the board game object with the given size and game attributes
        """
        self.size = size
        self.grid = [['0' for x in range(size) for y in range(size)]]
        self.num_ships = num_ships
        self.name = name
        self.type = type
        self.guesses = []
        self.ships = {}


def random_point(size):
    """."""

def validate_coordinates(x, y, board):
    """."""

def populate_board():
    """
    Initializes game boards and placing ships on them.
    Returns a tuple containing computer and player board.

    """
    size = 10 # Board size can be changed here.
    computer_board = Board(size)
    player_board = Board(size)
    return computer_board, player_board


def make_guess(board):
    """."""

def play_game(computer_board, player_board):
    """."""

def new_game():
    """
    Starts a new game, configuring the board size and ship count, clearing scores, and initializing the game boards.
    """
    scores = {"computer": 0, "player": 0}
    
    print("""
▀█████████▄     ▄████████     ███         ███      ▄█          ▄████████    ▄████████    ▄█    █▄     ▄█     ▄███████▄    ▄████████
  ███    ███   ███    ███ ▀█████████▄ ▀█████████▄ ███         ███    ███   ███    ███   ███    ███   ███    ███    ███   ███    ███
  ███    ███   ███    ███    ▀███▀▀██    ▀███▀▀██ ███         ███    █▀    ███    █▀    ███    ███   ███▌   ███    ███   ███    █▀ 
 ▄███▄▄▄██▀    ███    ███     ███   ▀     ███   ▀ ███        ▄███▄▄▄       ███         ▄███▄▄▄▄███▄▄ ███▌   ███    ███   ███       
▀▀███▀▀▀██▄  ▀███████████     ███         ███     ███       ▀▀███▀▀▀     ▀███████████ ▀▀███▀▀▀▀███▀  ███▌ ▀█████████▀  ▀███████████
  ███    ██▄   ███    ███     ███         ███     ███         ███    █▄           ███   ███    ███   ███    ███                 ███
  ███    ███   ███    ███     ███         ███     ███▌    ▄   ███    ███    ▄█    ███   ███    ███   ███    ███           ▄█    ███
▄█████████▀    ███    █▀     ▄████▀      ▄████▀   █████▄▄██   ██████████  ▄████████▀    ███    █▀    █▀    ▄████▀       ▄████████▀ 
                                                  ▀                                                                                
""")
    print("Let's start a new game!\n")
    player_name = input("Please enter your name: \n")
    


new_game()