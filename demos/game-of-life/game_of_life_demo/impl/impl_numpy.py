import numpy as np


def init_grid(w, h, p):
    return np.random.choice((0, 1), w * h, p=(1.0 - p, p)).reshape(h, w)


def grid_update(grid):
    m, n = grid.shape

    grid_neighbor = np.zeros((m + 2, n + 2), dtype=grid.dtype)

    grid_neighbor[0:-2, 0:-2] = grid
    grid_neighbor[1:-1, 0:-2] += grid
    grid_neighbor[2:, 0:-2] += grid
    grid_neighbor[0:-2, 1:-1] += grid
    grid_neighbor[2:, 1:-1] += grid
    grid_neighbor[0:-2, 2:] += grid
    grid_neighbor[1:-1, 2:] += grid
    grid_neighbor[2:, 2:] += grid

    grid_neighbor[1, 1:-1] += grid_neighbor[-1, 1:-1]
    grid_neighbor[-2, 1:-1] += grid_neighbor[0, 1:-1]
    grid_neighbor[1:-1, 1] += grid_neighbor[1:-1, -1]
    grid_neighbor[1:-1, -2] += grid_neighbor[1:-1, 0]

    grid_neighbor[1, 1] += grid_neighbor[-1, -1]
    grid_neighbor[-2, -2] += grid_neighbor[0, 0]
    grid_neighbor[1, -2] += grid_neighbor[-1, 0]
    grid_neighbor[-2, 1] += grid_neighbor[0, -1]

    dead_rules = np.logical_and(grid == 0, grid_neighbor[1:-1, 1:-1] == 3)
    alive_rules = np.logical_and(
        grid == 1,
        np.logical_or(grid_neighbor[1:-1, 1:-1] == 2, grid_neighbor[1:-1, 1:-1] == 3),
    )

    grid_out = np.logical_or(alive_rules, dead_rules)

    return grid_out.astype(grid.dtype)


def asnumpy(x):
    return x
