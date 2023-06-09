import time
from blink import get_random_blink
from fire_animation import fire
from spaceship import animate_spaceship

BLINK_CNT = 100
SPEED = 1
ROW_BOUND, COLUMN_BOUND = 1, 1


def draw(canvas):
    canvas.nodelay(True)
    canvas.border()
    coroutines = [
        get_random_blink(canvas, ROW_BOUND, COLUMN_BOUND)
        for _ in range(BLINK_CNT)
    ]
    coroutines.append(fire(canvas))

    while True:
        for coroutine in coroutines.copy():
            try:
                coroutine.send(None)
            except StopIteration:
                coroutines.remove(coroutine)
                coroutines.append(animate_spaceship(canvas,
                                                    ROW_BOUND, COLUMN_BOUND,
                                                    SPEED))
        canvas.refresh()
        time.sleep(0.1)
