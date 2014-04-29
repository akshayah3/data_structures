# -*- coding: utf-8 -*-
"""
Created on Tue Apr 29 16:01:54 2014

@author: akshay
"""

"""
Karatsuba Multiplication
"""
def check_even(q):
    if len(q)%2 == 0:
        return True
    else:
        return False

def compute_value(q): 
    z = len(q)
    if check_even(q):
        l = int(q[0:(z)/2])
        a = (10**((z/2)))*l
        b = int(q[z/2:])
        return a, b, l
    """else:
        a = 10**((z + 1)/2)*int(q[0:(z - 1)/2])
        b = int(q[(z - 1)/2:])
        return a, b"""       
def karatsuba(x, y):
        a,b,k = compute_value(x)
        c,d,f = compute_value(y)
        if check_even(x) and check_even(y):
            return 10**len(x)*a*b + 10**(len(x)/2)*(a*d + b*c) + b*d
            



        
x = raw_input('enter the first number')
y = raw_input('enter the second number')
print compute_value(x)
print compute_value(y)
akshay = karatsuba(x, y)
print akshay