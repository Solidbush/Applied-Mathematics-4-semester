from Output import *


@painter_decorator
def brents_method(l, r, eps, s=1):
    gr = (math.sqrt(5) - 1) / 2
    m = w = v = l + gr * (r - l)
    fm = fw = fv = s * f(m)
    d = e = 0
    u = float('+inf')
    algo_type = None
    debug_start(l, r, *[m, w, v, fm, fw, fv, algo_type])
    while r - l > eps:
        g, e = e, d
        if len({m, w, v}) == len({fm, fw, fv}) == 3:
            p = ((m - w) ** 2) * (fm - fv) - ((m - v) ** 2) * (fm - fw)
            q = 2 * ((m - w) * (fm - fv) - (m - v) * (fm - fw))
            u = m - p / q

        if l + eps <= u <= r - eps and 2 * abs(u - m) < g:
            algo_type = 'spi'
            d = abs(u - m)
        else:
            algo_type = 'gss'
            if m < (r + l) * .5:
                d = r - m
                u = m + gr * d
            else:
                d = m - l
                u = m - gr * d

        if abs(u - m) < eps:
            return u

        fu = s * f(u)

        if fu <= fm:
            if u >= m:
                l = m
            else:
                r = m
            v, w, m = w, m, u
            fv, fw, fm = fw, fm, fu

        else:
            if u >= m:
                r = u
            else:
                l = u

            if fu <= fw or w == m:
                v, w = w, u
                fv, fw = fw, fu
            elif fu <= fv or v == m or v == w:
                v = u
                fv = fu

        debug_tick(l, r, d, *[m, w, v, fm, fw, fv, algo_type])

    return (l + r) / 2


brents_method(8, 14, 0.001)
print(debug_result(*['l', 'r', 'm', 'w', 'v', 'f(m)', 'f(w)', 'f(v)', 'algo_type']))
