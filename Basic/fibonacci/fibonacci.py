def fibonacci(idx):
    x, y = 1, 1
    for i in range(idx - 1):
        x, y = y, x+y
    return x
