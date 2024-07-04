def fibonacci(limit):
    x=0
    y=1
    for i in range (limit):
        z=x+y
        x=y
        y=z
    return x
    
def fibonacci_recursive(limit):
    if limit <= 1:
        return limit
    return fibonacci_recursive(limit-1) + fibonacci_recursive(limit-2)

def userinput():
    limit = int(input("Enter limit: "))
    return limit

print(fibonacci(userinput()))