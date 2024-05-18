from perfect_numbers import perfect_numbers

def test():
    failed = []
    passed = []

    # 1
    (passed if perfect_numbers(6) is True else failed).append(1)

    # 2
    (passed if perfect_numbers(28) is True else failed).append(2)

    # 3
    (passed if perfect_numbers(496) is True else failed).append(3)

    # 4
    (passed if perfect_numbers(137438691328) is True else failed).append(4)

    # 5
    (passed if perfect_numbers(55) is False else failed).append(5)

    # 6
    (passed if perfect_numbers(137438691325) is False else failed).append(5)
    
    if failed:
        print(f"Failed tests: {failed}")
    else:
        print("PASSED!")


if __name__ == "__main__":
    test()
