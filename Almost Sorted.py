'''
Given an array of integers, determine whether the array can be sorted in ascending order using only one of the following operations one time.

Swap two elements.
Reverse one sub-segment.
Determine whether one, both or neither of the operations will complete the task. Output is as follows.

If the array is already sorted, output yes on the first line. You do not need to output anything else.

If you can sort this array using one single operation (from the two permitted operations) then output yes on the first line and then:

If elements can only be swapped,  and , output swap l r in the second line.  and  are the indices of the elements to be swapped, assuming that the array is indexed from  to .
If elements can only be reversed, for the segment , output reverse l r in the second line.  and  are the indices of the first and last elements of the subarray to be reversed, assuming that the array is indexed from  to . Here  represents the subarray that begins at index  and ends at index , both inclusive.
If an array can be sorted both ways, by using either swap or reverse, choose swap.

If the array cannot be sorted either way, output no on the first line.
Example

Either swap the  and  at indices 3 and 4, or reverse them to sort the array. As mentioned above, swap is preferred over reverse. Choose swap. On the first line, print yes. On the second line, print swap 3 4.

Function Description

Complete the almostSorted function in the editor below.

almostSorted has the following parameter(s):

int arr[n]: an array of integers
Prints

Print the results as described and return nothing.
Input Format

The first line contains a single integer , the size of .
The next line contains  space-separated integers  where .

Constraints



All  are distinct.

Output Format

If the array is already sorted, output yes on the first line. You do not need to output anything else.

If you can sort this array using one single operation (from the two permitted operations) then output yes on the first line and then:

a. If elements can be swapped,  and , output swap l r in the second line.  and  are the indices of the elements to be swapped, assuming that the array is indexed from  to .

b. Otherwise, when reversing the segment , output reverse l r in the second line.  and  are the indices of the first and last elements of the subsequence to be reversed, assuming that the array is indexed from  to .

 represents the sub-sequence of the array, beginning at index  and ending at index , both inclusive.

If an array can be sorted by either swapping or reversing, choose swap.

If you cannot sort the array either way, output no on the first line.
Sample Input 1

STDIN   Function
-----   --------
2       arr[] size n = 2
4 2     arr = [4, 2]
Sample Output 1

yes
swap 1 2
Explanation 1

You can either swap(1, 2) or reverse(1, 2). You prefer swap.

Sample Input 2

3
3 1 2
Sample Output 2

no
Explanation 2

It is impossible to sort by one single operation.

Sample Input 3

6
1 5 4 3 2 6
Sample Output 3

yes
reverse 2 5
Explanation 3

You can reverse the sub-array d[2...5] = "5 4 3 2", then the array becomes sorted.
'''


#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'almostSorted' function below.
#
# The function accepts INTEGER_ARRAY arr as parameter.
#

def almostSorted(arr):
    # Write your code here
    n = len(arr)

    # Helper function to check if the array is sorted
    def is_sorted(arr):
        return all(arr[i] <= arr[i+1] for i in range(n-1))

    if is_sorted(arr):
        # Array is already sorted
        print("yes")
    else:
        # Find the first and last elements that are out of place
        left, right = 0, n - 1
        while left < right and arr[left] < arr[left+1]:
            left += 1
        while right > left and arr[right] > arr[right-1]:
            right -= 1

        # Try swapping the elements
        arr[left], arr[right] = arr[right], arr[left]
        if is_sorted(arr):
            print("yes")
            print(f"swap {left+1} {right+1}")
            return
        else:
            # Swap back the elements for further checks
            arr[left], arr[right] = arr[right], arr[left]

        # Try reversing a subsegment
        arr[left:right+1] = reversed(arr[left:right+1])
        if is_sorted(arr):
            print("yes")
            print(f"reverse {left+1} {right+1}")
            return
        else:
            # Array cannot be sorted
            print("no")

if __name__ == '__main__':
    n = int(input().strip())

    arr = list(map(int, input().rstrip().split()))

    almostSorted(arr)
