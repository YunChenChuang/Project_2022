"""
File: bouncing_ball.py
Name: AO Chuang
"""

from campy.graphics.gobjects import GOval
from campy.graphics.gwindow import GWindow
from campy.gui.events.timer import pause
from campy.gui.events.mouse import onmouseclicked

VX = 5  # Horizontal velocity of ball
DELAY = 10  # Animation pause (ms)
GRAVITY = 1
SIZE = 20  # Size of ball
REDUCE = 0.9  # The percentage of velocity reduced, after bouncing from the ground
START_X = 30  # initial y-coordinate of the ball
START_Y = 40  # initial y-coordinate of the ball
REPEAT_LIMIT = 3  # Maximum number of the bouncing loops, which is the ball will stick on windows after repeat N times.

window = GWindow(800, 500, title='bouncing_ball.py')  # build the window

ball = GOval(SIZE, SIZE)  # create the ball

# Global Variable
bouncing_count = 0  # count the number of bouncing loops


def main():
    """
    This program simulates a bouncing ball at (START_X, START_Y)
    that has VX as x velocity and 0 as y velocity. Each bounce reduces
    y velocity to REDUCE of itself.
    """
    # put the ball on window
    ball.filled = True
    ball.fill_color = 'black'
    window.add(ball, START_X, START_Y)

    # click to start bouncing
    onmouseclicked(bouncing)


def bouncing(mouse):
    vy = 0  # Vertical velocity of ball
    global bouncing_count
    if bouncing_count < REPEAT_LIMIT:  # ball will repeat bouncing loop 'REPEAT_LIMIT' times, which is 3 in this case
        bouncing_count += 1
        while ball.x + SIZE < window.width:  # loop will end when ball bouncing over the right edge of window
            vy += GRAVITY  # Vertical velocity effect by Gravity
            ball.move(VX, vy)
            pause(DELAY)  # pause the animation

            if (ball.y + SIZE) >= window.height:  # when ball touched ground
                if vy >= 0:  # velocity will always be positive
                    vy = -vy * REDUCE  # vertical velocity changes when touch the ground

        window.add(ball, START_X, START_Y)  # put ball to the initial position


if __name__ == "__main__":
    main()
