# -*- coding: utf-8 -*-
"""
Created on Fri May  9 23:12:34 2014

@author: akshay
"""
"""Efficiet as it doesn't involve a tail recursion"""
def fibonacci(n):
    if n<=1:
        return (n,0)
    else:    
        a,b = fibonacci(n-1)
        return (a+b,a)
    
