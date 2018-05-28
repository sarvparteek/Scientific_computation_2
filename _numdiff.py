'''
module: _numdiff.py
author: Luis Paris
description:
- formulas from Chapra's numerical methods textbook
- chapters on numeric differentiation
- implemented from algorithms/pseudocode provided
'''

def fwddif1h(f, xi, h):
    "computes 1st forward finite difference with higher accuracy"
    return (-f(xi+2*h) + 4*f(xi+h) - 3*f(xi)) / (2*h)

def bwddif1h(f, xi, h):
    "computes 1st backward finite difference with higher accuracy"
    return (f(xi-2*h) - 4*f(xi-h) + 3*f(xi)) / (2*h)

def cntdif1h(f, xi, h):
    "computes 1st centered finite difference with higher accuracy"
    return (-f(xi+2*h) + 8*f(xi+h) - 8*f(xi-h) + f(xi-2*h)) / (12*h)