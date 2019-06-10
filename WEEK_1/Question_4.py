#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Thu Jun  6 01:24:18 2019

@author: chris
"""

'''
    Question 4 asked us to write a function which looks through a list of int's
    and returns '1' if a triplet exists and 0 if not.

    My approach to this was to first sort the list using the builtin python
    "list.sort()". This places all of the values in ascending order. If you
    want to sort them into descending order instead, you simply call:
    list_var_name.sort(reverse = True). Or if you simply want to return the
    sorted list, use the method "sorted", see syntax below.

    The built-in python sort methods have worst-case time complexity of
    O(n log n): https://wiki.python.org/moin/TimeComplexity

    Next, because the values are sorted, if any of the tests fail with the
    first three values, the first value needs to simply push forward to the
    position the third value was in (2 spaces) and then run the tests again.
    This can be run inside of a loop or this could be done recursively. If at
    any time the tests pass, return 1 and the program terminates.
'''
a = [1, 2, 3]
a.sort(reverse=True)
print(a)  # Should show "[3, 2, 1]"
a.sort()
print(a)

a = sorted(a, reverse=True)
print(a)  # Now they are in descending order again
a = sorted(a)
print(a)  # Now the nums are back in ascending order

a = [10, 2, 5, 1, 8, 20]
b = [10, 50, 5, 1]


def tri_count(l_nums):
    if len(l_nums) < 3:
        return 0
    for i in range(len(l_nums)):
        if not isinstance(l_nums[i], int):
            print(i)
            return 0

    l_nums.sort()

    p = 0
    while p in range(len(l_nums)-2):
        q = p+1
        r = q+1

        if check_triple(l_nums[p], l_nums[q], l_nums[r]):
            return 1
        p += 2
    return 0


def check_triple(p, q, r):

    return (((p+q) > r) and ((q+r) > p) and ((p+r) > q))


print(tri_count(a))  # Should return 1
print(tri_count(b))  # Should return 0
