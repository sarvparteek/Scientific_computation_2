'''
module: _series.py
author: Luis Paris
description:
- formulas from Chapra's numerical methods textbook
- chapter on truncation errors & the taylor series
- implemented from algorithms/pseudocode provided
'''

import math

def taylor(dfdx, n, xi, h, start=0):
    "computes the nth order taylor series of f(xi+1)"
    #n: order
    #xi: reference point
    #h: step-size (h = xi+1 - xi)
    #dfdx(j,xi): jth derivative of f(xi) for j=0,1,..,n"  [dfdx(0,xi) is f(xi)]
    sum = 0;
    for i in range(start, n+1):  # loop from i=start to n
        sum += dfdx(i, xi) * h**i / math.factorial(i)
    return sum

def R(dfdx, n, xi, h):
    "compute the nth order remainder of the taylor series of f(xi+1)"
    #n: order
    #xi: reference point
    #h: step-size (h = xi+1 - xi)
    return taylor(dfdx, 20, xi, h, n+1)  #we use n=20 here instead of infinity
                                         #also to prevent factorial() overflow

def fwddif1(f, xi, h):
    "computes 1st forward finite difference"
    return (f(xi+h) - f(xi)) / h

def bwddif1(f, xi, h):
    "computes 1st backward finite difference"
    return (f(xi) - f(xi-h)) / h

def cntdif1(f, xi, h):
    "computes 1st centered finite difference"
    return (f(xi+h) - f(xi-h)) / (2*h)

def Af( dfdx1, xi, Ax):
    "computes the error propagation delta f(x)"
    #dfdx1: 1st derivative of f(x)
    #xi: reference point
    #Ax: delta x, the given error estimate
    return math.fabs(dfdx1(xi)) * Ax
