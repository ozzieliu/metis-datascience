"""
Pair Problem - 2/4/2016
Ozzie with Thomas

Write a function to calculate factorials, and accompanying unit tests.
"""

import unittest

## Recursion
def factorial(n):
    """
    Straight forward implementation of factorial with recursion
    """
    if n == 0:
        return 1
    else:
        return n * factorial(n-1)

## Iteration
def factorial_iterate(n):
    result = 1
    while n > 1:
        result = result * n
        n = n-1

    return result

## There are faster and more efficient ways to do factorial

class TestFactorial(unittest.TestCase):

  def test_factorial(self):
      self.assertEqual(factorial(5), 120)
      self.assertEqual(factorial(4), 12)

if __name__ == '__main__':
    unittest.main()
