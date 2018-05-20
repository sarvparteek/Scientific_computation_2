#script: ex-15.1b-todo.py (modified exercise 15.1, p.391)
#author: Luis Paris
#tests linear programming methods for constrained optimization:
# - graphics method
# - simplex method

import numpy as np, matplotlib.pyplot as plt
import _linalg2, _linprog, math

#objective function to maximize
#Z = 1.75x + 1.25y
Z_coefs = [1.75, 1.25]

#constraints
#1.2x + 2.25y <= 14
#x + 1.1y <= 8
#2.5x + y <= 9
constraints = [[1.2, 2.25, 14],
               [1, 1.1, 8],
               [2.5,  1, 9],
               ]
#bounds
#x >= 0
#y >= 0
bounds = [[0, math.inf],
          [0, math.inf]]

#helper functions
def Z_func(x_vector): return sum(Z_coefs * x_vector)  #compute objective function given x_vector
def y_Z(xpts, Z): return (Z - Z_coefs[0] * xpts) / Z_coefs[1]  #solve Z for y, so we can plot it
def Y_cts(i, x): return (constraints[i,-1] - constraints[i,0]*x) / constraints[i,1]
def X_cts(i, y): return (constraints[i,-1] - constraints[i,1]*y) / constraints[i,0]
def get_feasible_solution_space():
    n = n_constraints
    xpts, ypts = [bounds[0][0], X_cts(1, bounds[1][0])], [bounds[1][0], bounds[1][0]]
    if n >= 3:
        x_vector = _linalg2.gauss( constraints[1:3, :-1], constraints[1:3, -1])
        xpts += [x_vector[0]]; ypts += [x_vector[1]]
    x_vector = _linalg2.gauss( constraints[0:n:n-1, :-1], constraints[0:n:n-1, -1])
    xpts += [x_vector[0]]; ypts += [x_vector[1]]
    xpts += [X_cts(0, bounds[1][1])]; ypts += [bounds[1][1]]
    xpts += [bounds[0][0]]; ypts += [bounds[1][1]]
    return xpts, ypts
#end FSS()
def plot(title, x_vecsol=None):  #plot constraints, bounds, and objective function for given Z
    plt.title('{}\nobjective function: Z = {}x + {}y = {}'.format(title, Z_coefs[0], Z_coefs[1], Z))
    for i in range(n_constraints):
        plt.plot(xpts, y_cts[i], '--b', label=None if i else 'constraints')
        plt.annotate("constraint {}".format(i),
             xy=(.5, Y_cts(i,.5)), xytext=(.5+.6, Y_cts(i,.5)+.6),
             arrowprops=dict(width=.25, headwidth=4, headlength=9))
    plt.plot(x_bds[0], ypts, '--y'); plt.plot(x_bds[1], ypts, '--y', label='x bounds')
    plt.plot(xpts, y_bds[0], '--g'); plt.plot(xpts, y_bds[1], '--g', label='y bounds')
    xpts_, ypts_ = get_feasible_solution_space()
    plt.fill(xpts_, ypts_, facecolor='g', alpha=.2, edgecolor='none',
             label='feasible solution space')
    plt.plot(xpts_, ypts_, 'og', label='extreme points')
    plt.plot(xpts, y_optimum, 'r', label='objective function')
    if x_vecsol is not None:
        plt.plot(x_vecsol[0], x_vecsol[1], 'or', label='most extreme point')
    plt.legend(loc="upper right", shadow=True)
    plt.xlabel('x-axis'); plt.ylabel('y-axis')
    plt.xlim(xlo, xhi); plt.ylim(ylo, yhi)
    plt.grid(True)
    plt.show()
#end plot()

#numpy array list conversions
Z_coefs = np.array(Z_coefs, dtype=float)
constraints = np.array(constraints, dtype=float)
bounds = np.array(bounds, dtype=float)

#constants
n_activities = len(Z_coefs)  #number of activities (x,y,...)
n_constraints = len(constraints)  #number of constraints

#a) graphical solution
print('Graphical method:\n')

xlo, xhi, ylo, yhi = -.5, 11, -.5, 11  #set lo,hi values of x,y for plotting
xpts = np.array([xlo, xhi]) #generate x start,end points for plotting
ypts = np.array([ylo, yhi]) #generate y start,end points for plotting

#compute y coords to plot constraints
y_cts = np.empty((n_constraints, n_activities))
for i in range(n_constraints):
    y_cts[i] = Y_cts(i, xpts)

#compute x,y coords to plot bounds
x_bds = [[x]*len(xpts) for x in bounds[0]]
y_bds = [[y]*len(xpts) for y in bounds[1]]

#compute y coords and plot for Z=0
Z = 0
y_optimum = y_Z(xpts, Z)
plot('Graphics method')

#compute y coords and plot for Z=5
Z = 5
y_optimum = y_Z(xpts, Z)
plot('Graphics method')

#from the graph it's clear that if we continue to increase Z,
#the objective function will continue to shift upwards in the
#positive y direction, eventually reaching the most extreme point
#before leaving the feasible solution space. Extreme points
#result from the intersection of two or more lines that confine
#the solution space. We must pick manually the two lines that
#create the last extreme point before the objective function
#intersects it and leaves such space. It could come from two
#constraints (the most common), one constraint and one bound,
#or two bounds (from different activities x,y). On either case,
#a graphical solution involves manually picking two lines and
#solve the system of equations to find the most extreme point:

#pick constraints manually to build A and b from augmented constraints matrix
A = np.empty((n_activities, n_activities))  #create matrix A
b = np.empty(n_activities)                  #create vector b
#(default: first n_activities constraints are selected from constraints matrix)
r = list(range(n_activities))  #[0, 1, ..., n_activities - 1]
r = [0, 2]  #uncomment and select correct rows from constraints matrix, if needed
for i in range(n_activities):
    A[i] = constraints[r[i], :-1]
    b[i] = constraints[r[i], -1]
#end for

#compute optimum activities vector x by solving equation set
x_vector = _linalg2.gauss(A, b)
Z = Z_func(x_vector)
print('x = {}\ny = {}\nZ = {}\n'.format(x_vector[0], x_vector[1], Z))

#compute y coords and plot for Z obtained by graphics method
y_optimum = y_Z(xpts, Z)  #save copy
y_optimum_graphics = y_optimum  #save copy for comparison
plot('Graphics method', x_vector)

#b) simplex method
print('Simplex method:\n')

#compute optimum activities vector x by using simplex method
x_vector = _linprog.simplex(Z_coefs, constraints, bounds, debug=True)

#simplex() method should display something like this in debug mode:
'''
     fun: -1366.6666666666667
 message: 'Optimization terminated successfully.'
     nit: 3
   slack: array([ 0.        ,  6.        ,  0.        ,  5.33333333,  1.33333333])
  status: 0
 success: True
       x: array([ 3.66666667,  4.66666667])
'''

#compute Z from optimum X vector obtained by simplex method
Z = Z_func(x_vector)
print("\nx = {}\ny = {}\nZ = {}".format(x_vector[0], x_vector[1], Z))

#compute y coords and plot for Z obtained by simplex method
y_optimum = y_Z(xpts, Z)
y_optimum_simplex = y_optimum  #save copy for comparison
plt.plot(x_vector[0], x_vector[1], 'or')
plot('Simplex method', x_vector)

if np.allclose(y_optimum_simplex, y_optimum_graphics):
    print("\nBoth Graphical and Simplex method solutions match!")
else:
    print("\nGraphical method solution does NOT match Simplex method solution!")
    print("Uncomment line 121 and select correct rows from constraints matrix.")
#end if