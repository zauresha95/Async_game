import asyncio
from sleep import sleep
from curses_tools import draw_frame


PHRASES = {
    1957: "First Sputnik",
    1961: "Gagarin flew!",
    1969: "Armstrong got on the moon!",
    1971: "First orbital space station Salute-1",
    1981: "Flight of the Shuttle Columbia",
    1998: 'ISS start building',
    2011: 'Messenger launch to Mercury',
    2020: "Take the plasma gun! Shoot the garbage!",
}


def get_garbage_delay_tics(year):
    if year < 1961:
        return None
    elif year < 1969:
        return 20
    elif year < 1981:
        return 14
    elif year < 1995:
        return 10
    elif year < 2010:
        return 8
    elif year < 2020:
        return 6
    else:
        return 2


async def draw_year(canvas, max_row, year):
    frame_prev = ''
    while True:
        year_int = year[0]
        if PHRASES.get(year_int, None) is not None:
            frame = f'{year_int}:{PHRASES[year_int]}'
        else:
            frame = f'{year_int}'
        draw_frame(canvas, max_row - 1, 1, frame_prev, negative=True)
        draw_frame(canvas, max_row - 1, 1, frame)

        await sleep(10)
        frame_prev = frame
        year[0] = year[0] + 1
