# -*- coding: utf-8 -*-
"""
Created on Sat May 17 13:57:06 2014

@author: akshay
"""

class Fifo:
    'Fastest implementation of FIFO queues'
    def __init__(self):
        self.nextin = 0
        self.nextout = 0
        self.data = {}
    def append(self, value):
        self.data[self.nextin] = value
        self.nextin += 1
    def pop(self, n=-1):
        value = self.data[self.nextout]
        del self.data[self.nextout]
        self.nextout += 1
        return value