def fibonacci(idx):
#jtal    pass # Implement Here!
  x=0
  y=1

  if idx==0:
    return x
  elif idx==1:
    return y
# else
  while idx > 1 :
    t=x
    x=y
    y+=t
    idx-=1

  return y 
