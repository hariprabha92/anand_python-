''' : Implement unix command grep. The grep command takes a string and a file as arguments and prints all lines in the file which contain the specified string.'''
import sys

fp = open(sys.argv[1])
for line in fp:
    if line.find(sys.argv[2]) != -1:
        print(line)
    else:
        pass
