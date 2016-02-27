"""
Pair Problem

You are given a list of numbers.

You want to find the block of numbers next to one another that add up to the biggest value for this list.

For example, if you have a list of 100 numbers, the answer could be that the numbers in positions 2 to 14 give the biggest sum, bigger than the sum for the numbers in positions 2 to 15 or 1 to 14 or 1 to 100 or any other such block of numbers that are next to one another.

Write code to find the optimal block for a given list of numbers.

Make sure your code runs in linear time.

Could be 1 number. Could be entire list. Numbers can be negative.
"""


def biggest_block(string):
    """
    Inchworm through the block, calculating each sum while incrementing end index.
    But if the sum is less than 0, it won't help any subsequent blocks, so we
    reset by changing position of the start index.
    """
    start = 0
    end = 1
    biggest_block = [start, end]
    biggest_sum = None
    n = len(string)
    while end < n:
        new_sum = sum(string[start:end])
        if new_sum > biggest_sum:
            biggest_sum = new_sum
            biggest_block = [start, end]
        if new_sum < 0:
            start = end
        end += 1
    return string[biggest_block[0]:biggest_block[1]]
​
#Test Cases
biggest_block([7, 9, -3, -10, -7, 8, -5, -5, -7, -7, 5, 1, 5, -8, 0, 8, -2, 4, 2, -1])
#[7, 9]
biggest_block([-2, 1, 2, 3, -1, 0, 100, -101, 50])
#[1, 2, 3, -1, 0, 100]
