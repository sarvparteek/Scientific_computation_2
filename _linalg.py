'''
module: _linalg.py
author: Luis Paris
description:
- formulas from Chapra's numerical methods textbook
- chapters on linear algebraic equations
- implemented from algorithms/pseudocode provided
'''

import numpy as np

#Gauss elimination method w/ scaling and partial pivoting
def gauss(A, b, tol=1e-5):
    n = len(A)
    if n != len(b):
        return None
    A = np.array(A, dtype=float)
    b = np.array(b, dtype=float)
    s = np.zeros(n)
    x = np.zeros(n)

    def subst():
        x[n-1] = b[n-1] / A[n-1,n-1]
        for i in range(n-2, -1, -1):
            sum = 0
            for j in range(i+1, n):
                sum += A[i,j] * x[j]
            #x[n-1] = (b[n-1] - sum) / A[n-1,n-1]  #incorrect from textbook
            x[i] = (b[i] - sum) / A[i,i]  #correct
    #end subst()

    def pivot(k):
        p = k
        big = abs(A[k,k] / s[k])
        for i in range(k+1, n):
            num = abs(A[i,k] / s[i])
            if num > big:
                big = num
                p = i
        if p != k:
            for j in range(k, n):
                A[p,j], A[k,j] = A[k,j], A[p,j]
            b[p], b[k] = b[k], b[p]
            s[p], s[k] = s[k], s[p]
    #end pivot()

    def elim():
        for k in range(0, n-1):
            pivot(k)
            if abs(A[k,k] / s[k]) < tol:
                return -1
            for i in range(k+1, n):
                factor = A[i,k] / A[k,k]
                for j in range(k+1, n):
                    A[i,j] -= factor * A[k,j]
                b[i] -= factor * b[k]
        return -1 if abs(A[n-1,n-1] / s[n-1]) < tol else 0
    #end elim()

    for i in range(0, n):
        s[i] = abs(A[i,0])
        for j in range(1, n):
            if abs(A[i,j]) > s[i]:
                s[i] = abs(A[i,j])
    if elim() < 0:
        return None
    subst()
    return x
#gauss()

def decompLU(A, tol=1e-5):
    n = len(A)
    A = np.array(A, dtype=float)
    L = np.identity(n)  #added (separate)
    o = np.zeros(n, dtype=int)
    s = np.zeros(n)

    #def subst():
    #    x[n-1] = b[n-1] / A[n-1,n-1]
    #    for i in range(n-2, -1, -1):
    #        sum = 0
    #        for j in range(i+1, n):
    #            sum += A[i,j] * x[j]
    #        #x[n-1] = (b[n-1] - sum) / A[n-1,n-1]  #incorrect from textbook
    #        x[i] = (b[i] - sum) / A[i,i]  #correct
    #end subst()

    def pivot(k):
        p = k
        big = abs(A[o[k],k] / s[o[k]])
        for i in range(k+1, n):
            num = abs(A[o[i],k] / s[o[i]])
            if num > big:
                big = num
                p = i
        if p != k:
            o[k],o[p] = o[p],o[k]  #added
            #for j in range(k, n):  #removed
            #    A[p,j], A[k,j] = A[k,j], A[p,j]  #removed
            #b[p], b[k] = b[k], b[p]  #removed
            #s[p], s[k] = s[k], s[p]  #removed
    #end pivot()

    def elim():
        for k in range(0, n-1):
            pivot(k)
            if abs(A[o[k],k] / s[k]) < tol:
                return -1
            for i in range(k+1, n):
                factor = A[o[i],k] / A[o[k],k]
                #A[o[i],k] = factor  #added (in place)
                A[o[i],k] = 0  #added (separate)
                L[i,k] = factor  #added (separate)
                for j in range(k+1, n):
                    A[o[i],j] -= factor * A[o[k],j]
                #b[o[i]] -= factor * b[o[k]]  #removed
        return -1 if abs(A[o[n-1],n-1] / s[o[n-1]]) < tol else 0
    #end elim()

    for i in range(0, n):
        o[i] = i  #added
        s[i] = abs(A[i,0])
        for j in range(1, n):
            if abs(A[i,j]) > s[i]:
                s[i] = abs(A[i,j])
    if elim() < 0:
        return None
    #subst()  #removed
    #return x
    #print("o = {}".format(o))
    return L, A[o]
#decompLU()
