#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Thu Jun  6 02:04:13 2019

@author: chris
"""

'''
    Question 6 asked us to write a function which rotates the last element in
    the input list "k" times.

    The approach I chose is to take the portion of the list from (k-1) to the
    end and then return that list appended with the list from index 0 to
    (k-1)
'''

a = [10, 50, 5, 1]


def rot_arr(a, k):
    return a[k:] + a[:k]


print(rot_arr(a, 2))  # Expected output [5, 1, 10, 50]
