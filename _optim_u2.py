
'''
module: _optim_u2.py
author: Luis Paris
description:
- formulas from Chapra's numerical methods textbook
- chapters on Optimization, the unconstrained case
- implemented from algorithms/pseudocode provided
TODO:
Part (A)
- given the segment [x0,x2] and any two points x1,xopt in between,
  fix the parabolic implementation below by considering the actual four cases:
    a) x1 < xopt, f(x1) < f(xopt); discard x0, adjust x0, x1 for next iter
    b) x1 < xopt, f(x1) > f(xopt); discard x2, adjust x1, x2 for next iter
    c) xopt < x1, f(xopt) < f(x1); discard x0, adjust x0, x1 for next iter
    d) xopt < x1, f(xopt) > f(x1); discard x2, adjust x1, x2 for next iter
- make parabolic() search method to work for locating minima too (ismax=False)
Part (B)
- read section 13.3, p.365 on Newton's method for optimum finding then try
  implement it in your favorite language. [Hint: you might want to implement
  it as a wrapper function over the newton's method for root finding already
  implemented in _roots.py from CISC600.]
'''

import _roots
def parabolic(f, x0, x1, x2, es100, imax=1000, ismax=True, debug=False):
    x0, x1, x2 = float(x0), float(x1), float(x2)
    iter = 1
    ea = 1.  #100%
    while True:
        f0, f1, f2 = f(x0), f(x1), f(x2)
        xopt = (f0*(x1**2-x2**2) + f1*(x2**2-x0**2) + f2*(x0**2-x1**2)) \
             / (2 * (f0*(x1-x2) + f1*(x2-x0) + f2*(x0-x1)))
        fopt = f(xopt)
        if debug:
            print('iter={}, x0={:.4f}, f0={:.4f}, x1={:.4f}, f1={:.4f}, x2={:.4f}, f2={:.4f}, xopt={:.4f}, fopt={:.4f}'
                  .format(iter, x0, f0, x1, f1, x2, f2, xopt, f(xopt)))
        if ea*100 < es100 or iter >= imax:
            break
        if xopt: ea = abs(1 - x1/xopt)
        if x1 < xopt and f1 < fopt:
            x0 = x1
            x1 = xopt
        elif x1 < xopt and f1 > fopt:
            x2 = xopt
        elif xopt < x1 and fopt < f1:
            x0 = xopt
        elif xopt < x1 and fopt > f1:
            x2 = x1
            x1 = xopt
        iter += 1
    #end while
    return xopt
#end parabolic()

def newton_wrapper(df, df2, x0, es100=0.5, debug=True):
    return _roots.newton(df, df2, x0, es100)

