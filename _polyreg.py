
'''
module: _polyreg.py
author: Luis Paris
description:
- formulas from Chapra's numerical methods textbook
- chapter on linear and polynomial regression
- implemented from algorithms/pseudocode provided
'''

import numpy as np
import _linalg2

#polynomial regression implementation (based on p.476, Chapra's 7th ed.)
def curvefit(x, y, order=1, debug=False):
    "fits curve to given x,y points using polynomial regression"
    m = order + 1
    n = min(len(x), len(y))
    if n < m:
        m = n
    A = np.zeros((m,m))
    b = np.zeros(m)
    for i in range(m):
        for j in range(i+1):
            k = i + j
            sum = 0.0
            for l in range(n):
                sum += x[l]**k
            A[i,j] = A[j,i] = sum
        #end for
        sum = 0.0
        for l in range(n):
            sum += y[l] * x[l]**i
        b[i] = sum
    #end for
    if debug: print("A =\n{}".format(A))
    if debug: print("b =\n{}".format(b))
    return np.linalg.solve(A, b)  #_linalg2.gauss(A, b, tol=1e-9)
#end curvefit()