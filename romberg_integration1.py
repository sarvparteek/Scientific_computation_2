#script: ex-romberg-todo.py
#author: Luis Paris

import math
import _plot, _numinteq

def f(x): return x * math.exp(2*x);

#true integral of f(x)
def Itf(x): return .25 * math.exp(2*x) * (2*x - 1);

#evaluation range
x0 = 0
xn = 3

#plot function
_plot.graph(f, xl=x0, xu=xn, title="f(x) = x.e^2x")

#true value of integral of f(x) between x0 and xn
tv = Itf(xn) - Itf(x0)
print("tv = {}".format(tv))

#approx. value of integral of f(x) using romberg's algorithm
av = _numinteq.romberg(f, x0, xn, es100=.5, tv=tv, debug=True)
print("av = {}".format(av))

et = (tv-av)/tv;
print("et = {}".format(et));