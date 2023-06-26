import asyncio
import curses
from params import obstacles, obstacles_in_last_collisions, year
from explosion import explode


async def fire_by_space(canvas,
                        space,
                        column_frame,
                        params,
                        rows_speed=-0.3,
                        columns_speed=0):
    if space and year[0] > 2000:
        start_column = params['column'] + column_frame // 2
        await fire(canvas, params['row'], start_column)
    else:
        await asyncio.sleep(0)


async def fire(canvas,
               start_row,
               start_column,
               rows_speed=-0.3,
               columns_speed=0):
    """Display animation of gun shot, direction and speed can be specified."""

    row, column = start_row, start_column
    canvas.addstr(round(row), round(column), '*')
    await asyncio.sleep(0)

    canvas.addstr(round(row), round(column), 'O')
    await asyncio.sleep(0)
    canvas.addstr(round(row), round(column), ' ')

    row += rows_speed
    column += columns_speed

    symbol = '-' if columns_speed else '|'

    rows, columns = canvas.getmaxyx()
    max_row, max_column = rows - 1, columns - 1

    curses.beep()

    while 1 < row < max_row and 1 < column < max_column:
        for obstacle in obstacles:
            if obstacle.has_collision(row, column):
                obstacles_in_last_collisions.append(obstacle)
                await explode(canvas, row, column)
                return True
        canvas.addstr(round(row), round(column), symbol)
        await asyncio.sleep(0)
        canvas.addstr(round(row), round(column), ' ')
        row += rows_speed
        column += columns_speed
