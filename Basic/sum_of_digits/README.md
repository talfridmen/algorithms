# Sum of Digits
##### From wikipedia
In mathematics, the digit sum of a natural number in a given number base is the sum of all its digits. For example, the digit sum of the decimal number 9045 would be $9+0+4+5=18$.

## What will we do?
We will create a function that will calculate the Sum of the Digits of a given number.

##### Example
If the user runs sum_of_digits(135):
The function should eventually return 9 (1+3+5).

## How will it work?
In order to sum the digits, we will have to split the number into its digits, and add them up. There are a few methods to do this, but we will focus on the `modulo` method.
This method focuses on extracting the singles digit from the number, and then removing it from the number.
for example, for the number 9045, we will start by adding the 5, then remove it from the number, to be left with 904. Then we will add 4 to the 5, and remove it from the number, to be left with 90. We will repeat this until we got rid of all the digits in the number.
See the [other methods](#othermethods) section for other options

## How do we implement it?
- Create a function that receives an integer
- initialize a new variable that will be responsible for summing the digits as we calculate them
- Create a loop to run once for each digit.
  - Think of what will be the breakpoint of the loop
- in each iteration of the loop, use the modulo function to extract the singles digit. Add it to the relevant variable we created above.
  - Think of how we will do this
- Then, remove the last digit by dividing the number by 10.
  - We assume the input parameter was of type integer, so python keeps the value as an integer by removing any digits after the decimal point, regardless of its value.
- after the loop completes, the value of summation variable should be the sum of all the digits, so we can return it.

## <a name="othermethods">Other Methods</a>
There are other methods to do this. While they are not necessarily as effective as the `modulo` method, we can use them to learn new skills.
### The String Method
A string is just a list of characters.
An integer can be turned into a string, and back.
We can use these features to calculate the sum:
- turn the integer into a string.
- iterate over the characters in it, turning each one back to an integer and sum them up

This can be more efficient when used on very large numbers, as running bigint calculations are more complex than normal integers.
### Recursion Method
We can turn the loop described in the `modulo` method into recursion.
- Create a breakpoint when the number is a single digit number
- sum the number's singles digit (above), with a call to the function with the number divided by 10.

This method is essentially the same as the `modulo` method, but it will take longer because calling a function in python has both a memory and a time consumption.