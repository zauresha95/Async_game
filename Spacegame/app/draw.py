import time
import random
from blink import get_random_blink
from obstacles import show_obstacles
from spaceship import animate_spaceship
from space_garbage import fill_orbit_with_garbage
from params import obstacles, BLINK_CNT, year
from game_scenario import draw_year


def draw(canvas):
    canvas.nodelay(True)
    canvas.border()
    # get the height and width of the window, that less than the border to 1
    rows, columns = canvas.getmaxyx()
    max_row, max_column = rows - 1, columns - 1
    #canvas.subwin(0, 0)
    coroutines = [
        get_random_blink(
            canvas,
            max_row,
            max_column,
            offset_tics=random.randint(0, BLINK_CNT)
        )
        for _ in range(BLINK_CNT)
    ]

    coroutines.append(
        animate_spaceship(
            canvas,
            coroutines,
            max_row,
            max_column
        )
    )

    coroutines.append(
            fill_orbit_with_garbage(
                canvas,
                coroutines,
                max_column)
    )

    coroutines.append(draw_year(canvas, max_row, year))

    while True:
        for coroutine in coroutines.copy():
            try:
                coroutine.send(None)
            except StopIteration:
                coroutines.remove(coroutine)

        canvas.refresh()
        time.sleep(0.1)