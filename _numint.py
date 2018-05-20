'''
module: _numint.py
author: Luis Paris
description:
- formulas from Chapra's numerical methods textbook
- implements discrete single/multi segment trapezoid rules
  (1st order newton-cotes integration formulas)
- chapters on numerical integration for discrete functions
- implemented from algorithms/pseudocode provided
'''

def trap(f0, f1, h):
    return h * (f0 + f1) / 2
#end trap()

def trapm(fpts, h, n):
    sum = fpts[0]
    for i in range(1,n):
        sum += 2*fpts[i]
    sum += fpts[n]
    return h * sum / 2
#end trapm()