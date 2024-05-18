from prime_factors import prime_factors

def test():
    failed = []
    passed = []

    # 1
    (passed if set(prime_factors(5)) == {5} else failed).append(1)
    
    # 2
    (passed if set(prime_factors(10)) == {2, 5} else failed).append(2)
    
    # 3
    (passed if set(prime_factors(100)) == {2, 2, 5, 5} else failed).append(3)
    
    # 4
    (passed if set(prime_factors(38220)) == {2, 2, 3, 5, 7, 7, 13} else failed).append(4)

    if failed:
        print(f"Failed tests: {failed}")
    else:
        print("PASSED!")


if __name__ == "__main__":
    test()
