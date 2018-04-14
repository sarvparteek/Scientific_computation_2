import math, cmath

def quadratic(a, b, c):
    disc = b*b - 4*a*c
    rad = math.sqrt(disc) if disc >= 0 else cmath.sqrt(disc)
    xr1 = -2*c / (b + rad)
    xr2 = -2*c / (b - rad)
    return xr1, xr2
#end quadratic()

def muller(f, xr, h, es100, imax=1000, debug=False):
    x2 = float(xr)
    x1 = float(xr + h)
    x0 = float(xr - h)
    ea = 100
    iter = 0
    while True:
        iter += 1
        h0 = x1 - x0
        h1 = x2 - x1
        d0 = (f(x1) - f(x0)) / h0
        d1 = (f(x2) - f(x1)) / h1
        a = (d1 - d0) / (h1 + h0)
        b = a*h1 + d1
        c = f(x2)
        disc = b*b - 4*a*c
        rad = math.sqrt(disc) if disc >= 0 else cmath.sqrt(disc)
        den = (b + rad) if b >= 0 else b - rad
        dxr = -2*c / den
        xr = x2 + dxr
        if xr: ea = abs(dxr / xr)
        if debug: print("iter={}, xr={:f}, ea={:%}".format(iter, xr, ea))
        if ea*100 < es100 or iter >= imax:
            break
        x0 = x1
        x1 = x2
        x2 = xr
    return xr
#end muller()