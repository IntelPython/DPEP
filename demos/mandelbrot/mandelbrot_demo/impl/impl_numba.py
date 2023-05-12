import numba as nb
import numpy as np

from mandelbrot_demo.impl.settings import MAX_ITER

nb.config.THREADING_LAYER = "omp"


@nb.jit(fastmath=True, nopython=True)
def color_by_intensity(intensity, c1, c2, c3):
    if intensity < 0.5:
        return c3 * intensity + c2 * (1.0 - intensity)
    else:
        return c1 * intensity + c2 * (1.0 - intensity)


@nb.jit(fastmath=True, nopython=True)
def mandel(x, y):
    c = complex(x, y)
    z = 0.0j
    for i in range(MAX_ITER):
        z = z * z + c
        if (z.real * z.real + z.imag * z.imag) > 4.0:
            return i
    return MAX_ITER


@nb.jit(fastmath=True, nopython=True, parallel=True)
def mandelbrot(w, h, zoom, offset, values):
    c1 = np.asarray([0.0, 0.0, 0.2])
    c2 = np.asarray([1.0, 0.7, 0.9])
    c3 = np.asarray([0.6, 1.0, 0.2])

    for x in nb.prange(w):
        for y in range(h):
            xx = (x - offset[0]) * zoom
            yy = (y - offset[1]) * zoom
            intensity = mandel(xx, yy) / MAX_ITER
            for c in range(3):
                color = color_by_intensity(intensity, c1[c], c2[c], c3[c])
                color = int(color * 255.0)
                values[x, y, c] = color
    return values


def init_values(w, h):
    return np.full((w, h, 3), 0, dtype=np.uint8)


def asnumpy(values):
    return values
