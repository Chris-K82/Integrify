#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Thu Jun  6 00:23:19 2019

@author: chris
"""

'''
    Question 2 asks us to write a recursive method for computing a factorial
    given an integer as an input into the function.

    Recursion happens when we call the method we are currently in in some
    manner where the input moves toward the base case. In this instance,
    when the input == 1, we simply want to return 1. Each subsequent return
    statement is then multiplied by the previous value back up the recursive
    method calls. It would look like this on a whiteboard:

        n = 4 * nfac(n - 1)
         n = 3 * nfac(n - 1)
          n = 2 * nfac(n - 1)
           n == 1: return n
           return 1 * 2 = 2 NOTE: The factorial of 0, 1, 2 is 0, 1, 2
          return 2 * 3 = 6        Therefore, theh base case would look
         return 6 * 4 = 24        like: if n in range(2): return n
'''


def rec_n_fact(n):
    if n in range(2):  # I will generally always test for the base case first.
        return n
    return n * rec_n_fact(n - 1)


print(rec_n_fact(4))
print(rec_n_fact(2))
print(rec_n_fact(1))
print(rec_n_fact(0))
