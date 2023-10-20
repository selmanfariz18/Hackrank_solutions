'''
Watson gives Sherlock an array of integers. His challenge is to find an element of the array such that the sum of all elements to the left is equal to the sum of all elements to the right.

Example


 is between two subarrays that sum to .


The answer is  since left and right sum to .

You will be given arrays of integers and must determine whether there is an element that meets the criterion. If there is, return YES. Otherwise, return NO.

Function Description

Complete the balancedSums function in the editor below.

balancedSums has the following parameter(s):

int arr[n]: an array of integers
Returns

string: either YES or NO
Input Format

The first line contains , the number of test cases.

The next  pairs of lines each represent a test case.
- The first line contains , the number of elements in the array .
- The second line contains  space-separated integers  where .

Constraints





Sample Input 0

2
3
1 2 3
4
1 2 3 3
Sample Output 0

NO
YES
Explanation 0

For the first test case, no such index exists.
For the second test case, , therefore index  satisfies the given conditions.

Sample Input 1

3
5
1 1 4 1 1
4
2 0 0 0
4
0 0 2 0
Sample Output 1

YES
YES
YES
Explanation 1

In the first test case,  is between two subarrays summing to .
In the second case,  is between two subarrays summing to .
In the third case,  is between two subarrays summing to .
'''

#!/bin/python3

import math
import os
import random
import re
import sys
import functools

#
# Complete the 'balancedSums' function below.
#
# The function is expected to return a STRING.
# The function accepts INTEGER_ARRAY arr as parameter.
#

def balancedSums(arr):
    # Write your code here
    found, pivot, left = 0, 0, 0
    right = functools.reduce(lambda x, y: x + y, arr[pivot + 1: len(arr) + 1], 0)
    found = (left == right)
    while (not found) and (pivot < len(arr) - 1):
        left = left + arr[pivot]
        right = right - arr[pivot + 1]
        pivot = pivot + 1
        found = (left == right)
        if found:
            break

    return "YES" if found == True else "NO"

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    T = int(input().strip())

    for T_itr in range(T):
        n = int(input().strip())

        arr = list(map(int, input().rstrip().split()))

        result = balancedSums(arr)

        fptr.write(result + '\n')

    fptr.close()
