# -*- coding: utf-8 -*-
"""
Created on Sat May 17 13:57:06 2014

@author: akshay
"""

def match(expr):
    '''Matching delimiters'''
    right = ')}]'
    left = '[{('
    S = ArrayStack() #  instantiated the ArrayStack
    for i in expr:
        if y in left:
            S.push(y)
        elif y in right:
            if S.is_empty():
                return False
            if right.index(y) != left.index(S.pop()):
                return False
    return S.is_empty            