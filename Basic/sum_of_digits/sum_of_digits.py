def sum_of_digits(num):
    sod = 0
    while num > 0:
        sod += num % 10
        num //= 10
    return sod
