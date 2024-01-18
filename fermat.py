# Alice Giola
# CS 4412
# Project 1 - Primality tester

import random


def prime_test(N, k):
    # This is main function, that is connected to the Test button. You don't need to touch it.
    return fermat(N,k), miller_rabin(N,k)


def mod_exp(x, y, N):
    # You will need to implement this function and change the return value.
    # Time complexity of O(n)
    output = 1
    x = x % N
    while (y > 0):
        if (y & 1): output = (output * x) % N
        y = y >> 1
        x = (x * x) % N
    return output

def fprobability(k):
    # You will need to implement this function and change the return value.
    # Time complexity of O(n)
    return 1 - (1 / (pow(2, k)))


def mprobability(k):
    # You will need to implement this function and change the return value.
    # Time complexity of O(n)
    return 1 - (1 / (pow(4, k)))


def fermat(N,k):
    # You will need to implement this function and change the return value, which should be
    # either 'prime' or 'composite'.
	#
    # To generate random values for a, you will most likley want to use
    # random.randint(low,hi) which gives a random integer between low and
    #  hi, inclusive.

    # Time complexity of O(k*logn)

    # Check for edge cases
    if N <= 1:
        return "composite"
    if N <= 3:
        return "prime"
    if  (N % 2 == 0):
        return "composite"

    # Implement Fermat algorithm
    for x in range(k):
        a = random.randint(1, N - 1)
        if (mod_exp(a, N-1, N) != 1): return "composite"
    return "prime"


def miller_rabin(N,k):
    # You will need to implement this function and change the return value, which should be
    # either 'prime' or 'composite'.
	#
    # To generate random values for a, you will most likley want to use
    # random.randint(low,hi) which gives a random integer between low and
    #  hi, inclusive.

    # Time complexity of O(k*log3n)

    # Check for edge cases
    if N <= 1:
        return "composite"
    if N <= 3:
        return "prime"
    if (N % 2 == 0):
        return "composite"

    # Implement Miller-Rabin algorithm
    a = 0
    r = N - 1
    while r % 2 == 0:
        a += 1
        r //= 2
    for x in range(k):
        c = random.randint(2, N - 1)
        d = mod_exp(c, r, N)
        if (d == N - 1 or d == 1): continue
        for x in range(a - 1):
            d = mod_exp(d, 2, N)
            if (d == N - 1): break
        else: return 'composite'
    return 'prime'

