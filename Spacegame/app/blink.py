import asyncio
import curses
import random


async def animate_blink(canvas, row, column, symbol):
    rnd = random.randint(1, 4)

    while True:
        if rnd == 4:
            canvas.addstr(row, column, symbol, curses.A_DIM)
            for i in range(20):
                await asyncio.sleep(0)

            canvas.addstr(row, column, symbol)
            for i in range(3):
                await asyncio.sleep(0)

            canvas.addstr(row, column, symbol, curses.A_BOLD)
            for i in range(5):
                await asyncio.sleep(0)

            canvas.addstr(row, column, symbol)
            for i in range(3):
                await asyncio.sleep(0)
        else:
            rnd += 1
            await asyncio.sleep(0)


def get_random_blink(canvas, row_bound, column_bound):
    simbols_list = ['+', '*', '.', ':']
    max_row, max_column = canvas.getmaxyx()
    row = random.randint(row_bound, max_row - row_bound - 1)
    column = random.randint(column_bound, max_column - column_bound - 1)
    simbol = random.choice(simbols_list)
    return animate_blink(canvas, row, column, simbol)
