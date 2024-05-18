def binary_search(lst, num):
    if len(lst) == 1:
        return 0 if lst[0] == num else None
    if lst[len(lst) // 2] <= num:
        val = binary_search(lst[len(lst) // 2:], num)
        if val is not None:
            return val + len(lst) // 2
        return None
    return binary_search(lst[:len(lst) // 2], num)
