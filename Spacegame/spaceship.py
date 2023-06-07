from sleep import Sleep
from curses_tools import draw_frame


async def animate_spaceship(canvas,
                            frame1,
                            frame2,
                            row=1,
                            column=1,
                            negative=False):
    draw_frame(canvas, row, column, frame1, negative)
    await Sleep(0.1)

    while True:
        draw_frame(canvas, row, column, frame1, negative=True)
        draw_frame(canvas, row, column, frame2, negative)
        await Sleep(0.1)

        draw_frame(canvas, row, column, frame2, negative=True)
        draw_frame(canvas, row, column, frame1, negative)
        await Sleep(0.1)
