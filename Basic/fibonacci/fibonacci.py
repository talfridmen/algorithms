def fibonacci(idx):
    x=0
    y=1
    for i in range(idx):
        new_y=x+y
        new_x=y
        y=new_y
        x=new_x
    return x
