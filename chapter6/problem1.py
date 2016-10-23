def multiply(m,n):
  if m=0 or n=1 :
    return m
  else :
    return m+multiply(m,n-1)
