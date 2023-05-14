import numpy as np

from game_of_life_demo import get_task_size_string
from game_of_life_demo.impl.arg_parser import parse_args
from game_of_life_demo.impl.impl_versioner import asnumpy
from game_of_life_demo.impl.impl_versioner import get_variant_string

DISPLAY_RES = DISPLAY_W, DISPLAY_H = 1920, 1080  # Window width and height
CELL_COLOR = (0, 255, 0)  # Color to be used for alive cells # BGR
CELL_SIZE = 2  # Cell size in pixels

FONT_SCALE = 0.5
FONT_COLOR = (255, 255, 255)  # BGR(A)
FONT_HEIGHT = 15
FONT_THICKNESS = 1
FONT = None

# Text box with performance statistics
TEXT_BOX_TOP_LEFT = (5, 7)  # Top-left corner
TEXT_BOX_BOTTOM_RIGHT = (420, 110)  # Bottom-right corner
TEXT_BOX_FONT_OFFSET = 10  # Offset from the top-left corner in pixels for drawing text
TEXT_BOX_COL2_OFFSET = (
    150  # Offset from the left (in pixels) for drawing text in second column
)
TEXT_BOX_COL3_OFFSET = (
    300  # Offset from the left (in pixels) for drawing text in third column
)
TEXT_BOX_ALPHA = 0.5  # Transparency of the text box background

# Game field size (GRID_W - number of cells horizontally, GRID_H - number of cells vertically)
GRID_W, GRID_H = DISPLAY_W // CELL_SIZE, DISPLAY_H // CELL_SIZE

ESC_KEYCODE = 27  # Finish demo by pressing Esc key
WINDOW_NAME = "Conway's Game of life"  # Window name


# *********************************************************************************************
# CONDITIONAL INITIALIZATIONS
# *********************************************************************************************

GUI_FLAG = parse_args().gui  # If user selected --gui CLI option

if GUI_FLAG:
    try:  # Importing OpenCV
        import cv2

        VISUALIZE_GAME = True
        FONT = cv2.FONT_HERSHEY_TRIPLEX
    except ModuleNotFoundError:
        VISUALIZE_GAME = False
else:
    VISUALIZE_GAME = False


def line_to_y(line_number):
    return TEXT_BOX_TOP_LEFT[1] + FONT_HEIGHT * line_number + TEXT_BOX_FONT_OFFSET


def draw_text(img, text, line_number, x_pos=TEXT_BOX_FONT_OFFSET):
    y_pos = line_to_y(line_number)
    cv2.putText(img, text, (x_pos, y_pos), FONT, FONT_SCALE, FONT_COLOR, FONT_THICKNESS)


def draw_statistics_line(img, name, line_number, fps, time):
    # no monospace fonts in OpenCV
    draw_text(img, name, line_number)
    draw_text(img, "FPS|time(ms)", line_number, TEXT_BOX_COL2_OFFSET)
    draw_text(img, f"{fps:4.1f}|{int(1000 * time)}", line_number, TEXT_BOX_COL3_OFFSET)


def draw_statistics(
    img,
    w,
    h,
    frame_count,
    update_time,
    update_tpf,
    draw_time,
    draw_tpf,
    total_time,
    total_tpf,
):
    p1 = TEXT_BOX_TOP_LEFT
    p2 = TEXT_BOX_BOTTOM_RIGHT

    sub_img = img[p1[1] : p2[1], p1[0] : p2[0]]
    black_bg = np.zeros(sub_img.shape, dtype=np.uint8)
    img[p1[1] : p2[1], p1[0] : p2[0]] = cv2.addWeighted(
        sub_img, TEXT_BOX_ALPHA, black_bg, 1.0 - TEXT_BOX_ALPHA, 1.0
    )
    draw_text(img, get_variant_string(), 0)
    draw_text(img, get_task_size_string(w, h), 1)
    draw_text(img, f"Frames: {(frame_count // 10) * 10}", 2)
    draw_statistics_line(img, "Computation", 3, 1 / update_tpf, update_time)
    draw_statistics_line(img, "Draw", 4, 1 / draw_tpf, draw_time)
    draw_statistics_line(img, "Total", 5, 1 / total_tpf, total_time)


def draw(
    grid,
    show_statistics,
    frame_count,
    update_time,
    update_tpf,
    draw_time,
    draw_tpf,
    total_time,
    total_tpf,
):
    if VISUALIZE_GAME:
        h, w = grid.shape
        img = np.zeros(shape=grid.shape + (3,), dtype=np.uint8)
        img[:, :, 1] = 255 * asnumpy(
            grid
        )  # The asnumpy() transfers data from device to host as needed
        img = cv2.resize(img, (DISPLAY_W, DISPLAY_H), interpolation=cv2.INTER_NEAREST)

        if show_statistics and frame_count > 0:
            draw_statistics(
                img,
                w,
                h,
                frame_count,
                update_time,
                update_tpf,
                draw_time,
                draw_tpf,
                total_time,
                total_tpf,
            )

        cv2.imshow(WINDOW_NAME, img)
        cv2.resizeWindow(WINDOW_NAME, DISPLAY_W, DISPLAY_H)


def test_esc_key_pressed():
    if VISUALIZE_GAME:
        return cv2.pollKey() == ESC_KEYCODE
    else:
        return False


def test_window_closed():
    if VISUALIZE_GAME:
        return not cv2.getWindowProperty(WINDOW_NAME, cv2.WND_PROP_VISIBLE)
    else:
        return False


def create_window():
    if VISUALIZE_GAME:
        cv2.namedWindow(WINDOW_NAME, cv2.WINDOW_GUI_NORMAL | cv2.WINDOW_AUTOSIZE)
        cv2.resizeWindow(WINDOW_NAME, DISPLAY_W, DISPLAY_H)
