
import numpy as np

def newton(x, y, xref, debug=False):
    n = len(x)
    if n != len(y):
        return None
    x = np.array(x, dtype=float)
    y = np.array(x, dtype=float)
    fdd = np.zeros((n,n))
    fdd[:, 0] = y
    for j in range(1, n):
        for i in range(0, n-j):
            fdd[i,j] = (fdd[i+1,j-1] - fdd[i,j-1]) / (x[i+j] - x[i])
        #end for
    #end for
    if debug: print("fdd = \n{}".format(fdd))
    b = np.zeros(n)
    ea = np.zeros(n)
    xterm = 1.
    b[0] = fdd[0,0]
    for i in range(1,n):
        xterm *= (xref - x[i-1])
        ytmp = b[i-1] + fdd[0,i] * xterm
        ea[i-1] = ytmp - b[i-1]
        b[i] = ytmp
    #end for
    return b, ea
#end newton()

def newton_eval(b, x, xref):
    n = len(b)
    if n != len(x):
        return None
    sum = b[0]
    xterm = 1.0
    for i in range(1,n):
        xterm *= (xref - x[i-1])
        sum += b[i] * xterm
    return sum
#end newton_eval()