'''
module: _roots.py
author: Luis Paris
description:
- formulas from Chapra's numerical methods textbook
- chapters on bracketing/open methods for root finding
- implemented from algorithms/pseudocode provided
'''

#bracketing methods... (chapter 5)

def bisect(f, xl, xu, es100, imax=1000, tv=0, debug=False, tab=10):
    "locates single root using bisection method"
    #f: function f(x)
    #xl,xu: lower,upper x brackets
    #es100: error tolerance in percentage (0-100)
    #imax: max # of iterations
    #tv: true value of root
    #tab: tabulated output (0: disable, n: spaces per tab)
    iter = 0
    x0 = xl
    if debug and tab:
        print("{:<{t}}{:<{t}}{:<{t}}{:<{t}}{:<{t}}{:<{t}}"
              .format("iter","xl","xu","xr","ea","et",t=tab))
    while True:
        xr = (xl + xu) / 2.0
        if xr: ea = abs(1 - x0 / xr)
        iter += 1
        if debug:
            print(("{:<{t}}{:<{t}f}{:<{t}f}{:<{t}f}{:<{t}.3%}{:<{t}.3%}" if tab else
                   "iter={}, xl={:f}, xu={:f}, xr={:f}, ea={:.3%}, et={:.3%}")
                  .format(iter,xl,xu,xr,ea,abs(1-xr/tv) if tv else 0,t=tab))
        test = f(xl) * f(xr)
        if test < 0: xu = xr
        elif test > 0: xl = xr
        else: ea = 0.0
        if ea*100 < es100 or iter >= imax:
            break
        x0 = xr
    return xr
#end bisect

def falsepos(f, xl, xu, es100, imax=1000, tv=0, debug=False, tab=10):
    "locates single root using false position method"
    #f: function f(x)
    #xl,xu: lower,upper x brackets
    #es100: error tolerance in percentage (0-100)
    #imax: max # of iterations
    #tv: true value of root
    #tab: tabulated output (0: disable, n: spaces per tab)
    iter = 0
    x0 = xl
    if debug and tab:
        print("{:<{t}}{:<{t}}{:<{t}}{:<{t}}{:<{t}}{:<{t}}"
              .format("iter","xl","xu","xr","ea","et",t=tab))
    while True:
        xr = (xl*f(xu) - xu*f(xl)) / (f(xu) - f(xl))
        if xr: ea = abs(1 - x0 / xr)
        iter += 1
        if debug:
            print(("{:<{t}}{:<{t}f}{:<{t}f}{:<{t}f}{:<{t}.3%}{:<{t}.3%}" if tab else
                   "iter={}, xl={:f}, xu={:f}, xr={:f}, ea={:.3%}, et={:.3%}")
                  .format(iter,xl,xu,xr,ea,abs(1-xr/tv) if tv else 0,t=tab))
        test = f(xl) * f(xr)
        if test < 0: xu = xr
        elif test > 0: xl = xr
        else: ea = 0.0
        if ea*100 < es100 or iter >= imax:
            break
        x0 = xr
    return xr
#end falsepos()

#open methods... (chapter 6)

import _series

def fixpt(f, x0, es100, imax=1000, tv=0, debug=False, tab=10):
    "locates single root using fixed point method"
    #f: function f(x)
    #x0: initial guess of x
    #es100: error tolerance in percentage (0-100)
    #imax: max # of iterations
    #tv: true value of root
    #tab: tabulated output (0: disable, n: spaces per tab)
    iter = 0
    if debug and tab:
        print("{:<{t}}{:<{t}}{:<{t}}{:<{t}}"
              .format("iter","xr","ea","et",t=tab))
    while True:
        xr = f(x0) + x0
        if xr: ea = abs(1 - x0 / xr)
        iter += 1
        if debug:
            print(("{:<{t}}{:<{t}f}{:<{t}.3%}{:<{t}.3%}" if tab else
                   "iter={}, xr={:f}, ea={:.3%}, et={:.3%}")
                  .format( iter,xr,ea,abs(1-xr/tv) if tv else 0,t=tab))
        if ea*100 < es100 or iter >= imax:
            break
        x0 = xr
    return xr
#end fixpt()

def newton(f, df, x0, es100, imax=1000, tv=0, debug=True, tab=10):
    "locates single root using newton-raphson method"
    #f: function f(x)
    #df: f'(x) = derivative of f(x)
    #es100: error tolerance in percentage (0-100)
    #imax: max # of iterations
    #tv: true value of root
    #tab: tabulated output (0: disable, n: spaces per tab)
    iter = 0
    if debug and tab:
        print("{:<{t}}{:<{t}}{:<{t}}{:<{t}}"
              .format("iter","xr","ea","et",t=tab))
    while True:
        xr = x0 - f(x0) / df(x0)
        if xr: ea = abs(1 - x0 / xr)
        iter += 1
        if debug:
            print(("{:<{t}}{:<{t}f}{:<{t}.3%}{:<{t}.3%}" if tab else
                   "iter={}, xr={:f}, ea={:.3%}, et={:.3%}")
                  .format( iter,xr,ea,abs(1-xr/tv) if tv else 0,t=tab))
        if ea*100 < es100 or iter >= imax:
            break
        x0 = xr
    return xr
#end newton()

def secant(f, x0, x1, es100, imax=1000, tv=0, debug=False, tab=10):
    "locates single root using secant method"
    #f: function f(x)
    #x0: first root guess (xi)
    #x1: second root guess (xi-1)
    #es100: error tolerance in percentage (0-100)
    #imax: max # of iterations
    #tv: true value of root
    #tab: tabulated output (0: disable, n: spaces per tab)
    iter = 0
    if debug and tab:
        print("{:<{t}}{:<{t}}{:<{t}}{:<{t}}"
              .format("iter","xr","ea","et",t=tab))
    while True:
        xr = x0 - f(x0) * (x1 - x0) / (f(x1) - f(x0))
        if xr: ea = abs(1 - x0 / xr)
        iter += 1
        if debug:
            print(("{:<{t}}{:<{t}f}{:<{t}.3%}{:<{t}.3%}" if tab else
                   "iter={}, xr={:f}, ea={:.3%}, et={:.3%}")
                  .format( iter,xr,ea,abs(1-xr/tv) if tv else 0,t=tab))
        if ea*100 < es100 or iter >= imax:
            break
        x0 = x1
        x1 = xr
    return xr
#end secant()
