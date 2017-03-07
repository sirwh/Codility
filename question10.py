# -*- coding: utf-8 -*-
"""
Created on Thu Feb 16 14:16:18 2017

@author: Jason Ma
"""

def solution(N):
    # write your code in Python 2.7
    count=0
    for i in range(1,int(N**0.5)+1):
        if N%i==0:
            count+=2
    if int(N**0.5)**2==N:
        count-=1
    return count

def solution2(N):
    # write your code in Python 2.7
    temp=int(N**0.5)
    while N%temp != 0:
        temp-=1
    return 2*(temp+N/temp)