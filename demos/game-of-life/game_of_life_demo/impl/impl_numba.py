import numpy as np
from game_of_life_demo.impl.arg_parser import parse_args
from numba import njit
from numba import prange

rules = np.array(
    [
        # 0  1  2  3  4  5  6  7  8   # Number of alive cell neighbors
        [0, 0, 0, 1, 0, 0, 0, 0, 0],  # Rule for dead cells
        [0, 0, 1, 1, 0, 0, 0, 0, 0],  # Rule for alive cells
    ]
)


def init_grid(w, h, p):
    return np.random.choice((0, 1), w * h, p=(1.0 - p, p)).reshape(h, w)


@njit(
    ["int32[:,:](int32[:,:])", "int64[:,:](int64[:,:])"], parallel=parse_args().parallel
)
def grid_update(grid):
    m, n = grid.shape
    grid_out = np.empty_like(grid)
    grid_padded = np.empty((m + 2, n + 2), dtype=grid.dtype)
    grid_padded[1:-1, 1:-1] = grid  # copy input grid into the center of padded one
    grid_padded[0, 1:-1] = grid[-1]  # top row of padded grid
    grid_padded[-1, 1:-1] = grid[0]  # bottom
    grid_padded[1:-1, 0] = grid[:, -1]
    grid_padded[1:-1, -1] = grid[:, 0]
    grid_padded[0, 0] = grid[-1, -1]
    grid_padded[-1, -1] = grid[0, 0]
    grid_padded[0, -1] = grid[-1, 0]
    grid_padded[-1, 0] = grid[0, -1]
    for i in prange(m):
        for j in range(n):
            v_self = grid[i, j]
            neighbor_population = grid_padded[i : i + 3, j : j + 3].sum() - v_self
            grid_out[i, j] = rules[v_self, neighbor_population]
    return grid_out


def asnumpy(x):
    return x
