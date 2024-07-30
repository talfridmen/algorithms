def fibonacci(idx):
    if(idx <= 1):
        return idx

    tempNumber = 0
    firstNumber = 1 
    secondNumber = 2

    for i in range(2, idx):
        tempNumber = secondNumber
        secondNumber += firstNumber
        firstNumber = tempNumber
    return firstNumber
