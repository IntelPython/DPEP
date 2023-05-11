import numpy as np
from numba import njit
from numba import prange


@njit(parallel=True)
def monte_carlo_pi_batch(batch_size):
    x = np.random.random(batch_size)
    y = np.random.random(batch_size)
    acc = 0
    for i in prange(batch_size):
        if x[i] * x[i] + y[i] * y[i] <= 1.0:
            acc += 1
    return 4.0 * acc / batch_size
