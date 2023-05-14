from time import time

PROB_ON = 0.2
MAX_FRAMES = 2000


def int_tuple(tuple_str):
    return tuple(map(int, tuple_str.split(",")))


def time_meter(last, total):
    def _time_meter(func):
        def impl(self, *args, **kwargs):
            start = time()
            res = func(self, *args, **kwargs)
            end = time()
            self.time[last] = end - start
            self.time[total] += end - start

            return res

        return impl

    return _time_meter


def get_task_size_string(w, h):
    return f"Task size {w}x{h}"
