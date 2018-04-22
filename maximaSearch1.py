__author__ = 'sarvps'
'''
Author: Sarv Parteek Singh
Course: CISC 601, Scientific Computation 2
HW    : #1, Pr. 13.4, 'Numerical methods for Engineers', 7th edition
Brief : Plot for a given function and determination of its maxima
'''

import numpy as np, math, matplotlib.pyplot as plt
import _optim_u2

def f(x): return -1.5 * x**6 - 2* x**4 + 12 * x

x0 = 0
x1 = 1
x2 = 2

x = np.linspace(x0, x2)
plt.plot(x, f(x))
plt.grid(True)


print("Pr. 13.4")
xopt = _optim_u2.parabolic(f, x0, x1, x2, es100=.05, debug=True)

print('\nxopt = {:.4f}'.format(xopt))
print('f(xopt)={:.4f}'.format(f(xopt)))

plt.show()