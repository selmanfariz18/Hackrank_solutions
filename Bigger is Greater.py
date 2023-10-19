'''
Lexicographical order is often known as alphabetical order when dealing with strings. A string is greater than another string if it comes later in a lexicographically sorted list.

Given a word, create a new word by swapping some or all of its characters. This new word must meet two criteria:

It must be greater than the original word
It must be the smallest word that meets the first condition
Example

The next largest word is .

Complete the function biggerIsGreater below to create and return the new string meeting the criteria. If it is not possible, return no answer.

Function Description

Complete the biggerIsGreater function in the editor below.

biggerIsGreater has the following parameter(s):

string w: a word
Returns
- string: the smallest lexicographically higher string possible or no answer

Input Format

The first line of input contains , the number of test cases.
Each of the next  lines contains .

Constraints

 will contain only letters in the range ascii[a..z].
Sample Input 0

5
ab
bb
hefg
dhck
dkhc
Sample Output 0

ba
no answer
hegf
dhkc
hcdk
Explanation 0

Test case 1:
ba is the only string which can be made by rearranging ab. It is greater.
Test case 2:
It is not possible to rearrange bb and get a greater string.
Test case 3:
hegf is the next string greater than hefg.
Test case 4:
dhkc is the next string greater than dhck.
Test case 5:
hcdk is the next string greater than dkhc.
Sample Input 1

6
lmno
dcba
dcbb
abdc
abcd
fedcbabcd
Sample Output 1

lmon
no answer
no answer
acbd
abdc
fedcbabdc
'''

#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'biggerIsGreater' function below.
#
# The function is expected to return a STRING.
# The function accepts STRING w as parameter.
#

def biggerIsGreater(w):
    # Write your code here
    w = list(w)

    # Find the first character from the right that is not in ascending order
    i = len(w) - 2
    while i >= 0 and w[i] >= w[i + 1]:
        i -= 1

    # If no such character is found, it's not possible to rearrange the string
    if i == -1:
        return "no answer"

    # Find the smallest character to the right of 'i' that is greater than w[i]
    j = len(w) - 1
    while w[j] <= w[i]:
        j -= 1

    # Swap w[i] and w[j]
    w[i], w[j] = w[j], w[i]

    # Reverse the substring to the right of 'i' to get the smallest possible string
    w[i + 1:] = reversed(w[i + 1:])

    return ''.join(w)

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    T = int(input().strip())

    for T_itr in range(T):
        w = input()

        result = biggerIsGreater(w)

        fptr.write(result + '\n')

    fptr.close()
