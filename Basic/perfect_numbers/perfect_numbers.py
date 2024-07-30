def perfect_numbers(num):
    if num < 6:
        return False
    from math import isqrt
    sum = 1
    for i in range(2,isqrt(num)+1):
        if num%i == 0:
            sum = sum + i + num//i
            
    if sum == num:
        return True
    else:
        return False
