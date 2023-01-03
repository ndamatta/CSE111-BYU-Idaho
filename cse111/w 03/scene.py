# Import the functions from the Draw 2-D library
# so that they can be used in this program.
from draw2d import \
    start_drawing, draw_line, draw_oval, draw_arc, \
    draw_rectangle, draw_polygon, draw_text, finish_drawing


def main():
    # Width and height of the scene in pixels
    scene_width = 800
    scene_height = 500

    # Call the start_drawing function in the draw2d.py
    # library which will open a window and create a canvas.
    canvas = start_drawing("Scene", scene_width, scene_height)



    # Call your drawing functions such
    # as draw_sky and draw_ground here.
    draw_sky(canvas, scene_width, scene_height)
    draw_ground(canvas, scene_width, scene_height)    


    # Call the finish_drawing function
    # in the draw2d.py library.
    finish_drawing(canvas)


# Define your functions such as
# draw_sky and draw_ground here.
def draw_sky(canvas, scene_width, scene_height):
    """Draw the sky and all the objects in the sky."""
    draw_rectangle(canvas, 0, scene_height / 3,
    scene_width, scene_height, width=0, fill="sky blue")

    #Draw clouds
    draw_cloud(canvas, 400, 400)
    draw_cloud(canvas, 300, 300)

    #Draw sun
    draw_sun(canvas, 500, 150)

def draw_ground(canvas, scene_width, scene_height):
    """Draw the ground and all the objects on the ground."""
    draw_rectangle(canvas, 0, 0,
        scene_width, scene_height / 3, width=0, fill="darkGreen")

def draw_cloud(canvas, x, y):
    diameter = 50
    space = 0
    interval = diameter + space

    for i in range(3):
        draw_oval(canvas, x, y, x + diameter, y + diameter, fill="ghostWhite", outline="ghostWhite")
        x += interval

def draw_sun(canvas, x, y):
    diameter = 50
    draw_oval(canvas, x, y, x + diameter, y + diameter, fill="yellow1", outline="ghostWhite")

# Call the main function so that
# this program will start executing.
main()