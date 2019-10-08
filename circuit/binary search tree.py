# -*- coding: utf-8 -*-
"""
Created on Sat Mar 23 17:50:17 2019

@author: Administrator
"""

# title: binary search tree

class BSTNode(object):
    """Anode in the BST"""
    def __init__(self, parent, k):
        """Create a node
        
        Args:
            parent: the node's parent
            k: the key of the node
        """
        self.key = k
        self.parent = parent
        self.left = None
        self.right = None
        
    def find(self, k):
        """find and return the node with key k
        Args:
            k: the key of node we want to find
        """
        if k == self.key:
            return self
        if k < self.key:
            if self.left == None:
                return None
            else:
                return self.left.find(k)
        else:
            if self.right == None:
                return None
            else:
                return self.right.find(k)
        
        
        
    def find_min(self):
        """find the node with minimum key in this tree
        
        Returns: 
            the node with minimum key
        """
        current = self
        while current.left is not None:
            current = current.left
        return current
    
    def next_large(self):
        """Return the nodes with the next large key
        """
        if self.right is not None:
            return self.right.find_min()
        current = self
        while current.parent is not None and current is current.parent.right:
            current = current.parent
        return self.parent
    
    def insert(self, node):
        """insert a node into BST
        
        Args:
            node: the node to be inserted
        """
        if node is None:
            return
        if node.key < self.key:
            if self.left is None:
                node.parent = self
                self.left = node
            else:
                self.left.insert(node)
        else:
            if self.right is None:
                node.parent = self
                self.right = node
            else:
                self.right.insert(node)
        
    def delete(self):
        """delete and return this node from BST
        """
        
        
        
        
        
        
        
        
        
        
            
        
        
        
        
                
        


        
