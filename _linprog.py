
'''
module: _linprog.py
author: Luis Paris
description:
- formulas from Chapra's numerical methods textbook
- chapters on Constrained Optimization and Linear Programming
- implemented from algorithms/pseudocode provided
comments:
- to install "scipy" python library on Windows:
  * close your Python editor - don't install from PyCharm editor
  * download numpy+mkl (numpy w/ math kernel library) first:
    http://www.lfd.uci.edu/~gohlke/pythonlibs/#numpy
    (choose according to your python version and installation)
    numpy-1.12.1+mkl-cp27-cp27m-win32.whl (Python 2.x 32-bit)
    numpy-1.12.1+mkl-cp27-cp27m-win_amd64.whl (Python 2.x 64-bit)
    numpy-1.12.1+mkl-cp34-cp34m-win32.whl (Python 3.x 32-bit)
    numpy-1.12.1+mkl-cp34-cp34m-win_amd64.whl (Python 3.x 64-bit)
  * download scipy:
    http://www.lfd.uci.edu/~gohlke/pythonlibs/#scipy
    (choose according to your python version and installation)
    scipy-0.19.0-cp27-cp27m-win32.whl (Python 2.x 32-bit)
    scipy-0.19.0-cp27-cp27m-win_amd64.whl (Python 2.x 64-bit)
    scipy-0.19.0-cp34-cp34m-win32.whl (Python 3.x 32-bit)
    scipy-0.19.0-cp34-cp34m-win_amd64.whl (Python 3.x 64-bit)
  * open command prompt, go to download folder, and install:
    cd <download-folder>
    pip install <numpy-package-name.whl>
    pip install <scipy-package-name.whl>
'''

import numpy as np, scipy.optimize as optim

def simplex(Z_coefs, constraints, bounds, ismax=True, debug=False):
    "returns optimum values for the activities vector x[0]...x[n-1] that optimizes objective-function Z"
    #Z_coefs: coefficients for objective function Z
    #    Z = Z_coefs[0]*x[0] + ... + Z_coefs[n-1]*x[n-1]
    #constraints: augmented n,n+1 matrix w/ constraint inequalities
    #    constraints[:,0]*x[0] + ... + constraints[:,n-1]*x[n-1] <= constraints[:,-1]
    #bounds: bounds for activities vector x[0]...x[n-1]:
    #   bounds[i,0] <= x[i] <= bounds[i,1]  (i=0,...,n-1)
    #ismax: True, optimmizes for maximum; False, optimizes for minimum
    #debug: display stats
    Z_coefs = np.array(Z_coefs, dtype=float)          #make sure list params
    constraints = np.array(constraints, dtype=float)  #  are numpy arrays
    bounds = np.array(bounds, dtype=float)            #
    A = constraints[:,:-1]  #split augmented matrix into matrix A
    b = constraints[:,-1]   #  and into vector b
    t_bounds = tuple([tuple(x) for x in bounds])  #convert bounds matrix to tuples
    res = optim.linprog(
        c = -Z_coefs if ismax else Z_coefs,
        A_ub = A, b_ub = b,
        bounds = t_bounds,
        method = "simplex")
    if debug: print(res)
    return res.x
#end simplex()