import time

from mandelbrot_demo.impl.impl_versioner import init_values
from mandelbrot_demo.impl.impl_versioner import mandelbrot
from mandelbrot_demo.impl.visualization import DISPLAY_H
from mandelbrot_demo.impl.visualization import DISPLAY_W
from mandelbrot_demo.impl.visualization import OFFSET
from mandelbrot_demo.impl.visualization import ZOOM
from mandelbrot_demo.impl.visualization import pg_draw
from mandelbrot_demo.impl.visualization import pg_finalize
from mandelbrot_demo.impl.visualization import pg_init
from mandelbrot_demo.impl.visualization import pg_prep_next_frame
from mandelbrot_demo.impl.visualization import pg_test_quit
from mandelbrot_demo.impl.visualization import pg_update_fps


class Fractal:
    def __init__(self, w, h, zoom, offset):
        self.w = w
        self.h = h
        self.values = init_values(w, h)
        self.zoom = zoom
        self.offset = offset
        self.need_recalculate = True

    def set_zoom(self, zoom):
        old_zoom = self.zoom
        if self.zoom != zoom:
            self.need_recalculate = True
            self.zoom = zoom
        return old_zoom

    def set_offset(self, offset):
        old_offset = self.offset
        if self.offset != offset:
            self.need_recalculate = True
            self.offset = offset
        return old_offset

    def calculate(self):
        self.values = mandelbrot(self.w, self.h, self.zoom, self.offset, self.values)
        self.need_recalculate = False

    def update(self):
        if self.need_recalculate:
            self.calculate()


def main():
    ds, clk = pg_init()

    zoom = ZOOM
    scale = 1.01
    incr = -5.0
    offset_x = OFFSET[0]
    offset_y = OFFSET[1]

    fractal = Fractal(DISPLAY_W, DISPLAY_H, zoom, (offset_x, offset_y))

    frames = 0
    do_game = True
    t1 = time.time()
    while do_game:
        # Test for windows close event
        do_game = pg_test_quit()

        # Draw objects
        pg_draw(ds, fractal)

        # Perform updates
        if frames % 300 == 0:
            scale = 1.0 / scale
            incr = -incr
        zoom *= scale
        offset_x += incr
        offset_y += incr

        fractal.set_zoom(zoom)
        fractal.set_offset((offset_x, offset_y))
        fractal.update()
        pg_update_fps(clk, frames)

        # Prepare for next frame
        frames, more_frames_flag = pg_prep_next_frame(frames, clk)
        do_game = do_game and more_frames_flag
    t2 = time.time()
    pg_finalize()
    print("Avg.fps:", frames / (t2 - t1))


if __name__ == "__main__":
    main()
