from sum_of_digits import sum_of_digits

def test():
    failed = []
    passed = []

    # 1
    (passed if sum_of_digits(2) == 2 else failed).append(1)

    # 2
    (passed if sum_of_digits(13) == 4 else failed).append(2)

    # 3
    (passed if sum_of_digits(5754853343) == 47 else failed).append(3)

    # 4
    (passed if sum_of_digits(10) == 1 else failed).append(4)

    if failed:
        print(f"Failed tests: {failed}")
    else:
        print("PASSED!")


if __name__ == "__main__":
    test()
