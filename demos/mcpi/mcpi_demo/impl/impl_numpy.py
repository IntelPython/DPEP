import numpy as np


def monte_carlo_pi_batch(batch_size):
    x = np.random.random(batch_size)
    y = np.random.random(batch_size)
    acc = np.count_nonzero(x * x + y * y <= 1.0)
    return 4.0 * acc / batch_size
