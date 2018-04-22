
'''
module: _optim_u3.py
author: Luis Paris
description:
- formulas from Chapra's numerical methods textbook
- chapters on Optimization, the unconstrained case
- implemented from algorithms/pseudocode provided
'''

import random

def random_search(f, xl, xu, yl, yu, imax=10000, imul=1000, ismax=True, debug=False):
    "locates optimum (maximum if ismax is True, else minimum)"
    #f: function f(x)
    #xl,xu: lower,upper x brackets
    #yl,yu: lower,upper y brackets
    #imax: max # of iterations
    #imul: multiple of iterations to display
    #ismax: locate maximum if True, else locate minimum
    #debug: display stats for each iteration
    x = xopt = random.uniform(xl, xu)
    y = yopt = random.uniform(yl, yu)
    fopt = f(x, y)
    for i in range(1, imax + 1):
        x = random.uniform(xl, xu)
        y = random.uniform(yl, yu)
        fxy = f(x, y)
        if (ismax and fxy > fopt) or (not ismax and fxy < fopt):
            fopt = fxy
            xopt = x
            yopt = y
        if debug and i % imul == 0:
            print("i={}, x={}, y={}, f(x, y) = {}".format(i, xopt, yopt, fopt))
    return xopt, yopt
#end random_search()