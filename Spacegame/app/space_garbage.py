import asyncio
import random
import os
from obstacles import Obstacle, show_obstacles
from curses_tools import draw_frame, get_frame, get_frame_size
from sleep import sleep
from params import obstacles, obstacles_in_last_collisions, year
from game_scenario import get_garbage_delay_tics


async def fly_garbage(canvas, column, garbage_frame, speed=0.5):
    """
    Animate garbage, flying from top to bottom.
    Сolumn position will stay same, as specified on start.
    """
    rows_number, columns_number = canvas.getmaxyx()

    column = max(column, 0)
    column = min(column, columns_number - 1)
    row = 0

    coroutine = show_obstacles(obstacles)
    loop = asyncio.get_event_loop()
    loop.create_task(asyncio.sleep(0))
    loop.create_task(coroutine)
    row_frame, column_frame = get_frame_size(garbage_frame)

    obstacle = Obstacle(row, column, row_frame, column_frame)
    obstacles.append(obstacle)

    while row < rows_number:
        draw_frame(canvas, row, column, garbage_frame)

        await asyncio.sleep(0)

        obstacles.remove(obstacle)
        draw_frame(canvas, row, column, garbage_frame, negative=True)
        if obstacle in obstacles_in_last_collisions:
            return True
        row += speed

        obstacle = Obstacle(row, column, row_frame, column_frame)
        obstacles.append(obstacle)


async def fill_orbit_with_garbage(canvas,
                                  coroutines,
                                  max_column,
                                  offset_tics=6):
    garbages_list = os.listdir('files/garbage')
    while True:
        tics = get_garbage_delay_tics(year[0])
        offset_tics = tics if tics else 6
        await sleep(offset_tics)
        column = random.randint(1, max_column)
        garbage_frame = get_frame(f"/garbage/{random.choice(garbages_list)}")
        coroutines.append(fly_garbage(canvas, column, garbage_frame, speed=0.5))
        await sleep(offset_tics)
