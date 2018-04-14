'''
module: _error.py
author: Luis Paris
description:
- formulas from Chapra's numerical methods 7th ed.
- chapter on approximations & round-off errors
- implemented from algorithms/pseudocode provided
'''

import math

def Et(tv, av):
    "computes true error"
    #tv: true value
    #av: approximate value
    return tv - av

def Ea(cv, pv):
    "computes approximate error"
    #cv: current value
    #pv: previous value
    return cv - pv

def et(tv, av):
    "computes true relative error"
    #tv: true value
    #av: approximate value
    return 1 - av / tv

def ea(cv, pv):
    "computes approximate relative error"
    #cv: current value
    #pv: previous value
    return 1 -  pv / cv

def ea100(cv, pv):
    "computes approximate relative error (%)"
    #cv: current value
    #pv: previous value
    return (1 -  pv / cv) * 100

def es(sigdigs):
    "computes error tolerance"
    #n: number of significant digits
    return .5 * 10**(-sigdigs)

def es100(sigdigs):
    "computes error tolerance (%)"
    #sigdigs: number of significant digits
    return .5 * 10**(2-sigdigs)

def sigdigs(es):
    "computes # of significant digits"
    #es: error tolerance
    return math.log10(0.5 / es)

def sigdigs100(es100):
    "computes # of significant digits"
    #es: error tolerance (%)
    return math.log10(0.5 / es100) + 2
