
import math
import numpy as np

def dft(f, N, h, t0=0.0, ndigs=4, debug=False, tab=10):
    Freal = np.zeros(N)
    Fimag = np.zeros(N)
    w0 = 2 * math.pi / N
    if debug and tab:
        print("{:<{t}}{:<{t}}{:<{t}}{:<{t}}".format("k","f(tk)","real","imag",t=tab))
    for k in range(N):
        for n in range(N):
            angle = k*w0*n
            fn = f(t0 + n*h)
            if k == n: fk = fn
            Freal[k] += fn * math.cos(angle) / N
            Fimag[k] += fn * math.sin(angle) / N
        #end for
        if debug:
            print(("{:<{t}}{:<{t}}{:<{t}}{:<{t}}" if tab else
                   "k={}, f(tk)={}, real={}, imag={}")
                  .format(k, round(fk,ndigs), round(Freal[k],ndigs), round(Fimag[k],ndigs), t=tab))
    #end for
    return Freal, Fimag
#end dft()