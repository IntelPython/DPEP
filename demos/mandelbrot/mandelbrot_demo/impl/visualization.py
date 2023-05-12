import os

from mandelbrot_demo.impl.arg_parser import parse_args
from mandelbrot_demo.impl.impl_versioner import asnumpy

GUI = parse_args().gui

if GUI:
    import pygame as pg

DISPLAY_RES = DISPLAY_W, DISPLAY_H = 1024, 800
FPS = 60

frames = parse_args().max_frames
if frames > 0:
    N_FRAMES = frames
else:
    N_FRAMES = 1000000

OFFSET_X = 1.4 * DISPLAY_W // 2
OFFSET_Y = DISPLAY_H // 2
OFFSET = (OFFSET_X, OFFSET_Y)
ZOOM = 2.5 / DISPLAY_H

if GUI:

    def set_display():
        os.environ["SDL_VIDEO_CENTERED"] = "1"

        pg.init()
        surface = pg.display.set_mode(DISPLAY_RES, pg.SCALED)
        clock = pg.time.Clock()

        return surface, clock

    def pg_init():
        surface, clock = set_display()
        return surface, clock

    def pg_draw(surface, fractal):
        surface.fill(pg.Color("black"))
        pg.surfarray.blit_array(surface, asnumpy(fractal.values))

    def pg_test_quit():
        do_game = True
        for event in pg.event.get():
            if event.type == pg.QUIT:
                do_game = False
        return do_game

    def pg_update_fps(clk, frames):
        pg.display.set_caption(f"FPS: {clk.get_fps():2.1f}, FRAMES:{frames}")

    def pg_prep_next_frame(frames, clk):
        pg.display.flip()
        clk.tick(FPS)
        frames += 1
        return frames, frames < N_FRAMES

    def pg_finalize():
        pg.quit()

else:

    def pg_init():
        return None, None

    def pg_draw(surface, fractal):
        pass

    def pg_test_quit():
        return True

    def pg_update_fps(clk, frames):
        pass

    def pg_prep_next_frame(frames, clk):
        frames += 1
        return frames, frames < N_FRAMES

    def pg_finalize():
        pass
