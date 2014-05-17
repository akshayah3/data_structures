# -*- coding: utf-8 -*-
"""
Created on Sat May 17 19:02:20 2014

@author: akshay
"""

class LinkedQueue:
    '''FIFO Queue implementation using a singly linked list for storage.'''
    
    class Node:
        '''Lightweight, nonpublic class for storing a singly linked node.'''
        
        def __init__(self, element, next):
            self.element = element
            self.next = next
    
    def __init__(self, head, size, tail):
        self.head = head
        self.size = size
        self.tail = tail 
    
    def __len__(self):
        return self.size

    def is_empty(self):
        return self.size == 0

    def enqueue(self, e):
        node = self.Node(e, self.head)
        if self.is_empty():
            self.head = node
        else:
            self.tail.next = node
        self.tail = node
        self.size += 1

    def top(self):
        if self.is_empty():
            return 'Error, the stack is empty'
        return self.head.element

    def dequeue(self):
        if self.is_empty():
            self.tail = None
            return 'Error, the stack is empty'
        value = self.head.element
        self.head = self.head.next
        self.size -= 1
        return value 
                        