'''
Madam Hannah Otto, the CEO of Reviver Corp., is fond of palindromes, or words that read the same forwards or backwards. She thinks palindromic brand names are appealing to millennials.

As part of the marketing campaign for the company's new juicer called the Rotator™, Hannah decided to push the marketing team's palindrome-searching skills to a new level with a new challenge.

In this challenge, Hannah provides a string  consisting of lowercase English letters. Every day, for  days, she would select two integers  and , take the substring  (the substring of  from index  to index ), and ask the following question:

Consider all the palindromes that can be constructed from some of the letters from . You can reorder the letters as you need. Some of these palindromes have the maximum length among all these palindromes. How many maximum-length palindromes are there?

For example, if ,  and , then we have,

image

Your job as the head of the marketing team is to answer all the queries. Since the answers can be very large, you are only required to find the answer modulo .

Complete the functions initialize and answerQuery and return the number of maximum-length palindromes modulo .

Input Format

The first line contains the string .

The second line contains a single integer .

The  of the next  lines contains two space-separated integers ,  denoting the  and  values Anna selected on the  day.

Constraints

Here,  denotes the length of .

Subtasks

For 30% of the total score:

For 60% of the total score:

Output Format

For each query, print a single line containing a single integer denoting the answer.

Sample Input 0

week
2
1 4
2 3
Sample Output 0

2
1
Explanation 0

On the first day,  and . The maximum-length palindromes are "ewe" and "eke".

On the second day,  and . The maximum-length palindrome is "ee".

image

Sample Input 1

abab
1
1 4
Sample Output 1

2
Explanation 1

Here, the maximum-length palindromes are "abba" and "baab".
'''

import math
import os
import random
import re
import sys
from collections import defaultdict
from copy import copy

#
# Complete the 'initialize' function below.
#
# The function accepts STRING s as parameter.
#
factorial = [1]
mod = 10 ** 9 + 7
c_count = [defaultdict(int)]


def initialize(s):
    # This function is called once before all queries.
    global factorial
    for i in range(1, int(1e5) + 10):
        factorial.append((factorial[i - 1] * i) % mod)

    global c_count
    for c in s:
        next_c = copy(c_count[-1])
        next_c[c] += 1
        c_count.append(next_c)


#
# Complete the 'answerQuery' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER l
#  2. INTEGER r
#

def egcd(a, b):
    if a == 0:
        return b, 0, 1
    else:
        g, y, x = egcd(b % a, a)
        return g, x - (b // a) * y, y


memo = {}


def mod_inverse(a, m):
    if a in memo:
        return memo[a]
    while a < 0:
        a += m
    g, x, y = egcd(a, m)
    if g != 1:
        raise Exception('Modular inverse does not exist')
    else:
        memo[a] = x % m
        return x % m


def answerQuery(l, r):
    # Return the answer for this query modulo 1000000007.
    d = defaultdict(int)
    for ch in c_count[r]:
        d[ch] += c_count[r][ch]
    for ch in c_count[l - 1]:
        d[ch] -= c_count[l - 1][ch]

    odd_count = 0
    for k, v in copy(d).items():
        if v & 1:
            odd_count += 1
        d[k] = v - (v & 1)

    res = 1
    total = 0
    for k, v in d.items():
        res *= mod_inverse(factorial[v // 2], mod)
        total += v // 2
        res %= mod
    return (max(1, odd_count) * res * factorial[total]) % mod


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    initialize(s)

    q = int(input().strip())

    for q_itr in range(q):
        first_multiple_input = input().rstrip().split()

        l = int(first_multiple_input[0])

        r = int(first_multiple_input[1])

        result = answerQuery(l, r)

        fptr.write(str(result) + '\n')

    fptr.close()
