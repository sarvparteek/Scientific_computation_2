
'''
module: _numinteq2_todo.py
author: Luis Paris
description:
- formulas from Chapra's numerical methods textbook
- chapters on numeric integration for continuous functions
- implemented from algorithms/pseudocode provided
'''

import numpy as np

def simpeq(f, x0, xn, n):
    h = (xn - x0) / float(n)
    x = x0
    sum = f(x)
    for i in range(1, n-1, 2):
        x += 2*h
        sum += 4*f(x - h) + 2*f(x)
    sum += 4*f(x + h) + f(xn)
    return h*sum/3.
#end simpeq()

xpts = []  #needed for displaying interpolation points/lines in ex-quadapt-todo.py

def quadapt(f, x0, xn, tol=1e-6, debug=False):
    def qstep(x0, xn, indent):  #indent used in debug mode only (for better visualization of recursive calls)
        if debug:
            xpts.append([x0, xn])
            #TODO: display indented qstep() recursive calls
        #end if
        I1 = simpeq(f, x0, xn, n=2)
        I2 = simpeq(f, x0, xn, n=4)
        if abs(I2 - I1) <= tol:
            I = I2 + (I2 - I1)/15
        else:
            xmid = (x0+xn)/2.
            Ia = qstep(x0, xmid, indent)
            Ib = qstep(xmid, xn, indent)
            I = Ia + Ib
        if debug:
            #TODO: display intended qstep() return value
            print('')
        #end if
        return I
    #end qstep()
    if debug: print("quadapt({}, {}) started".format(x0, xn))
    I = qstep(x0, xn, indent=4)
    if debug: print("--> I = {}".format(I)); print("quadapt({}, {}) ended\n".format(x0, xn))
    return I
#end quadapt()