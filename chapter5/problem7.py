import os
import sys
def split(filename,n):
	i,count=1,0
	fp=open("file_%d.txt"%(i),'w')
	for line in open(filename):
		if count == n :

			fp.close
			fp=open('file_%d.txt'%(i),'w')
			count=1
			i+=1
		fp.write(line)
		count+=1
	fp.close()



split(sys.argv[1],int(sys.argv[2]))
#split("a.txt",2)
