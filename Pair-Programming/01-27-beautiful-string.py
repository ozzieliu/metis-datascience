"""
Pair Programming - 1/27/16
Ozzie with Diana

When John was a little kid he didn't have much to do. There was no internet, no
Facebook, and no programs to hack on. So he did the only thing he could... he
evaluated the beauty of strings in a quest to discover the most beautiful string
in the world.

Given a string s, little Johnny defined the beauty of the string as the sum of
the beauty of the letters in it. The beauty of each letter is an integer between
1 and 26, inclusive, and no two letters have the same beauty. Johnny doesn't
care about whether letters are uppercase or lowercase, so that doesn't affect
the beauty of a letter. (Uppercase 'F' is exactly as beautiful as lowercase 'f',
for example.)

You're a student writing a report on the youth of this famous hacker. You found
the string that Johnny considered most beautiful. What is the maximum possible
beauty of this string?

"""

a = 'ABbCcc'
b = 'Good luck in the Facebook Hacker Cup this year!'
c = 'Ignore punctuation, please :)'
d = 'Sometimes test cases are hard to make up.'
e = 'So I just go consult Professor Dalves'

import string

def beautify(words):
    ## Make lowercase, strip puncutation, and remove whitespace
    words = words.strip().replace(' ', '').translate(None, string.punctuation).lower()
    ## Count number of characters and store it in a dictionary
    letters = {char:words.count(char) for char in words}

    ## Sort the letters by their frequency
    sorted_letters = [letters[x] for x in sorted(letters, key = lambda x: letters[x], reverse = True)]
    ## asssign value for most common to least common letters
    value = range(26, 26-len(sorted_letters), -1)
    ## Calculate the beautiful number
    print sum([a*b for a,b in zip(sorted_letters, value)])

beautify(a)
beautify(b)
beautify(c)
beautify(d)
beautify(e)
