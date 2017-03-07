# -*- coding: utf-8 -*-
"""
Spyderエディタ

これは一時的なスクリプトファイルです
"""

def solution(A, B, K):
    # write your code in Python 2.7
    if A%K==0:
        return B/K-A/K+1
    else:
        return B/K-A/K

def solution2(A): 
    # write your code in Python 2.7
    count=0
    sumA=sum(A)
    for i in A:
        if i==0:
            count+=sumA
            if count>1000000000:
                return -1
        else:
            sumA-=1
    return count