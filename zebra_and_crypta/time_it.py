import time


def time_it(n, fn, *args):
    if isinstance(n, int):
        times = [time_once(fn, *args)[0] for _ in range(n)]
    else:
        times = []
        # total_time = time_once(fn, *args)[0]
        while sum(times) < n:
            times.append(time_once(fn, *args)[0])
    print('avg = %fs' % (sum(times)/n))


def time_once(fn, *args):
    t0 = time.clock()
    res = fn(*args)
    t1 = time.clock()
    return (t1-t0, res)


def fn(N=10):
    for _ in range(N*1000000):
        pass


time_it(22, fn, 1)
