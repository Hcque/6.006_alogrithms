# -*- coding: utf-8 -*-
"""
Created on Tue Apr 23 09:28:16 2019

@author: Administrator
"""

from minheap import*
import unittest

class Testheap(unittest.TestCase):
    def test_insert_1(self):
        h = MinHeap()
        for i in [4,2,1]:
            h.insert(i)
        self.assertEqual(h.heap, [0,1,4,2])
        
    def test_insert_2(self):
        h = MinHeap()
        for i in [4,2,1]:
            h.insert(i)
        h.insert(3)
        self.assertEqual(h.heap, [0,1,3,2,4])
    
    def test_delete_1(self):
        h = MinHeap()
        for i in [4,2,1]:
            h.insert(i)
        h.insert(3)
        min = h.del_min()
        self.assertEqual(min, 1)
        
    def test_delete_2(self):
        h = MinHeap()
        for i in [4,2,1]:
            h.insert(i)
        h.insert(3)
        h.del_min()
        self.assertEqual(h.heap, [0,2,3,4])
        

if __name__ == '__main__':
    res = unittest.main(verbosity=3, exit=False)
    