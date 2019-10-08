# -*- coding: utf-8 -*-
"""
Created on Tue Apr 23 08:55:05 2019

@author: Administrator
"""

def counting_sort(L, k):
    """Return a sorted list, it is also stable.
    Input:
        L (list): unsorted list
        k (int): maximum element in L
    """
    # computer counting list
    pos = [0]*(k+1)
    for i in L:
        pos[i] = pos[i] + 1
    
    # computer "less than" counting list
    pos_new = [0]*(k+1)
    for j in range(1, k+1):
        pos_new[j] = pos_new[j-1] + pos[j-1]
    
    # do counting sort
    ans = [None]*len(L)
    for k in L:
        ans[pos_new[k]] = k
        pos_new[k] = pos_new[k] + 1
    return ans


