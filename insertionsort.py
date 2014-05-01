# -*- coding: utf-8 -*-
"""
Created on Wed Apr 30 23:37:30 2014

@author: akshay
"""



def insertion_sort(A):
    for i in range(0,len(A)):
        key = A[i]
        j = i + 1
        while j <= len(A) - 1 and A[j] > key:
            A[j - 1] = A[j]
            j += 1
        A[j - 1] = key


if __name__ == "__main__":
    A = [1,5,9,3,4]
    print "unsorted(A): " + str(A)
    insertion_sort(A)
    print "sorted(A): "+ str(A)

