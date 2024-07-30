import sys
def sum_of_digits(number):
    sum = 0
    for digit in str(number):
        sum += int(digit)
    return sum
    

def get_input():
    if len(sys.argv) !=2:
        print ("Run me with python program.py <integer>")
        sys.exit(1)
    try:   
        argument = int(sys.argv[1])
        return argument
    except ValueError:
        print (f"Error: - Please provide with valid int")
        exit(1)

print(f"Sum of input is: {sum_of_digits(get_input())}")