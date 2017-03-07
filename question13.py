# -*- coding: utf-8 -*-
"""
Created on Fri Feb 17 11:02:10 2017

@author: Jason Ma
"""

def solution(A, B):
    # write your code in Python 2.7
    L=len(A)
    fib=fibarray(L)
    result=[0]*L
    for i in xrange(0,L):
        result[i]=fib[A[i]] % (1<<B[i])
    return result

def fibarray(L):
    fib=[1]*(L+1)
    for i in xrange(2,L+1):
        fib[i]=fib[i-1]+fib[i-2]
    return fib
    