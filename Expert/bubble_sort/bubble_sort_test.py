from bubble_sort import bubble_sort

def test():
    failed = []
    passed = []

    # 1
    (passed if bubble_sort([1, 2, 3]) == [1, 2, 3] else failed).append(1)

    # 2
    (passed if bubble_sort([1, 3, 2]) == [1, 2, 3] else failed).append(2)

    # 3
    (passed if bubble_sort([3, 2, 1]) == [1, 2, 3] else failed).append(3)

    # 4
    (passed if bubble_sort([5, 7, 3, 5, 9, 3, 3, 1]) == [1, 3, 3, 3, 5, 5, 7, 9] else failed).append(4)
    
    if failed:
        print(f"Failed tests: {failed}")
    else:
        print("PASSED!")


if __name__ == "__main__":
    test()