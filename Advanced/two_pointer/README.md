# Two Pointer
#### From GeeksForGeeks
Two pointers is really an easy and effective technique that is typically used for searching pairs in a sorted array.
Given a sorted array A (sorted in ascending order), having N integers, find if there exists any pair of elements (A[i], A[j]) such that their sum is equal to X.

## What will we do?
We will implement the Two Pointer algorithm to detect if there is a pair of elements in an array of integers which the sum of the two elements is a specific value.

## How will it work?
We will start by looking at the two eges of the array. Everytime we will ask - are the two elements add up to the value that we are looking for, and if not we will move one of the pointers inwards in the list, deciding which one by the value of the sum in relation to the number we are looking for

## How do we implement it?
- Create a function that receives a list and an integer.
- Initialize two variables representing the indexes we are currently checking. One will point at index 0, while the other at the last element of the list
- Create a loop - think what should be the break condition.
- In each iteration, check if the current elements add up to the number we are looking for and decide what to do:
  - If it is what we want - return it
  - If it is greater, move the upper index 1 down. 
  - If it is lower, move the lower index 1 up. 
- If the loop ends with no answer - there is none.

## Other methods
It is also possible to implement this using recursion. Think how, and implement it.