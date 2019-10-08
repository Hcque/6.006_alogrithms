# -*- coding: utf-8 -*-
"""
Created on Sat Sep 21 06:53:05 2019

@author: Administrator
"""

class MaxHeap:
    def __init__(self):
        self.list = [0]
        self.current_size = 0
    
    def swap_up(self, i):
        while i//2 > 0 and self.list[i//2] < self.list[i]:
            self.list[i//2], self.list[i]  = self.list[i], self.list[i//2]
            i = i//2
    def insert(self, x):
        self.size.append(x)
        self.current_size += 1
        self.swap_up(self.current_size)
        
    def find_max(self):
        return self.list[1]
    
    def max_child(self, i):
        # assume i has child
        # only left child
        if i*2 == self.current_size:
            return i*2
        else:
            if self.list[i*2] > self.list[i*2+1]:
                return i*2
            else:
                return i*2+1
    def swap_down(self, i):
        # i has children
        while i*2 >= self.current_size:
            mc = self.max_child(i)
            if self.list[mc] > self.list[i]:
                self.list[mc], self.list[i] = self.list[i], self.list[mc]
                i = mc
    def delete_max(self):
        # swap max with the last element
        self.list[1], self.list[-1] = self.list[-1], self.list[1]
        # pop max 
        ans = self.list.pop()
        self.current_size -= 1
        # fix RI
        self.swap_down(1)
        
        return ans
    
    
    
    
    
    
    
    
    
    
    
    
    
    
        
            