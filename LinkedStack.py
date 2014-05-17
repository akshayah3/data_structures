# -*- coding: utf-8 -*-
"""
Created on Sat May 17 18:10:57 2014

@author: akshay
"""

class LinkedStack:
    '''LIFO Stack implementation using a singly linked list for storage.'''
    
    class Node:
        '''Lightweight, nonpublic class for storing a singly linked node.'''
        
        def __init__(self, element, next):
            self.element = element
            self.next = next
    
    def __init__(self, head, size):
        self.head = head
        self.size = size
    
    def __len__(self):
        return self.size

    def is_empty(self):
        return self.size == 0

    def push(self, e):
        node = self.Node(e, self.head)
        self.head = node
        self.size += 1

    def top(self):
        if self.is_empty():
            return 'Error, the stack is empty'
        return self.head.element

    def pop(self):
        if self.is_empty():
            return 'Error, the stack is empty'
        value = self.head.element
        self.head = self.head.next
        self.size -= 1
        return value                 