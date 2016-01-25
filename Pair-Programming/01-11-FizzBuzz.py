"""
## Pair programming 01 - 1/11/2016
## FizzBuzz
## Ozzie with Matt

Pair Problem

This is Fizz Buzz. It is perhaps the most well-known interview programming problem. You're not super likely to see this exact problem in an interview, but you should be familiar with it, and certainly able to solve it.

Write a program that prints the numbers from 1 to 100. But for multiples of three print “Fizz” instead of the number and for the multiples of five print “Buzz”. For numbers which are multiples of both three and five print “FizzBuzz”.
For example, the output (just for the section 8 to 16) could look like this:

8
Fizz
Buzz
11
Fizz
13
14
FizzBuzz
16
"""

for number in range(1,101):
    if number % 3 == 0 and number % 5 == 0:
        print 'FizzBuzz'
    elif number % 3 == 0:
        print 'Fizz'
    elif number % 5 == 0:
        print 'Buzz'
    else:
        print number
