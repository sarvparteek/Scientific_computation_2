#script: ex-romberg-todo.py
#author: Luis Paris

import math
import _plot, _numinteq

def f(x): return (x + 1/x) **2 ;

#true integral of f(x)
def Itf(x): return (1/3 * x**3) - 1/x + 2*x;

#evaluation range
x0 = 1
xn = 2

#plot function
_plot.graph(f, xl=x0, xu=xn, title="f(x) = (x + 1/x)^2 ")

#true value of integral of f(x) between x0 and xn
tv = Itf(xn) - Itf(x0)
print("tv = {}".format(tv))

#approx. value of integral of f(x) using romberg's algorithm
av = _numinteq.romberg(f, x0, xn, es100=.5, tv=tv, debug=True)
print("av = {}".format(av))

et = (tv-av)/tv;
print("et = {}".format(et));