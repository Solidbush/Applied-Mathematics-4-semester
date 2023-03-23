from Output import *


@painter_decorator
def dichotomous_search(l, r, eps, s=1):
    debug_start(l, r, *[0, 0, 0, 0])
    delta = eps / 3

    while r - l > eps:
        m = (l + r) * 0.5
        x1 = m - delta
        x2 = m + delta
        if s * f(x1) > s * f(x2):
            l = x1
        else:
            r = x2
        debug_tick(l, r, r - l, *[x1, x2, f(x1), f(x2)])
    return (l + r) * 0.5


dichotomous_search(8, 14, 0.001)
print(debug_result(*['l', 'r', 'x1', 'x2', 'f(x1)', 'f(x2)']))
