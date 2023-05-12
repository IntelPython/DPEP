import numpy as np

from mandelbrot_demo.impl.impl_numpy import mandelbrot


def test_numpy():
    w = 2
    h = 2
    zoom = 1.0
    offset = (0.0, 0.0)
    colors = np.full((w, h, 3), 0, dtype=np.uint8)

    colors = mandelbrot(w, h, zoom, offset, colors)
    s = colors.astype(np.int32).sum()
    assert s == 2055
