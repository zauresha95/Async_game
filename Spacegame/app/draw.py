import time
import random
from blink import get_random_blink
from fire_animation import fire
from spaceship import animate_spaceship

BLINK_CNT = 100
SPEED = 1


def draw(canvas):
    canvas.nodelay(True)
    canvas.border()
    # get the height and width of the window, that less than the border to 1
    rows, columns = canvas.getmaxyx()
    max_row, max_column = rows - 1, columns - 1

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
        fire(
            canvas,
            start_row=max_row//2,
            start_column=max_column//2,
            max_row=max_row,
            max_column=max_column
        )
    )
    coroutines.append(
        animate_spaceship(
            canvas,
            max_row,
            max_column,
            SPEED
        )
    )

    while True:
        for coroutine in coroutines.copy():
            try:
                coroutine.send(None)
            except StopIteration:
                coroutines.remove(coroutine)

        canvas.refresh()
        time.sleep(0.1)
