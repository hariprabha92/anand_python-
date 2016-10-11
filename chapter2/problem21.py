''' Write a program wrap.py that takes filename and width as aruguments and wraps the lines longer than width.

$ python wrap.py she.txt 30
I'm sure that the shells are s
eashore shells.
So if she sells seashells on t
he seashore,
The shells that she sells are
seashells I'm sure.
She sells seashells on the sea
shore; '''
import sys
fp=open(sys.argv[1])
a=int(sys.argv[2])
line=[]
for line in fp:
#	print line 
#	print len(line)
#	print a
	if (len(line)) != a:
		print line
		print line[a:]
	else:
		pass
