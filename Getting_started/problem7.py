#How many multiplications are performed when each of the following lines of code is executed?

numcalls = 0
def square(x):
    global numcalls
    numcalls = numcalls + 1
    return x * x
    
    
print square(5)
print square(2*5)

number_of_muliplications=numcalls
print number_of_muliplications
