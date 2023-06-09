import asyncio
from curses_tools import draw_frame, get_frame
from curses_tools import get_frame_size, read_controls


async def animate_spaceship(canvas, row_bound, column_bound, speed):
    frame1 = get_frame('rocket_frame_1.txt')
    frame2 = get_frame('rocket_frame_2.txt')
    row_frame1, column_frame1 = get_frame_size(frame1)
    row_frame2, column_frame2 = get_frame_size(frame2)

    max_row, max_column = canvas.getmaxyx()
    row = (max_row - row_frame1) // 2
    column = (max_column - column_frame1) // 2

    draw_frame(canvas, row, column, frame1)
    await asyncio.sleep(0)

    while True:
        draw_frame(canvas, row, column, frame1, negative=True)
        row, column = get_controls_row_column(
            canvas,
            row, column,
            row_frame2, column_frame2,
            max_row, max_column,
            row_bound, column_bound,
            speed
        )
        draw_frame(canvas, row, column, frame2)
        await asyncio.sleep(0)

        draw_frame(canvas, row, column, frame2, negative=True)

        row, column = get_controls_row_column(
            canvas,
            row, column,
            row_frame1, column_frame1,
            max_row, max_column,
            row_bound, column_bound,
            speed
        )
        draw_frame(canvas, row, column, frame1)
        await asyncio.sleep(0)


def get_controls_row_column(canvas, row,
                            column, row_frame,
                            column_frame,
                            max_row, max_column,
                            row_bound, column_bound,
                            speed):
    row_step, column_step, space = read_controls(canvas)
    if row_step in [1, -1] or column_step in [1, -1]:
        row_new = row + row_step * speed
        column_new = column + column_step * speed
        max_row_bound = max_row - row_frame - row_bound
        max_column_bound = max_column - column_frame - column_bound
        if (row_bound <= row_new <= max_row_bound and
                column_bound <= column_new <= max_column_bound):
            return row_new, column_new

    return row, column
