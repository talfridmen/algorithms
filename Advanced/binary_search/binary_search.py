def binary_search(lst, num):
    if not lst:
        return None
    elif len(lst)==1:
        if lst[0] == num:
            return 0
        else:
            return None

    i = round(len(lst)/2)
    
    if lst[i] == num:
        return i
    elif lst[i] > num:
        return binary_search(lst[:i],num)
    elif lst[i] < num:
        e = binary_search(lst[-i:],num)
        if e == None:
            return None
        else:
            return i + e + len(lst)%2
