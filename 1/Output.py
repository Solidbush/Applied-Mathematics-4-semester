import math
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

plt.style.use('dark_background')
pd.set_option('display.float_format', lambda x: '%.4f' % x)


def f(x):
    return math.sin(0.5 * math.log(x) * x) + 1


def painter_decorator(func):
    def draw(*args):
        p = func(*args)
        xx = np.arange(max(0.1, p - 10), p + 10, 0.05)
        yy = np.array([f(x) for x in xx])
        plt.plot(xx, yy)
        plt.scatter(p, f(p), color='b')
        print(f"Min point x: {'%.7f' % p}. Function f(p) = {'%.7f' % f(p)}")
        plt.show()

    return draw


prev_step = 0
debug_list = []


def debug_start(l, r, *args):
    global prev_step, debug_list
    debug_list = [[l, r] + list(args) + [None]]
    prev_step = r - l


def debug_tick(l, r, step, *args):
    global prev_step, debug_list
    attitude = step / prev_step
    prev_step = step
    debug_list.append([l, r] + list(args) + [attitude])


def debug_result(*args):
    global debug_list
    args = list(args) + ['attitude']
    frame = pd.DataFrame(debug_list, columns=args)
    ord_args = args
    r_id = 1
    while r_id < len(args) - 1 and not ord_args[r_id + 1].startswith('f'):
        ord_args[r_id], ord_args[r_id + 1] = ord_args[r_id + 1], ord_args[r_id]
        r_id += 1

    return frame[ord_args]