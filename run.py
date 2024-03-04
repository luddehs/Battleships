import random

scores = {"computer": 0, "player": 0}

class Board:
    """
    Represents the game board.
    """

    def __init__(self, size, num_ships, name, type):
        """
        Initialize the board game object with the given size and game attributes.
        """
        self.size = size
        self.grid = [['0' for x in range(size) for y in range(size)]]
        self.num_ships = num_ships
        self.name = name
        self.type = type
        self.guesses = []
        self.ships = []
    
    def print(self):
        for row in self.board:
            print(" ".join(row))


def random_point(size):
    """
    Random coordinates generator.
    """
    return random.randint(0, size - 1), random.randint(0, size - 1)

def validate_coordinates(x, y, board):
    """."""

def populate_board(board):
    """
    Random ship placement.
    """
    for _ in range(board.num_ships):
        while True:
            x, y = random_point(board.size)
            if (x, y) not in board.ships: 
                board.ships.append((x, y))
                break


def make_guess(board):
    """."""

def play_game(computer_board, player_board):
    """."""

def new_game():
    """
    Starts a new game, configuring the board size and ship count, clearing scores, and initializing the game boards.
    """
    size = 5
    num_ships = 4
    scores = {"computer": 0, "player": 0}
    print("BATTLESHIPS\n")
    print("Let's start a new game!\n")
    player_name = input("Please enter your name: \n")
    
    computer_board = Board(size, num_ships, "Computer", type="computer")
    player_board = Board(size, num_ships, player_name, type="player")

    for _ in range(num_ships):
        populate_board(player_board)
        populate_board(computer_board)

    play_game(computer_board, player_board)

new_game()