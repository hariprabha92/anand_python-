''' Write a function reverse to reverse a list. Can you do this without using list slicing?'''
def reverse(l):
	l.insert(0,0)
	j=len(l)-1
	l=[l[i] for i in range(j,0,-1)]
	
	return l
a=reverse([1, 2, 3, 4])
print a
