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
    draw_cloud(canvas, 400, 400)
    draw_cloud(canvas, 150, 300)
    draw_cloud(canvas, 650, 300)
    draw_sun(canvas, 650, 350, 100)

    draw_ground(canvas, scene_width, scene_height)
    draw_house(canvas, 350, 250)
    draw_house(canvas, 550, 325)

    # Call the finish_drawing function
    # in the draw2d.py library.
    finish_drawing(canvas)


# Define your functions such as
# draw_sky and draw_ground here.
def draw_sky(canvas, scene_width, scene_height):
    """Draw the sky as background."""
    draw_rectangle(canvas, 0, scene_height / 3,
    scene_width, scene_height, width=0, fill="sky blue")

def draw_ground(canvas, scene_width, scene_height):
    """Draw the ground as background."""
    draw_rectangle(canvas, 0, 0,
        scene_width, scene_height / 3, width=0, fill="darkGreen")

def draw_cloud(canvas, x, y):
    """Draw a cloud made of 3 ovals"""
    diameter = 50
    space = 0
    interval = diameter + space

    for i in range(3):
        draw_oval(canvas, x, y, x + diameter, y + diameter, fill="ghostWhite", outline="ghostWhite")
        x += interval

def draw_sun(canvas, x, y, diameter=50):
    """Draw a sun made of an oval"""
    draw_oval(canvas, x, y, x + diameter, y + diameter, fill="yellow1", outline="ghostWhite")

def draw_house(canvas, peak_x, peak_y):
    """Draw one house at location (peak_x, peak_y)"""

    # Compute the coordinates of the roof, base and door.
    roof_left  = peak_x - 70
    roof_right = peak_x + 70
    roof_bottom = peak_y - 120

    base_left  = peak_x - 50
    base_right = peak_x + 50
    base_bottom = peak_y - 200

    door_left  = peak_x - 15
    door_right = peak_x + 15
    door_bottom = peak_y - 200
    door_center = base_bottom + 50
    

    # Draw the house base.
    draw_rectangle(canvas, base_left, base_bottom, base_right, roof_bottom, fill="khaki1")

    # Draw the house roof.
    draw_polygon(canvas, roof_left, roof_bottom, peak_x, peak_y, roof_right, roof_bottom, fill="tomato2")
    
    #Draw door of house
    draw_rectangle(canvas, door_left, door_bottom, door_right, door_center, fill="tomato2")

def draw_grid(canvas, width, height, interval, color="blue"):
    """Draw a grid to see coordinates for x and y on window"""
    # Draw a vertical line at every x interval.
    label_y = 15
    for x in range(interval, width, interval):
        draw_line(canvas, x, 0, x, height, fill=color)
        draw_text(canvas, x, label_y, f"{x}", fill=color)

    # Draw a horizontal line at every y interval.
    label_x = 15
    for y in range(interval, height, interval):
        draw_line(canvas, 0, y, width, y, fill=color)
        draw_text(canvas, label_x, y, f"{y}", fill=color)

# Call the main function so that
# this program will start executing.
main()