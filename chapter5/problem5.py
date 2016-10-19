''' Write a function to compute the total number of lines of code in all python files in the specified directory recursively.'''
import sys
import os
count=0
c=0
def readlines(a):
	global c
	for l in open(a):
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
