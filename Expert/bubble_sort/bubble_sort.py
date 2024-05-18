def bubble_sort(lst):
    changed = True
    while changed:
        changed = False
        for i in range(len(lst) - 1):
            if lst[i] > lst[i+1]:
                lst[i], lst[i+1] = lst[i+1], lst[i]
                changed = True
    return lst


