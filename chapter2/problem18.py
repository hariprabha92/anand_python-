'''  Write a program to print each line of a file in reverse order. '''



def reverse():
        f=open('she.txt')
        l=[]
        for i in f:
                print i[::-1]
reverse()

