''' Write a function cumulative_product to compute cumulative product of a list of numbers.'''
def cumulative_sum(l):

	for i in range(1,len(l)):
		l[i]=l[i-1]+l[i] 
	return l
print cumulative_sum(['a','b','c','d'])
print cumulative_sum([4, 3, 2, 1])
