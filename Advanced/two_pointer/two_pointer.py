def two_pointer(lst, num):
#jtal    pass # Implement Here!
   ilow=0
   ihigh=len(lst)-1

   while(ilow<ihigh):
      sum=lst[ilow]+lst[ihigh]
      if sum==num: return True
      elif sum > num: ihigh-=1 
      else: ilow+=1

   return False
