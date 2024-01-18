#!/usr/bin/python3
# Made by MEGA

"""
    the method that determines the num of min operations given n chars
"""


def minOperations(n):
    """
        the function that calculates the fewest num of operations
        needed to give a result of exactly n H chars in a file
        args: n: Num of chars to be displayed
        return:
               number of min operations
    """

    now = 1
    start = 0
    counter = 0
    while now < n:
        remainder = n - now
        if (remainder % now == 0):
            start = now
            now += start
            counter += 2
        else:
            now += start
            counter += 1
    return counter
