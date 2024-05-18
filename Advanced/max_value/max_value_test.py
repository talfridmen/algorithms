from max_value import max_value

def test():
    failed = []
    passed = []

    # 1
    (passed if max_value([1,2,3,4,5]) == 5 else failed).append(1)

    # 2
    (passed if max_value([1,3,5,4,2]) == 0 else failed).append(2)

    # 3
    (passed if max_value([-1, -2, -3, -4, -5]) == -1 else failed).append(3)

    # 4
    (passed if max_value([12,54,65,5,65,41,3,58,2,15]) == 65 else failed).append(4)
    
    if failed:
        print(f"Failed tests: {failed}")
    else:
        print("PASSED!")


if __name__ == "__main__":
    test()
