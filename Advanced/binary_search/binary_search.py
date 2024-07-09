def binary_search(lst, num):
#jtal    pass # Implement Here!
   startIdx=0
   endIdx=len(lst)-1
   
   while(startIdx<=endIdx):
      midIdx=(startIdx+endIdx)//2
      if lst[midIdx] == num: return midIdx
      elif lst[midIdx] < num: startIdx=midIdx+1
      elif lst[midIdx] > num: endIdx=midIdx-1

   return None
