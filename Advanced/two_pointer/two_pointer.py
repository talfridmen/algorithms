def two_pointer(lst, num):
    p1, p2 = 0, len(lst) - 1
    while p2 > p1 and lst[p1] + lst[p2] != num:
        if lst[p1] + lst[p2] < num:
            p1 += 1
        else:
            p2 -= 1
    return lst[p1] + lst[p2] == num