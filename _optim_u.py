
'''
module: _optim_u_to.py
author: Luis Paris
description:
- formulas from Chapra's numerical methods textbook
- chapters on Optimization, the unconstrained case
- implemented from algorithms/pseudocode provided
TODO:
- make gold() search method work for locating minima too (ismax=False)
'''

import math

def gold(f, xlo, xhi, es100, imax=1000, ismax=True, debug=False):
    xlo = float(xlo)
    xhi = float(xhi)
    R = (math.sqrt(5) - 1) / 2.
    d = R*(xhi - xlo)
    x1 = xlo + d
    x2 = xhi - d
    f1 = f(x1)
    f2 = f(x2)
    iter = 1
    ea = 1.  #100%
    while True:
        if debug:
            print('iter={}, xlo={:.4f}, f(xlo)={:.4f}, x2={:.4f}, f(x2)={:.4f}, '
                  'x1={:.4f}, f(x1)={:.4f}, xhi={:.4f}, f(xhi)={:.4f}, d={:.4f}'
                  .format(iter, xlo, f(xlo), x2, f(x2), x1, f(x1), xhi, f(xhi), d))
        if ea*100 < es100 or iter >= imax:
            break
        d *= R
        xint = xhi - xlo
        if f1 > f2:
            xopt = x1
            fopt = f1
            xlo = x2
            x2 = x1
            x1 = xlo + d
            f2 = f1
            f1 = f(x1)
        else:
            xopt = x2
            fopt = f2
            xhi = x1
            x1 = x2
            x2 = xhi - d
            f1 = f2
            f2 = f(x2)
        if xopt:
            ea = (1. - R) * abs(xint / xopt)
        iter += 1
    #end while
    return xopt
#end gold