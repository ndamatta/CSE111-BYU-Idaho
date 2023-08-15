# This program uses the Draw 2-D library to create a simple scene
# with a sky, clouds, and a sun above a ground.
# It defines functions to draw different elements of the scene and then uses these functions in the main program.

# Import necessary functions from the Draw 2-D library.
from draw2d import \
    start_drawing, draw_line, draw_oval, draw_arc, \
    draw_rectangle, draw_polygon, draw_text, finish_drawing

# Define the main function that drives the program's execution.
def main():
    # Set the width and height of the scene in pixels.
    scene_width = 800
    scene_height = 500

    # Call start_drawing to create a canvas.
    canvas = start_drawing("Scene", scene_width, scene_height)

    # Call the functions to draw the sky and the ground.
    draw_sky(canvas, scene_width, scene_height)
    draw_ground(canvas, scene_width, scene_height)

    # Call finish_drawing to complete the canvas.
    finish_drawing(canvas)

# Draw the sky and objects in the sky.
def draw_sky(canvas, scene_width, scene_height):
    """Draw the sky and objects in the sky."""
    # Draw the sky background using a filled rectangle.
    draw_rectangle(canvas, 0, scene_height / 3, scene_width, scene_height, width=0, fill="sky blue")

    # Draw clouds using the draw_cloud function.
    draw_cloud(canvas, 400, 400)
    draw_cloud(canvas, 300, 300)

    # Draw the sun using the draw_sun function.
    draw_sun(canvas, 500, 150)

# Draw the ground and objects on the ground.
def draw_ground(canvas, scene_width, scene_height):
    """Draw the ground and objects on the ground."""
    # Draw the ground using a filled rectangle.
    draw_rectangle(canvas, 0, 0, scene_width, scene_height / 3, width=0, fill="darkGreen")

# Draw a cloud at the specified position (x, y).
def draw_cloud(canvas, x, y):
    diameter = 50
    space = 0
    interval = diameter + space

    for i in range(3):
        # Draw oval shapes to represent clouds.
        draw_oval(canvas, x, y, x + diameter, y + diameter, fill="ghostWhite", outline="ghostWhite")
        x += interval

# Draw the sun at the specified position (x, y).
def draw_sun(canvas, x, y):
    diameter = 50
    # Draw an oval shape to represent the sun.
    draw_oval(canvas, x, y, x + diameter, y + diameter, fill="yellow1", outline="ghostWhite")

# Call the main function to start the program's execution.
if __name__ == "__main__":
    main()
