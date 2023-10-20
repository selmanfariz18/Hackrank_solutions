'''
 is a chess piece that moves in an L shape. We define the possible moves of  as any movement from some position  to some  satisfying either of the following:

 and , or
 and
Note that  and  allow for the same exact set of movements. For example, the diagram below depicts the possible locations that  or  can move to from its current location at the center of a  chessboard:

image

Observe that for each possible movement, the Knight moves  units in one direction (i.e., horizontal or vertical) and  unit in the perpendicular direction.

Given the value of  for an  chessboard, answer the following question for each  pair where :

What is the minimum number of moves it takes for  to get from position  to position ? If it's not possible for the Knight to reach that destination, the answer is -1 instead.
Then print the answer for each  according to the Output Format specified below.

Input Format

A single integer denoting .

Constraints

Output Format

Print exactly  lines of output in which each line  (where ) contains  space-separated integers describing the minimum number of moves  must make for each respective  (where ). If some  cannot reach position , print -1 instead.

For example, if , we organize the answers for all the  pairs in our output like this:

(1,1) (1,2)
(2,1) (2,2)
Sample Input 0

5
Sample Output 0

4 4 2 8
4 2 4 4
2 4 -1 -1
8 4 -1 1
Explanation 0

The diagram below depicts possible minimal paths for , , and :

image

One minimal path for  is:

We then print 4 4 2 8 as our first line of output because  took  moves,  took  moves,  took  moves, and  took  moves.

In some of the later rows of output, it's impossible for  to reach position . For example,  can only move back and forth between  and  so it will never reach .
'''

#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'knightlOnAChessboard' function below.
#
# The function is expected to return a 2D_INTEGER_ARRAY.
# The function accepts INTEGER n as parameter.
#

def allMoves(i, j, a, b, n):
    moves = []
    deltas = [(a, b,), (a, -b), (-a, b), (-a, -b)]
    deltas.extend([(b, a), (b, -a), (-b, a), (-b, -a)])
    for delta in deltas:
        if 0 <= i + delta[0] < n and 0 <= j + delta[1] < n:
            moves.append((i + delta[0], j + delta[1]))
    return moves


def findDistance(n, a, b):
    distance = [[-1 for x in range(n)] for x in range(n)]
    distance[n - 1][n - 1] = 0
    todo = [(n - 1, n - 1)]
    while len(todo) > 0:
        (i, j) = todo.pop(0)
        new_moves = allMoves(i, j, a, b, n)
        for move in new_moves:
            if distance[move[0]][move[1]] == -1:
                distance[move[0]][move[1]] = distance[i][j] + 1
                todo.append((move[0], move[1]))
                if move[0] == 0 and move[1] == 0:
                    break
    return distance[0][0]


def knightlOnAChessboard(n):
    # Write your code here
    answer = [[0 for x in range(n - 1)] for x in range(n - 1)]
    for i in range(n - 1):
        for j in range(n - 1):
            answer[i][j] = findDistance(n, i + 1, j + 1)
    for i in range(n - 1):
        return answer


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    result = knightlOnAChessboard(n)

    fptr.write('\n'.join([' '.join(map(str, x)) for x in result]))
    fptr.write('\n')

    fptr.close()
