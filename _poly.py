'''
module: _poly.py
author: Luis Paris
description:
- formulas from Chapra's numerical methods textbook
- chapter on roots of polynomials
- implemented from algorithms/pseudocode provided
'''

import numpy as np

def eval(p, x):
    "evaluates polynomial p at x"
    #p: polynomial
    #x: actual x value
    sum = 0
    for i in range(len(p)):
        sum += p[i] * (x ** i)
    return sum
#end eval()

#deflate routine, page 181
def defl(p, t):
    "deflates polynomial (divides by monomial x-t)"
    #p: polynomial
    #t: estimate root from monomial (x - t)
    n = len(p) - 1
    r = float(p[n])
    q = np.array(p[:-1], dtype=float)
    for i in range(n-1, -1, -1):
        s = p[i]
        q[i] = r
        r = s + r * t
    #end for
    return q, np.array([r])
#end defl()

#poldiv() routine, page 182
def div(p, d):
    "divides polynomial p with (lower-order) polynomial d"
    n, m = len(p) - 1, len(d) - 1
    r = np.array(p, dtype=float)
    q = np.zeros(n+1, dtype=float)
    for k in range(n-m, -1, -1):
        q[k+1] = r[m+k] / d[m]
        for j in range(m+k-1, k-1, -1):
            r[j] -= q[k+1] * d[j-k]
    return q[1:n-m+2], r[:m]
#end div()

def tostr(p):
    "converts polynomial p in array form to a string"
    s = ""
    n = len(p) - 1
    x = abs(p[n])
    if n == 0 or (float(x) != 0 and float(x) != 1):
        s += "{}{}".format(p[n], "*" if n else "")
    elif float(p[n]) == -1: s += "-"
    if n: s += "x"
    if p[n]: s += "{} ".format("**" + str(n) if n > 1 else "")
    for i in range(n-1, -1, -1):
        x = abs(p[i])
        if p[i]:
            s += "{} {}".format("-" if p[i] < 0 else "+",
                                str(x) if float(x) != 1 else "")
            if x > 1: s += "{}".format("*" if i else "")
            if i: s += "x"
            s += "{}".format("**" + str(i) + " " if i > 1 else ""
                             if i == 0 and float(x) == 1 else " ")
        if i == 0 and float(x) == 1: s += str(x)
    return s.strip()
#end tostr()
