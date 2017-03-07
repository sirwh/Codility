# -*- coding: utf-8 -*-
"""
Created on Fri Feb 17 12:29:09 2017

@author: Jason Ma
"""

def solution(A):
    # write your code in Python 2.7
    if A[0]>=0:
        ind=0
    elif A[-1]<=0:
            ind=len(A)-1
    else:
        for i in xrange(0,len(A)):
            if A[i]>=0:
                ind=i
                break
    head=tail=ind
    count=1
    value=abs(A[ind])
    while True:
        if head>0 and tail <len(A)-1:
            if -A[head-1] > A[tail+1]:
                cand=A[tail+1]
                tail+=1
            else:
                cand=A[head-1]
                head-=1
        elif head>0 and tail >=len(A)-1:
            cand=A[head-1]
            head-=1
        elif head<=0 and tail <len(A)-1:
            cand=A[tail+1]
            tail+=1
        else:
            break
        if abs(cand)!=value:
            value=abs(cand)
            count+=1
    return count

solution([-2,-2])