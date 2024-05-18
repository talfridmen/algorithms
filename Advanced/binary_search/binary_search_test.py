from binary_search import binary_search

def test():
    failed = []
    passed = []

    # 1
    (passed if binary_search([1,2,3,4,5], 3) == 2 else failed).append(1)

    # 2
    (passed if binary_search([1,2,3,4,5], 1) == 0 else failed).append(2)

    # 3
    (passed if binary_search([1,2,3,4,5], 4) == 3 else failed).append(3)

    # 4
    (passed if binary_search([1,2,3,4,5], 8) is None else failed).append(4)

    # 5
    (passed if binary_search([1,2,4,5], 3) is None else failed).append(5)
    
    if failed:
        print(f"Failed tests: {failed}")
    else:
        print("PASSED!")


if __name__ == "__main__":
    test()
