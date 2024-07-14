from two_pointer import two_pointer

def test():
    failed = []
    passed = []

    # 1
    (passed if two_pointer([1,3,4,6,7], 8) is True else failed).append(1)
    
    # 2
    (passed if two_pointer([1,3,4,6,7], 4) is True else failed).append(2)
    
    # 3
    (passed if two_pointer([1,3,4,6,7], 9) is True else failed).append(3)
    
    # 4
    (passed if two_pointer([1,3,4,6,7], 10) is True else failed).append(4)
    
    # 5
#jtal this test should return false    (passed if two_pointer([1,3,4,8,11], 6) is True else failed).append(5)
    (passed if two_pointer([1,3,4,8,11], 6) is False else failed).append(5)
    
    # 6
    (passed if two_pointer([1,3,4,8,11], 13) is False else failed).append(6)

    if failed:
        print(f"Failed tests: {failed}")
    else:
        print("PASSED!")


if __name__ == "__main__":
    test()
