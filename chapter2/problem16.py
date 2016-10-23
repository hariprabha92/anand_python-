''' Write a function extsort to sort a list of files based on extension.'''
def extsort(l):
	l.sort(key=lambda x:xsplit(".")[-1])
	return l



print extsort(['a.c', 'a.py', 'b.py', 'bar.txt', 'foo.txt', 'x.c'])

