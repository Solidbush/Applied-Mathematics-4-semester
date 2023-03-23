from Output import *


@painter_decorator
def fibonacci_search(l, r, eps, s=1):
    fib = np.array([1, 1])
    while fib[-1] <= (r - l) / eps:
        fib = np.append(fib, fib[-1] + fib[-2])

    d = lambda k: (r - l) * (fib[n - k] / fib[n - k + 1])
    n = len(fib) - 1
    x1, x2 = r - d(1), l + d(1)
    f1, f2 = s * f(x1), s * f(x2)
    debug_start(l, r, *[x1, x2, f1, f2])
    for k in range(1, n):
        if f1 > f2:
            l, x1, f1 = x1, x2, f2
            x2 = l + d(k)
            f2 = s * f(x2)
        else:
            r, x2, f2 = x2, x1, f1
            x1 = r - d(k)
            f1 = s * f(x1)
        debug_tick(l, r, r - l, *[x1, x2, f1, f2])
    return (l + r) * 0.5


fibonacci_search(8, 14, 0.001)
print(debug_result(*['l', 'r', 'x1', 'x2', 'f(x1)', 'f(x2)']))
