import sys
import os
count=0
c=0
def readlines(a):
        global c
        for line in open(a):
		if not line.startswith('#') and line != '':
                	c+=1
        return c
def readDir(d):
        global count
        for p in os.listdir(d):
                f=os.path.join(d,p)
                if  os.path.isfile(f) :
                        if f.endswith('.py'):
                                count += 1
                                readlines(p)
                else:
                        readDir(f)
        return count,c



print('Number of python files and total number of lines of code:',readDir('.'))

