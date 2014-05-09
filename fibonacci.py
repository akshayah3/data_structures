# -*- coding: utf-8 -*-
"""
Created on Fri May  9 23:12:34 2014

@author: akshay
"""

def fibonacci(n):
    if n<=1:
        return (n,0)
    else:    
        a,b = fibonacci(n-1)
        return (a+b,a)
    