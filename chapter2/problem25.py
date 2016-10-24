''' Python provides a built-in function map that applies a function to each element of a list. Provide an implementation for map using list comprehensions.'''

''' >>> def square(x): return x * x
...
>>> map(square, range(5))
[0, 1, 4, 9, 16] '''

def map(fun,r):
	return [fun(i) for i in r]



square=lambda x:x*x
print (map(square,range(10)))


