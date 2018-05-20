#script: integral1.py
#author: Sarv Parteek Singh
#Solves Pr21.1 from Chapra's book, 'Numerical Methods for Engineers', 7th Edition

import numpy as np, matplotlib.pyplot as plt
import _numint, _numint2, _polyreg, _poly

def f(x): return 6 + np.cos(x)

x0 = 0
xn = 0.5 * np.pi

# ------------- Single application of Trapezoidal rule ------------------------------------------------
n = 1  #only 1 segment needed for single application of trapezoidal rule
print("----- Single application of Trapezoidal rule -------")

#compute step size
h = (xn - x0) / float(n)

#generate x,y points
axpts = np.linspace(x0, xn, n+1)  #generate n+1 points in x, equally spaced between x0,xn
#axpts = np.arange(x0, xn+h, h)  #this is another way, but less accurate than np.linspace()
print("xpts = {}".format(axpts))
aypts = f(axpts)  #generate n+1 points in y, between f(x0),f(xn)
print("ypts = {}".format(aypts))

#apply single trapezoidal rule to estimate closed integral between x0,xn
av = _numint.trap(aypts[0], aypts[n], h=xn-x0)
print("av = {}".format(av))

#true integral of f(x)
def Itf(x): return 6*x + 3*np.sin(x)

#true value of integral of f(x) between x0 and xn
tv = Itf(xn) - Itf(x0)
print("tv = {}".format(tv))

#compute and display true errors
print("Et = {}".format(tv - av))
print("et = {:%}".format(1 - av/tv))

#estimate plotting x range
xlo = x0 - (xn-x0)/50.
xhi = xn + (xn-x0)/50.

#plot function f(x)
xpts = np.linspace(xlo, xhi, 1000)  #1000 pts for smooth effect
plt.plot(xpts, f(xpts), 'b', label='true function')

#fill area for integral estimate
plt.fill_between(axpts, aypts, facecolor='g', alpha=.2, edgecolor='g', label='integral estimate')

#fill area for error
xpts = np.linspace(x0, xn, 1000)
plt.fill(xpts, f(xpts), facecolor='r', alpha=.2, edgecolor='none', label='error')

#show plot w/ title, legend, etc.
plt.title('Single application of trapezoidal integration rule')
plt.legend(loc="upper left", shadow=True)
plt.xlabel('x-axis'); plt.ylabel('y-axis')
plt.xlim(xlo, xhi)
plt.grid(True)
plt.show()

# ------------ Multiple application of Trapezoidal rule -------------------
print("-------------- Multiple application of Trapezoidal rule --------------------")
for n in [2,4]:  #n >= 2 segments needed for multiple application of trapezoidal rule
    print("\nn = {}:\n".format(n))

    #compute step size
    h = (xn - x0) / float(n)

    #generate x,y points
    axpts = np.linspace(x0, xn, n+1)  #generate n+1 points in x, equally spaced between x0,xn
    #axpts = np.arange(x0, xn+h, h)  #this is another way, but less accurate than np.linspace()
    print("xpts = {}".format(axpts))
    aypts = f(axpts)  #generate n+1 points in y, between f(x0),f(xn)
    print("ypts = {}".format(aypts))

    #apply multiple trapezoidal rules to estimate closed integral between x0,xn
    av = _numint.trapm(aypts, h, n)
    print("av = {}".format(av))

    #true value of integral of f(x) between x0 and xn
    tv = Itf(xn) - Itf(x0)
    print("tv = {}".format(tv))

    #compute and display true errors
    print("Et = {}".format(tv - av))
    print("et = {:%}".format(1 - av/tv))

    #estimate plotting x range
    xlo = x0 - (xn-x0)/50.
    xhi = xn + (xn-x0)/50.

    #plot function f(x)
    m = 1000  #number of points for smooth plotting effect
    xpts = np.linspace(xlo, xhi, m)
    plt.plot(xpts, f(xpts), 'b', label='true function')

    #draw vertical segments & interpolation points for integral estimate
    #TO DO...

    #fill area for integral estimate
    plt.fill_between(axpts, aypts, facecolor='g', alpha=.2, edgecolor='g', label='integral estimate')

    #fill area for error
    xpts = np.linspace(x0, xn, m)
    for i in range(n):
        xrange = xpts[int(i*m/n): int((i+1)*m/n)]
        plt.fill(xrange, f(xrange), facecolor='r', alpha=.2, edgecolor='none',
                 label=None if i else 'error = {:.4%}'.format(1-av/tv))
    #end for

    #show plot w/ title, legend, etc.
    plt.title('Multiple application of trapezoidal integration rule')
    plt.legend(loc="upper left", shadow=True)
    plt.xlabel('x-axis'); plt.ylabel('y-axis')
    plt.xlim(xlo, xhi)
    plt.grid(True)
    plt.show()

#end for

# -------------------- Single application of Simpson's 1/3 rule ----------------------------
n = 2  #two segments needed for single application of simpson's 1/3 rule
print("--------------- Single application of Simpson's 1/3 rule ---------------")

#compute step size
h = (xn - x0) / float(n)

#generate x,y points
axpts = np.linspace(x0, xn, n+1)  #generate n+1 points in x, equally spaced between x0,xn
#axpts = np.arange(x0, xn+h, h)  #this is another way, but less accurate than np.linspace()
print("xpts = {}".format(axpts))
aypts = f(axpts)  #generate n+1 points in y, between f(x0),f(xn)
print("ypts = {}".format(aypts))

#apply single simpson's 1/3 rule to estimate closed integral between x0,xn
av = _numint2.simp13(aypts[0], aypts[1], aypts[2], h)
print("av = {}".format(av))

#true value of integral of f(x) between x0 and xn
tv = Itf(xn) - Itf(x0)
print("tv = {}".format(tv))

#compute and display true errors
print("Et = {}".format(tv - av))
print("et = {:%}".format(1 - av/tv))

#estimate plotting x range
xlo = x0 - (xn-x0)/50.
xhi = xn + (xn-x0)/50.

#plot function f(x)
m = 1000  #number of points for smooth plotting effect
xpts = np.linspace(xlo, xhi, m)
plt.plot(xpts, f(xpts), 'b', label='true function')

#draw vertical segments & interpolation points for integral estimate
#TO DO...

#fill area for integral estimate
xpts = np.linspace(x0, xn, m)
parabolic_coefs = _polyreg.curvefit(axpts, aypts, order=2)
ypts = _poly.eval(parabolic_coefs, xpts)
plt.fill_between(xpts, ypts, facecolor='g', alpha=.2, edgecolor='g', label='integral estimate')

#fill area for error
#TO DO...

#show plot w/ title, legend, etc.
plt.title("Single application of Simpson's 1/3 integration rule")
plt.legend(loc="upper left", shadow=True)
plt.xlabel('x-axis'); plt.ylabel('y-axis')
plt.xlim(xlo, xhi)
plt.grid(True)
plt.show()

# ------------------- Multiple segments of Simpson's 1/3 rule -----------------------------------------
print(" ---------------- Multiple segments of Simpson's 1/3 rule -------------------")
for n in [4,12]:  #n >= 2 segments needed for multiple applications of simpson's 1/3 rule
    print("\nn = {}:\n".format(n))

    #compute step size
    h = (xn - x0) / float(n)

    #generate x,y points
    axpts = np.linspace(x0, xn, n+1)  #generate n+1 points in x, equally spaced between x0,xn
    #axpts = np.arange(x0, xn+h, h)  #this is another way, but less accurate than np.linspace()
    print("xpts = {}".format(axpts))
    aypts = f(axpts)  #generate n+1 points in y, between f(x0),f(xn)
    print("ypts = {}".format(aypts))

    #apply multiple simpson's 1/3 rule to estimate closed integral between x0,xn
    av = _numint2.simp13m(aypts, h, n)
    print("av = {}".format(av))

    #true value of integral of f(x) between x0 and xn
    tv = Itf(xn) - Itf(x0)
    print("tv = {}".format(tv))

    #compute and display true errors
    print("Et = {}".format(tv - av))
    print("et = {:%}".format(1 - av/tv))

    #estimate plotting x range
    xlo = x0 - (xn-x0)/50.
    xhi = xn + (xn-x0)/50.

    #plot function f(x)
    m = 1000  #number of points for smooth plotting effect
    xpts = np.linspace(xlo, xhi, m)
    plt.plot(xpts, f(xpts), 'b', label='true function')

    #draw vertical segments & interpolation points for integral estimate
    #TO DO...

    #fill area for integral estimate
    #TO DO...

    #fill area for error
    #TO DO...

    #show plot w/ title, legend, etc.
    plt.title("Multiple application of Simpson's 1/3 integration rule")
    plt.legend(loc="upper left", shadow=True)
    plt.xlabel('x-axis'); plt.ylabel('y-axis')
    plt.xlim(xlo, xhi)
    plt.grid(True)
    plt.show()

#end for

# -------------------- Single application of Simpson's 3/8 rule ----------------------------
n = 3  #three segments needed for single application of simpson's 3/8 rule
print("--------------- Single application of Simpson's 3/8 rule ---------------")

#compute step size
h = (xn - x0) / float(n)

#generate x,y points
axpts = np.linspace(x0, xn, n+1)  #generate n+1 points in x, equally spaced between x0,xn
#axpts = np.arange(x0, xn+h, h)  #this is another way, but less accurate than np.linspace()
print("xpts = {}".format(axpts))
aypts = f(axpts)  #generate n+1 points in y, between f(x0),f(xn)
print("ypts = {}".format(aypts))

#apply single simpson's 1/3 rule to estimate closed integral between x0,xn
av = _numint2.simp38(aypts[0], aypts[1], aypts[2], aypts[3], h)
print("av = {}".format(av))

#true value of integral of f(x) between x0 and xn
tv = Itf(xn) - Itf(x0)
print("tv = {}".format(tv))

#compute and display true errors
print("Et = {}".format(tv - av))
print("et = {:%}".format(1 - av/tv))

#estimate plotting x range
xlo = x0 - (xn-x0)/50.
xhi = xn + (xn-x0)/50.

#plot function f(x)
m = 1000  #number of points for smooth plotting effect
xpts = np.linspace(xlo, xhi, m)
plt.plot(xpts, f(xpts), 'b', label='true function')

#draw vertical segments & interpolation points for integral estimate
#TO DO...

#fill area for integral estimate
xpts = np.linspace(x0, xn, m)
parabolic_coefs = _polyreg.curvefit(axpts, aypts, order=2)
ypts = _poly.eval(parabolic_coefs, xpts)
plt.fill_between(xpts, ypts, facecolor='g', alpha=.2, edgecolor='g', label='integral estimate')

#fill area for error
#TO DO...

#show plot w/ title, legend, etc.
plt.title("Single application of Simpson's 3/8 integration rule")
plt.legend(loc="upper left", shadow=True)
plt.xlabel('x-axis'); plt.ylabel('y-axis')
plt.xlim(xlo, xhi)
plt.grid(True)
plt.show()

# ------------------- Multiple segments of Simpson's 3/8 rule -----------------------------------------
print(" ---------------- Multiple segments of Simpson's 3/8 rule -------------------")
for n in [5,13]:  #n >= 2 segments needed for multiple applications of simpson's 1/3 rule
    print("\nn = {}:\n".format(n))

    #compute step size
    h = (xn - x0) / float(n)

    #generate x,y points
    axpts = np.linspace(x0, xn, n+1)  #generate n+1 points in x, equally spaced between x0,xn
    #axpts = np.arange(x0, xn+h, h)  #this is another way, but less accurate than np.linspace()
    print("xpts = {}".format(axpts))
    aypts = f(axpts)  #generate n+1 points in y, between f(x0),f(xn)
    print("ypts = {}".format(aypts))

    #apply multiple simpson's 1/3 rule to estimate closed integral between x0,xn
    av = _numint2.simp38m(aypts, h, n)
    print("av = {}".format(av))

    #true value of integral of f(x) between x0 and xn
    tv = Itf(xn) - Itf(x0)
    print("tv = {}".format(tv))

    #compute and display true errors
    print("Et = {}".format(tv - av))
    print("et = {:%}".format(1 - av/tv))

    #estimate plotting x range
    xlo = x0 - (xn-x0)/50.
    xhi = xn + (xn-x0)/50.

    #plot function f(x)
    m = 1000  #number of points for smooth plotting effect
    xpts = np.linspace(xlo, xhi, m)
    plt.plot(xpts, f(xpts), 'b', label='true function')

    #draw vertical segments & interpolation points for integral estimate
    #TO DO...

    #fill area for integral estimate
    #TO DO...

    #fill area for error
    #TO DO...

    #show plot w/ title, legend, etc.
    plt.title("Multiple application of Simpson's 3/8 integration rule")
    plt.legend(loc="upper left", shadow=True)
    plt.xlabel('x-axis'); plt.ylabel('y-axis')
    plt.xlim(xlo, xhi)
    plt.grid(True)
    plt.show()

#end for