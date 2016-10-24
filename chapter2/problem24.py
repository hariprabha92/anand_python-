'''  Provide an implementation for zip function using list comprehensions.'''
def zip(l1,l2):
	
	return [(l1[i],l2[i]) for i in range(len(l1))]



print (zip([1,2,3],['a','b','c']))
