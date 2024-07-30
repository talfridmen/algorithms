def is_prime(num):
    pass # Implement Here!
    
    if num<=1: 
        return False
    if num==2:
        return True

# I'm creating 2 different variables, X recieves num as an integer and Y is set with 2 to divide it in the while loop
    X=2


# In this while loop I will check for the reminder of the dividing action, I'll use a for loop that will check for the reminder and if it is '0' it will return false, otherwise it will return true
    
    while (X<num):
        if num%X==0:
            return False
        X +=1

    return True


    
        


