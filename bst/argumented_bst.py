# -*- coding: utf-8 -*-
"""
Created on Sun Apr 21 08:52:04 2019

@author: Administrator
"""

# -*- coding: utf-8 -*-
"""
Created on Sat Apr 20 14:14:39 2019

@author: Administrator
"""

class BSTNode:
    def __init__(self, key, parent, left, right):
        self.key = key
        self.parent = parent
        self.left = left
        self.right = right
    
    
    def find(self, k):
        if self.key == k:
            return self
        elif k < self.key:
            if self.left is None:
                return None
            else:
                return self.left.find(k)
        else:
            if self.right is None:
                return None
            else: 
                return self.right.find(k)
    
    def find_min(self):
        current = self
        while current.left is not None:
            current = current.left
        return current
    
    def next_larger(self):
        if self.right is not None:
            return self.right.find_min()
        # has no right child, go up until first right parent.
        current = self
        while (current.parent is not None) and \
        (current.parent.right is current):
            current = current.parent
        return current.parent
    
    def insert(self, Node):
        if Node.key < self.key:
            if self.min.key > Node.key:
                self.min = Node
            if self.left is None:
                self.left = Node
                Node.parent = self
            else:
                return self.left.insert(Node)
        else:
            if self.right is None:
                self.right = Node
                Node.parent = self
            else:
                return self.right.insert(Node)
    
    def delete(self):
        # has no child or one child
        if self.left is None or self.right is None:
            if self.parent.left is self:
                self.parent.left = self.left or self.right
                if self.parent.left is not None:
                    self.parent.left.parent = self.parent
                    self.parent.min = self.left.min # case 1
                else:
                    self.parent.min = self.parent # case 2
                # propagate
                current = self.parent
                while current.parent is not None and current.parent.left is current:
                    current.parent.min = current.min
                    current = current.parent
            else:
                self.parent.right = self.left or self.right
                if self.parent.right is not None:
                    self.parent.right.parent = self.parent
            return self
        # has two children, swap with candidate:s.
        else:
          s = self.next_larger()
          s.key, self.key = self.key, s.key
          return s.delete()
        
        
        