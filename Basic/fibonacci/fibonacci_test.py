from fibonacci import fibonacci

def test():
    failed = []
    passed = []

    # 1
    (passed if fibonacci(1) == 1 else failed).append(1)

    # 2
    (passed if fibonacci(2) == 1 else failed).append(2)

    # 3
    (passed if fibonacci(10) == 55 else failed).append(3)

    # 4
    (passed if fibonacci(1024) == 4506699633677819813104383235728886049367860596218604830803023149600030645708721396248792609141030396244873266580345011219530209367425581019871067646094200262285202346655868899711089246778413354004103631553925405243 else failed).append(4)
    
    if failed:
        print(f"Failed tests: {failed}")
    else:
        print("PASSED!")


if __name__ == "__main__":
    test()
