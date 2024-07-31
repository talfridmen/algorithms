def prime_factors(num):
    factors = []
    if -3<=num<=3 :
        factors.append(num)
        return factors

    i = 2

    while num != 1 and num != -1:
        if num%i == 0:
            factors.append(i)
            num = num//i
        else:
            i+=1

    return factors
