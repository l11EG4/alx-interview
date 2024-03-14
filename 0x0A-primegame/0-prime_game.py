#!/usr/bin/python3
# made by mega

def isWinner(x, nums):

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

    # this loop for Iterates Over Multiple of prime num and marks them as
    for i in range(2, len(ls)):
        try:
            ls[i * x] = 0
        except (ValueError, IndexError):
            break
