"""
Pair Problem - 02/01/2016
Ozzie with James

Write a function that takes three arguments:

A list of lists, X_train, where each inner list is of length three and represents the position of a Wookiee in space, along the traditional x, y, and z axes.
A list of strings, y, the same length as the outer list X_train, where each string represents the color of a Wookiee at the corresponding position.
A list of lists, X_test, where each inner list is of length three and represents the position in space of a Wookiee of unknown color.
The function should produce a list of strings, the same length as the outer list, representing for each unknown Wookiee the color of the closest known Wookiee.

For example:
"""

X_train = [[1,   1,  1],
           [0,   0,  0],
           [-1, -1, -1],
           [10, 10, 10]]

y_train = ['red',
           'white',
           'blue',
           'chartreuse']

X_test = [[1.1, 1.1, 1.1]]

import scipy
​
def nearest_wookiee(X_train, y_train, wookiee, k):
    """
    For each position that I'm searching for, find the k closest wookiee and
    return its color value.
    """
    results = {scipy.spatial.distance.euclidean(key, wookiee):value for key,value in wookie_dict.items()}
    results = sorted(results.items())[:k]
    return [position[1] for position in results]
​
​
for wookiee in X_test:
    print nearest_wookiee(X_train, y_train, wookiee, 2)
