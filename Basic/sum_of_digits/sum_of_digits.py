def sum_of_digits(num):
    sum=0
    while num//10 > 0:
        sum = sum + num%10
        num = num//10

    return sum + num
