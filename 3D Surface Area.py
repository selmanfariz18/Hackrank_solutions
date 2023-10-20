'''
Madison is a little girl who is fond of toys. Her friend Mason works in a toy manufacturing factory . Mason has a 2D board  of size  with  rows and  columns. The board is divided into cells of size  with each cell indicated by its coordinate . The cell  has an integer  written on it. To create the toy Mason stacks  number of cubes of size  on the cell .

Given the description of the board showing the values of  and that the price of the toy is equal to the 3d surface area find the price of the toy.

Input Format

The first line contains two space-separated integers  and  the height and the width of the board respectively.

The next  lines contains  space separated integers. The  integer in  line denotes .

Constraints

Output Format

Print the required answer, i.e the price of the toy, in one line.

Sample Input 0

1 1
1
Sample Output 0

6
Explanation 0

image The surface area of  cube is 6.

Sample Input 1

3 3
1 3 4
2 2 3
1 2 4
Sample Output 1

60
Explanation 1

image

The object is rotated so the front row matches column 1 of the input, heights 1, 2, and 1.

The front face is 1 + 2 + 1 = 4 units in area.
The top is 3 units.
The sides are 4 units.
None of the rear faces are exposed.
The underside is 3 units.
The front row contributes 4 + 3 + 4 + 3 = 14 units to the surface area.
'''

#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'surfaceArea' function below.
#
# The function is expected to return an INTEGER.
# The function accepts 2D_INTEGER_ARRAY A as parameter.
#

def surfaceArea(height, width, board):
    # Write your code here
    surface_area = 0

    for i in range(height):
        for j in range(width):
            h = board[i][j]
            if h > 0:
                # Calculate the surface area of the top and bottom faces
                surface_area += 2

                # Calculate the surface area of the four side faces
                surface_area += 4 * h

            # Check the adjacent cells to the left and above
            if i > 0:
                surface_area -= 2 * min(h, board[i - 1][j])
            if j > 0:
                surface_area -= 2 * min(h, board[i][j - 1])

    return surface_area

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    first_multiple_input = input().rstrip().split()

    H = int(first_multiple_input[0])

    W = int(first_multiple_input[1])

    A = []

    for _ in range(H):
        A.append(list(map(int, input().rstrip().split())))

    result = surfaceArea(H,W,A)

    fptr.write(str(result) + '\n')

    fptr.close()
