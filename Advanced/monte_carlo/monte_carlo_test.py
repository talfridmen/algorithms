from monte_carlo import monte_carlo

def test():
    failed = []
    passed = []

    # 1
    (passed if 3 < monte_carlo(1000000) < 3.3 else failed).append(1)

    if failed:
        print(f"Failed tests: {failed}")
    else:
        print("PASSED!")


if __name__ == "__main__":
    test()
