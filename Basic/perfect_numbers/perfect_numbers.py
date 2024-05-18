def perfect_numbers(num):
    summ = 0
    for i in range(1, int(num ** 0.5) + 1):
        if num % i == 0:
            summ += i
            if num // i > i:
                summ += num // i
    return summ == 2 * num