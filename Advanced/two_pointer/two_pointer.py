def two_pointer(lst, num):
    first_i, last_i = 0, len(lst)-1
    while first_i <= last_i:
        sum = lst[first_i] + lst[last_i]
        if sum == num:
            return True
        elif sum > num:
            last_i -= 1
        else:
            first_i += 1
    return False
