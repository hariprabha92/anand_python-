''' Write a function extsort to sort a list of files based on extension.'''
def extsort(l):
	l=[a lambda x:x.split('.')]
	return l
print extsort(['a.c', 'a.py', 'b.py', 'bar.txt', 'foo.txt', 'x.c'])

