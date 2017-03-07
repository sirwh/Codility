# -*- coding: utf-8 -*-
"""
Created on Thu Feb 16 09:47:14 2017

@author: Jason Ma
"""
def solution(A):
    # write your code in Python 2.7
    value=[]
    size=0
    for i in xrange(len(A)):
        if size==0:
            value=A[i]
            size+=1
        else:
            if A[i]!=value:
                size-=1
            else:
                size+=1
    if size==0:
        return -1
    else:
        count=0
        for i in xrange(len(A)):
            if value==A[i]:
                count+=1
                pos = i
        if count > len(A)/2:
            return pos
        else:
            return -1
        
def solution2(A):
    # write your code in Python 2.7
    value=[]
    size=0
    for i in xrange(len(A)):
        if size==0:
            value=A[i]
            size+=1
        else:
            if A[i]!=value:
                size-=1
            else:
                size+=1
    if size==0:
        return 0
    else:
        count=0
        for i in xrange(len(A)):
            if value==A[i]:
                count+=1
        if count > len(A)/2:
            leader=value
        else:
            return 0
    countL=0
    countR=count
    sizeL=0
    sizeR=len(A)
    result=0
    for i in xrange(len(A)-1):
        sizeL+=1
        sizeR-=1
        if A[i]==leader:
            countL+=1
            countR-=1
        if float(countL)/sizeL > 0.5 and float(countR)/sizeR > 0.5:
            result+=1
    return result