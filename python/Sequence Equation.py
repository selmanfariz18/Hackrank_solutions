'''
Given a sequence of  integers,  where each element is distinct and satisfies . For each  where , that is  increments from  to , find any integer  such that  and keep a history of the values of  in a return array.

Example


Each value of  between  and , the length of the sequence, is analyzed as follows:

, so
, so
, so
, so
, so
The values for  are .

Function Description

Complete the permutationEquation function in the editor below.

permutationEquation has the following parameter(s):

int p[n]: an array of integers
Returns

int[n]: the values of  for all  in the arithmetic sequence  to
Input Format

The first line contains an integer , the number of elements in the sequence.
The second line contains  space-separated integers  where .

Constraints

, where .
Each element in the sequence is distinct.
Sample Input 0

3
2 3 1
Sample Output 0

2
3
1
Explanation 0

Given the values of , , and , we calculate and print the following values for each  from  to :

, so we print the value of  on a new line.
, so we print the value of  on a new line.
, so we print the value of  on a new line.
Sample Input 1

5
4 3 5 1 2
Sample Output 1

1
3
5
4
2
'''

#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'permutationEquation' function below.
#
# The function is expected to return an INTEGER_ARRAY.
# The function accepts INTEGER_ARRAY p as parameter.
#

def permutationEquation(p):
    # Write your code here
    n = len(p)
    # Create a dictionary to map elements to their indices
    element_to_index = {}
    for i in range(n):
        element_to_index[p[i]] = i + 1  # Adding 1 to make it 1-based index

    result = []
    for x in range(1, n + 1):
        # Find the index of x in the array p
        index_x = element_to_index[x]
        # Find the index of the element at index_x to get y
        index_y = element_to_index[index_x]
        result.append(index_y)

    return result

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    p = list(map(int, input().rstrip().split()))

    result = permutationEquation(p)

    fptr.write('\n'.join(map(str, result)))
    fptr.write('\n')

    fptr.close()
