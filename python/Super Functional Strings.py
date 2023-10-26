'''
We define a function, , on a string, , as follows:

where:

 denotes the number of characters in string .
 denotes the number of distinct characters in string .
Consuela loves creating string challenges and she needs your help testing her newest one! Given a string, , consisting of  lowercase letters, compute the summation of function  (provided above) over all possible distinct substrings of . As the result is quite large, print it modulo .

Input Format

The first line contains a single integer, , denoting the number of test cases.
Each of the  subsequent lines contains a string, .

Constraints

The sum of  over all test cases does not exceed .
Scoring

 for  of test data.
 for  of test data.
 for  of test data.
Output Format

For each test case, print the answer modulo .

Sample Input

3
aa
aba
abc
Sample Output

3
19
38
Explanation

Test 0:

 and  are the only distinct substrings.


Test 1:

, , , , and  are the only distinct substrings.



'''

#!/bin/python3

#
# Complete the 'superFunctionalStrings' function below.
#
# The function is expected to return an INTEGER.
# The function accepts STRING s as parameter.
#

import os
from bisect import bisect_left, bisect_right
from itertools import zip_longest, islice

MODULUS = 7 + 10 ** 9

STRING_LENGTH = 10 ** 5

SUM_POWERS = [[0] * (STRING_LENGTH + 1) for k in range(27)]
for k in range(1, 27):
    for n in range(1, STRING_LENGTH + 1):
        SUM_POWERS[k][n] = (SUM_POWERS[k][n - 1] + pow(n, k, MODULUS)) % MODULUS


def get_sum_powers(left, right, k):
    if left > right or right <= 0:
        return 0
    if left <= 0:
        return (SUM_POWERS[k][right] + MODULUS - SUM_POWERS[k][left - 1]) % MODULUS
    return (SUM_POWERS[k][right] + MODULUS - SUM_POWERS[k][left - 1]) % MODULUS


def get_occurrences(s):
    n = len(s)
    occurrences = [[] for _ in range(26)]
    for i in range(n):
        occurrences[ord(s[i]) - ord('a')].append(i)
    return occurrences


def occurrences_from_i(occurrences, i):
    occurrences_i = []
    for j in range(26):
        if len(occurrences[j]) == 0 or i > occurrences[j][-1]:
            continue
        first = bisect_left(occurrences[j], i)
        occurrences_i.append(occurrences[j][first])
    return sorted(occurrences_i)


def get_sorted_indices(items):
    unique_items = sorted(set(items))
    index_map = dict(zip(unique_items, range(len(unique_items))))
    return [index_map[v] for v in items]


def build_suffix_array(s):
    n = len(s)
    k = 1
    suffix_array = get_sorted_indices(s)
    while max(suffix_array) < n - 1:
        suffix_array = get_sorted_indices([a * (n + 1) + b + 1 for
                                           (a, b) in zip_longest(suffix_array,
                                                               islice(suffix_array, k, None),
                                                               fillvalue=-1)])
        k <<= 1
    return suffix_array


def longest_common_prefix(suffix_array, s):
    inverted_suffix_array = build_suffix_array(s)
    n = len(inverted_suffix_array)
    suffix_array = [0] * n
    for i in range(n):
        suffix_array[inverted_suffix_array[i]] = i
    lcp = [0] * n
    k = 0
    for i in range(n):
        if inverted_suffix_array[i] == n - 1:
            k = 0
            continue
        j = suffix_array[inverted_suffix_array[i] + 1]
        while i + k < n and j + k < n and s[i + k] == s[j + k]:
            k += 1
        lcp[inverted_suffix_array[i] + 1] = k
        if k > 0:
            k -= 1
    return suffix_array, lcp


def solve_string(s):
    n = len(s)
    occurrences = get_occurrences(s)
    suffix_arr, lcp_array = longest_common_prefix(s, s)
    result = 0

    for i in range(n):
        occ_from_i = occurrences_from_i(occurrences, suffix_arr[i])
        t = suffix_arr[i] + lcp_array[i]
        if t >= occ_from_i[-1]:
            result = (result + get_sum_powers(lcp_array[i] + 1, n - suffix_arr[i], len(occ_from_i))) % MODULUS
            continue
        k = bisect_right(occ_from_i, t)
        result = (result + get_sum_powers(lcp_array[i] + 1, occ_from_i[k] - suffix_arr[i], k)) % MODULUS
        for j in range(k + 1, len(occ_from_i)):
            result = (result + get_sum_powers(occ_from_i[j - 1] - suffix_arr[i] + 1, occ_from_i[j] - suffix_arr[i], j)) % MODULUS
        result = (result + get_sum_powers(occ_from_i[-1] - suffix_arr[i] + 1, n - suffix_arr[i], len(occ_from_i))) % MODULUS

    return result


def calculate_super_functional_strings(t):
    results = []
    for _ in range(t):
        s = input()
        result = solve_string(s)
        results.append(result)
    return results


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')
    test_cases = int(input().strip())
    results = calculate_super_functional_strings(test_cases)
    for result in results:
        fptr.write(str(result) + '\n')
    fptr.close()

