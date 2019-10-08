# -*- coding: utf-8 -*-
"""
Created on Tue Apr 23 09:03:49 2019

@author: Administrator
"""

from counting_sort import*
import unittest

class TestCS(unittest.TestCase):
    def test_1(self):
        L = [2,5,3,0,2,3,0,3]
        k = 5
        result = counting_sort(L, k)
        expected = [0,0,2,2,3,3,3,5]
        self.assertEqual(result, expected)
    
    def test_2(self):
        L = [4,1,3,4,3]
        k = 4
        result = counting_sort(L, k)
        expected = [1,3,3,4,4]
        self.assertEqual(result, expected)


if __name__ == '__main__':
    res = unittest.main(verbosity=3, exit=False)
