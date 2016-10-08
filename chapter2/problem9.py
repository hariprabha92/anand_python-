'''  Write a function cumulative_product to compute cumulative product of a list of numbers.'''
def cumulative_product(l):
	#a=[]
        for i in range(1,len(l)):
                l[i]=l[i-1]*l[i]
        return l
print cumulative_product([1, 2, 3, 4])

