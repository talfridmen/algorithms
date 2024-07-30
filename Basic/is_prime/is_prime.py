import sys
#Test if argument is a prime number
def is_prime(number):
    if number >1:
        #Starting range from 4 and see if the modulu has remainders
        for i in range(2,int(number/2)+1):
            print (f"Iteration: {i-1} - Remainder of {number} % {i}: {number %i}")
            #I know it's not usually common to declare var on iterations but it saved suplicating 'number %i'
            remainder = number %i
            #Test if the remainder is 0
            if remainder == 0:
                print (f"{number} is not a prime number since remainder is: {remainder}")
                return False
        else:
            #I wanted to keep the remainder var to explain why it's prime, but 2 & 3 are not iterated thus 
            #'i' is not declared at this point
            if number ==2 or number ==3:
                print(f"{number} is a prime number")
            #Ultimately not primes and not 2,3 condition => this is a prime number       
            else:
                print(f"{number} is a prime number since remainder is: {remainder}")
            return True
    else:
        print (f"{number} is not a prime number")
        return False