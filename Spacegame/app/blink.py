import asyncio
import curses
import random
from sleep import sleep


async def animate_blink(canvas, row, column, symbol, offset_tics):
    while True:
        await sleep(offset_tics)
        canvas.addstr(row, column, symbol, curses.A_DIM)
        await sleep(20)
        canvas.addstr(row, column, symbol)
        await sleep(3)
        canvas.addstr(row, column, symbol, curses.A_BOLD)
        await sleep(5)
        canvas.addstr(row, column, symbol)
        await sleep(3)


def get_random_blink(canvas, max_row, max_column, offset_tics):
    simbols_list = ['+', '*', '.', ':']
    row = random.randint(1, max_row - 1)
    column = random.randint(1, max_column - 1)
    simbol = random.choice(simbols_list)
    return animate_blink(canvas, row, column, simbol, offset_tics)
