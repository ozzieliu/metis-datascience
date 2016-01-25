"""
Pair Programming - 01/19/16
Ozzie and Justin

------------
Pair Problem

A version of this problem was faced at a whiteboard by a Metis student in an interview for a data scientist position on April 16, 2015.

In programming languages, and especially in Lisps, there can be a lot of parentheses. The parentheses have to be "balanced" to be valid. For example, ()(()) is balanced, but ()()) is not balanced. Also, )((()) is not balanced.

Write a function that takes a string and returns True if the string's parentheses are balanced, False if they are not.

Here are examples to test your function with:

(()()()()) should return True
(((()))) should return True
(()((())())) should return True
((((((()) should return False
())) should return False
(()()))(() should return False
"""

## Strategy here is to use a stack data structure. Adding to the stack at occurence
## of ( and popping off at ). If stack is not empty, there's an imbalance.

def check_balance(parens):
    stack = []
    for i in parens:
        if i == '(':
            stack.append(i)
        elif i == ')':
            try:
                stack.pop()
            except:
                return False
        else:
            pass
    return not stack

check_balance('(()()()())')
