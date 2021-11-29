"""
File: draw_line.py
Name: AO Chuang
-------------------------
TODO:
"""

from campy.graphics.gobjects import GOval, GLine
from campy.graphics.gwindow import GWindow
from campy.gui.events.mouse import onmouseclicked


# constant control the diameter of the window
WINDOW_WIDTH = 1000
WINDOW_HEIGHT = 1000

# constant control the radius of the circle
SIZE = 10

# constant controls the pause time of the animation
DELAY = 1000

# build the window
window = GWindow(width=WINDOW_WIDTH, height=WINDOW_HEIGHT, title='Draw line')

# global variables
point = 0
circle = GOval(SIZE, SIZE)


def main():
    """
    This program creates lines on an instance of GWindow class.
    There is a circle indicating the user’s first click. A line appears
    at the condition where the circle disappears as the user clicks
    on the canvas for the second time.
    """
    onmouseclicked(point_count)


def point_count(event):
    global point  # recall the global variables
    point += 1  # 'point' will count the number of clicks
    x = event.x  # the x-coordinate of click
    y = event.y  # the x-coordinate of click

    if point % 2 != 0:  # point is odd, the 1st click
        window.add(circle, x=x - SIZE / 2, y=y - SIZE / 2)  # show 'circle' on where was clicked
    else:  # point is even, the 2nd click
        line = GLine(circle.x, circle.y, x, y)  # creating a line from the 1st click to the 2nd click
        window.remove(circle)  # remove the circle created at the 1st clicked
        window.add(line)  # show 'line' on window


if __name__ == "__main__":
    main()
