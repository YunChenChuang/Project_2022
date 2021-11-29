"""
stanCode Breakout Project
Adapted from Eric Roberts's Breakout by
Sonja Johnson-Yu, Kylie Jue, Nick Bowman,
and Jerry Liao.

YOUR DESCRIPTION HERE
"""

from campy.gui.events.timer import pause
from breakoutgraphics import BreakoutGraphics
from campy.graphics.gobjects import GLabel

FRAME_RATE = 1000 / 120 # 120 frames per second
NUM_LIVES = 3			# Number of attempts


def main():
    graphics = BreakoutGraphics()
    lives = NUM_LIVES

    life = GLabel(f'LIVES: {lives}')
    life.font = 'SansSerif-20'
    graphics.window.add(life, graphics.ball.height, graphics.window.height)
    brick_num = graphics.brick_num

    while True:

        if (lives > 0) and (brick_num > 0):

            # reset ball to the center of window
            window_x_center = (graphics.window.width - graphics.ball.width)/2
            window_y_center = (graphics.window.height - graphics.ball.height)/2

            # reset variables in the being of each life
            graphics.window.add(graphics.ball, window_x_center, window_y_center)
            print('lives = ', lives)
            graphics.game_starter = 0
            dx = 0
            dy = 0

            while True:

                pause(FRAME_RATE)
                if brick_num == 0:
                    break

                if graphics.game_starter == 1:  # reset dx, dy when the first click
                    dx = graphics.dx
                    dy = graphics.dy
                    graphics.game_starter += 1

                graphics.ball.move(dx, dy)
                print('dx, dy = ', dx, dy)

                x = int(graphics.ball.x)
                y = int(graphics.ball.y)
                x_rr = int(graphics.ball.x + graphics.ball.width)
                y_rr = int(graphics.ball.y + graphics.ball.height)

                top_border = 0
                bottom_border = graphics.window.height - graphics.ball.height/2
                right_border = 0
                left_border = graphics.window.width - graphics.ball.width/2

                x_bounce = False
                y_bounce = False

                #  bouncing
                if x <= right_border or x >= left_border:
                    x_bounce = True
                if y <= top_border:
                    y_bounce = True
                elif y >= bottom_border:
                    lives -= 1
                    life.text = f'LIVES: {lives}'
                    pause(FRAME_RATE*100)
                    break

                none_count = 0
                not_none_count = 0
                collide_at_x = 0
                collide_at_y = 0

                for i in range(x, x_rr+1, graphics.ball.width):
                    for j in range(y, y_rr+1, graphics.ball.height):

                        maybe_obj = graphics.window.get_object_at(i, j)

                        if maybe_obj is not None:
                            not_none_count += 1
                            collide_at_x = i
                            collide_at_y = j

                if not_none_count > 0:
                    collide_obj = graphics.window.get_object_at(collide_at_x, collide_at_y)

                    if collide_obj == graphics.paddle:
                        if dy > 0:
                            y_bounce = True
                    elif collide_obj is not life:
                        graphics.window.remove(collide_obj)
                        brick_num -= 1
                        y_bounce = True

                if x_bounce is True:
                    dx = -dx
                if y_bounce is True:
                    dy = -dy

        if lives == 0:
            lose = GLabel(f'YOU  LOSE!!!!')
            lose.font = 'SansSerif-50'
            lose_w = lose.width
            lose.color = 'red'
            graphics.window.add(lose, (graphics.window.width - lose_w)/2 , graphics.window.height/2)
            break

        elif brick_num == 0:
            win = GLabel(f'YOU  WIN')
            win.font = 'SansSerif-50'
            win_w = win.width
            win.color = 'gold'
            graphics.window.add(win, (graphics.window.width - win_w) / 2, graphics.window.height / 2)
            break


if __name__ == '__main__':
    main()
