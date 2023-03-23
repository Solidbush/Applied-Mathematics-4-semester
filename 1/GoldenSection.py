from Output import *


@painter_decorator
def golden_section_search(l, r, eps, s=1):
    d = lambda: gr * (r - l)
    gr = (math.sqrt(5) - 1) * .5
    x1, x2 = r - d(), l + d()
    f1, f2 = s * f(x1), s * f(x2)
    debug_start(l, r, *[x1, x2, f1, f2])
    while r - l > eps:
        if f1 > f2:
            l, x1, f1 = x1, x2, f2
            x2 = l + d()
            f2 = s * f(x2)
        else:
            r, x2, f2 = x2, x1, f1
            x1 = r - d()
            f1 = s * f(x1)
        debug_tick(l, r, r - l, *[x1, x2, f1, f2])

    return (l + r) * 0.5


golden_section_search(8, 14, 0.001)
print(debug_result(*['l', 'r', 'x1', 'x2', 'f(x1)', 'f(x2)']))
