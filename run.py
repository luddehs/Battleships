import random

scores = {"computer": 0, "player": 0}

def validate_data():
    """."""
class Board:
    """."""

def random_point(size):
    """."""

def validate_coordinates(x, y, board):
    """."""

def populate_board():
    """."""

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
    player_name = input("Please enter your name: ")


new_game()