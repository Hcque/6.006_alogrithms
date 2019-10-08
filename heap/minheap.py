# -*- coding: utf-8 -*-
"""
Created on Sun Apr 21 09:57:39 2019

@author: Administrator
"""

class MinHeap:
    def __init__(self):
        self.heap = [0] 
        self.size = 0
    
    def per_up(self, i):
        while i//2 > 0:
            if self.heap[i] < self.heap[i//2]:
                self.heap[i], self.heap[i//2] = self.heap[i//2], self.heap[i]
            i = i//2
            
    def insert(self, x):
        self.heap.append(x)
        self.size = self.size + 1
        self.per_up(self.size)
        
    def min_child(self, i):
        if self.heap[i*2] < self.heap[i*2+1]:
            mc_idx = i*2
        else:
            mc_idx = i*2 + 1
        return mc_idx
    
    def per_down(self, i):
        while (i*2) <= self.size:
            if i*2 == self.size: # have only left child
                if self.heap[i*2] < self.heap[i]:
                    self.heap[i*2], self.heap[i] = self.heap[i], self.heap[i*2]
                    i = i*2
            else: # have two children
                mc_idx = self.min_child(i)
                if self.heap[mc_idx] < self.heap[i]:
                    self.heap[mc_idx], self.heap[i] = self.heap[i], self.heap[mc_idx]
                    i = mc_idx
                       
    def del_min(self):
        self.heap[1], self.heap[self.size] = \
        self.heap[self.size], self.heap[1]
        min = self.heap.pop()
        self.size = self.size - 1
        self.per_down(1)        
        return min
        
        
        
            