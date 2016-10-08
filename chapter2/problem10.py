'''Write a function unique to find all the unique elements of a list.'''
def unique(l):
	a=[]
	[ a.append(i) for i in l if i not in a]
	return a
print unique([1, 2, 1, 3, 2, 5])
