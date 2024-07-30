def fibonacci(idx):
    if(idx <= 2):
        if(idx < 0): 
            return -1
        if(idx == 0): 
            return 0
        if(idx == 1): 
            return 1
        if(idx == 2): 
            return 1

    i = 2 
    firstDigit = 1 
    secondDigit = 2
    tempDigit = 0
    while(i < idx):
        tempDigit = secondDigit
        secondDigit += firstDigit
        firstDigit = tempDigit
        i = i + 1 
    print(f"fibonacci[{idx}] = {firstDigit}")
    return firstDigit

fibonacci(10)