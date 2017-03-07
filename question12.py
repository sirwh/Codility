# -*- coding: utf-8 -*-
"""
Created on Fri Feb 17 10:25:13 2017

@author: Jason Ma
"""

def solution(N, M):
    # write your code in Python 2.7
    lcm=N*M/gcd(N,M)
    return lcm/M
       
def gcd(a,b):
    if a % b==0:
        return b
    else:
        return gcd(b,a%b)