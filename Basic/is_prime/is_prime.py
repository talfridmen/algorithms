def is_prime(num):
#jtal    pass # Implement Here!
  if num==1:
    return False;
#else
  idx=2
  while(idx*idx <= num):   # I didn't use the sqrt math function as we still didn't talk about it.
    if num%idx == 0:
      return False
    idx+=1
#else
  return True
  
