def bubble_sort(lst):
    swap = True
    while swap:
        swap = False
        for i in range(0,len(lst)-1):
            if lst[i] > lst[i+1]:
                swap = True
                lst[i], lst[i+1] = lst[i+1], lst[i]
    return lst
