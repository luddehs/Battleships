import random
import pyfiglet

scores = {"computer": 0, "player": 0}


class Board:
    """
    Represents the game board with its attributes and methods.
    """

    def __init__(self, size, num_ships, name, type):
        """
        Initializes the game board object with specified attributes.
        """
        self.size = size
        self.board = [['.' for _ in range(size)] for _ in range(size)]
        self.num_ships = num_ships
        self.name = name
        self.type = type
        self.guesses = []
        self.ships = []

    def print_board(self, show=False):
        """
        Prints the current state of the board.
        """
        y_i = 0
        for row in self.board:
            x_i = 0
            row_chars = ''
            for coordinate in row:
                if (y_i, x_i) in self.guesses and (y_i, x_i) in self.ships:
                    row_chars += ' *'
                elif show is False and (y_i, x_i) not in self.guesses:
                    row_chars += ' .'
                elif show is True and (y_i, x_i) in self.ships:
                    row_chars += ' @'
                else:
                    row_chars += ' ' + coordinate
                x_i += 1
            print(f'{row_chars} \n')
            y_i += 1

    def guess(self, x, y):
        """
        Allows making a guess on the board and updates the board accordingly.
        """
        self.guesses.append((x, y))
        self.board[x][y] = "X"

        if (x, y) in self.ships:
            self.board[x][y] = "*"
            return "Hit!"
        else:
            return "Miss!"


def random_point(size):
    """
    Generates random coordinates within the specified size.
    """
    return random.randint(0, size - 1), random.randint(0, size - 1)


def validate_coordinates(x, y, board):
    """
    Validates the given coordinates against the board size.
    """
    return 0 <= x < board.size and 0 <= y < board.size


def populate_board(board):
    """
    Populates the board with ships at random positions.
    """
    while len(board.ships) < board.num_ships:
        x, y = random_point(board.size)
        if (x, y) not in board.ships:
            board.ships.append((x, y))


def make_guess(board):
    """
    Allows the player to input coordinates for making a guess.
    """
    print("Top left corner is: 0 0")
    while True:
        try:
            x, y = map(int, input("Launch missiles at coordinates:\n").split())
            if not validate_coordinates(x, y, board):
                print("Invalid coordinates! Enter valid coordinates.")
                continue
            if (x, y) in board.guesses:
                print("Target has already been hit. Enter new coordinates.")
                continue
            break
        except ValueError:
            print("Invalid input! Enter two integers ranging from 0 to 4.")

    result = board.guess(x, y)
    print(result)


def play_game(computer_board, player_board, player_name):
    """
    Runs the main game loop until one player wins.
    """
    while True:
        print(f"\n{player_name}'s Board:")
        player_board.print_board(True)
        make_guess(computer_board)

        print("\nComputer's Board:")
        computer_board.print_board()
        x, y = random_point(player_board.size)
        while (x, y) in player_board.guesses:
            x, y = random_point(player_board.size)
        result = player_board.guess(x, y)
        print(f"Computer launched missiles towards: {x} {y} - {result}")

        if result == "Hit!":
            scores["computer"] += 1
        elif result == "Miss!":
            scores["player"] += 1

        if all(coord in player_board.guesses for coord in player_board.ships):
            print("\nComputer wins!")
            break
        elif all(coord in computer_board.guesses
                 for coord in computer_board.ships):
            print("\nPlayer wins!")
            break


def get_username():
    """
    Prompts the user to enter their username.
    """
    input_is_valid = False
    while input_is_valid is False:
        player_name = input("Enter fleet name:\n")
        if len(player_name) >= 3:
            input_is_valid = True
        else:
            print("Fleet name must consist of at least three characters")
    return player_name


def new_game():
    """
    Starts a new game, initializing game boards and clearing scores.
    """
    size = 5
    num_ships = 4
    scores["computer"] = 0
    scores["player"] = 0
    print(pyfiglet.figlet_format("BATTLESHIPS", justify="center", width=80,))
    print("Welcome!\n")
    print(f"Each game board is a {size}x{size} grid.")
    print(f"Launch missiles by entering coordinates: 0 0 for top left.")
    print(f"Destroy {num_ships} of your opponents battleships to win.")
    print("Only one fleet can be victorious!\n")
    global player_name
    player_name = get_username()

    computer_board = Board(size, num_ships, "Computer", type="computer")
    player_board = Board(size, num_ships, player_name, type="player")

    for _ in range(num_ships):
        populate_board(player_board)
        populate_board(computer_board)

    play_game(computer_board, player_board, player_name)


new_game()
