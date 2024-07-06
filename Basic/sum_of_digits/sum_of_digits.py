def sum_of_digits(num):
#jtal    pass # Implement Here!
   sum=0
   while (num>0):
      sum += num%10
      num = num//10

   return sum
