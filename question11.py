# -*- coding: utf-8 -*-
"""
Created on Thu Feb 16 15:11:03 2017

@author: Jason Ma
"""

def solution(N, P, Q):
    # write your code in Python 2.7
    primes=[1]*(N+1)
    primes[0]=primes[1]=0
    i=2 # remove the multipliers of primes not exceeding sqrt n
    while i*i<=N: # not exceeding sqrt n
        if primes[i]==1: # primes
            k=i*i
            while k<=N:
                primes[k]=0
                k+=i
        i+=1
    result=[0]*len(Q)
    for i in xrange(0,len(Q)):
        result[i]=sum(primes[P[i]:Q[i]+1])
    return result
        
print(solution(26, [1, 4, 16], [26, 10, 20]))