'''
Sherlock considers a string to be valid if all characters of the string appear the same number of times. It is also valid if he can remove just  character at  index in the string, and the remaining characters will occur the same number of times. Given a string , determine if it is valid. If so, return YES, otherwise return NO.

Example

This is a valid string because frequencies are .


This is a valid string because we can remove one  and have  of each character in the remaining string.


This string is not valid as we can only remove  occurrence of . That leaves character frequencies of .

Function Description

Complete the isValid function in the editor below.

isValid has the following parameter(s):

string s: a string
Returns

string: either YES or NO
Input Format

A single string .

Constraints

Each character
Sample Input 0

aabbcd
Sample Output 0

NO
Explanation 0

Given , we would need to remove two characters, both c and d  aabb or a and b  abcd, to make it valid. We are limited to removing only one character, so  is invalid.

Sample Input 1

aabbccddeefghi
Sample Output 1

NO
Explanation 1

Frequency counts for the letters are as follows:

{'a': 2, 'b': 2, 'c': 2, 'd': 2, 'e': 2, 'f': 1, 'g': 1, 'h': 1, 'i': 1}

There are two ways to make the valid string:

Remove  characters with a frequency of : .
Remove  characters of frequency : .
Neither of these is an option.

Sample Input 2

abcdefghhgfedecba
Sample Output 2

YES
Explanation 2

All characters occur twice except for  which occurs  times. We can delete one instance of  to have a valid string.
'''


#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'isValid' function below.
#
# The function is expected to return a STRING.
# The function accepts STRING s as parameter.
#

def isValid(s):
    # Write your code here
    # Step 1: Count character frequencies
    char_count = {}
    frequency_count = {}

    for char in s:
        if char in char_count:
            char_count[char] += 1
        else:
            char_count[char] = 1

        # Update freq_count
        count = char_count[char]
        if count in frequency_count:
            frequency_count[count] += 1
        else:
            frequency_count[count] = 1


    # Step 3: Check if it's possible to make the string valid
    if len(frequency_count) == 1:
        # All characters have the same frequency
        return "YES"
    elif len(frequency_count) == 2:
        # Check if one of the conditions is met
        frequency_list = list(frequency_count.keys())
        frequency1, frequency2 = frequency_list[0], frequency_list[1]
        count1, count2 = frequency_count[frequency1], frequency_count[frequency2]

        if (count1 == 1 and (frequency1 - 1 == frequency2 or frequency1 == 1)) or (count2 == 1 and (frequency2 - 1 == frequency1 or frequency2 == 1)):
            return "YES"

    return "NO"

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    result = isValid(s)

    fptr.write(result + '\n')

    fptr.close()
