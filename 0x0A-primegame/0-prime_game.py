#!/usr/bin/python3
# Made by mEGA
"""this script  for Prime Game"""


def isWinner(x, nums):
    """
    this method  winner of a set of prime number removal games.

    Args:
        x (int): The num of rounds.
        nums (list of int): A list of integers where each integer n denotes
        a set of consecutive int starting from 1 up to and including n.

    Returns:
        str: for The name of the player who won the most rounds (either "Ben"
        or "Maria").
        None: If this winner it cannot be determined.

    Raises:
        None.
    """
    # this Check for invalid input
    if x <= 0 or nums is None:
        return None
    if x != len(nums):
        return None
    # Init scores and array of possible prime numbers
    ben = 0
    maria = 0
    # for Create a list 'a' of length sorted(nums)[-1] + 1 with all elements
    # init to 1
    a = [1 for x in range(sorted(nums)[-1] + 1)]
    # This for first two elements of the list, a[0] and a[1], are set to 0
    # for because 0 and 1 are not prime numbers
    a[0], a[1] = 0, 0
    # Use this Save of Eratosthenes algorithm to generate array of prime numbers
    for i in range(2, len(a)):
        rm_multiples(a, i)
    # for Play each round of the game
    for i in nums:
        # If the sum of prime num in the set is even, Ben wins
        if sum(a[0:i + 1]) % 2 == 0:
            ben += 1
        else:
            maria += 1
    # for Determine the winner of the game
    if ben > maria:
        return "Ben"
    if maria > ben:
        return "Maria"
    return None


def rm_multiples(ls, x):
    """
    this function Removes multiples of a prime number from an array of possible prime
    numbers.

    Args:
        ls (list of int): for An array of possible prime numbers.
        x (int): for The prime number to remove multiples of.

    Returns:
        None.

    Raises:
        None.
    """
    # this loop for Iterates Over Multiple of prime num and marks them as
    for i in range(2, len(ls)):
        try:
            ls[i * x] = 0
        except (ValueError, IndexError):
            break
