"""
Pair Problem - 2/2/2016
Ozzie & Emily

Generating Fibonacci numbers is a classic programming exercise.

Each Fibonacci number is the sum of the two previous. Starting with 1 and 2, we have fib(1) == 1, fib(2) == 1, fib(3) == 2, fib(4) == 3, fib(5) == 5, and fib(6) == 8. A little further on, fib(12) == 144.

Write a function definition skeleton with doctests that cover all the examples given above. Run the doctests to confirm that your tests fail.

Fill in the function definition to calculate Fibonacci numbers. Run your doctests to confirm that the tests pass.

If you have time, think about edge cases, and try to make your implementation more efficient.
"""


fib_dict = {1: 1, 2: 1}

def fib(n):
    """
    >>> fib(1)
    1
    >>> fib(2)
    1
    >>> fib(3)
    2
    >>> fib(4)
    3
    >>> fib(5)
    5
    >>> fib(6)
    8
    >>> fib(12)
    144
    """

    ## Do some informal memoization to cut down on recursion depth for
    ## subsequent calls.
    if n in fib_dict:
        return fib_dict[n]

    result = fib(n-1) + fib(n-2)

    fib_dict[n]=result
    return result

if __name__ == "__main__":
    import doctest
    doctest.testmod(verbose = True)
