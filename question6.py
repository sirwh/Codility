# -*- coding: utf-8 -*-
"""
Created on Tue Feb 14 14:48:09 2017

@author: Jason Ma
"""

def solution(A):
    # write your code in Python 2.7
    count=len(A)
    if count==1 or count==0:
        return count
    A.sort()
    for i in xrange(1,count):
        if A[i]==A[i-1]:
            count-=1
    return count

def solution2(A):
    # write your code in Python 2.7
    A.sort()
    cand = A[-1]*A[-2]*A[-3]
    if A[1] >= 0:
        return cand
    return max(cand,A[0]*A[1]*A[-1])

def solution3(A):
    # write your code in Python 2.7
    A.sort()
    for i in xrange(2,len(A)):
        if A[i-2]+A[i-1]>A[i]:
            return 1
    return 0