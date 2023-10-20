'''
James found a love letter that his friend Harry has written to his girlfriend. James is a prankster, so he decides to meddle with the letter. He changes all the words in the letter into palindromes.

To do this, he follows two rules:

He can only reduce the value of a letter by , i.e. he can change d to c, but he cannot change c to d or d to b.
The letter  may not be reduced any further.
Each reduction in the value of any letter is counted as a single operation. Find the minimum number of operations required to convert a given string into a palindrome.

Example

The following two operations are performed: cde → cdd → cdc. Return .

Function Description

Complete the theLoveLetterMystery function in the editor below.

theLoveLetterMystery has the following parameter(s):

string s: the text of the letter
Returns

int: the minimum number of operations
Input Format

The first line contains an integer , the number of queries.
The next  lines will each contain a string .

Constraints


 | s |
All strings are composed of lower case English letters, ascii[a-z], with no spaces.

Sample Input

STDIN   Function
-----   --------
4       q = 4
abc     query 1 = 'abc'
abcba
abcd
cba
Sample Output

2
0
4
2
Explanation

For the first query, abc → abb → aba.
For the second query, abcba is already a palindromic string.
For the third query, abcd → abcc → abcb → abca → abba.
For the fourth query, cba → bba → aba.
'''

#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'theLoveLetterMystery' function below.
#
# The function is expected to return an INTEGER.
# The function accepts STRING s as parameter.
#

def theLoveLetterMystery(s):
    # Write your code here
    string = list(s)
    res = 0
    first = []
    second = []

    if len(string) % 2 == 1:
        first = list(map(lambda x: ord(x), string[: len(string) // 2]))
        first = first[::-1]
        second = list(map(lambda x: ord(x), string[len(string) // 2 + 1:]))
    else:
        first = list(map( lambda x: ord(x), string[: len(string) // 2 - 1]))
        first = first[::-1]
        second = list(map(lambda x: ord(x), string[len(string) // 2 + 1:]))
        res = abs(ord(string[len(string) // 2 - 1]) - ord(string[len(string) // 2]))

    for i in range(len(first)):
        if first[i] != second[i]:
            res += abs(first[i] - second[i])
            first[i] = min(first[i], second[i])
            second[i] = first[i]

    return res


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    q = int(input().strip())

    for q_itr in range(q):
        s = input()

        result = theLoveLetterMystery(s)

        fptr.write(str(result) + '\n')

    fptr.close()
