#!/usr/bin/env python2
# -*- coding: utf-8 -*-
import timeit
import numpy as np
import sklearn
"""
Created on Thu Jun  6 01:58:09 2019

@author: chris
"""

'''
    Question 5 asked us to write a function which finds the missing num in an
    unsorted list of nums and then return that num.

    The approach here is to use the mathematical principle that in a list of
    nums from 1...N + 1, their sum = (n(n+1))/2. Knowing that if we simply
    sum the nums in the input list and then subtract that from the expected sum
    based on the len of the input list, that return value will be the missing
    num in the input list.
'''


def find_num(a):
    input_sum = sum(a)
    n = len(a) + 1
    return int(n*(n+1)/2 - input_sum)


def find_num_2(a):
    b = [x for x in range(a[0], a[-1] + 1)]
    a = set(a)
    return list(a ^ set(b))


def wrapper(func, *args, **kwargs):
    def wrapped():
        return func(*args, **kwargs)
    return wrapped


def pick_func(func_1, func_2, a):
    wrapped_1 = wrapper(func_1, a)
    wrapped_2 = wrapper(func_2, a)
    result_1 = float(timeit.timeit(wrapped_1, number=1000))
    result_2 = float(timeit.timeit(wrapped_2, number=1000))
    dif = abs(result_1 - result_2)

    if result_1 < result_2:
        print('The run time of func_1 ' +
              'is: {} vs func_2: {}.'.format(result_1, result_2))
        print('Therefore, using func_1 results in a time savings ' +
              'of: {}'.format(dif))

    else:
        print('The run time of func_1 ' +
              'is: {} vs func_2: {}.'.format(result_1, result_2))
        print('Therefore, using func_2 results in a ' +
              'time savings of: {}'.format(dif))


a = [1, 3, 4, 5, 7, 8, 9, 10]
b = [4, 3, 1, 2, 6]
c = np.arange(10**6)

# pick_func(find_num, find_num_2, a)
pick_func(find_num, find_num_2, b)
# pick_func(find_num, find_num_2, c)
