def max_value(lst):
    mx = lst[0]
    for v in lst:
        if v > mx:
            mx = v
    return mx
