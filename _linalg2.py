'''
module: _linalg2.py
author: Luis Paris
description:
- formulas from Chapra's numerical methods textbook
- chapters on linear algebraic equations
- implemented from algorithms/pseudocode provided
- reuses/shares functions needed for gauss elim and LU decomp
'''

import numpy as np

def scale(A):  #compute scale vector (max absolute elem in each row)
    n = len(A)
    s = np.empty(n)
    for i in range(n):
        s[i] = max(abs(A[i,:]))  #added (get max absolute elem on ith row)
        #s[i] = abs(A[i,0])         #removed
        #for j in range(1, n):      #removed
        #    if abs(A[i,j]) > s[i]: #removed
        #        s[i] = abs(A[i,j]) #removed
    return s
#end scale()

def pivot(A, k, o, s, b=None):
    n = len(A)
    p = k
    big = abs(A[o[k],k] / s[o[k]])
    for i in range(k+1, n):
        num = abs(A[o[i],k] / s[o[i]])
        if num > big:
            big = num
            p = i
    if p != k:
        o[k],o[p] = o[p],o[k]  #added (swap row indexes - FASTER!)
        #for j in range(k, n):                #removed
        #    A[p,j], A[k,j] = A[k,j], A[p,j]  #removed
        #b[p], b[k] = b[k], b[p]              #removed
        #s[p], s[k] = s[k], s[p]              #removed
#end pivot()

def elim(A, o, s, tol=1e-5, b=None):
    n = len(A)
    if b is None:
        L = np.identity(n)
    for k in range(0, n-1):
        pivot(A, k, o, s)
        if abs(A[o[k],k] / s[k]) < tol:
            return -1
        for i in range(k+1, n):
            factor = A[o[i],k] / A[o[k],k]
            if b is None:
                #A[o[i],k] = factor  #added (in place)
                A[o[i],k] = 0    #added (separate)
                L[i,k] = factor  #added (separate)
            for j in range(k+1, n):
                A[o[i],j] -= factor * A[o[k],j]
            if b is not None: b[o[i]] -= factor * b[o[k]]  #removed
    return -1 if abs(A[o[n-1],n-1] / s[o[n-1]]) < tol else 0, L if b is None else None
#end elim()

def subst(A, b, o=None, dir="bwd"):  #performs backward (default) or forward substitution
    n = len(A)         #dir="bwd" (backward); or dir="fwd" (forward)
    x = np.zeros(n)
    fwd = (dir != "bwd")
    k = 0 if fwd else n-1
    if o is None: o = [i for i in range(n)]
    x[k] = b[o[k]] / A[o[k],k]
    for i in range(1, n) if fwd else range(n-2, -1, -1):
        sum = 0
        for j in range(i-1, -1, -1) if fwd else range(i+1, n):
            sum += A[o[i],j] * x[j]
        #x[n-1] = (b[o[n-1]] - sum) / A[o[n-1],n-1]  #incorrect from textbook
        x[i] = (b[o[i]] - sum) / A[o[i],i]  #correct
    return x
#end subst()

#Gauss elimination method w/ scaling and partial pivoting
def gauss(A, b, tol=1e-5):
    n = len(A)
    A_ = np.array(A, dtype=float)
    b_ = np.array(b, dtype=float)
    o = [i for i in range(n)]  #[0, 1, 2, ..., n-1]
    s = scale(A_)
    err, _ = elim(A_, o, s, tol, b_)
    return subst(A_, b_, o) if not err else None
#gauss()

#LU decomposition method w/ scaling and partial pivoting
def decompLU(A, tol=1e-5):
    n = len(A)
    U = np.array(A, dtype=float)
    o = [i for i in range(n)]  #[0, 1, 2, ..., n-1]
    s = scale(U)
    err, L = elim(U, o, s, tol)
    return (L, U[o], o) if not err else None
#decompLU()
