import dpnp as np

from mandelbrot_demo.impl.settings import MAX_ITER

c1 = np.asarray([0.0, 0.0, 0.2])
c2 = np.asarray([1.0, 0.7, 0.9])
c3 = np.asarray([0.6, 1.0, 0.2])


def color_by_intensity(intensity):
    intensity = np.broadcast_to(intensity[:, :, np.newaxis], intensity.shape + (3,))
    return np.where(
        intensity < 0.5,
        c3 * intensity + c2 * (1.0 - intensity),
        c1 * intensity + c2 * (1.0 - intensity),
    )


def mandelbrot(w, h, zoom, offset, values):
    x = np.linspace(0, w, num=w, dtype=np.float32)
    y = np.linspace(0, h, num=h, dtype=np.float32)
    xx = (x - offset[0]) * zoom
    yy = (y - offset[1]) * zoom
    c = xx + 1j * yy[:, np.newaxis]

    n_iter = np.full(c.shape, 0)  # 2d array
    z = np.zeros(c.shape, dtype=np.csingle)  # 2d array too
    mask = n_iter < MAX_ITER  # Initialize with True
    for i in range(MAX_ITER):
        z[mask] = z[mask] ** 2 + c[mask]
        mask = mask & (np.abs(z) <= 2.0)
        n_iter[mask] = i

    intensity = n_iter.T / MAX_ITER
    values = (color_by_intensity(intensity) * 255).astype(np.int32)
    return values


def init_values(w, h):
    return np.full((w, h, 3), 0, dtype=np.int32)


def asnumpy(values):
    return np.asnumpy(values)
