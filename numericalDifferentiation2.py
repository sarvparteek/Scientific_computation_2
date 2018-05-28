#script: ex-23.1.py
#author: Sarv Parteek Singh
#Pr. 23.2, 'Numerical Methods' by Chapra, 7th edition

import _series
import _numdiff
import math, _plot

def f(x): return math.log(x)

def dfdx(i,x):
    return {
        0: f(x),
        1: 1/x,
        2: -1/(x**2),
        3: 2/(x**3),
        4: -6/(x**4)
    }.get(i,0)

xi = 25
h = 2

#plot function
x0 = 20;
xn = xi + 1;
_plot.graph(f, xl=x0, xu=xn, title="f(x) = log(x)")
def df(x): return dfdx(1,x)
_plot.graph(df,xl=x0, xu=xn, title="f(x) = 1/x")

tv = dfdx(1,xi)
print("tv = {}".format(tv))

print("************* Regular 1st finite differences ****************")

fav = _series.fwddif1(f, xi, h)
bav = _series.bwddif1(f, xi, h)
cav = _series.cntdif1(f, xi, h)
print("Forward av = {}\nBackward av = {}\nCentered av = {}".format(fav, bav, cav))

etf = abs(1 - fav/tv)
etb = abs(1 - bav/tv)
etc = abs(1 - cav/tv)
print("Forward et = {:%}\nBackward et = {:%}\nCentered et = {:%}".format(etf, etb, etc))

print("************* High-accuracy 1st finite differences ************")

fav = _numdiff.fwddif1h(f, xi, h)
bav = _numdiff.bwddif1h(f, xi, h)
cav = _numdiff.cntdif1h(f, xi, h)
print("Forward av = {}\nBackward av = {}\nCentered av = {}".format(fav, bav, cav))

etf = abs(1 - fav/tv)
etb = abs(1 - bav/tv)
etc = abs(1 - cav/tv)
print("Forward et = {:%}\nBackward et = {:%}\nCentered et = {:%}".format(etf, etb, etc))