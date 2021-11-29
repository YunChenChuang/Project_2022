"""
stanCode Breakout Project
Adapted from Eric Roberts's Breakout by
Sonja Johnson-Yu, Kylie Jue, Nick Bowman, 
and Jerry Liao

YOUR DESCRIPTION HERE
"""
from campy.graphics.gwindow import GWindow
from campy.graphics.gobjects import GOval, GRect
from campy.gui.events.mouse import onmouseclicked, onmousemoved
from campy.graphics.gcolor import GColor
import random

BRICK_SPACING = 5      # Space between bricks (in pixels). This space is used for horizontal and vertical spacing.
BRICK_WIDTH = 40       # Height of a brick (in pixels).
BRICK_HEIGHT = 15      # Height of a brick (in pixels).
BRICK_ROWS = 10        # Number of rows of bricks.
BRICK_COLS = 10        # Number of columns of bricks.
BRICK_OFFSET = 50      # Vertical offset of the topmost brick from the window top (in pixels).
BALL_RADIUS = 20       # Radius of the ball (in pixels).
PADDLE_WIDTH = 75      # Width of the paddle (in pixels).
PADDLE_HEIGHT = 15     # Height of the paddle (in pixels).
PADDLE_OFFSET = 50     # Vertical offset of the paddle from the window bottom (in pixels).

INITIAL_Y_SPEED = 7  # Initial vertical speed for the ball.
MAX_X_SPEED = 5        # Maximum initial horizontal speed for the ball.


class BreakoutGraphics:

    def __init__(self, ball_radius = BALL_RADIUS, paddle_width = PADDLE_WIDTH,
                 paddle_height = PADDLE_HEIGHT, paddle_offset = PADDLE_OFFSET,
                 brick_rows = BRICK_ROWS, brick_cols = BRICK_COLS,
                 brick_width = BRICK_WIDTH, brick_height = BRICK_HEIGHT,
                 brick_offset = BRICK_OFFSET, brick_spacing = BRICK_SPACING,
                 title='Breakout'):

        # Create a graphical window, with some extra space
        window_width = brick_cols * (brick_width + brick_spacing) - brick_spacing
        window_height = brick_offset + 3 * (brick_rows * (brick_height + brick_spacing) - brick_spacing)
        self.window = GWindow(width=window_width, height=window_height, title=title)

        # Create a paddle
        self.paddle = GRect(paddle_width, paddle_height)
        self.paddle.filled = True
        self.paddle.color = GColor(50, 60, 80)
        self.paddle.fill_color = GColor(50, 60, 80)
        self.window.add(self.paddle, x=(window_width - paddle_width)/2, y=window_height - (paddle_offset + paddle_height))

        # Center a filled ball in the graphical window
        self.ball = GOval(ball_radius, ball_radius)
        self.ball.filled = True
        self.ball.color = GColor(140, 140, 150)
        self.ball.fill_color = GColor(140, 140, 150)
        self.window.add(self.ball, x=(window_width - ball_radius)/2, y=(window_height - ball_radius)/2)

        # Default initial velocity for the ball
        self.__dy = 0
        self.__dx = 0

        # Initialize our mouse listeners
        self.game_starter = 0
        onmouseclicked(self.game_start)
        onmousemoved(self.paddle_move)

        # Draw bricks
        self.brick_num = brick_cols * brick_rows
        x = 0
        y = brick_offset
        for col in range(brick_cols):  # the number of columns will be 'brick_cols'
            for row in range(brick_rows):  # the number of row will be 'brick_rows'
                self.brick = GRect(brick_width, brick_height)  # create brick with given width and height
                self.brick.filled = True

                color_count = col / brick_cols
                if color_count <= 0.1:
                    self.brick.color = GColor(150, 170, 250)
                    self.brick.fill_color = GColor(150, 170, 250)
                elif color_count <= 0.3:
                    self.brick.color = GColor(120, 140, 225)
                    self.brick.fill_color = GColor(120, 140, 225)
                elif color_count <= 0.5:
                    self.brick.color = GColor(80, 100, 190)
                    self.brick.fill_color = GColor(80, 100, 190)
                elif color_count <= 0.7:
                    self.brick.color = GColor(50, 70, 150)
                    self.brick.fill_color = GColor(50, 70, 150)
                else:
                    self.brick.color = GColor(20, 40, 120)
                    self.brick.fill_color = GColor(20, 40, 120)

                self.window.add(self.brick, x=x, y=y)  # add 'brick' to window
                x += brick_width + brick_spacing

            x = 0  # clean x-coordinate
            y += brick_height + brick_spacing

    def paddle_move(self, event):
        right_edge = self.paddle.width / 2
        left_edge = self.window.width - self.paddle.width / 2

        if (event.x >= right_edge) and (event.x <= left_edge):
            x = event.x - self.paddle.width / 2
            y = self.paddle.y
            self.window.add(self.paddle, x, y)

    def game_start(self, _):
        self.game_starter += 1
        self.__dy = INITIAL_Y_SPEED
        self.__dx = random.randrange(1, MAX_X_SPEED)
        if random.random() > 0.5:
            self.__dx = -self.__dx

    @property
    def dx(self):
        return self.__dx

    @property
    def dy(self):
        return self.__dy


