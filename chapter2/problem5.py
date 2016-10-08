''''Write a function factorial to compute factorial of a number. Can you use the product function defined in the previous example to compute factorial?'''
def factorial(l):
        p=1
        for i in range(1,l+1):
                p=p*i
        return p
a=factorial(4)
print a
