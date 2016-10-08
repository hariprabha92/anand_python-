'''  Write a function group(list, size) that take a list and splits into smaller lists of given size.'''
def group(l,s):
	i=len(l)
	l=[l[j:j+s] for j in range(0,i,s)]
	return l
print group([1, 2, 3, 4, 5, 6, 7, 8, 9], 4)
	
		


