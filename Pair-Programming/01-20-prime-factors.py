"""
Pair Programming - 01/20/16
Ozzie and Nitika

------------
Pair Problem

Project Euler ("Euler" rhymes with "boiler") is a site with a lot of problems you can solve. Solving Project Euler problems is a fun way to work on your coding (and mathematical) skills.

If you make an account on Project Euler, you can submit solutions to verify that you've solved a problem correctly. The following is Problem 3:

The prime factors of 13195 are 5, 7, 13 and 29.

What is the largest prime factor of the number 600851475143 ?
See if you can optimize your solution. What is the complexity of your program?

## Our approach here is to start with the smallest prime (2) and continue to try
increasing factors. But also dividing the number n by any factors to reduce its
size. We'll be left with a list of the factors, of which we just return the largest.
"""

def prime_factor(n):
    factor = []
    i = 2
    while i <= n:
        while n%i==0:
            factor.append(i)
            n = n//i
        i+=1
    return max(factor)
​
prime_factor(600851475143)
