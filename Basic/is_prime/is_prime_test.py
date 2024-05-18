from is_prime import is_prime

def test():
    failed = []
    passed = []

    # 1
    (passed if is_prime(2) is True else failed).append(1)

    # 2
    (passed if is_prime(13) is True else failed).append(2)

    # 3
    (passed if is_prime(5754853343) is True else failed).append(3)

    # 4
    (passed if is_prime(10) is False else failed).append(4)

    # 5
    (passed if is_prime(1) is False else failed).append(5)
    
    if failed:
        print(f"Failed tests: {failed}")
    else:
        print("PASSED!")


if __name__ == "__main__":
    test()
