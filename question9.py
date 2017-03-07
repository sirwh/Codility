# -*- coding: utf-8 -*-
"""
Created on Thu Feb 16 13:21:11 2017

@author: Jason Ma
"""
def solution1(A):
    # write your code in Python 2.7
    y=1
    max_slice=max_ending=0
    for i in xrange(3,len(A)):
        temp1=max_ending+A[i-1]
        temp2=max_ending+A[y]
        if temp1>=temp2:
            max_ending=max(0,temp1)
        else:
            max_ending=max(0,temp2)
            y=i-1
        max_slice=max(max_slice, max_ending)
    return max_slice

def solution2(A):
    # write your code in Python 2.7
    max_slice=max_ending=A[0]
    for i in xrange(1,len(A)):
        max_ending=max(A[i],max_ending+A[i])
        max_slice=max(max_slice, max_ending)
    return max_slice

def solution3(A):
    # write your code in Python 2.7
    max_slice=max_ending=0
    for i in xrange(1,len(A)):
        max_ending=max(0,max_ending+A[i]-A[i-1])
        max_slice=max(max_slice, max_ending)
    return max_slice