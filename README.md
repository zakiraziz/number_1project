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
Follow the on-screen prompts to play the game.# number_1project\




Turtle Graphics Color Pattern 

This Python project creates a colorful geometric pattern using the turtle graphics library. It draws shapes with dynamic color transitions, forming an evolving 
spiral-like design. The colors smoothly shift using the HSV color model, making the design vibrant and dynamic.



How it Works:

The turtle moves in a loop, drawing shapes at varying angles while changing colors.

The colorsys.hsv_to_rgb() function is used to convert HSV values to RGB for smooth color transitions.


The turtle resets its position to the center after each iteration, gradually rotating to create a spiral effect.



Features:


Color Transitions: Smooth transitions using the HSV color space.


Geometric Design: Repeated shapes with varying angles, creating a spiral pattern.


Customizable: You can modify the speed, size, and colors to create different patterns.


Code:

python

Copy code

from turtle import *

import colorsys

#

# Main drawing loop

for j in range(300):

    fun()
    goto(0, 0)  # Return to center
    
    rt(10)  # Rotate to create spiral effect



done()

Instructions:

Install Python and make sure you have the turtle library installed (it comes pre-installed with Python).

Run the script in a Python environment.



Watch the turtle draw a colorful, spiraling pattern.

Customization:

Adjust the pensize() to change the line thickness.

Modify the values in fd() and rt() to create different shapes and effects.

Change the speed of drawing by modifying speed().

