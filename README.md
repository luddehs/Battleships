# Battleships 

Battleships is an engaging strategy-based guessing game where you can challenge the computer. At the outset, both the player and the computer receive a 5x5 grid, each with four randomly positioned ships. The ship locations are concealed from the opposing player; while the player can view their own ships, the computer's ships remain hidden. To make a guess, input coordinates, comprising one row integer and one column integer separated by a space. After guessing, you will either hit or miss; duplicates of the same coordinates are not allowed. The ultimate aim of the game is to sink all of the opponent's ships.


The live link can be found here - [Battleships]()

![Site Mockup]()

Table of Contents

  * [Site Owner Goals](#site-owner-goals)
  * [Logic Flow](#logic-flow)  
  * [Features](#features)
    + [](#)
    + [](#)
    + [](#)
    + [](#)
    + [](#)
    + [Features Left to Implement](#features-left-to-implement)
  * [Testing](#testing)
    + [Validator Testing](#validator-testing)
      - [Python](#python)
      - [Accessibility](#accessibility)
    + [Input Testing](#input-testing)
    + [Game Testing](#game-testing)
    + [Fixed Bugs](#fixed-bugs)
      - [](#)
    + [Known Bugs](#known-bugs)
  * [Technologies Used](#technologies-used)
    + [Languages](#languages)
    + [Frameworks - Libraries - Programs Used](#frameworks---libraries---programs-used)
  * [Deployment](#deployment)
  * [Cloning](#cloning)
  * [Credits](#credits)
    + [Content](#content)
    + [Media](#media)
    + [Resources Used](#resources-used)
  * [Acknowledgments](#acknowledgments)


## How to Play
- Before starting the game, you need to choose a name consisting of at least three letters and press enter.
- Once your name is validated, your game board, consisting of five rows and five columns, will be displayed, with four ships randomly positioned on it.
- Your opponent, the computer, will also receive a game board with its ships hidden from you.
- Now, the game begins:
  - Make a guess by entering coordinates.
  - Input two integers ranging from 0 to 4, separated by a space. The top-left corner corresponds to row 0, column 0.
  - Press enter to submit your guess.
- Updated game boards will be printed and reveal the outcome of each guess:
  - If your guess hits a ship, a "*" will appear at the coordinates, accompanied by a "Hit!" message.
  - If your guess misses, an "X" will appear at the coordinates, along with a "Miss!" message.
- To win, either you or the computer must sink all of the opponent's ships.

## Logic Flow

![Flow Chart]()


## Features

### Title and Introduction Section
- The user is greeted by the title "Battleships," a welcome message and an input asking for their name.
- The "Battleships" title was created using Pyfiglet, which converts ASCII text into ASCII art fonts.
- Beneath the title, instructions on how to play are provided.
- Once the user is ready to play, they are prompted to enter their name. 

![Welcome Screen]()

- Strong data validation is applied to the username input. Users are required to input usernames consisting of a minimum of three characters. If the user enters invalid data, an error message prompt: "Fleet name must consist of at least three characters" and users will be prompted to re-enter their name.

### Game Features

## Data Model

## Testing

### PEP8 Testing

### Input Testing

### Other Game Testing

## Libraries and Technologies Used

### Python Libraries:

### Programs Used

## Known Bugs

## Fixed Bugs


### Missing * Display of Ship Hits on Player's Board 
Previously, when the computer successfully hit a ship, the * character indicating the hit was not displayed on the player's board.
To address this issue, I had to modify the print_board method in the Board class. Now, regardless of the value of the show parameter, hits on opponent ships are always displayed with the * character on the boards.

### Game Loop Prematurely Terminates
Previously, the game loop prematurely terminated before all four ships had been hit by either the player or the computer. The termination condition solely relied on the number of hits rather than ensuring all ships had been sunk. This leads to incorrect game endings, potentially declaring a winner before all ships are actually destroyed. To fix this bug, I had to update the play_game function to check if all ships on the opposing board had been sunk rather than just counting the number of hits. This ensures that the game continues until all ships on either board are destroyed, resolving the premature termination issue.

## Deployment

## Credits 

### Resources Used

## Acknowledgments