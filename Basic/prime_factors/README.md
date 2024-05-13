# prime_factors
##### From wikipedia
Prime factorization of any given number is to breakdown the number into its factors until all of its factors are prime numbers. This can be achieved by dividing the given number from smallest prime number and continue it until all its factors are prime.

## What will we do?
We will write a function that receives an input number, and breaks it down to all its prime numbers.

## How will it work?
In order to get all the prime factors, we can divide the number again and again by its smallest divisor, until we get to 1. 
For example, the number 300 will break down as follows:
$ 300 / 2 = 150 $
$ 150 / 2 = 75 $
$ 75 / 3 = 25 $
$ 25 / 5 = 5 $
$ 5 / 5 = 1 $
we got the prime list of $ 2,2,3,5,5 $

## How do we implement it?
- Create a function that receives an input integer
- Create a list of factors to append the results to
- Create an integer variable for the next factor to check
- Create a loop that stops when the number is equal 1
- In each iteration of the loop, check if the number is divisible by the factor.
- If it is divisible, append the factor to the list, and divide the number by the factor
- If it is not divisible, add 1 to the factor, and try again

This is a simplistic solution. There are other solutions. Think if and how you can improve on this method.