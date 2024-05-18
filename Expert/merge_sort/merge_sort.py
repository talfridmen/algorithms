def merge_sort(lst):
    if len(lst) == 1:
        return lst
    else:
        l_bottom, l_top = merge_sort(lst[:len(lst)//2]), merge_sort(lst[len(lst)//2:])
        new_l = []
        i, j = 0, 0
        while i < len(l_bottom) and j < len(l_top):
            if l_bottom[i] <= l_top[j]:
                new_l.append(l_bottom[i])
                i += 1
            else:
                new_l.append(l_top[j])
                j += 1
        if i == len(l_bottom):
            new_l.extend(l_top[j:])
        elif j == len(l_top):
            new_l.extend(l_bottom[i:])
        else:
            raise ValueError("1")
        return new_l
