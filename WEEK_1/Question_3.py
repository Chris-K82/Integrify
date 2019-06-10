#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Thu Jun  6 00:38:56 2019

@author: chris
"""

'''
    Question 3 asked us to write a function which looks through an arry
    of int's' and return the count of unique ABSOLUTE values.

    So, generally a "set" data type would do well here, however, with the word
    "ABSOLUTE" it essentially means we will have to consider that, in this
    context, "-5" is semantically the same as "5".

    My approach to this will be to use a lambda expression. You can read more
    about these expressions at:
https://medium.com/better-programming/lambda-map-and-filter-in-python-4935f248593

    So essentially, I want to map each element in the input list to its' abs
    value in an output list, cast that output list to a set type, and then
    return the len of that list.
'''


def count_uniq_abs_vals(a):
    return len(set(map(lambda x: abs(x), a)))


a = [1, 2, 3, -1, 4, 3]
print(count_uniq_abs_vals(a))  # This test should return 4
