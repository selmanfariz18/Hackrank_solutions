'''
A gene is represented as a string of length  (where  is divisible by ), composed of the letters , , , and . It is considered to be steady if each of the four letters occurs exactly  times. For example,  and  are both steady genes.

Bear Limak is a famous biotechnology scientist who specializes in modifying bear DNA to make it steady. Right now, he is examining a gene represented as a string . It is not necessarily steady. Fortunately, Limak can choose one (maybe empty) substring of  and replace it with any string of the same length.

Modifying a large substring of bear genes can be dangerous. Given a string , can you help Limak find the length of the smallest possible substring that he can replace to make  a steady gene?

Note: A substring of a string  is a subsequence made up of zero or more contiguous characters of .

As an example, consider . The substring  just before or after  can be replaced with  or . One selection would create .

Function Description

Complete the  function in the editor below. It should return an integer that represents the length of the smallest substring to replace.

steadyGene has the following parameter:

gene: a string
Input Format

The first line contains an interger  divisible by , that denotes the length of a string .
The second line contains a string  of length .

Constraints

 is divisible by
Subtask

 in tests worth  points.
Output Format

Print the length of the minimum length substring that can be replaced to make  stable.

Sample Input

8
GAAATAAA
Sample Output

5
Explanation

One optimal solution is to replace  with  resulting in .
The replaced substring has length .
'''

#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'steadyGene' function below.
#
# The function is expected to return an INTEGER.
# The function accepts STRING gene as parameter.
#

def steadyGene(gene):
    # Write your code here
    min_length_string = len(gene)

    occurences = dict()
    occurences["A"] = 0
    occurences["C"] = 0
    occurences["G"] = 0
    occurences["T"] = 0

    expected = len(gene) // 4

    for g in gene:
        occurences[g] += 1

    for x in occurences:
        occurences[x] = max(0, occurences[x] - expected)

    if occurences['A'] == 0 and occurences['G'] == 0 and occurences['C'] == 0 and occurences['T'] == 0:
        return 0

    found = dict()
    found["A"] = 0
    found["C"] = 0
    found["G"] = 0
    found["T"] = 0

    tail = 0
    head = 0

    while head != len(gene):
        found[gene[head]] += 1
        if found["A"] >= occurences["A"] and \
                found["C"] >= occurences["C"] and \
                found["G"] >= occurences["G"] and \
                found["T"] >= occurences["T"]:
            min_length_string = min(min_length_string, head - tail + 1)

            while found[gene[tail]] > occurences[gene[tail]]:
                found[gene[tail]] -= 1
                tail += 1
                min_length_string = min(min_length_string, head - tail + 1)
        head += 1

    return min_length_string

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    gene = input()

    result = steadyGene(gene)

    fptr.write(str(result) + '\n')

    fptr.close()
