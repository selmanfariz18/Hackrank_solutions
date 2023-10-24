'''
Alice was given the  integers from  to . She wrote all possible permutations in increasing lexicographical order, and wrote each permutation in a new line. For example, for , there are  possible permutations:

She then chose one permutation among them as her favorite permutation.

After some time, she forgot some elements of her favorite permutation. Nevertheless, she still tried to write down its elements. She wrote a  in every position where she forgot the true value.

She wants to know the sum of the line numbers of the permutations which could possibly be her favorite permutation, i.e., permutations which can be obtained by replacing the s. Can you help her out?

Since the sum can be large, find it modulo .

Input Format

The first line contains a single integer .

The next line contains  space-separated integers  denoting Alice's favorite permutation with some positions replaced by .

Constraints

The positive values appearing in  are distinct.
Subtask

For ~33% of the total points,
Output Format

Print a single line containing a single integer denoting the sum of the line numbers of the permutations which could possibly be Alice's favorite permutation.

Sample Input 0

4
0 2 3 0
Sample Output 0

23
Explanation 0

The possible permutations are  and . The permutation  occurs on line  and the permutation  occurs on line . Therefore the sum is .

Sample Input 1

4
4 3 2 1
Sample Output 1

24
Explanation 1

There is no missing number in the permutation. Therefore, the only possible permutation is , and it occurs on line . Therefore the sum is .
'''


#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'solve' function below.
#
# The function is expected to return a LONG_INTEGER.
# The function accepts INTEGER_ARRAY x as parameter.
#

class fenwick:
    def __init__(self, n):
        self.tree = [0] * (n + 1)

    def update(self, i):
        i += 1
        while i < len(self.tree):
            self.tree[i] += 1
            i += i & (-i)

    def query(self, i):
        # i is 0 based index
        sum = 0
        i += 1
        while i > 0:
            sum += self.tree[i]
            i -= i & (-i)
        return sum


def solve(x):
    # Write your code here
    n = len(x)
    mod = 1000000007
    missing = [True] * n
    bit1 = fenwick(n)
    bit2 = fenwick(n)

    for i in range(n):
        x[i] -= 1
        if x[i] != -1:
            missing[x[i]] = False

    missisng_elems = []

    for i in range(n):
        if missing[i]:
            missisng_elems.append(i)

    missing_sum = 0
    m = len(missisng_elems)

    for i in missisng_elems:
        missing_sum += i
        if i < n - 1:
            bit2.update(i + 1)

    fact = [1] * 500010

    for i in range(1, 500010):
        fact[i] = i * fact[i - 1] % mod

    total_cost = 0
    p = 0
    y = 0

    for i in range(n - 1):
        if x[i] != -1:
            if m == 0:
                D1 = bit1.query(x[i])
                bit1.update(x[i] + 1)
                cost = (x[i] - D1) * fact[n - i - 1]
            else:
                D1 = bit1.query(x[i]) * m
                no_of_smaller_missing_elems = bit2.query(x[i])
                D2 = no_of_smaller_missing_elems * p
                # print('D1:{} D2:{}'.format(D1, D2))
                bit1.update(x[i] + 1)
                cost = (x[i] * m - (D1 + D2)) * fact[m - 1] * fact[n - i - 1]
                y += m - no_of_smaller_missing_elems
        else:
            if p == 0:
                cost = (missing_sum - y) * fact[m - 1] * fact[n - i - 1]
            else:
                D1 = p * m * (m - 1) // 2
                D2 = y * (m - 1)
                cost = (missing_sum * (m - 1) - (D1 + D2)) * fact[m - 2] * fact[n - i - 1]
            p += 1

        total_cost += cost % mod

    return (total_cost + fact[m]) % mod


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    a = list(map(int, input().rstrip().split()))

    result = solve(a)

    fptr.write(str(result) + '\n')

    fptr.close()
