'''  Write a program reverse.py to print lines of a file in reverse order.

$ cat she.txt
She sells seashells on the seashore;
The shells that she sells are seashells I'm sure.
So if she sells seashells on the seashore,
I'm sure that the shells are seashore shells.

$ python reverse.py she.txt
I'm sure that the shells are seashore shells.
So if she sells seashells on the seashore,
The shells that she sells are seashells I'm sure.
She sells seashells on the seashore; '''
def reverse():
	f=open('she.txt')
	l=[]
	[l.append(line) for line in f]
	for i in range(-1,-len(l)-1,-1):
		print l[i]
reverse()
