'''
A border of a string is a proper prefix of it that is also a suffix. For example:

a and abra are borders of abracadabra,
kan and kankan are borders of kankankan.
de is a border of decode.
Note that decode is not a border of decode because it's not proper.

A palindromic border is a border that is palindromic. For example,

a and ana are palindromic borders of anabanana,
l, lol and lolol are palindromic borders of lololol.
Let's define  as the number of palindromic borders of string . For example, if  lololol, then .

Now, a string of length  has exactly  non-empty substrings (we count substrings as distinct if they are of different lengths or are in different positions, even if they are the same string). Given a string , consisting only of the first 8 lowercase letters of the English alphabet, your task is to find the sum of  for all the non-empty substrings  of . In other words, you need to find:

where  is the substring of  starting at position  and ending at position .
Since the answer can be very large, output the answer modulo .

Input Format

The first line contains a string consisting of  characters.

Output Format

Print a single integer: the remainder of the division of the resulting number by .

Constraints


All characters in the string can be any of the first 8 lowercase letters of the English alphabet (abcdefgh).

Sample Input 1

ababa
Sample Output 1

5
Sample Input 2

aaaa
Sample Output 2

10
Sample Input 3

abcacb
Sample Output 3

3
Explanation

 ababa has 15 substrings but only 4 substrings have palindromic borders.

 aba
 ababa
 bab
 aba
'''

#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'palindromicBorder' function below.
#
# The function is expected to return an INTEGER.
# The function accepts STRING s as parameter.
#

def monoString(s):
    cc = s[0]
    for c in s:
        if c != cc:
            return False
    return True


def monoStringResult(s):
    output = 0
    for i in range(2, len(s) + 1):
        output += i * (i - 1) // 2
        output %= 1000000007
    return output


def calculatePalindromeBorders(palindrome_dict):
    output = 0
    for palindrome, times in palindrome_dict.items():
        output += times * (times - 1) // 2
    return output


def palindromicBorder(s):
    # Write your code here
    if monoString(s):
        return monoStringResult(s)
    output = 0

    odd = [[], {}, 1]
    for c in s:
        if c not in odd[1]:
            odd[1][c] = 0
        odd[1][c] += 1
    for i in range(len(s)):
        odd[0].append(i)
    output += calculatePalindromeBorders(odd[1])

    even = [[], {}, 1]
    for i in range(len(s) - 1):
        if s[i] == s[i + 1]:
            even[0].append(i)
            ss = s[i:i + 2]
            if ss not in even[1]:
                even[1][ss] = 0
            even[1][ss] += 1
    output += calculatePalindromeBorders(even[1])

    for l in range(3, len(s)):
        if l % 2 == 0:
            working_tuple = even
        else:
            working_tuple = odd

        new_tuple = [[], {}, 1]
        for index in working_tuple[0]:
            if index - 1 >= 0 and index + l - 2 < len(s) and s[index - 1] == s[index + l - 2]:
                new_tuple[0].append(index - 1)
                ss = s[index - 1:index - 1 + l]
                if ss not in new_tuple[1]:
                    new_tuple[1][ss] = 0
                new_tuple[1][ss] += 1

        output += calculatePalindromeBorders(new_tuple[1])
        output %= 1000000007
        if l % 2 == 0:
            even = new_tuple
        else:
            odd = new_tuple
    return output

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    result = palindromicBorder(s)

    fptr.write(str(result) + '\n')

    fptr.close()
