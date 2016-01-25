"""
## Pair Programming 1/12/2016
## Reverser of string
## Ozzie with Bryan
Pair Problem

You may be asked to write code that reads from standard input and/or writes to standard output. For example, you will be asked to do that now.

Write a program that reads from standard input and writes each line reversed to standard output. For example, if your Python script is called "reverser.py", you could do this at a command line:

echo -e "first line\nsecond line" | python reverser.py
And the output should be:

enil tsrif
enil dnoces
"""

# magic string reverse super useful and stuff
import sys

n = sys.stdin.read()

def rev(n): return n[::-1]

print(rev(n))
