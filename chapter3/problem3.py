import os
def read(d):
	return ( f for f in os.listdir(d)
		if os.path.isfile(f))




for f in read('.'):
	l=os.stat(f)
	print (f,l[6],l[8])
	



