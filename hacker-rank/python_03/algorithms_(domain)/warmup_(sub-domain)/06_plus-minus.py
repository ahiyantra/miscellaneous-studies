# https://www.hackerrank.com/challenges/plus-minus/problem

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
PrepareAlgorithmsWarmupPlus Minus
Plus Minus
59 more points to get your next star!
Rank: 2599871|Points: 41/100
Problem Solving
Your Plus Minus submission got 10.00 points.  
You are now 59 points away from the 2nd star for your problem solving badge.
Try the next challenge | Try a Random Challenge
Problem
Submissions
Leaderboard
Discussions
Editorial
Given an array of integers, calculate the ratios of its elements that are positive, negative, and zero. Print the decimal value of each fraction on a new line with  places after the decimal.

Note: This challenge introduces precision problems. The test cases are scaled to six decimal places, though answers with absolute error of up to  are acceptable.

Example

There are  elements, two positive, two negative and one zero. Their ratios are ,  and . Results are printed as:

0.400000
0.400000
0.200000
Function Description

Complete the plusMinus function in the editor below.

plusMinus has the following parameter(s):

int arr[n]: an array of integers
Print
Print the ratios of positive, negative and zero values in the array. Each value should be printed on a separate line with  digits after the decimal. The function should not return a value.

Input Format

The first line contains an integer, , the size of the array.
The second line contains  space-separated integers that describe .

Constraints



Output Format

Print the following  lines, each to  decimals:

proportion of positive values
proportion of negative values
proportion of zeros
Sample Input

STDIN           Function
-----           --------
6               arr[] size n = 6
-4 3 -9 0 4 1   arr = [-4, 3, -9, 0, 4, 1]
Sample Output

0.500000
0.333333
0.166667
Explanation

There are  positive numbers,  negative numbers, and  zero in the array.
The proportions of occurrence are positive: , negative:  and zeros: .

Language
Python 3
More
12345678910111213141516343536371718192021222324252627282930313233
    print(ratPos)
    print(ratNeg)
    print(ratZer)

if __name__ == '__main__':
    n = int(input().strip())

    arr = list(map(int, input().rstrip().split()))

    plusMinus(arr)

Line: 33 Col: 18

Test against custom input
Problem Solving
You have earned 10.00 points!
You are now 59 points away from the 2nd star for your problem solving badge.
16%41/100
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

Test case 11
Compiler Message
Success
Input (stdin)
5
0 0 -1 1 1
Expected Output
0.400000
0.200000
0.400000
Hidden Test Case
Use print or log statements to debug why your hidden test cases are failing. Hidden test cases are used to evaluate if your code can handle different scenarios, including corner cases.

Authorvatsalchanana
DifficultyEasy
Max Score10
Submitted By1555866
Need Help?
View discussions
View editorial
View top submissions
rate this challenge

MORE DETAILS
Download problem statement
Download sample test cases
Suggest Edits
Share on FacebookShare on TwitterShare on LinkedIn
BlogScoringEnvironmentFAQAbout UsSupportCareersTerms Of ServicePrivacy Policy
values, ``` ``` , Prints the values to a stream, or to sys.stdout by default. sep   string inserted between values, default a space. end   string appended after the last value, default a newline. file   a file-like object (stream); defaults to the current sys.stdout. flush   whether to forcibly flush the stream., hint

""""

#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'plusMinus' function below.
#
# The function accepts INTEGER_ARRAY arr as parameter.
#

def plusMinus(arr):
    # Write your code here
    posInt = 0
    negInt = 0
    zerInt = 0
    total = len(arr)
    for v0 in arr:
        if v0 > 0 :
            posInt += 1
        elif v0 < 0:
            negInt += 1
        else:
            zerInt += 1
    ratPos = posInt/total
    ratNeg = negInt/total
    ratZer = zerInt/total
    print(ratPos)
    print(ratNeg)
    print(ratZer)

if __name__ == '__main__':
    n = int(input().strip())

    arr = list(map(int, input().rstrip().split()))

    plusMinus(arr)
