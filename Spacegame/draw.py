import time

from blink import get_random_blink
from spaceship import animate_spaceship
from curses_tools import draw_frame, get_frame
from curses_tools import get_frames_size, get_controls_row_column

BLINK_CNT = 10
SPEED = 10
ROW_START, COLUMN_START = 1, 1


def draw(canvas):
    canvas.nodelay(True)
    canvas.border()

    frame1 = get_frame('rocket_frame_1.txt')
    frame2 = get_frame('rocket_frame_2.txt')
    row_frame, column_frame = get_frames_size(frame1, frame2)
    max_row, max_column = canvas.getmaxyx()
    row, column = ROW_START, COLUMN_START
    coroutines = [get_random_blink(canvas) for _ in range(BLINK_CNT)]
    coroutines.append(animate_spaceship(canvas, frame1, frame2, row, column))

    while True:
        row_new, column_new = get_controls_row_column(
            canvas,
            row, column,
            row_frame, column_frame,
            max_row, max_column,
            speed=SPEED
        )
        if (row, column) != (row_new, column_new):
            draw_frame(canvas, row, column, frame1, negative=True)
            draw_frame(canvas, row, column, frame2, negative=True)
            row, column = row_new, column_new
            coroutines[-1] = animate_spaceship(canvas,
                                               frame1,
                                               frame2,
                                               row,
                                               column)

        for coroutine in coroutines.copy():
            coroutine.send(None)
            canvas.refresh()

        time.sleep(0.1)
