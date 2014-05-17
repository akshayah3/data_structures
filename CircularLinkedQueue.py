# -*- coding: utf-8 -*-
"""
Created on Sat May 17 20:06:02 2014

@author: akshay
"""

class LinkedStack:
    '''LIFO Stack implementation using a singly linked list for storage.'''
    
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
        '''Add an element to the back of queue.'''
        newest = self.Node(e, None)
        if self.is_empty( ):
            newest.next = newest
        else:
            newest.next = self.tail.next
        self.tail. next = newest
        self.tail = newest
        self.size += 1

    def top(self):
        if self.is_empty():
            return 'Error, the stack is empty'
        return self.tail.next.element

    def dequeue(self):
        if self.is_empty( ):
            raise Empty( Queue is empty )
        oldhead = self.tail.next
        if self.size == 1:
            self.tail = None
        else:
            self.tail.next = oldhead.next
        self.size −= 1
        return oldhead.element

    def rotate(self):
        if self.size > 1:
            self.tail = self.tail.next                