Number Guessing Game
Welcome to the Number Guessing Game! This is a simple command-line game where the player tries to guess a randomly generated number within a specified range.

Features
Random number generation within a user-defined range.
Player has a limited number of attempts to guess the number.
Provides feedback whether the guess is too high, too low, or correct.
Option to play again after a game is over.
Prerequisites
Python 3.x installed on your system.
How to Run the Game
Clone the Repository:

bash
Copy code
git clone https://github.com/yourusername/number-guessing-game.git
cd number-guessing-game
Run the Game:

bash

python number_guessing_game.py
How to Play
When you start the game, you will be prompted to enter the range within which the number will be generated.
You will then be prompted to guess the number within a specified number of attempts.
After each guess, you will receive feedback indicating whether your guess is too high, too low, or correct.
If you guess the number within the allowed attempts, you win! Otherwise, you lose.
After the game ends, you have the option to play again or exit.
Example
mathematica

Welcome to the Number Guessing Game!
Enter the lower bound of the range: 1
Enter the upper bound of the range: 100
I have generated a number between 1 and 100. You have 10 attempts to guess it.

Enter your guess: 50
Too high!

Enter your guess: 25
Too low!

Enter your guess: 37
Correct! You guessed the number in 3 attempts.

Do you want to play again? (yes/no): no
Thank you for playing!
Code Overview
The main functionality is contained in number_guessing_game.py. Below is a brief description of the key sections:

Imports:

python
import random
Function to Get User Input:
This function ensures valid input for the range and guesses.

python
def get_valid_input(prompt, lower_bound=None, upper_bound=None):
    ...
Main Game Loop:
This function contains the logic for running the game.

python
def play_game():
    ...
Program Entry Point:
The game starts here, asking the player if they want to play again after each game.

python
if __name__ == "__main__":
    while True:
        play_game()
        ...
Contributing
If you'd like to contribute to the project, please fork the repository and use a feature branch. Pull requests are warmly welcome.

License
This project is licensed under the MIT License - see the LICENSE file for details.

Contact
If you have any questions or feedback, feel free to contact me at roobikaviswanathan@gmail.com.
