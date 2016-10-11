'''  Implement unix commands head and tail. The head and tail commands take a file as argument and prints its first and last 10 lines of the file respectively.'''
def head_tail():
        f=open('she.txt')
        l=[]
        [l.append(line) for line in f]
	a=l[:3]
	b=l[len(l)-2: ]
	p(a)
	p(b)
def p(l):
	for i in l:
		print i
head_tail()
