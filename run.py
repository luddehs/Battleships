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
        """
        Prints current state of the board.
        """

        for row in self.board:
            print(" ".join(row))

    def guess(self, x, y):
        """
        Allows making a guess on the board.
        """
        self.guesses.append((x, y))
        self.board[x][y] = "X"

        if (x, y) in self.ships:
            self.board[x][y] = "!"
            return "Hit"
        else:
            return "Miss"
    
    def add_ship(self, x, y, type="computer"):
        if len(self.ships) >= self.num_ships:
            print("Error: you cannot add any more ships!")
        else:
            self.ships.append((x, y))
            if self.type == "player":
                self.board[x][y] = "#"

def random_point(size):
    """
    Random coordinates generator.
    """
    return random.randint(0, size - 1), random.randint(0, size - 1)

def validate_coordinates(x, y, board):
    """
    Validate the given coordinates.
    """
    return 0 <= x < board.size and 0 <= y < board.size

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
    """
    Enables ability for player to input coordinates.
    """
    while True:
        try:
            x, y = map(int, input("Enter coordinates (row column): ").split())
            if not validate_coordinates(x, y, board):
                print("Invalid coordinates! Please enter coordinates within board bonds.")
                continue
            break
        except ValueError:
            print("Invalid input! Please enter two integers separated by space (row column).")

def play_game(computer_board, player_board):
    """."""

def new_game():
    """
    Starts a new game, configuring the board size and ship count, clearing scores, and initializing the game boards.
    """
    size = 5
    num_ships = 4
    scores = {"computer": 0, "player": 0}
    print("Welcome to BATTLESHIPS!\n")
    print(f"The game board size is {size} rows and columns.")
    print(f"Destroy {num_ships} of your opponents battleships to win.")
    print("Send your missiles by entering coordinates.")
    print("Top left corner is row: 0, col: 0\n")
    print("Let's start a new game!\n")
    player_name = input("Please enter your name: \n")
    
    computer_board = Board(size, num_ships, "Computer", type="computer")
    player_board = Board(size, num_ships, player_name, type="player")

    for _ in range(num_ships):
        populate_board(player_board)
        populate_board(computer_board)

    play_game(computer_board, player_board)

new_game()