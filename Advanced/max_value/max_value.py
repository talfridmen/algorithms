def max_value(lst):
    max=lst[0]
    i=0
    while i < len(lst):
        if lst[i] > max:
            max = lst[i]
        i += 1
    
    return max
