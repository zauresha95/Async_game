import random
import curses
from sleep import Sleep


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
    row = random.randint(1, max_row - 2)
    column = random.randint(1, max_column - 2)
    simbol = random.choice(simbols_list)
    return animate_blink(canvas, row, column, simbol)
