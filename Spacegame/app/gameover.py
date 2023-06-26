import asyncio
from obstacles import Obstacle, show_obstacles
from curses_tools import draw_frame, get_frame, get_frame_size
from params import obstacles, obstacles_in_last_collisions


async def show_gameover(canvas, row, column, row_space, column_space, space_frame):
    frame = get_frame('game_over.txt')
    row_frame, column_frame = get_frame_size(frame)
    # get the height and width of the window, that less than the border to 1
    rows, columns = canvas.getmaxyx()
    max_row, max_column = rows - 1, columns - 1
    # get the start position
    max_row, max_column = max_row - row_frame, max_column - column_frame
    row_start = max_row // 2 + 1
    column_start = max_column // 2 + 1

    for obstacle in obstacles:
        if obstacle.has_collision(row, column, row_space, column_space):
            obstacles_in_last_collisions.append(obstacle)
            draw_frame(canvas, row, column, space_frame, negative=True)
            while True:
                draw_frame(canvas, row_start, column_start, frame)
                await asyncio.sleep(0)
            return True
    await asyncio.sleep(0)
