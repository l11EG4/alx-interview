#!/usr/bin/python3
# Made by MEGA
""" this Script for Making changes """


def makeChange(coins, total):
    """ this method for Generate changes needed to reach total

    Args:
        coins ([List]):for  [List of Coins available]
        total ([int]): for [Total Amount needed]
    """
    if total <= 0:
        return 0
    check = 0
    temp = 0
    coins.sort(reverse=True)
    for i in coins:
        while check < total:
            check += i
            temp += 1
        if check == total:
            return temp
        check -= i
        temp -= 1
    return -1
