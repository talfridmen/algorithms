def perfect_numbers(num):
#    pass # Implement Here!
	sum=1
	for d in range(2,num):
	   if num%d == 0:
	      sum+=d

	if sum==num: return True
	else: return False
