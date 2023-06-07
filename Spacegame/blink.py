import random
import curses
from sleep import Sleep
from params import ROW_START, COLUMN_START


async def animate_blink(canvas, row, column, symbol):
    while True:
        canvas.addstr(row, column, symbol, curses.A_DIM)
        for i in range(20):
            await Sleep(0.1)

        canvas.addstr(row, column, symbol)
        for i in range(3):
            await Sleep(0.1)

        canvas.addstr(row, column, symbol, curses.A_BOLD)
        for i in range(5):
            await Sleep(0.1)

        canvas.addstr(row, column, symbol)
        for i in range(3):
            await Sleep(0.1)


def get_random_blink(canvas):
    simbols_list = ['+', '*', '.', ':']
    max_row, max_column = canvas.getmaxyx()
    row = random.randint(ROW_START, max_row - ROW_START)
    column = random.randint(COLUMN_START, max_column - COLUMN_START)
    simbol = random.choice(simbols_list)
    return animate_blink(canvas, row, column, simbol)
