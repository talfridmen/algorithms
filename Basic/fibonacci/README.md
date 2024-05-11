# Monte-Carlo
##### From wikipedia
In mathematics, the Fibonacci sequence is a sequence in which each number is the sum of the two preceding ones. Numbers that are part of the Fibonacci sequence are known as Fibonacci numbers, commonly denoted Fn . The sequence commonly starts from 0 and 1, although some authors start the sequence from 1 and 1 or sometimes (as did Fibonacci) from 1 and 2. Starting from 0 and 1, the sequence begins:
$0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144, ....$

## What will we do?
We will create a function that will calculate the N'th value of the fibonacci sequence

## How will it work?
There are multiple methods to calculate the N'th value of the fibonacci sequence. We will work with a simple loop-implementation. For more practice you can try implementing more methods, as described bellow in the ["other methods"](#othermethods) section bellow.

## How do we implement it?
We will implement this function with a loop.
- Create a function that receives the index of the sequence that we want to calculate.
- Start with two variables - `x` and `y`.
- Create a loop to run as many times as required, as requested by the user.
- in each loop, replace `x` and `y` with the new values - `x` will receive the value of `x + y` and `y` will receive the previous value of `x`
  - Think of how to implement these substitutions
- after the loop completes, the value of `x` should be the correct value, so we should return it.

_Notice: This is not the most efficiet solution. The most efficient solution is using the [Direct Solution](#direct). This one is, though, a more interesting implementation solution.

## <a name="othermethods">Other Methods</a>
If you want to practice more techniques, we can do this in more methods, as described bellow:
### <a name="direct">Direct calculation</a>
It is possible to get the exact value of the N'th fibonacci sequence by a simple quick calculation.
This is the direct approach, but we do need to be careful with this one, as python's implementation of floating point numbers sometimes rounds some values, so we can get values that are close, but not exact.

The way to do this, is with the following equation:
$\frac{(\frac{1 + \sqrt 5}{2}) ^ n - (\frac{1 + \sqrt 5}{2}) ^ n}{\sqrt 5}$

### Recursion
Fibonacci is one of the most classic methods to teach recursion.
Recursion is when you try to calculate a large number by splitting it into smaller problems, and solving them - again and again and again.

For the fibonacci number, as we know the N'th value is simply the sum of the N-1'th value and the N-2'th value. Or in formal mathematical syntax:
$a_n = a_{n-1} + a_{n-2}$

This means, that if we are asked to calculate the value of the N'th element, we can use the same function to calculate the values of the N-1'th element and the N-2'th element.
Then, to calculate the N-1'th element, we will want to calculate the N-2'th and the N-3'th element. And so on and on.
Until when? Until we get to the basic values - the 1'st value which is 1, and the second value which is also 1. These values will be returned by the function without any calculation.

_Notice: this is not a very efficient solution. It takes O($2^n$) time, which is one of the worst time complexities available._

### Recursion with memoization
As you might have noticed in the previous method, bothe the N'th element and the N-1'th elemnt require the N'2th element. if we go deeper, the N-3'th value is required in 3 different calculations - N-1 once, and N-2 twice. 
as we go deeper in, these calculations repeat themselves again and again.
This means that if we want to calculate the N'th element, we will calculate some of the elements many many times. 

As calculating any element in this method is quite difficult, we will want to avoid calculating it over and over again.

We will use memoisation!
memoisation allows us to "remember" old value we had calculated in the past, and use it directly instead of calculating it again.
we can create a list of objects that will be N cells long. each will be filled with the value in its index as we go along.

_Notice: this is still not a very efficient solution. Although it only runs in O(n) time, it also takes O(n) space in memory. Still much better than simple recursion_