"""
File: bouncing_ball.py
Name: AO Chuang
"""

from campy.graphics.gobjects import GOval
from campy.graphics.gwindow import GWindow
from campy.gui.events.timer import pause
from campy.gui.events.mouse import onmouseclicked

VX = 5
DELAY = 10
GRAVITY = 1
SIZE = 20
REDUCE = 0.9
START_X = 30
START_Y = 40
REPEAT = 3  # limitation of the number of the bouncing loops

# build the window
window = GWindow(800, 500, title='bouncing_ball.py')

# create the ball
ball = GOval(SIZE, SIZE)

# global variable
vy = 0  # the Y-velocity
n = 0  # 'n' will count the umber of bouncing loops


def main():
    """
    This program simulates a bouncing ball at (START_X, START_Y)
    that has VX as x velocity and 0 as y velocity. Each bounce reduces
    y velocity to REDUCE of itself.
    """
    # set the ball on window
    ball.filled = True
    ball.fill_color = 'black'
    window.add(ball, START_X, START_Y)

    # click to start bouncing
    onmouseclicked(bouncing)


def bouncing(mouse):
    global vy
    global n
    if ball.x == START_X and ball.y == START_Y:  # ball will start bouncing only when it came back to initial position
        if n < REPEAT:  # ball will bouncing 'REPEAT' times, which is 3 in this case
            n += 1  # 'n' will count the umber of bouncing loops
            while True:
                vy += GRAVITY  # 'vy' is affected by 'GRAVITY'
                ball.move(VX, vy)  # moving the ball with the given X-velocity and Y-velocity
                pause(DELAY)  # 'DELAY' is the speed of the animation

                if (ball.y + SIZE) >= window.height:  # when ball touched ground
                    if vy >= 0:  # 'vy' will always be positive
                        vy = -vy * REDUCE  # velocity changes after touched the ground

                if ball.x + SIZE >= window.width:  # when ball went out of window
                    break  # stop bouncing
        window.add(ball, START_X, START_Y)  # put ball to the initial position


if __name__ == "__main__":
    main()
