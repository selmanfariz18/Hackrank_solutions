'''
Little Bobby loves chocolate. He frequently goes to his favorite  store, Penny Auntie, to buy them. They are having a promotion at Penny Auntie. If Bobby saves enough wrappers, he can turn them in for a free chocolate.

Example



He has  to spend, bars cost , and he can turn in  wrappers to receive another bar. Initially, he buys  bars and has  wrappers after eating them. He turns in  of them, leaving him with , for  more bars. After eating those two, he has  wrappers, turns in  leaving him with  wrapper and his new bar. Once he eats that one, he has  wrappers and turns them in for another bar. After eating that one, he only has  wrapper, and his feast ends. Overall, he has eaten  bars.

Function Description

Complete the chocolateFeast function in the editor below.

chocolateFeast has the following parameter(s):

int n: Bobby's initial amount of money
int c: the cost of a chocolate bar
int m: the number of wrappers he can turn in for a free bar
Returns

int: the number of chocolates Bobby can eat after taking full advantage of the promotion
Note: Little Bobby will always turn in his wrappers if he has enough to get a free chocolate.

Input Format

The first line contains an integer, , the number of test cases to analyze.
Each of the next  lines contains three space-separated integers: , , and . They represent money to spend, cost of a chocolate, and the number of wrappers he can turn in for a free chocolate.

Constraints

Sample Input

STDIN   Function
-----   --------
3       t = 3 (test cases)
10 2 5  n = 10, c = 2, m = 5 (first test case)
12 4 4  n = 12, c = 4, m = 4 (second test case)
6 2 2   n = 6,  c = 2, m = 2 (third test case)
Sample Output

6
3
5
Explanation

Bobby makes the following  trips to the store:

He spends  on  chocolates at  apiece. He then eats them and exchanges all  wrappers to get  more. He eats  chocolates.
He spends his  on  chocolates at  apiece. He has  wrappers, but needs  to trade for his next chocolate. He eats  chocolates.
He spends  on  chocolates at  apiece. He then exchanges  of the  wrappers for  additional piece. Next, he uses his third leftover chocolate wrapper from his initial purchase with the wrapper from his trade-in to do a second trade-in for  more piece. At this point he has  wrapper left, which is not enough to perform another trade-in. He eats  chocolates.
'''

#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'chocolateFeast' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER n
#  2. INTEGER c
#  3. INTEGER m
#

def chocolateFeast(n, c, m):
    # Write your code here
    # Calculate the initial number of chocolates Bobby can buy
    chocolates_bought = n // c
    wrappers = chocolates_bought

    total_chocolates = chocolates_bought

    # While Bobby has enough wrappers to trade for more chocolates
    while wrappers >= m:
        # Calculate the additional chocolates Bobby can get from trading wrappers
        additional_chocolates = wrappers // m
        total_chocolates += additional_chocolates

        # Calculate the remaining wrappers after the trade
        remaining_wrappers = wrappers % m

        # Bobby has eaten the additional chocolates and has new wrappers
        wrappers = additional_chocolates + remaining_wrappers

    return total_chocolates


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    t = int(input().strip())

    for t_itr in range(t):
        first_multiple_input = input().rstrip().split()

        n = int(first_multiple_input[0])

        c = int(first_multiple_input[1])

        m = int(first_multiple_input[2])

        result = chocolateFeast(n, c, m)

        fptr.write(str(result) + '\n')

    fptr.close()
