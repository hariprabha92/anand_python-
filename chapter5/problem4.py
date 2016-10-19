'''  Write a function to compute the number of python files (.py extension) in a specified directory recursively.'''
import sys
import os
count=0
def readDir(d):
	global count
	for p in os.listdir(d):
		f=os.path.join(d,p)	
		if  os.path.isfile(f) :
			if f.endswith('.py'):
				count += 1
		else:
			readDir(f)
	return count       


#djlgdl
print('Number of python files:',readDir('..'))

