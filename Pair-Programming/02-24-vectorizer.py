"""
Pair Problem #1

text= ['It was the best of times, it was the worst of times.','My name is Inigo Montoya.You killed my father. Prepare to die.', 'Too weird to live, too rare to die!']

1) Using sklearn.feature_extraction.text CountVectorizer function, (also fit and transform) convert a collection of text documents to a matrix of token counts.

You will get a sparse matrix of output. ex:

(0, 0) 1 (0, 5) 2 (0, 11) 2 (0, 14) 2 (0, 15) 2 (0, 18) 2 (0, 20) 1 ... ... ...

Can you explain what each row of this matrix represents?
"""

from sklearn.feature_extraction.text import CountVectorizer
import numpy as np

text= ['It was the best of times, it was the worst of times.','My name is Inigo Montoya.You killed my father. Prepare to die.', 'Too weird to live, too rare to die!']

cv = CountVectorizer()
cv.fit_transform(text).shape

print cv.fit_transform(text)
​
print cv.fit_transform(text).toarray()

print cv.get_feature_names()
