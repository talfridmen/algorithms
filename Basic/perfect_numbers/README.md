# Perfect Numbers
##### From wikipedia
A number is called a perfect number if by adding all the positive divisors of the number (except itself), the result is the number itself.

## What will we do?
We will create a test, that receives a number, and tests whether it is a perfect number or not.

## How will it work?
To find if a number is perfect, we need to calculate all of its positive divisors, except itself and sum them together.

## How do we implement it?
- Create a function that receives an input integer
- Initialize an integer variable responsible to sum the divisors
- Create a loop to run for every possible factor from 1 to N-1.
- For each iteration, check if this is a divisor
  - How?
- If it is a divisor add it to the sum variable
- After the loop finishes, check if we received the correct value, and return the result.

If you want to improve this even further, think how you can reduce the iterations required, but make sure to beware of edge-cases :)
