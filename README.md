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


Turtle Graphics Spiral Pattern
This Python project generates a vibrant, rotating spiral using the turtle graphics library. The design features smooth color transitions and a growing spiral pattern, creating a mesmerizing visual effect.

How it Works:
The turtle draws a spiral with each step growing larger than the previous one.
Colors change dynamically based on the HLS (Hue, Lightness, Saturation) color space, ensuring smooth and continuous transitions.
The turtle turns at a specific angle after each step, which creates the spiral effect.
Features:
Color Transitions: Color shifts continuously using the HLS color model.
Spiral Growth: The distance traveled by the turtle increases with each step, causing the pattern to expand outward.
Customizable: You can modify the size, speed, and color parameters to create different spiral effects.
Code:
python
Copy code
from turtle import *
import colorsys

# Setup turtle environment
bgcolor('black')
speed(0)  # Fastest drawing speed
pensize(2)
tracer(10)

def draw_spiral():
    h = 0  # Initial hue value
    n = 100  # Total number of colors
    for i in range(300):
        c = colorsys.hls_to_rgb(h, 0.5, 1)  # Generate RGB color from HLS
        h += 1 / n  # Increment hue value for smooth transitions
        color(c)  # Set the pen color
        forward(i * 2)  # Move forward, increasing the step
        right(59)  # Turn right to create a spiral effect


# Run the function to start drawing

draw_spiral()

done()

Instructions:

Install Python and make sure the turtle library is available (it comes pre-installed with Python).

Run the script in any Python environment.

Observe as a colorful spiral pattern is generated on the screen.

Customization:

Colors: Adjust the h and n values in colorsys.hls_to_rgb() to alter the color range and transiti
ons.
Spiral Shape: Modify the right(59) angle or the forward(i * 2) distance to change the shape and style of the spiral.

Speed and Size: Adjust the speed() or pensize() to modify the drawing speed and thickness.

Example Output:

This script will generate a continuously expanding spiral with a vibrant color gradient.





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



    Turtle Graphics - Circular Pattern Animation
    
This project uses Python's turtle library to generate a mesmerizing circular pattern animation with dynamic colors. The pattern continuously changes as the 
turtle moves, creating a beautiful and colorful design against a black background.


Requirements

To run this project, you need:


Python 3.x
turtle library (pre-installed with Python)
colorsys library (to handle the color transitions)
Installation
Clone the repository:

bash
Copy code
git clone https://github.com/zakiraziz/number_1project.git
Navigate to the project directory:

bash
Copy code
cd number_1project
Run the Python script:

bash
Copy code
python 03_project.py
Code Explanation
Background Color: The background is set to black using bgcolor('black'), which makes the colorful design stand out.

Speed: The animation is sped up using tracer(100) to ensure that the drawing process is fast and smooth.

Drawing Logic:

The draw function creates circular patterns using turtle's circle method. The radius of the circles changes based on the loop, creating a growing effect.
The turtle moves at angles determined by ang and n to generate symmetrical patterns.
Color Transition: The colors are dynamically generated using hsv_to_rgb(h, 1, 1), where the hue (h) is continuously incremented to smoothly transition between colors.

Main Loop: The for loop runs 500 times, with each iteration drawing a combination of circles at different angles and sizes, creating a vibrant, evolving pattern.

Output Example
The program will output a stunning, spiraling circular pattern with a variety of colors blending into each other, as shown below:



(Add a screenshot or GIF of the program's output here)





done()

