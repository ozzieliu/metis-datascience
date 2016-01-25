"""
Pair Programming - 01/14/16
Ozzie and Jordan
------------
Pair Problem

The data for this problem are the numbers 2, 7, 1, 5, and 10.

We want to know which of the numbers from 0 to 10 (by tenths) gives the smallest result when we do the following:

For each of the numbers in the data, subtract the candidate number and then square the result, then add up these numbers.

For example, to test the candidate number 8.2, we do the following:

2 - 8.2 = -6.2
         (-6.2)**2 = 38.44
7 - 8.2 = -1.2
         (-1.2)**2 = 1.44
1 - 8.2 = -7.2
         (-7.2)**2 = 51.84
5 - 8.2 = -3.2
         (-3.2)**2 = 10.24
10 - 8.2 = 1.8
           1.8**2  = 3.24

38.44 + 1.44 + 51.84 + 10.24 + 3.24 = 105.2
For candidate number 8.2, the result is 105.2. Can we get a smaller result for any of the other candidate numbers? Try them all and find the candidate number that gives the smallest result.

You might identify a shortcut to solving this problem. Write the code to try all the candidate numbers anyway.

Once you have an answer, also make a plot to show the results for all the candidate numbers.

As an extension, consider what class of problem this exercise represents. Can you write a general solution? Can you write a faster general solution?
"""

import matplotlib.pyplot as plt

## Approach 1 - straight forward calculation
def attempt1():
    total = 1000
    candidate = 0
    graphlist = []

    def find_candidate(number):
        global total
        global candidate
        result = (2-number)**2 + (7-number)**2 + (1-number)**2 + (5-number)**2 + (10-number)**2
        graphlist.append(result)
        if result < total:
            total = result
            candidate = number

    x = [float(j) / 10 for j in range(0, 101, 1)]
    for i in x:
        find_candidate(i)

    print total
    print candidate

    plt.plot(x,graphlist)
    plt.show()


## Attempt 2: more concise
def attempt2():
    y = []
    ## helper function to run the calculations
    def test(number):
        data = [2,7,1,5,10]
        result = sum([float(i-number)**2 for i in data])
        y.append(result)
        return result

    x = [float(j) / 10 for j in range(0, 101, 1)]
    results = {candidate:test(candidate) for candidate in x}

    print "Candidate: %r. Value: %r" %(min(results, key = results.get), min(results.values()))

    plt.plot(x,y)
    plt.show()
