# Is Prime
##### From wikipedia
A primality test is an algorithm for determining whether an input number is prime. Among other fields of mathematics, it is used for cryptography. Unlike integer factorization, primality tests do not generally give prime factors, only stating whether the input number is prime or not.

## What will we do?
We will create a test, that receives a number, and tests whether it is prime or not.

## How will it work?
There are multiple methods to test if a number is prime. For large numbers, like used in cryptography, a probabilistic or heuristic test is normally used, as it is "good enough", and worth the mistakes in order to make it a quicker check.
We will actually test this is a more definitive approach, which might take longer.
The way this test works, is by trying every possible factor, and testing if the number is divisible by it. If even one is found that is not 1 or the number itself - the number is not prime. Otherwise, it is prime.

## How do we implement it?
- Create a function that receives an integer
- Create a loop to run for every possible factor.
  - Think of what will the limits of the loop be
- in each iteration of the loop, use the modulo function to check if the number is divisible by it.
  - How?
- Once we hit a number that we find to be a divisor of our input number, it is an indication that it is not a prime number. Otherwise, if we finish the loop, we can say with certainty it is prime
