'''
Flatland is a country with a number of cities, some of which have space stations. Cities are numbered consecutively and each has a road of  length connecting it to the next city. It is not a circular route, so the first city doesn't connect with the last city. Determine the maximum distance from any city to its nearest space station.

Example


There are  cities and city  has a space station. They occur consecutively along a route. City  is  unit away and city  is  units away. City  is  units from its nearest space station as one is located there. The maximum distance is .

Function Description

Complete the flatlandSpaceStations function in the editor below.

flatlandSpaceStations has the following parameter(s):

int n: the number of cities
int c[m]: the indices of cities with a space station
Returns
- int: the maximum distance any city is from a space station

Input Format

The first line consists of two space-separated integers,  and .
The second line contains  space-separated integers, the indices of each city that has a space-station. These values are unordered and distinct.

Constraints

There will be at least  city with a space station.
No city has more than one space station.
Output Format

Sample Input 0

STDIN   Function
-----   --------
5 2     n = 5, c[] size m = 2
0 4     c = [0, 4]
Sample Output 0

2
Explanation 0

This sample corresponds to following graphic:

hreasy(5).png

The distance to the nearest space station for each city is listed below:

 has distance , as it contains a space station.
 has distance  to the space station in .
 has distance  to the space stations in  and .
 has distance  to the space station in .
 has distance , as it contains a space station.
We then take .

Sample Input 1

6 6
0 1 2 4 3 5
Sample Output 1

0
Explanation 1

In this sample,  so every city has space station and we print  as our answer.
'''

#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the flatlandSpaceStations function below.
def flatlandSpaceStations(n, c):
    c.sort()

    max_distance = 0

    # Calculate the maximum distance between space stations and cities in between
    for i in range(len(c) - 1):
        distance = (c[i + 1] - c[i]) // 2
        max_distance = max(max_distance, distance)

    # Check if there are cities before the first space station and after the last space station
    max_distance = max(max_distance, c[0], n - 1 - c[-1])

    return max_distance

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    nm = input().split()

    n = int(nm[0])

    m = int(nm[1])

    c = list(map(int, input().rstrip().split()))

    result = flatlandSpaceStations(n, c)

    fptr.write(str(result) + '\n')

    fptr.close()
