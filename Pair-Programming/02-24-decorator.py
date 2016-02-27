"""
Pair Problem #2

This function is boring:

def square(x):
    return x * x

square(5)
## 25

Write a decorator called talky so that when you run this:

@talky
def square(x):
    return x * x

answer = square(5)
You get the following output:

Oh hi!
The result sure is 25!
Extension: Write a decorator talky_with, so that when you run this:

@talky_with("Aaron")
def square(x):
    return x * x

answer = square(5)
You get the following output:

Oh hi! I'm Aaron.
The result sure is 25!
"""


def talky(func):
    def func_wrapper(x):
        return "Oh hi!\nThe result sure is {}!".format(func(x))
    return func_wrapper
​
@talky
def square(x):
    return x * x
​
print square(5)
​
​
​
def talky_with(name):
    def tags_decorator(func):
        def func_wrapper(x):
            return "Oh hi! I'm {}.\nThe result sure is {}!".format(name,func(x))
        return func_wrapper
    return tags_decorator
​
@talky_with("Aaron")
def square(x):
    return x * x
​
print square(5)
