def fibonacci(idx):
    x = 1
    y = 0
    for i in range(idx):
        y,x = x,y
        x = x+y
    return y


def user_input ():
    iteration_number = int(input("Please enter the number of wanted iterations:"))
    return iteration_number

if __name__ == "__main__":
    print(fibonacci(user_input()))