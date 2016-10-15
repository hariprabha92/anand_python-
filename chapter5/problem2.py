'''  Write a program that takes one or more filenames as arguments and prints all the lines which are longer than 40 characters.'''
import sys
def readlines(files):
	
	return(line for f in files 
		for line in open(f) 
		if len(line)>40)
	
def main():
	lines=readlines(sys.argv[1:])
	for line in lines:
		print(line)
	
	
if __name__=='__main__':
	main()

