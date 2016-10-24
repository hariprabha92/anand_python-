



def filter(fun,r):
        return [i for i in r
			if fun(i)]



even=lambda x:x%2==0
print (filter(even,range(10)))

