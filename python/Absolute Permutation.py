'''
We define  to be a permutation of the first  natural numbers in the range . Let  denote the value at position  in permutation  using -based indexing.

 is considered to be an absolute permutation if  holds true for every .

Given  and , print the lexicographically smallest absolute permutation . If no absolute permutation exists, print -1.

Example


Create an array of elements from  to , . Using  based indexing, create a permutation where every . It can be rearranged to  so that all of the absolute differences equal :

pos[i]  i   |pos[i] - i|
  3     1        2
  4     2        2
  1     3        2
  2     4        2
Function Description

Complete the absolutePermutation function in the editor below.

absolutePermutation has the following parameter(s):

int n: the upper bound of natural numbers to consider, inclusive
int k: the absolute difference between each element's value and its index
Returns

int[n]: the lexicographically smallest permutation, or  if there is none
Input Format

The first line contains an integer , the number of queries.
Each of the next  lines contains  space-separated integers,  and .

Constraints

Sample Input

STDIN   Function
-----   --------
3       t = 3 (number of queries)
2 1     n = 2, k = 1
3 0     n = 3, k = 0
3 2     n = 3, k = 2
Sample Output

2 1
1 2 3
-1
Explanation

Test Case 0:

perm.png

Test Case 1:

perm(1).png

Test Case 2:
No absolute permutation exists, so we print -1 on a new line.
'''


#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'absolutePermutation' function below.
#
# The function is expected to return an INTEGER_ARRAY.
# The function accepts following parameters:
#  1. INTEGER n
#  2. INTEGER k
#

def absolutePermutation(n, k):
    # Write your code here
    if k == 0:
        # If k is 0, the permutation is the natural numbers from 1 to n.
        return list(range(1, n + 1))

    if n % (2 * k) != 0:
        # No absolute permutation is possible.
        return [-1]

    perm = [0] * n
    for i in range(n):
        if (i // k) % 2 == 0:
            perm[i] = i + k + 1
        else:
            perm[i] = i - k + 1

    return perm

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    t = int(input().strip())

    for t_itr in range(t):
        first_multiple_input = input().rstrip().split()

        n = int(first_multiple_input[0])

        k = int(first_multiple_input[1])

        result = absolutePermutation(n, k)

        fptr.write(' '.join(map(str, result)))
        fptr.write('\n')

    fptr.close()
