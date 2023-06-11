import asyncio
from curses_tools import draw_frame, get_frame
from curses_tools import get_frame_size, read_controls


async def animate_spaceship(canvas, max_row, max_column, speed):
    frame1 = get_frame('rocket_frame_1.txt')
    frame2 = get_frame('rocket_frame_2.txt')
    row_frame1, column_frame1 = get_frame_size(frame1)
    row_frame2, column_frame2 = get_frame_size(frame2)
    row_frame = max(row_frame1, row_frame2)
    column_frame = max(column_frame1, column_frame2)

    max_row, max_column = max_row - row_frame, max_column - column_frame

    # get the start position
    row = max_row // 2 + 1
    column = max_column // 2 + 1

    draw_frame(canvas, row, column, frame1)
    await asyncio.sleep(0)

    while True:
        draw_frame(canvas, row, column, frame1, negative=True)
        row, column = get_controls_row_column(
            canvas,
            row, column,
            max_row, max_column,
            speed
        )
        draw_frame(canvas, row, column, frame2)
        await asyncio.sleep(0)

        draw_frame(canvas, row, column, frame2, negative=True)

        row, column = get_controls_row_column(
            canvas,
            row, column,
            max_row, max_column,
            speed
        )
        draw_frame(canvas, row, column, frame1)
        await asyncio.sleep(0)


def get_controls_row_column(canvas,
                            row, column,
                            max_row, max_column,
                            speed):
    row_step, column_step, space = read_controls(canvas)
    row = row + row_step * speed
    column = column + column_step * speed
    return max(1, min(row, max_row)), max(1, min(column, max_column))
