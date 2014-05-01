# -*- coding: utf-8 -*-
"""
Created on Thu May  1 18:48:59 2014

@author: akshay
"""


def bubbleSort(alist):
    for passnum in range(len(alist)-1,0,-1):
        for i in range(passnum):
            if alist[i]>alist[i+1]:
                alist[i], alist[i + 1] = alist[i + 1], alist[i]

alist = [54,26,93,17,77,31,44,55,20]
bubbleSort(alist)
print(alist)
 
