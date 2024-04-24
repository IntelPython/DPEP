import numpy as np
from game_of_life_demo import MAX_FRAMES
from game_of_life_demo import PROB_ON
from game_of_life_demo import get_task_size_string
from game_of_life_demo import time_meter
from game_of_life_demo.impl.arg_parser import parse_args
from game_of_life_demo.impl.impl_versioner import get_variant_string
from game_of_life_demo.impl.impl_versioner import grid_update
from game_of_life_demo.impl.impl_versioner import init_grid
from game_of_life_demo.impl.visualization import VISUALIZE_GAME
from game_of_life_demo.impl.visualization import create_window
from game_of_life_demo.impl.visualization import draw
from game_of_life_demo.impl.visualization import test_esc_key_pressed
from game_of_life_demo.impl.visualization import test_window_closed


class Grid:
    draw_last = "draw_time_last"
    draw_total = "draw_time_total"

    update_last = "update_time_last"
    update_total = "update_time_total"

    def __init__(self, w, h, p):
        self.w = w
        self.h = h
        self.time = {
            self.draw_last: 0,
            self.draw_total: 0,
            self.update_last: 0,
            self.update_total: 0,
        }
        self.grid = init_grid(w, h, p)

    def get_statistics(self, frame_count):
        update_time = self.time[self.update_last]
        update_tpf = (
            self.time[self.update_total] / frame_count if frame_count > 0 else 0.0
        )
        draw_time = self.time[self.draw_last]
        draw_tpf = self.time[self.draw_total] / frame_count if frame_count > 0 else 0.0
        total_time = update_time + draw_time
        total_tpf = update_tpf + draw_tpf
        return update_time, update_tpf, draw_time, draw_tpf, total_time, total_tpf

    @time_meter(draw_last, draw_total)
    def draw(self, show_statistics, frame_count):
        (
            update_time,
            update_tpf,
            draw_time,
            draw_tpf,
            total_time,
            total_tpf,
        ) = self.get_statistics(frame_count)
        draw(
            self.grid,
            show_statistics,
            frame_count,
            update_time,
            update_tpf,
            draw_time,
            draw_tpf,
            total_time,
            total_tpf,
        )

    @time_meter(update_last, update_total)
    def update(self):
        self.grid = grid_update(self.grid)


def main(argv=None):
    np.random.seed(777777777)

    w, h = parse_args(argv).task_size
    grid = Grid(w, h, PROB_ON)

    create_window()

    frames = 0
    do_game = True

    stop_frame = parse_args(argv).frames_count
    if stop_frame == 0:
        stop_frame = MAX_FRAMES

    print(get_variant_string())
    print(get_task_size_string(w, h))

    while do_game:
        # Checks for game termination
        esc_pressed = test_esc_key_pressed()
        window_closed = test_window_closed()

        # Draw objects
        grid.draw(parse_args().stats, frames)

        # Perform updates
        grid.update()

        frames += 1
        do_game = (0 < frames <= stop_frame) and not (esc_pressed or window_closed)

    _, update_tpf, _, draw_tpf, _, total_tpf = grid.get_statistics(frames)
    print(f"Total frames {frames}")
    print("Average fps:")
    print(f"    Computation {1/update_tpf:4.1f}")
    if VISUALIZE_GAME:
        print(f"    Draw        {1/draw_tpf:4.1f}")
        print(f"    Total       {1/total_tpf:4.1f}")


if __name__ == "__main__":
    main()
