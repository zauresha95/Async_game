SPACE_KEY_CODE = 32
LEFT_KEY_CODE = 260
RIGHT_KEY_CODE = 261
UP_KEY_CODE = 259
DOWN_KEY_CODE = 258


def read_controls(canvas):
    """Read keys pressed and returns tuple witl controls state."""

    rows_direction = columns_direction = 0
    space_pressed = False

    while True:
        pressed_key_code = canvas.getch()

        if pressed_key_code == -1:
            # https://docs.python.org/3/library/curses.html#curses.window.getch
            break

        if pressed_key_code == UP_KEY_CODE:
            rows_direction = -1

        if pressed_key_code == DOWN_KEY_CODE:
            rows_direction = 1

        if pressed_key_code == RIGHT_KEY_CODE:
            columns_direction = 1

        if pressed_key_code == LEFT_KEY_CODE:
            columns_direction = -1

        if pressed_key_code == SPACE_KEY_CODE:
            space_pressed = True

    return rows_direction, columns_direction, space_pressed


def draw_frame(canvas, start_row, start_column, text, negative=False):
    """
    Draw multiline text fragment on canvas,
    erase text instead of drawing if negative=True is specified.
    """

    rows_number, columns_number = canvas.getmaxyx()

    for row, line in enumerate(text.splitlines(), round(start_row)):
        if row < 0:
            continue

        if row >= rows_number:
            break

        for column, symbol in enumerate(line, round(start_column)):
            if column < 0:
                continue

            if column >= columns_number:
                break

            if symbol == ' ':
                continue

            # Check that current position it is not in a lower right corner of the window
            # Curses will raise exception in that case. Don`t ask why…
            # https://docs.python.org/3/library/curses.html#curses.window.addch
            if row == rows_number - 1 and column == columns_number - 1:
                continue

            symbol = symbol if not negative else ' '
            canvas.addch(row, column, symbol)


def get_frame_size(text):
    """Calculate size of multiline text fragment, return pair — number of rows and colums."""

    lines = text.splitlines()
    rows = len(lines)
    columns = max([len(line) for line in lines])
    return rows, columns


def get_frames_size(text1, text2):
    """Calculate size of multiline text fragment, return pair — number of rows and colums."""

    rows, columns = (0, 0)
    for text in [text1, text2]:
        lines = text.splitlines()
        rows_new = len(lines)
        columns_new = max([len(line) for line in lines])
        rows = rows_new if rows_new > rows else rows
        columns = columns_new if columns_new > columns else columns_new
    return rows, columns


def get_frame(path_file):
    with open(f"files/{path_file}", "r") as my_file:
        frame = my_file.read()
        return frame


def get_controls_row_column(canvas, row, column, row_frame, column_frame, max_row, max_column, speed=1):
    row_step, column_step, space = read_controls(canvas)
    if row_step in [1, -1] or column_step in [1, -1]:
        row_new = row + row_step * speed
        column_new = column + column_step * speed
        if (1 <= row_new <= max_row - row_frame - 1 and
                1 <= column_new <= max_column - column_frame - 1):
            return row_new, column_new
    return row, column
