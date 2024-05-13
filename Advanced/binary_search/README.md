# Binary Search
##### From wikipedia
In computer science, binary search is a method used for finding an item in a sorted list. It is an algorithm that is more efficient than linear search, which will go through every item in the list of items to find a particular item. However, the given list of items must be sorted first before a binary search algorithm can be used.

The binary search algorithm works by repeatedly splitting the sorted list into two and working on the part of the list that may contain the item that you are looking for until the final list contains only one item.

## What will we do?
We will implement the binary search algorithm, as a function that gets a sorted list of integers and an integer to look for, and return the index if the integer in the list.
If the object doesn't exist in the list, we will return None.

## How will it work?
To find the item, we will first check the middle index. If it is larger than the wanted item, we will go to the middle of the lower half. If it is smaller, we will go to the top half, and repeat this process.
There are two main approaches for this algorithm, and I encourage you to implement both. We will start with the [Loop](#loop) approach, and continue to the [Recursive](#recursive) approach

## <a name="loop">How do we implement it? - Loop approach</a>
- Create a function that receives a list of integers and an integer to search for
- Create 3 indexes - one will start at 0, one will be at the end of the list, and one in the middle.
- Run a loop that will go on as long as the start and end indexes are not pointing to the same index
- In each iteration: 
  - calculate the middle index
  - check if the value in the middle index is:
    - Equal - return the index
    - Greater - move the end index to the middle index
    - Lower - move the start index to the middle index
- If we exit the loop without returning any value, return None, as we never found the required value

## <a name="recursive">How do we implement it? - Recursive approach</a>
- Create a function that receives a list of integers and an integer to search for
- If the list is empty, return None
- If the list is of size 1, check if the value is equal the number we searched for and return 0 or None accordingly.
- Check if the middle index of the list has a value:
  - Equals: return the index
  - Greater: run the function again with only the bottom half of the list
  - Lower: run the function again with only the top half of the list
    - What did we forget?