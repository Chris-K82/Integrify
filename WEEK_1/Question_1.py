#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Jun  5 22:50:15 2019

@author: chris
"""
import scipy


def function(n):

    if n > 7:
        print("Course Passed.")

    elif n < 5:
        print('The current value of n is: {}\n'.format(n))
        n += 1
        return function(n)

    else:
        print('The current value of n is: {}\n'.format(n))
        n += 1
        return function(n)


def val_input(n):
    return isinstance(n, int) and n in range(11)


def get_num():
    try:
        n = int(input("Please only enter whole numbers between 0 and 10: "))
        while not val_input(n):
            n = int(input("Please only enter whole numbers between 0 and 10: "))
        return n
    except ValueError:
        print("Invalid entry, try again.")
        return get_num()


def run_program():

    call_func = input("Would you like to run the program? Y/N  ").lower()

    while not (call_func[0] == 'y' or call_func[0] == 'n'):
        call_func = input("Please select whether you would like to continue. Enter \"Y\" or \"N\"  ").lower()
    if call_func[0] == 'y':
        n = get_num()
        function(n)
        run_program()
    else:
        return 0


run_program()
