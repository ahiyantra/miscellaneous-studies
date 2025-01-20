# https://www.hackerrank.com/challenges/diagonal-difference/problem

"""

HackerRank Home
|
Prepare
Certify
Compete
Apply
Search


|
Switch to..

ahiyantra
PrepareAlgorithmsWarmupDiagonal Difference
Diagonal Difference
49 more points to get your next star!
Rank: 2413240|Points: 51/100
Problem Solving
Your Diagonal Difference submission got 10.00 points.  
You are now 49 points away from the 2nd star for your problem solving badge.
Try the next challenge | Try a Random Challenge
Problem
Submissions
Leaderboard
Discussions
Editorial
HackerRank Logo
|
PrepareAlgorithmsWarmupDiagonal Difference
Exit Full Screen View
Problem	Submissions	Leaderboard	Discussions	Editorial
Given a square matrix, calculate the absolute difference between the sums of its diagonals.

For example, the square matrix  is shown below:

1 2 3
4 5 6
9 8 9  
The left-to-right diagonal = . The right to left diagonal = . Their absolute difference is .

Function description

Complete the  function in the editor below.

diagonalDifference takes the following parameter:

int arr[n][m]: an array of integers
Return

int: the absolute diagonal difference
Input Format

The first line contains a single integer, , the number of rows and columns in the square matrix .
Each of the next  lines describes a row, , and consists of  space-separated integers .

Constraints

Output Format

Return the absolute difference between the sums of the matrix's two diagonals as a single integer.

Sample Input

3
11 2 4
4 5 6
10 8 -12
Sample Output

15
Explanation

The primary diagonal is:

11
   5
     -12
Sum across the primary diagonal: 11 + 5 - 12 = 4

The secondary diagonal is:

     4
   5
10
Sum across the secondary diagonal: 4 + 5 + 10 = 19
Difference: |4 - 19| = 15

Note: |x| is the absolute value of x

Language
Python 3
More
910111213141516172930313233343536373828232418192526273940414222202143
    len1Darr = len(arr)
    counter = list(range(0, len1Darr))
    for ind in counter:
        diagAsum += arr[ind][ind]
        diagBsum += arr[-(ind+1)][ind]
    result = abs(diagAsum-diagBsum)
    return result
    

if __name__ == '__main__':

Line: 21 Col: 24

Test against custom input
Problem Solving
You have earned 10.00 points!
You are now 49 points away from the 2nd star for your problem solving badge.
30%51/100
Congratulations
You solved this challenge. Would you like to challenge your friends?Share on FacebookShare on TwitterShare on LinkedIn

Test case 0

Test case 1

Test case 2

Test case 3

Test case 4

Test case 5

Test case 6

Test case 7

Test case 8

Test case 9

Test case 10
Compiler Message
Success
Input (stdin)
3
11 2 4
4 5 6
10 8 -12
Expected Output
15
BlogScoringEnvironmentFAQAbout UsSupportCareersTerms Of ServicePrivacy Policy
values, ``` ``` , Prints the values to a stream, or to sys.stdout by default. sep   string inserted between values, default a space. end   string appended after the last value, default a newline. file   a file-like object (stream); defaults to the current sys.stdout. flush   whether to forcibly flush the stream., hint

"""

#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'diagonalDifference' function below.
#
# The function is expected to return an INTEGER.
# The function accepts 2D_INTEGER_ARRAY arr as parameter.
#

def diagonalDifference(arr):
    # Write your code here
    diagAsum = 0
    diagBsum = 0
    result = 0
    len1Darr = len(arr)
    counter = list(range(0, len1Darr))
    for ind in counter:
        diagAsum += arr[ind][ind]
        diagBsum += arr[-(ind+1)][ind]
    result = abs(diagAsum-diagBsum)
    return result
    

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    arr = []

    for _ in range(n):
        arr.append(list(map(int, input().rstrip().split())))

    result = diagonalDifference(arr)

    fptr.write(str(result) + '\n')

    fptr.close()
