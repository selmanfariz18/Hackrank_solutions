'''Given an array of bird sightings where every element represents a bird type id, determine the id of the most frequently sighted type. If more than 1 type has been spotted that maximum amount, return the smallest of their ids.

Example

There are two each of types  and , and one sighting of type . Pick the lower of the two types seen twice: type .

Function Description

Complete the migratoryBirds function in the editor below.

migratoryBirds has the following parameter(s):

int arr[n]: the types of birds sighted
Returns

int: the lowest type id of the most frequently sighted birds
Input Format

The first line contains an integer, , the size of .
The second line describes  as  space-separated integers, each a type number of the bird sighted.

Constraints

It is guaranteed that each type is , , , , or .
Sample Input 0

6
1 4 4 4 5 3
Sample Output 0

4
Explanation 0

The different types of birds occur in the following frequencies:

Type :  bird
Type :  birds
Type :  bird
Type :  birds
Type :  bird
The type number that occurs at the highest frequency is type , so we print  as our answer.

Sample Input 1

11
1 2 3 4 5 4 3 2 1 3 4
Sample Output 1

3
Explanation 1

The different types of birds occur in the following frequencies:

Type :
Type :
Type :
Type :
Type :
Two types have a frequency of , and the lower of those is type .'''


#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'migratoryBirds' function below.
#
# The function is expected to return an INTEGER.
# The function accepts INTEGER_ARRAY arr as parameter.
#

def migratoryBirds(arr):
    # Write your code here
    bird_freq = {}
    for bird_type in arr:
        if bird_type in bird_freq:
            bird_freq[bird_type] += 1
        else:
            bird_freq[bird_type] = 1

    # Find the maximum frequency.
    max_freq = 0
    for bird_type, freq in bird_freq.items():
        if freq > max_freq:
            max_freq = freq

    # Get the list of bird types with the maximum frequency.
    max_freq_bird_types = []
    for bird_type, freq in bird_freq.items():
        if freq == max_freq:
            max_freq_bird_types.append(bird_type)

    # Return the smallest ID of the bird types with the maximum frequency.
    return min(max_freq_bird_types)

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    arr_count = int(input().strip())

    arr = list(map(int, input().rstrip().split()))

    result = migratoryBirds(arr)

    fptr.write(str(result) + '\n')

    fptr.close()
