import asyncio
from curses_tools import draw_frame, get_frame
from curses_tools import get_frame_size, read_controls
from fire_animation import fire_by_space
from physics import update_speed
from sleep import sleep
from gameover import show_gameover


async def animate_spaceship(canvas, coroutines, max_row, max_column):
    frame1 = get_frame('rocket_frame_1.txt')
    frame2 = get_frame('rocket_frame_2.txt')
    row_frame1, column_frame1 = get_frame_size(frame1)
    row_frame2, column_frame2 = get_frame_size(frame2)
    row_frame = max(row_frame1, row_frame2)
    column_frame = max(column_frame1, column_frame2)
    row_speed = column_speed = 0
    max_space_row = max_row - row_frame
    max_space_column = max_column - column_frame
    # get the start position
    row = max_row // 2 + 1
    column = max_column // 2 + 1
    params = {
        'row': row,
        'column': column,
        'row_speed': row_speed,
        'column_speed': column_speed
    }
    draw_frame(canvas, row, column, frame1)
    await sleep(2)

    while True:

        row_step, column_step, space = read_controls(canvas)
        draw_frame(
            canvas,
            params['row'], params['column'],
            frame1,
            negative=True
        )
        params = get_controls_row_column(
            row_step, column_step,
            max_space_row, max_space_column,
            **params
        )
        draw_frame(
            canvas,
            params['row'], params['column'],
            frame2
        )
        coroutines.append(
            fire_by_space(
                canvas, space,
                column_frame,
                params
            )
        )
        await show_gameover(
            canvas,
            params['row'], params['column'],
            row_frame, column_frame, frame2
        )

        row_step, column_step, space = read_controls(canvas)
        coroutines.append(
            fire_by_space(
                canvas, space, column_frame, params
            )
        )
        await asyncio.sleep(0)

        row_step, column_step, space = read_controls(canvas)
        draw_frame(
            canvas,
            params['row'], params['column'],
            frame2, negative=True
        )
        params = get_controls_row_column(
            row_step, column_step,
            max_space_row, max_space_column,
            **params
        )
        draw_frame(
            canvas,
            params['row'], params['column'],
            frame1
        )
        coroutines.append(
            fire_by_space(
                canvas, space, column_frame, params
            )
        )
        await asyncio.sleep(0)

        row_step, column_step, space = read_controls(canvas)
        coroutines.append(
            fire_by_space(
                canvas, space, column_frame, params
            )
        )
        await show_gameover(
            canvas,
            params['row'], params['column'],
            row_frame, column_frame,
            frame1
        )
        await asyncio.sleep(0)


def get_controls_row_column(row_step, column_step,
                            max_space_row, max_space_column,
                            row, column,
                            row_speed, column_speed):
    row_speed, column_speed = update_speed(
        row_speed, column_speed,
        row_step, column_step
    )
    row = row + row_speed
    column = column + column_speed
    params = {
        'row': max(1, min(row, max_space_row)),
        'column': max(1, min(column, max_space_column)),
        'row_speed': row_speed,
        'column_speed': column_speed
    }
    return params
