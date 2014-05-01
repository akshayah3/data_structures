# -*- coding: utf-8 -*-
"""
Created on Thu May  1 16:58:05 2014

@author: akshay
"""

def merge(left, right):
    A = []
    i ,j = 0, 0
    while i < len(left) and j < len(right):
        if left[i] <= right[j]:
            A.append(left[i])
            i += 1
        else:
            A.append(right[j])
            j += 1
    A += left[i:]
    A += right[j:]
    return A


def mergesort(A):
    if len(A) > 1:
        q = len(A) // 2
        left = mergesort(A[:q])
        right = mergesort(A[q:])
        return merge(left, right)
    return A

if __name__ == "__main__":
    A = [1,6,4,3,2,7,8,19]
    print "unsorted(A): " + str(A)
    print "mergesort(A): " + str(mergesort(A))