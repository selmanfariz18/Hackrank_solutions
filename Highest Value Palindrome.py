'''
Palindromes are strings that read the same from the left or right, for example madam or 0110.

You will be given a string representation of a number and a maximum number of changes you can make. Alter the string, one digit at a time, to create the string representation of the largest number possible given the limit to the number of changes. The length of the string may not be altered, so you must consider 's left of all higher digits in your tests. For example  is valid,  is not.

Given a string representing the starting number, and a maximum number of changes allowed, create the largest palindromic string of digits possible or the string '-1' if it is not possible to create a palindrome under the contstraints.

Example


Make  replacements to get .



Make  replacement to get .

Function Description

Complete the highestValuePalindrome function in the editor below.

highestValuePalindrome has the following parameter(s):

string s: a string representation of an integer
int n: the length of the integer string
int k: the maximum number of changes allowed
Returns

string: a string representation of the highest value achievable or -1
Input Format

The first line contains two space-separated integers,  and , the number of digits in the number and the maximum number of changes allowed.
The second line contains an -digit string of numbers.

Constraints

Each character  in the number is an integer where .
Output Format

Sample Input 0

STDIN   Function
-----   --------
4 1     n = 4, k = 1
3943    s = '3943'
Sample Output 0

3993
Sample Input 1

6 3
092282
Sample Output 1

992299
Sample Input 2

4 1
0011
Sample Output 2

-1
Explanation

Sample 0

There are two ways to make  a palindrome by changing no more than  digits:



'''

#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'highestValuePalindrome' function below.
#
# The function is expected to return a STRING.
# The function accepts following parameters:
#  1. STRING s
#  2. INTEGER n
#  3. INTEGER k
#

def highestValuePalindrome(s, n, k):
    # Write your code here
    strr = list(s)
    palindrome = list(s)

    l = 0
    r = n - 1

    while l <= r:
        if strr[l] != strr[r]:
            palindrome[l] = palindrome[r] = max(strr[l], strr[r])
            k -= 1
        l += 1
        r -= 1

    if k < 0:
        return "-1"

    l = 0
    r = n - 1

    while l <= r:
        if l == r:
            if k > 0:
                palindrome[l] = "9"

        if palindrome[l] < "9":
            if k >= 2 and palindrome[l] == strr[l] and palindrome[r] == strr[r]:
                k -= 2
                palindrome[l] = palindrome[r] = "9"

            elif k >= 1 and (palindrome[l] != strr[l] or palindrome[r] != strr[r]):
                k -= 1
                palindrome[l] = palindrome[r] = "9"

        l += 1
        r -= 1

    return "".join(palindrome)

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    first_multiple_input = input().rstrip().split()

    n = int(first_multiple_input[0])

    k = int(first_multiple_input[1])

    s = input()

    result = highestValuePalindrome(s, n, k)

    fptr.write(result + '\n')

    fptr.close()
