Snake, Water, Gun Game



This is a simple Python implementation of the classic Snake, Water, Gun game. It mimics the popular "Rock, Paper, Scissors" game, with the following rules:



Snake beats Water.
Water beats Gun.
Gun beats Snake.


The game randomly assigns a choice to the computer and prompts the user to input their choice. The winner is determined based on the game's rules.

Rules of the Game


1 for Snake


-1 for Water


0 for Gun


Winning Conditions:


Snake (1) vs. Water (-1) → Snake wins


Water (-1) vs. Gun (0) → Water wins


Gun (0) vs. Snake (1) → Gun wins

If both the player and the computer choose the same option, it’s a draw.



How to Play


User Input: The user is prompted to enter their choice:

's' for Snake.

'w' for Water.

'g' for Gun.

Computer's Choice: The computer's choice is fixed in this version (set to -1, which represents Water), but it can be randomized in the future

.

Result: The program evaluates the user's choice against the computer's choice and prints whether the user won, lost, or the game is a draw.



Sample Gameplay


Input:


rust



Copy code
Enter your choice (s for snake, w for water, g for gun): 



Output:



Copy code
You win!


Clone or download the Python file.

Run the script using Python:

bash
Copy code
python snake_water_gun.py
Follow the on-screen prompts to play the game.# number_1project
