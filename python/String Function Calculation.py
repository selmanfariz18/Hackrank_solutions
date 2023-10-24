'''
Jane loves strings more than anything. She has a string  with her, and value of string  over function  can be calculated as given below:

Jane wants to know the maximum value of  among all the substrings  of string . Can you help her?

Input Format
A single line containing string  .

Output Format
Print the maximum value of  among all the substrings  of string .

Constraints

The string consists of lowercase English alphabets.

Sample Input 0

aaaaaa
Sample Output 0

12
Explanation 0

f('a') = 6
f('aa') = 10
f('aaa') = 12
f('aaaa') = 12
f('aaaaa') = 10
f('aaaaaa') = 6
Sample Input 1

abcabcddd
Sample Output 1

9
Explanation 1

f values of few of the substrings are shown below:

f("a") = 2
f("b") = 2
f("c") = 2
f("ab") = 4
f("bc") = 4
f("ddd") = 3
f("abc") = 6
f("abcabcddd") = 9
Among the function values 9 is the maximum one.
'''

#!/bin/python3

import os
import re
from itertools import islice, zip_longest

#
# Complete the 'maxValue' function below.
#
# The function is expected to return an INTEGER.
# The function accepts STRING t as a parameter.
#

def toIntKeysBest(l):
    seen = set()
    ls = []
    for e in l:
        if e not in seen:
            ls.append(e)
            seen.add(e)
    ls.sort()
    index = {v: i for i, v in enumerate(ls)}
    return [index[v] for v in l]


def inverseArray(l):
    n = len(l)
    ans = [0] * n
    for i in range(n):
        ans[l[i]] = i
    return ans


def suffixArrayBest(s):
    n = len(s)
    k = 1
    line = toIntKeysBest(s)
    while max(line) < n - 1:
        line = toIntKeysBest([a * (n + 1) + b + 1
                              for (a, b) in
                              zip_longest(line, islice(line, k, None), fillvalue=-1)])
        k <<= 1
    return line


def suffixMatrixBest(t):
    n = len(t)
    k = 1
    line = toIntKeysBest(t)
    ans = [line]
    while max(line) < n - 1:
        line = toIntKeysBest([a * (n + 1) + b + 1
                              for (a, b) in
                              zip_longest(line, islice(line, k, None), fillvalue=-1)])
        ans.append(line)
        k <<= 1
    return ans


def lcp(sm, i, j):
    n = len(sm[-1])
    if i == j:
        return n - i
    k = 1 << (len(sm) - 2)
    ans = 0
    for line in sm[-2::-1]:
        if i >= n or j >= n:
            break
        if line[i] == line[j]:
            ans += k
            i += k
            j += k
        k >>= 1
    return ans


def maxValue(t):
    res = inverseArray(suffixArrayBest(t))
    mtx = suffixMatrixBest(t)

    lcp_res = []
    for n in range(len(res) - 1):
        lcp_res.append(lcp(mtx, res[n], res[n + 1]))
    lcp_res.append(0)

    max_score = len(t)

    lcp_res_len = len(lcp_res)

    for i, num in enumerate(res):
        if lcp_res[i] <= 1:
            continue
        lcp_res_i = lcp_res[i]

        cnt = 2
        for j in range(i + 1, lcp_res_len):
            if lcp_res[j] >= lcp_res_i:
                cnt += 1
            else:
                break
        for j in range(i - 1, -1, -1):
            if lcp_res[j] >= lcp_res_i:
                cnt += 1
            else:
                break

        max_score = max(cnt * lcp_res_i, max_score)

    return max_score

if __name__ == '__main__':
    t = input()
    result = maxValue(t)
    print(result)
