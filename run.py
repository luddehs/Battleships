import random
import pyfiglet

scores = {"computer": 0, "player": 0}
class Board:
    """
    Represents the game board.
    """

    def __init__(self, size, num_ships, name, type):
        """
        Initialize the board game object with game attributes.
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
        Prints current state of the board.
        """
        print("Top left corner is row: 0, col: 0")
        print(self.ships)
        y_index = 0

        for row in self.board:
            x_index = 0
            row_chars = ''
            for coordinate in row:
                if show is False:
                    row_chars += f' {coordinate}'
                else:
                    if (y_index, x_index) in self.ships:
                        row_chars +=  ' #'
                    else:
                        row_chars += f' {coordinate}'
                x_index = x_index + 1
            print(f'{row_chars} \n')
            y_index = y_index + 1
            
    def guess(self, x, y):
        """
        Allows making a guess on the board.
        """
        self.guesses.append((x, y))
        self.board[x][y] = "X"
        
        if (x, y) in self.ships:
            self.board[x][y] = "*"
            return "Hit"
        else:
            return "Miss"
    

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
    while len(board.ships) < board.num_ships:
        x, y = random_point(board.size)
        if (x, y) not in board.ships: 
            board.ships.append((x, y))

def make_guess(board):
    """
    Enables ability for player to input coordinates.
    """
    while True:
        try:
            x, y = map(int, input("Fire missiles by entering coordinates: ").split())
            if not validate_coordinates(x, y, board):
                print("Invalid coordinates! Please enter valid coordinates.")
                continue
            if (x, y) in board.guesses:
                print("Target has already been hit! Please enter new coordinates.")
                continue
            break
        except ValueError:
            print("Invalid input! Please enter two integers ranging from 0 to 4, separated by space.")
    
    result = board.guess(x, y)
    print(result)

def play_game(computer_board, player_board, player_name):
    """
    Main game loop.
    """
    while True:
        print(f"\n{player_name}'s Board:")
        player_board.print_board(True)
        make_guess(computer_board)

        print("\nComputer's Board:")
        computer_board.print_board()
        x, y = random_point(player_board.size)
        result = player_board.guess(x, y)
        print(f"Computer guessed: ({x}, {y}) - {result}")

        if result == "Hit":
            scores["computer"] += 1
        elif result == "Miss":
            scores["player"] += 1

        if scores["computer"] == player_board.num_ships:
            print("\nComputer wins!")
            break
        elif scores["player"] == computer_board.num_ships:
            print("\nPlayer wins!")
            break

def get_username():
    input_is_valid = False
    while input_is_valid is False:
        player_name = input("Please enter your name: \n")
        if len(player_name) >=3:
            input_is_valid = True
        else:
            print('Username must consists of at least 3 letters.')
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
    print(f"The game board size is {size} rows and columns.")
    print(f"Destroy {num_ships} of your opponents battleships to win.")
    print("Send your missiles by entering coordinates.")
    #print("Top left corner is row: 0, col: 0\n")
    print("Let's start a new game!\n")
    global player_name
    player_name = get_username()
    
    computer_board = Board(size, num_ships, "Computer", type="computer")
    player_board = Board(size, num_ships, player_name, type="player")

    for _ in range(num_ships):
        populate_board(player_board)
        populate_board(computer_board)

    play_game(computer_board, player_board, player_name)

new_game()