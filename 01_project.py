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
