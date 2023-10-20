'''
Lauren has a chart of distinct projected prices for a house over the next several years. She must buy the house in one year and sell it in another, and she must do so at a loss. She wants to minimize her financial loss.

Example

Her minimum loss is incurred by purchasing in year  at  and reselling in year  at . Return .

Function Description

Complete the minimumLoss function in the editor below.

minimumLoss has the following parameter(s):

int price[n]: home prices at each year
Returns

int: the minimum loss possible
Input Format

The first line contains an integer , the number of years of house data.
The second line contains  space-separated long integers that describe each .

Constraints

All the prices are distinct.
A valid answer exists.
Subtasks

 for  of the maximum score.
Sample Input 0

3
5 10 3
Sample Output 0

2
Explanation 0

Lauren buys the house in year  at  and sells it in year  at  for a minimal loss of .

Sample Input 1

5
20 7 8 2 5
Sample Output 1

2
Explanation 1

Lauren buys the house in year  at  and sells it in year  at  for a minimal loss of .
'''

#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'minimumLoss' function below.
#
# The function is expected to return an INTEGER.
# The function accepts LONG_INTEGER_ARRAY price as parameter.
#

def minimumLoss(price):
    # Write your code here
    dictionary = {price[i]: i for i in range(len(price))}
    price = sorted(price)

    minimum = 10000000

    for i in range(1, len(price)):
        if dictionary[price[i]] < dictionary[price[i - 1]]:
            minimum = min(minimum, price[i] - price[i - 1])

    return minimum

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    price = list(map(int, input().rstrip().split()))

    result = minimumLoss(price)

    fptr.write(str(result) + '\n')

    fptr.close()
