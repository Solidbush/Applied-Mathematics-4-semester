from Output import *
from scipy.interpolate import lagrange


@painter_decorator
def parabolic_interpolation(l, r, eps, s=1):
    m = (l + r) / 2

    # for lagrange
    xx = np.arange(l, r, 0.05)
    yy = np.array([f(x) for x in xx])
    parables = []

    f1, f2, f3 = s * f(l), s * f(m), s * f(r)
    debug_start(l, r, *[m, f1, f2, f3])
    while r - l > eps:
        p = ((m - l) ** 2) * (f2 - f3) - ((m - r) ** 2) * (f2 - f1)
        q = 2 * ((m - l) * (f2 - f3) - (m - r) * (f2 - f1))
        u = m - p / q
        fu = s * f(u)
        lagr = lagrange([l, m, r], [f1, f2, f3])
        parables.append(s * lagr(xx))
        if m > u:
            if f2 < fu:
                l, f1 = u, fu
            else:
                r, f3 = m, f2
                m, f2 = u, fu
        else:
            if f2 > fu:
                l, f1 = m, f2
                m, f2 = u, fu
            else:
                r, f3 = u, fu
        debug_tick(l, r, r - l, *[m, f1, f2, f3])

    p = (l + r) / 2
    plt.scatter(p, f(p), c='r')
    for i in parables:
        plt.plot(xx, i, c='w', linestyle='--', alpha=.3)
    plt.plot(xx, yy)
    plt.show()
    return p


parabolic_interpolation(8, 14, 0.001)
print(debug_result(*['l', 'r', 'm', 'f(l)', 'f(m)', 'f(r)']))
