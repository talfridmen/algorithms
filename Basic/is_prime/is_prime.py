def is_prime(num):
    from math import isqrt
    if num == 1:
        return False

    for i in range(2,isqrt(num)+1):
        if num%i == 0:
            return False

    return True
