from time import time


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
