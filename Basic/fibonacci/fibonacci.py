def fibonacci(idx):
    x=0
    y=1
    if idx <= 0:
        return False

    for i in range(idx):
        curr = x+y
        y = x
        x = curr

    return x
