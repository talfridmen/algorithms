def binary_search(lst, num):
    from statistics import mean
    first_i, last_i, i = 0, len(lst)-1, len(lst)//2
    
    while first_i < last_i:
        i = int(mean([last_i,first_i]))
        if lst[i] == num:
            return i
        elif lst[i] > num:
            if last_i == i:
                return None
            last_i = i
        else:
            if first_i == i:
                return None
            first_i = i

    return None

