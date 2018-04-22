__author__ = 'sarvps'
'''
Author: Sarv Parteek Singh
Course: CISC 601, Scientific Computation 2
HW    : #1, Pr. 13.2, 'Numerical methods for Engineers', 7th edition
Brief : Plot for a given function and determination of its maxima
'''

import numpy as np, math, matplotlib.pyplot as plt
import _optim_u2

def f(x): return -1.5 * x**6 - 2* x**4 + 12 * x

x0 = -10
x1 = 1
x2 = 10

x = np.linspace(x0, x2)
plt.plot(x, f(x))
plt.grid(True)


#f'(x) = -9x**5 - 8x**3 + 12
def df(x): return -9*x**5 - 8*x**3 + 12.

#f''(x) = -45x**4 - 24x**2
def df2(x): return -45*x**4 - 24*x**2
print("Pr. 13.2")
xopt = _optim_u2.newton_wrapper(df, df2, x0=0.2, es100=0.5, debug=True)

print("xopt = {}".format(xopt))
print("fopt = {}".format(f(xopt)))
plt.show()

